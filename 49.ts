// function groupAnagrams(strs: string[]): string[][] {
//   const anagramHashMap = new Map<string, string[]>();

//   for (let i = 0; i < strs.length; i++) {
//     const strHashArray = new Array(26).fill(0);

//     for (let c of strs[i]) {
//       strHashArray[c.charCodeAt(0) - 97] += 1;
//     }

//     const strHash = strHashArray.join("#");

//     const anagrams = anagramHashMap.get(strHash) || [];
//     anagrams.push(strs[i]);
//     anagramHashMap.set(strHash, anagrams);
//   }

//   return Array.from(anagramHashMap.values());
// }

function groupAnagrams(strs: string[]): string[][] {
  const hashMap = new Map<string, string[]>();

  for (const str of strs) {
    const letterFrequencies = new Array(26).fill(0);

    const letters = [];

    for (const s of str) {
      letterFrequencies[s.charCodeAt(0) - "a".charCodeAt(0)] += 1;
      letters.push(s);
    }

    console.log(letters.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).);
    console.log(letterFrequencies.join("-"));
  }

  return Array.from(hashMap.values());
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
