class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        setbits = bin(num2)[2:].count("1")
        x = list(bin(num1)[2:])
        c1 = x.count("1")
        if(c1 > setbits):
            rem = c1 - setbits
            for i in range(len(x)-1, -1, -1):
                if(x[i] == "1"):
                    x[i] = "0"
                    rem -= 1
                if(rem == 0):
                    break

        elif(c1 < setbits):
            rem = setbits - c1
            for i in range(len(x)-1, -1, -1):
                if(x[i] == "0"):
                    x[i] = "1"
                    rem -= 1
                if(rem == 0):
                    break
            if(rem):
                x.extend(["1" for _ in range(0, rem)])

        return int("".join(x), 2)