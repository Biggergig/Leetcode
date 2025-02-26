class Solution:
    def numberToWords(self, num: int, say_zero=True) -> str:
        if num == 0: return "Zero" if say_zero else ""
        ones = [
            "", # avoid saying zero except explicitly
            "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen",
        ]
        if num < len(ones): return ones[num]

        tens = [
            None, None, "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety",
        ]
        if num < 100:
            return f"{tens[num//10]} {ones[num%10]}".strip()
        for bound, mod ,title in [
            (100, 10, ""),
            (1_000, 100,"Hundred "),
            (1_000_000, 1000,"Thousand "),
            (1_000_000_000, 1000000,"Million "),
            (2**31,1_000_000_000,"Billion "),
        ]:
            if num < bound:
                return f"{self.numberToWords(num//mod)} {title}{self.numberToWords(num%mod, False)}".strip()
