function findRepeatedDnaSequences(s: string): string[] {
  let dnsSequenceMap: Map<string, number> = new Map();
  let left = 1,
    right = 10;
  let res: string[] = [];

  dnsSequenceMap.set(s.slice(0, 10), 1);

  while (right < s.length) {
    let sequence = s.slice(left, right + 1);
    if (!dnsSequenceMap.has(sequence)) {
      dnsSequenceMap.set(sequence, 1);
    } else {
      dnsSequenceMap.set(sequence, (dnsSequenceMap.get(sequence) || 0) + 1);
    }
    right++;
    left++;
  }

  for (let [key, value] of dnsSequenceMap.entries()) {
    if (value > 1) res.push(key);
  }
  return res;
}

console.log(findRepeatedDnaSequences("AAAAAAAAAAA"));
