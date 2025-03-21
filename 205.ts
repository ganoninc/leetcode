function isIsomorphic(s: string, t: string): boolean {
  if (s.length != t.length) {
    return false;
  }

  let mapping = new Map<string, string>();
  let alreadyMappedCharsOfT = new Set<string>();

  for (let i = 0; i < s.length; i++) {
    if (!mapping.has(s[i])) {
      if (alreadyMappedCharsOfT.has(t[i])) return false;

      mapping.set(s[i], t[i]);
      alreadyMappedCharsOfT.add(t[i]);
    } else {
      if (mapping.get(s[i]) != t[i]) {
        return false;
      }
    }
  }

  return true;
}

// console.log(isIsomorphic("foo", "bar"));
// console.log(isIsomorphic("egg", "add"));
// console.log(isIsomorphic("paper", "title"));
console.log(isIsomorphic("badc", "baba"));

// b --> b
// a --> a
// d -->
