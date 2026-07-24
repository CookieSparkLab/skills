#!/usr/bin/env node
import fs from "node:fs";

const file = process.argv[2];
if (!file) {
  console.error("Usage: node validate_svg.mjs <diagram.svg>");
  process.exit(2);
}

const svg = fs.readFileSync(file, "utf8");
const errors = [];
const warnings = [];

if (!/<svg\b[^>]*\bviewBox=/.test(svg)) errors.push("Missing SVG viewBox.");
if (!/xmlns=["']http:\/\/www\.w3\.org\/2000\/svg["']/.test(svg)) errors.push("Missing SVG xmlns.");
if (/<rect\b[^>]*(?:width=["'](?:1920|100%)["'][^>]*height=["'](?:1080|100%)["']|height=["'](?:1080|100%)["'][^>]*width=["'](?:1920|100%)["'])[^>]*fill=["'](?!none|transparent|#[0-9A-Fa-f]{8})/.test(svg)) {
  errors.push("Possible opaque full-canvas rectangle; transparent background is required.");
}

const nodeMatches = [...svg.matchAll(/<g\b[^>]*data-role=["']node["'][^>]*data-bbox=["']([^"']+)["'][^>]*>/g)];
const connectorMatches = [...svg.matchAll(/<(?:path|polyline)\b[^>]*data-role=["']connector["'][^>]*data-points=["']([^"']+)["'][^>]*>/g)];

if (!nodeMatches.length) warnings.push("No annotated nodes found.");
if (!connectorMatches.length) warnings.push("No annotated connectors found.");

const boxes = nodeMatches.map((match, index) => {
  const nums = match[1].split(",").map(Number);
  if (nums.length !== 4 || nums.some(Number.isNaN)) {
    errors.push(`Node ${index + 1} has invalid data-bbox.`);
    return null;
  }
  return { index, x: nums[0], y: nums[1], w: nums[2], h: nums[3] };
}).filter(Boolean);

const inside = (p, b, gap = 12) =>
  p.x > b.x - gap && p.x < b.x + b.w + gap &&
  p.y > b.y - gap && p.y < b.y + b.h + gap;

const segmentHitsBox = (a, b, box) => {
  if (inside(a, box) || inside(b, box)) return true;
  const left = box.x - 12;
  const right = box.x + box.w + 12;
  const top = box.y - 12;
  const bottom = box.y + box.h + 12;
  if (a.x === b.x) return a.x > left && a.x < right && Math.max(a.y, b.y) > top && Math.min(a.y, b.y) < bottom;
  if (a.y === b.y) return a.y > top && a.y < bottom && Math.max(a.x, b.x) > left && Math.min(a.x, b.x) < right;
  warnings.push("A diagonal connector segment requires visual inspection.");
  return false;
};

for (const [connectorIndex, match] of connectorMatches.entries()) {
  const points = match[1].trim().split(/\s+/).map(pair => {
    const [x, y] = pair.split(",").map(Number);
    return { x, y };
  });
  if (points.length < 2 || points.some(p => Number.isNaN(p.x) || Number.isNaN(p.y))) {
    errors.push(`Connector ${connectorIndex + 1} has invalid data-points.`);
    continue;
  }
  for (let i = 0; i < points.length - 1; i++) {
    for (const box of boxes) {
      const endpointNode = i === 0 || i === points.length - 2;
      if (endpointNode && (inside(points[0], box, 1) || inside(points.at(-1), box, 1))) continue;
      if (segmentHitsBox(points[i], points[i + 1], box)) {
        errors.push(`Connector ${connectorIndex + 1} crosses node ${box.index + 1} safety zone.`);
      }
    }
  }
}

const firstText = svg.search(/<text\b/);
const lastConnector = Math.max(...connectorMatches.map(match => match.index), -1);
if (firstText >= 0 && lastConnector > firstText) {
  errors.push("A connector is painted after text. Put all connectors before nodes and labels.");
}

for (const message of warnings) console.warn(`WARN: ${message}`);
for (const message of errors) console.error(`ERROR: ${message}`);

if (errors.length) process.exit(1);
console.log(`OK: ${boxes.length} nodes and ${connectorMatches.length} connectors passed static checks.`);
