from art import *

class Ganesha:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
    
    def crown(self):
        # crown part 1
        for r in range(self.row):
            for c in range(self.col):
                if  r== 0 and c == 9:
                    print("*", end="")
                elif(r==1 and c in range(8,11)):
                    print("*", end="")
                elif (r==2 and c in range(6,13)):
                    print("*", end="")
                elif(r==3 and c in range(4,15)):
                    print("*", end="")
                elif(r==4 and c in range(2,17)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        # crown part 2
        # crown part 3
    
    def test(self):
        # crown part 1
        for r in range(self.row):
            for c in range(self.col):
                if  r== 2 and c == 10:
                    print("*", end="")
                elif(r==3 and c in range(9,12)):
                    print("*", end="")
                elif (r==4 and c in range(8,14)):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()
        
        for r in range(self.row):
            for c in range(self.col):
                if r==5 and c in range(5,8):
                    print("#", end="")
                elif(r==5 and c in range(8,11)):
                    print("*", end="")
            

if __name__=="__main__":
    obj = Ganesha(18,18)
    obj.test()
    
    
        