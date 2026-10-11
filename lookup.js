#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, 'codes.json');
const codes = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

const query = process.argv.slice(2).join(' ').trim().toLowerCase();

console.log('='.repeat(68));
console.log(" Clive Barker's Hellraiser: Revival — Safe Codes & Keypad Lookup");
console.log(' Web Interactive Map & Guides: https://hellraisergamehub.com');
console.log('='.repeat(68));

if (!query) {
  console.log('\nAll 10 Verified Safe Codes (Patch 1.02):\n');
  console.log(`${'#'.padEnd(3)} ${'Location'.padEnd(32)} ${'Code'.padEnd(8)} Loot`);
  console.log('-'.repeat(68));
  for (const item of codes) {
    const codeStr = item.code + (item.alternate_code ? ` / ${item.alternate_code}` : '');
    console.log(`${String(item.id).padEnd(3)} ${item.location.padEnd(32)} ${codeStr.padEnd(8)} ${item.loot}`);
  }
  console.log('\nTip: Run `node lookup.js <keyword>` (e.g. `node lookup.js sewer` or `node lookup.js music`)');
} else {
  const matched = codes.filter(c => 
    c.location.toLowerCase().includes(query) ||
    c.chapter.toLowerCase().includes(query) ||
    c.loot.toLowerCase().includes(query)
  );

  if (matched.length === 0) {
    console.log(`\nNo safe codes matched query: '${query}'`);
    console.log('Visit https://hellraisergamehub.com/blog/all-safe-codes-keypad-combinations for complete walkthrough.');
  } else {
    console.log(`\nFound ${matched.length} match(es) for '${query}':\n`);
    for (const item of matched) {
      console.log(`[${item.id}] ${item.location} (${item.chapter})`);
      console.log(`    Code: ${item.code}` + (item.alternate_code ? ` (Alternative: ${item.alternate_code})` : ''));
      console.log(`    Loot: ${item.loot}`);
      console.log(`    Hint: ${item.hint}\n`);
    }
  }
}
