int isEnglishVowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

char* reverseVowels(char *s) {
    int left = 0;
    int right = strlen(s) - 1;

    while (left < right) {
        if (isEnglishVowel(s[left]) && isEnglishVowel(s[right])) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        } else if (!isEnglishVowel(s[right])) {
            right--;
        } else {
            left++;
        }
    }

    return s;
}