void reverseString(char* s, int sSize) {
    char* left = s;
    char* right = s + sSize - 1;
    char temp;

    while(left < right){
        temp = *left;
        *left = *right;
        *right = temp;

        left++;
        right--;
    }
}