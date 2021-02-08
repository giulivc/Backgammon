class Board (dict) : 

    def __init__(self, *args, **kwargs) : 
        super().__init__(*args, **kwargs)
        for i in range(1, 25) : 
            if not i in self : 
                self[i] = []
        self[-1] = []
    
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

    def checkerOnBar(self, color) : 

            if not self[-1] : 
                return False
            else : 
                for ar in self[-1] : 
                    if ar[0] == color : 
                        return True
                return False

       

    def moveIsPossible(self, color, start, dest, throw) : 

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
                    if dest < 19 :
                        print("You can only re-enter on point 24 to 19")

        ## check if there are any force moves

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
        


    def moveChecker(self, color, start, dest) : 
        
        self[start][1] -= 1
            
        if self[start][1] == 0 : 
            self[start] = []
                
        if not self[dest] : 
            self[dest] = [color, 1]
                    
        elif self[dest][0] == color :
            self[dest][1] += 1
            
        else : 

            if color == 'b' :
                self[-1].append(['w', 1])
                print("A white checker is now on the bar")
            else : 
                self[-1].append(['b', 1])
                print("A black checker is now on the bar")
                    
            self[dest] = [color, 1]

        print(self)


    #def allCheckersInHomeBoard(self, color) :

    #def startBearingOff(self, color) : 
