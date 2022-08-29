class Solution:
    def addBinary(self, a: str, b: str) -> str:
        loop_high_limit = max(len(a), len(b))
        i = 1
        reversed_result = ""
        to_be_added_at_next_iteration = 0
        while i <= loop_high_limit:
            current_a_index = len(a) - i
            current_b_index = len(b) - i

            if current_a_index < len(a) and current_a_index >= 0:
                a_as_int = int(a[current_a_index])
            else:
                a_as_int = 0

            if current_b_index < len(b)  and current_b_index >= 0:
                b_as_int = int(b[current_b_index])
            else:
                b_as_int = 0


            subtotal = to_be_added_at_next_iteration + a_as_int + b_as_int

            if subtotal > 1:
                to_be_added_at_next_iteration = 1
            else :
                to_be_added_at_next_iteration = 0

            if subtotal % 2 != 0:
                reversed_result += "1"
            else:
                reversed_result += "0"

            i = i + 1

        if to_be_added_at_next_iteration == 1:
            reversed_result += "1"

        return reversed_result[::-1]
        
solution = Solution()
print(solution.addBinary("11", "1"))