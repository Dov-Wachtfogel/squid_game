import random


class digits4:
    def __init__(self):
        self.num = str(random.randint(1000, 9999))
        self.someone_win = False

    def check_num(self, num: int | str):
        num = str(num)
        A_num = 0
        B_num = 0
        for i in range(4):
            if num[i] == self.num[i]:
                A_num += 1
            elif num[i] in self.num:
                B_num += 1
        if A_num == 4:
            self.someone_win = True
        return f'{A_num}A{B_num}B'
