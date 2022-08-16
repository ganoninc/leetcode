class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        will_result_be_negative = False
        if dividend < 0 and divisor >= 0:
            dividend = abs(dividend)
            will_result_be_negative = True
        elif dividend >= 0 and divisor < 0:
            divisor = abs(divisor)
            will_result_be_negative = True
        elif dividend < 0 and divisor < 0:
            dividend = abs(dividend)
            divisor = abs(divisor)

        if divisor == 1:
            if will_result_be_negative: 
                if dividend > (pow(2,31) ):
                    dividend = (pow(2,31) )
                return -dividend
            else:
                if dividend > (pow(2,31) - 1):
                    dividend = (pow(2,31) - 1)
                return dividend

        result_data = self.get_result(dividend, divisor)

        result = result_data["result"]

        if result > (pow(2,31) - 1):
            result = (pow(2,31) - 1)

        if will_result_be_negative:
            if result == (pow(2,31) - 1):
                result = result + 1
            result = result -result -result

        return result


    def get_result(self, dividend: int, divisor: int) -> dict:
        result_data = {
            "dividend_remain" : 0,
            "result" : 0,
            "used_left_shifts": 0,
            "used_left_shifts_value" : 0
        }

        if dividend < divisor:
            result_data["dividend_remain"] = dividend
        else:
            tested_value = 0
            needed_left_shits = 0
            result = 0
            previous_result = 0

            while dividend >= tested_value:
                needed_left_shits = needed_left_shits + 1
                if result == 0:
                    result = 2
                    previous_result = 1
                else:
                    previous_result = result
                    result = result + result
                tested_value = divisor << needed_left_shits

            result = result - previous_result
            needed_left_shits = needed_left_shits - 1

            dividend_remain_after_big_closest_found = dividend - (divisor << needed_left_shits)

            sub_result_data = self.get_result(dividend_remain_after_big_closest_found, divisor)

            result_data["dividend_remain"] = dividend_remain_after_big_closest_found - sub_result_data["used_left_shifts_value"]
            result_data["result"] = result + sub_result_data["result"]
            result_data["used_left_shifts"] = needed_left_shits + sub_result_data["used_left_shifts"]
            result_data["used_left_shifts_value"] = (divisor << needed_left_shits) + sub_result_data["used_left_shifts_value"]

        return result_data

        

solution = Solution()
print(solution.divide(10, 3))