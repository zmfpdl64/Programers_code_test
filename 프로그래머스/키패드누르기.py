

class righth:
    def __init__(self):        
        self.x = 2
        self.y = 3
    def move(self, x, y):
        self.x = x
        self.y = y
        
    
class lefth:
    def __init__(self):        
        self.x = 0
        self.y = 3
    def move(self, x, y):
        self.x = x
        self.y = y

            


            
def solution(numbers, hand):
    right = righth()
    left = lefth()
    a = ''
    for i in numbers:
        if i == 1:
            x = 0
            y = 0
        elif i == 2:
            x = 1
            y = 0
        elif i == 3:
            x = 2
            y = 0
        elif i == 4:
            x = 0
            y = 1
        elif i == 5:
            x = 1
            y = 1
        elif i == 6:
            x = 2
            y = 1
        elif i == 7:
            x = 0
            y = 2
        elif i == 8:
            x = 1
            y = 2
        elif i == 9:
            x = 2
            y = 2
        elif i == 0:
            x = 1
            y = 3
        
        rl = abs(right.x - x) + abs( right.y - y)
        ll = abs(left.x - x) + abs( left.y - y)
        if x == 2:
            right.move(x, y)
            a += 'R'
        elif x == 0:
            left.move(x, y)
            a += 'L'
        elif rl < ll:
            right.move(x, y)
            a += 'R'
        elif ll < rl:
            left.move(x, y)
            a += 'L'
        elif rl == ll:
            if hand == 'right':
                right.move(x,y)
                a += 'R'
            else:
                left.move(x,y)
                a += 'L'



    return a

#b = [1,3,4,5,8,2,1,4,5,9,5]
b = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(solution(b, 'left'))


