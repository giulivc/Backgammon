## class Board inherits from dict
## key : point number
## value : list consisting of [color of checkers, number of checkers] on that point (key)


class Board (dict) : 

    ## arguments are only the keys occupied with at least one checker
    ## all other points (and bar) are initialized as empty lists
    def __init__(self, *args, **kwargs) : 
        super().__init__(*args, **kwargs)
        for i in range(1, 25) : 
            if not i in self : 
                self[i] = []
        self[-1] = []
    

    ## print method to print backgammon board
    def __str__(self) : 

        result = ""
        result += "-" * 122 + "\n"
        result += "-" * 122 + "\n"
        
        for i in range(14) :
            result += "||\t"
            
            if i == 0 :
                for j in range(1, 13) :
                    
                    if j == 7 :
                        result += "||\t||\t"
                    
                    
                    if j < 10 :
                        j = " " + str(j)
                    
                    result += str(j) + "\t"
                                
            elif i == 13 :
                
                for j in range(24, 12, -1) :
                    
                    if j == 18 :
                        result += "||\t||\t"
                        
                    result += str(j) + "\t"
                
            elif i <= 5 : 
                for point in range(1, 13) :
                    if point == 7: 
                        result += "||\t||\t"
                    if not self[point]:
                        result += "\t"
                    else :
                        if self[point][1] >= i :
                            if self[point][1] >= 5 + i : 
                                if self[point][1] >= 10 + i :
                                    result += " " + self[point][0] * 3 + "\t" 
                                else : 
                                    result += " " + self[point][0] * 2 + "\t" 
                            else : 
                                result += " " + self[point][0] + "\t" 
                        else :
                            result += "\t"
            
            elif i == 6 or i == 7 :
                result += "\t" * 6
                result += "||\t||\t"
                result += "\t" * 6
                
            elif i >= 8 : 
                for point in range(24, 12, -1) :
                    if point == 18: 
                        result += "||\t||\t"
                    if not self[point]:
                        result += "\t"
                    else :
                        if self[point][1] >= 13 - i :
                            if self[point][1] >= 18 - i : 
                                if self[point][1] >= 23 - i :
                                    result += " " + self[point][0] * 3 + "\t" 
                                else : 
                                    result += " " + self[point][0] * 2+ "\t" 
                            else : 
                                result += " " + self[point][0] + "\t" 
                        else :
                            result += "\t"
                    
            result += "||\t\n"
        
        result += "-" * 122 + "\n"
        result += "-" * 122 + "\n"
        
        return result

    ## checks if checker of color has a checker on bar
    def checkerOnBar(self, color) : 

            if not self[-1] : 
                return False
            else : 
                for ar in self[-1] : 
                    if ar[0] == color : 
                        return True
                return False

       
    ## checks if a certain move from start to dest is possible for the color's throwing
    def moveIsPossible(self, color, start, dest, throw) : 

        ### force moves or no move is possible any more 

        if dest == -1 :
            if not self.allCheckersInHomeBoard(color) : 
                print("You cannot bear off! All of your checkers have to be in home board!")
                return False
            else : 
                if self[start] and self[start][0] == color :

                    if color == 'w' : 
                        if start > 6 :
                            print("You can only bear off checkers on point 1 to 6")
                            return False

                        if not start in throw : 
                            
                            for dice in throw : 
                                if dice > start: 
                                    for i in range(start + 1, 7) : 
                                        if self[i] and self[i][0] == color :
                                            print("There are checkers you have to bear off first!")
                                            return False

                                    return True
                                else: 
                                    continue

                            print("This move is not possible with your throwing")
                            return False

                        else : 
                            return True
                            
                        
                    else :
                        if start < 19 :
                            print("You can only bear off checkers on point 24 to 19")

                        if not start in throw : 
                
                            for dice in throw : 
                                if dice > 25 - start: 
                                    for i in range(19, start) : 
                                        if self[i] and self[i][0] == color :
                                            print("There are checkers you have to bear off first!")
                                            return False

                                    return True
                                else: 
                                    continue

                            print("This move is not possible with your throwing")
                            return False
                            
                        else : 
                            return True  
                
                else :
                    print("None of your checkers is on", start)
                    return False   

        if self.checkerOnBar(color) :
            if not start == -1 :
                print("You have to re-enter a checker on the bar first")
                return False 
            else : 
                if color == 'b' : 
                    if dest > 6 :
                        print("You can only re-enter on point 1 to 6")
                        return False
                    if not dest in throw :
                        print("This move is not possible with your throwing")
                        return False
                    
                else :
                    if dest < 19 :
                        print("You can only re-enter on point 24 to 19")

                    if not (25 - dest) in throw :
                        print("This move is not possible with your throwing")
                        return False

                if not self[dest] : 
                        return True 
                else :

                    if not self[dest][0] == color and self[dest][1] > 1 : 
                        print("You cannot move your checker to", dest)
                        print("This point is occupied by the opponent")

                        return False    
                    else :  
                        return True

        ## TO DO: check if there are any force moves

        if (color == 'b' and start > dest) or (color == 'w' and start < dest): 
            print("You cannot move in this direction")
            return False

        if not abs(start - dest) in throw :
            print("This move is not possible with your throwing")
            return False

        if self[start] and self[start][0] == color : 

            if not self[dest] : 
                return True 

            else :

                if not self[dest][0] == color and self[dest][1] > 1 : 
                    print("You cannot move your checker to", dest)
                    print("This point is occupied by the opponent")

                    return False    
                else :  
                    return True
                    
        else : 
            print("None of your checkers is on", start)
            return False 
        


    ## moves checker of certain color on point 'start' to point 'dest' (overwrites board instance)
    def moveChecker(self, color, start, dest, throw) : 
             

        if dest == -1 : 
            self.bearOff(color, start)
            if color == 'w' : 
                if start in throw : 
                    return start
                else : 
                    for dice in throw : 
                        if dice > start : 
                            return dice

            else : 
                if (25 - start) in throw : 
                    return 25 - start
                else : 
                    for dice in throw : 
                        if dice > (25 - start) : 
                            return dice
        
        elif not self[dest] : 
            self[dest] = [color, 1]
                    
        elif self[dest][0] == color :
            self[dest][1] += 1
            
        else : 

            ## check if there was already one
            if color == 'b' :
                self[-1].append(['w', 1])
                print("A white checker is now on the bar")
            else : 
                self[-1].append(['b', 1])
                print("A black checker is now on the bar")
                    
            self[dest] = [color, 1]

        
        if start == -1 :
            for ar in self[-1] :
                if ar[0] == color : 
                    if ar[1] == 1 :
                        self[-1].remove(ar)
                    else :
                        ar[1] -= 1
                    break
                
            print(self)

            if color == 'b' : 
                return dest
            else :
                return 25 - dest

        else : 
            self[start][1] -= 1
            
            if self[start][1] == 0 : 
                self[start] = []
            
            print(self)

            return abs(start - dest)

        


    def allCheckersInHomeBoard(self, color) :

        if self.checkerOnBar(color) : 
            return False

        if color == 'b' : 
            a = 1 
            b = 19

        else : 
            a = 7
            b = 25
            
        for point in range(a, b): 
            if self[point] and self[point][0] == color : 
                return False

        return True


    ## beared off checkers are removed from board dict
    def bearOff(self, color, point) : 
    
        if self[point][1] == 1 :
            self[point] = []
        else : 
            self[point][1] -= 1

        print(self)

    ## checks if there are any checkers of color on board
    def allCheckersBearedOff(self, color) : 

        if self.checkerOnBar(color) : 
            return False

        for point in self : 
            if self[point] and self[point][0] == color : 
                return False

        return True 

