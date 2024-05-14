import re

class TicTacToe:
    def __init__(self) -> None:
        """
        Definition of the hash that is a bidmensional list
        """ 
        self.hash = [[" " for i in range(3)] for j in range(3)]
        self.symbols = ["X", "O"]
        self.__round = 0
        # Instructions how the game works
        title = open("./title.txt", mode="r+")
        print(title.read())
        input("Press enter for start.")
            
    def __repr__(self) -> str:
        """
        The string representation of the Tic Tac Toe game
        """
        foo = ""
        for i, row in enumerate(self.hash):
            for j, col in enumerate(row):
                if (i == 2 and j == 2):
                    foo += f"{col}" 
                    continue
                if (j > 1):
                    foo += f"{col} \n"
                    continue
                foo += f"{col} | "
        return foo    

    def __format__(self) -> list:
        """
        This method formats the game and change X to 1 and O to 0
        """
        foo = [['','',''] for i in range(3)]
        for i,row in enumerate(self.hash):
            for j,col in enumerate(row):
                if (col == "X"):
                    foo[i][j] = 1
                elif (col == "O"):
                    foo[i][j] = 0
        return foo
    
    def take_input(self) -> int:
        """
        This method takes the user input uses regex expression to prevent bad inputs
        """
        while True:  
            ipt = input(f"\nPlayer {self.__round % 2 + 1} you are {self.symbols[self.__round % 2]}, Please type a number for play:")
            if (re.match(r"^[1-9]{1}$", ipt)):
                return int(ipt)
            print("Invalid number try another one!")
            continue

    def check(self) -> int:
        """
        This checks who won
        """
        if (self.__round >= 4):
            for i,row in enumerate(self.__format__()):
                try:
                    if ((sum(row) == 0 or sum(row) == 3) and len(row) == 3):
                        return 1 if sum(row) == 3 else 2
                    if (i == 0):
                        for j,col in enumerate(row):
                            if (col != '' and col == self.__format__()[1][j] and col == self.__format__()[2][j]):
                                print(col)
                                return 1 if col == 1 else 2 
                            if (col != '' and (self.__format__()[0][0] == self.__format__()[1][1] and self.__format__()[0][0] == self.__format__()[2][j+2]) or
                                (self.__format__()[0][2] == self.__format__()[1][1] and self.__format__()[0][2] == self.__format__()[2][0])):
                                if (self.__format__()[0][2] == self.__format__()[1][1]):
                                    return 1 if self.__format__()[0][2] == 1 else 2 
                                return 1 if self.__format__()[0][0] == 1 else 2     
                except:
                    pass

    def play(self) -> None:
        while (self.__round < 9):
            res = self.check()
            if (res == 1 or res == 2):
                print(f"Player {res} Won!")
                break
            input = self.take_input()
            if (input <= 3 and self.hash[0][input - 1] == " "):
                self.hash[0][input - 1] = self.symbols[self.__round % 2]
                self.__round += 1
            elif (input >= 4 and input <= 6 and self.hash[1][input - 4] == " "):
                self.hash[1][input - 4] = self.symbols[self.__round % 2]
                self.__round += 1
            elif (input >= 7 and self.hash[2][input - 7] == " "):
                self.hash[2][input - 7] = self.symbols[self.__round % 2]
                self.__round += 1
            print(f"\n{str(self)}\n")
        

if __name__ == "__main__":
    j = TicTacToe()
    j.play()        
