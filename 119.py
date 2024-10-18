from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        direct_parent_values = [1]
        latest_row = [1]

        for row_index in range(2, rowIndex + 2):
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

            latest_row = children_values
            direct_parent_values = children_values

        return latest_row

solution = Solution()
print(solution.getRow(5))