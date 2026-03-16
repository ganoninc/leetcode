function lengthOfLongestSubstring(s: string): number {
  if (s.length === 0) {
    return 0;
  }

  let left = 0,
    right = 1,
    maxLength = 1;

  const window = new Set<string>();
  window.add(s[left]);

  while (right < s.length && left < s.length) {
    if (window.has(s[right])) {
      window.delete(s[left]);
      left += 1;
    } else {
      maxLength = Math.max(maxLength, right - left + 1);
      window.add(s[right]);
      right += 1;
    }
  }

  return maxLength;
}

console.log(lengthOfLongestSubstring("abcabcbb"));
