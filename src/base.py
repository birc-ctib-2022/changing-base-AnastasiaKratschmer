"""Changing bases."""

from email.mime import base


digits = {}

for i in range(0, 10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'


def change_to_base(i,b):
        if i== 0:
            return [0]
        else:
            number_in_b=[]
            while i>0:
                q=(i//b)
                r=i%b
                number_in_b.append(r)
                i=q
            number_in_b.reverse()
            better_format = int("".join(map(str, number_in_b)))
            print(better_format)

change_to_base(10000,13)

