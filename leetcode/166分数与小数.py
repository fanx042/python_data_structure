class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:

        sign = ''
        if num * den < 0:
            sign = '-'
        num = abs(num)
        den = abs(den)
        if num % den == 0:
            return sign + str(int(num / den))
        left_part = num // den
        right_part_str = []
        right_aprt_ans = []
        right_part = ''
        mid = num % den
        right_aprt_ans.append(mid)
        while mid != 0:
            mid_ = mid * 10
            right_part_str.append(str(mid_ // den))
            mid = mid_ % den
            if mid in right_aprt_ans:
                break
            right_aprt_ans.append(mid)

        idx = right_aprt_ans.index(mid)

        right_part = right_part.join(right_part_str)
        if idx != len(right_part):
            return sign + str(left_part) + '.' + right_part[:idx] + '(' + right_part[idx:]+')'
        else:
            return sign + str(left_part) + '.' + right_part
