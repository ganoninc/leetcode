from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        if numRows == 1:
            return result

        direct_parent_values = [1]

        for row_index in range(2, numRows + 1):
            children_values = []

            for child_index in range(0, row_index):
                if child_index == 0:
                    left_parent_value = 0
                else:
                    left_parent_value = direct_parent_values[child_index - 1]

                if child_index == row_index-1:
                    right_parent_value = 0
                else:
                    right_parent_value = direct_parent_values[child_index]

                child_value = left_parent_value + right_parent_value
                children_values.append(child_value)

            result.append(children_values)
            direct_parent_values = children_values

        return result

# solution = Solution()
# print(solution.generate(5))