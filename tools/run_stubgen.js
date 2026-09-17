// Exécute le générateur de stub extrait du bundle (cf extract_stub.py) sur les game data.
// Usage : run_stubgen.js <stubgen_parts.js> <game_data.json> <out.pyi> <out.d.ts> <out_member_to_ls.json>
const fs = require('fs');
const [parts, dataPath, outPyi, outDts, outMap] = process.argv.slice(2);
const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
const m = { exports: {} };
new Function('module', 'exports', fs.readFileSync(parts, 'utf8'))(m, m.exports);
fs.writeFileSync(outPyi, m.exports.buildPyi(data.constants));
fs.writeFileSync(outDts, m.exports.dtsTemplate);
fs.writeFileSync(outMap, JSON.stringify(m.exports.memberToLs, null, 1));
console.log('  stub brut :', outPyi, fs.statSync(outPyi).size, 'octets');
