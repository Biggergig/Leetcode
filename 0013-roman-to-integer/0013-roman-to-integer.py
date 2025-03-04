class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        replaces = [
            ("IV","I"*4),
            ("IX","I"*9),
            ("XL","X"*4),
            ("XC","X"*9),
            ("CD","C"*4),
            ("CM","C"*9),
        ]
        for a,b in replaces:
            s = s.replace(a,b)
        return sum(values[c] for c in s)