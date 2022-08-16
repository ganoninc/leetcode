class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        accepted_number = range(pow(-2,31), pow(2,31) - 1)
        # print(accepted_number)

        x_as_string = str(x)

        if is_negative:
            x_as_string = x_as_string[1:]

        reversed_x_as_string = x_as_string[::-1]

        if is_negative:
            reversed_x_as_string = "-" + reversed_x_as_string

        reversed_x_as_int = int(reversed_x_as_string)

        if is_negative and reversed_x_as_int >= 0:
            return 0
        elif not is_negative and reversed_x_as_int < 0:
            return 0
        elif reversed_x_as_int not in accepted_number:
            return 0

        # print(reversed_x_as_int)
        return reversed_x_as_int

solution = Solution()
print(solution.reverse(1534236469))