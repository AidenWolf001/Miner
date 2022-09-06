import random


class Minefield:
    def __init__(self, field_size = [30, 30], numer_of_mine = 200):
        self.field_size = field_size
        self.number_of_mine = numer_of_mine
        self.field_list = [[0 for i in range(field_size[0])] for j in range(field_size[1])]
        self.__random_mine(numer_of_mine)
        self.__add_mine()
        self.__add_mark()

    def __random_mine(self, number_of_mine):
        mine_list = []
        while len(mine_list) < number_of_mine:
            x = random.randint(0, self.field_size[0]-1)
            y = random.randint(0, self.field_size[1]-1)
            if not [x, y] in mine_list:
                mine_list.append([x, y])
        self.mine_list = mine_list

    def __add_mine(self):
        for i in self.mine_list:
            x, y = i
            self.field_list[x][y] = '*'

    def __add_mark(self):
        for i in range(self.field_size[1]):
            for j in range(self.field_size[0]):
                number = 0
                if self.field_list[i][j] != '*':
                    fs = []
                    fs.append([j - 1, i - 1])
                    fs.append([j, i - 1])
                    fs.append([j + 1, i - 1])
                    fs.append([j - 1, i])
                    fs.append([j, i])
                    fs.append([j + 1, i])
                    fs.append([j - 1, i + 1])
                    fs.append([j, i + 1])
                    fs.append([j + 1, i + 1])

                    for f in fs:
                        if f[0] >= 0 and f[1] >= 0 and f[0] < self.field_size[0] and f[1] < self.field_size[1]:
                            if self.field_list[f[1]][f[0]] == '*':
                                number += 1
                    self.field_list[i][j] = number

    def display(self):
        for i in range(self.field_size[1]):
            for j in range(self.field_size[0]):
                print(self.field_list[i][j], end=' ')
            print()

if __name__ == '__main__':
    a = Minefield()
    a.display()