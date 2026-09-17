// Évalue un chunk i18n Vue (fonctions `normalize`) en JSON plat.
// Usage : parse_i18n.js doc <doc.fr-xxx.js> <out.json>      (clés func_X / const_X ...)
//         parse_i18n.js locale <locale-fr-xxx.js> <out.json> (namespaces weapon / chip / effect ...)
const fs = require('fs');
const [mode, src, out] = process.argv.slice(2);
let s = fs.readFileSync(src, 'utf8');
const ctx = { normalize: a => a.join(''), interpolate: x => x, named: x => '{' + x + '}', list: x => '{' + x + '}', plural: x => x[0] };
const evalNs = ns => { const o = {}; for (const k in ns) { try { o[k] = ns[k](ctx); } catch { o[k] = '<?>'; } } return o; };
let result;
if (mode === 'doc') {
  s = s.replace(/^const \w+=/, '').replace(/;\s*export\{[^}]*\};?\s*$/, '');
  result = evalNs(new Function('return (' + s + ')')());
} else {
  s = s.replace(/^import\{s as a\}from"[^"]+";/, 'let captured=null;const a=(l,v)=>{captured=v};')
       .replace(/export\{\w+ as translations\};?\s*$/, 'return captured;');
  const V = new Function(s)();
  result = {};
  for (const ns of ['weapon', 'chip', 'effect', 'characteristic', 'entity']) result[ns] = evalNs(V[ns] || {});
}
fs.writeFileSync(out, JSON.stringify(result, null, 1));
console.log('  ', out, Object.keys(result).length, 'entrées');
