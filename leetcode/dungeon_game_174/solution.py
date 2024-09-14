class Solution:
    def __init__(self):
        self.m = 200
        self.n = 200
        self.max_num = -40000001
        self.maxHP = [ [ [self.max_num, self.max_num] for _ in range(self.n)] for _ in range(self.m) ]

    def maxHPF(self, i, j, dungeon):
        if i ==0 and j == 0: return self.maxHP[i][j]
        if i < 0 or j < 0:
            return [self.max_num, self.max_num]
        if self.maxHP[i][j][0] == self.max_num:
            self.maxHPF(i-1,j, dungeon)
            self.maxHPF(i,j-1, dungeon)
            # self.maxHP[i][j][0] = max(self.maxHPF(i-1,j, dungeon)[0], self.maxHPF(i,j-1, dungeon)[0]) + dungeon[i][j]
            if self.maxHP[i-1][j][1] > self.maxHP[i][j-1][1]:
                self.maxHP[i][j][0] = self.maxHP[i-1][j][0] + dungeon[i][j]
                self.maxHP[i][j][1] = min(self.maxHP[i-1][j][1], self.maxHP[i][j][0])
            else:
                self.maxHP[i][j][0] = self.maxHP[i][j-1][0] + dungeon[i][j]
                self.maxHP[i][j][1] = min(self.maxHP[i][j-1][1], self.maxHP[i][j][0])
        return self.maxHP[i][j]
            
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.m = len(dungeon)
        self.n = len(dungeon[0])
        self.maxHP[0][0][0] = dungeon[0][0]
        self.maxHP[0][0][1] = dungeon[0][0]
        if self.maxHP[0][0][1] > 0:
            self.maxHP[0][0][1] = 0
        
        a = -self.maxHPF(self.m-1, self.n-1, dungeon)[1] + 1
        # for i in range(self.m):
        #     for j in range(self.n):
        #         print(self.maxHP[i][j], end=" ")
        #     print()
        return a


