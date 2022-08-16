class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False

        if x > 9 and x % 10 == 0:
            return False

        if x < 10:
            return True

        xAsString = str(x)

        result = True
        j = len(xAsString) - 1
        for i in range(0, len(xAsString), 1):
            if(j < i):
                break

            if(xAsString[i] != xAsString[j]):
                result = False
                break

            j = j - 1

        return result
        # print(pow(10,31))
        # for i in range(10, pow(10,31), 10):

        # intAsByteArray = bytearray(x)
        # return intAsByteArray == intAsByteArray.reverse()


print(Solution.isPalindrome(Solution, 424))