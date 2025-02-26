class Solution:
    def numberToWords(self, num: int, say_zero=True) -> str:
        if say_zero and num == 0: return "Zero"
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
        if num < 1000:
            return f"{ones[num//100]} Hundred {self.numberToWords(num%100, False)}".strip()
        if num < 1_000_000:
            return f"{self.numberToWords(num//1000)} Thousand {self.numberToWords(num%1000, False)}".strip()
        if num < 1_000_000_000:
            return f"{self.numberToWords(num//1_000_000)} Million {self.numberToWords(num%1_000_000, False)}".strip()
        return f"{self.numberToWords(num//1_000_000_000)} Billion {self.numberToWords(num%1_000_000_000, False)}".strip()