#Level 4+

from math import *                                                                           #Imported all functions from math which some will be utilized later.
def XYVSeperation(ans):                                                                      #Defining function "XYVSeperation", used in order to seperate the form (x, y)V
    ans = ans.replace(" ","")                                                                #Takes out all the spaces within the input to simplify the process
    if ans.count(",") and ans.count("(") and ans.count(")") and ans.find("(") == 0:          #Makes sure the input contains all the symbols within the correct input format. Otherwise it does not pass this point
        x = ans[ans.find("(") + 1:ans.find(",")]                                             #Pulls the x-value out of the input, leaving any symbols stays with it
        y = ans[ans.find(",") + 1:ans.find(")")]                                             #Pulls the y-value out of the input, leaving any symbols stays with it
        xCompare = x.replace("-","").replace("+","")                                         #Removes any math symbols such as "-" and "+" from x
        yCompare = y.replace("-","").replace("+","")                                         #Removes any math symbols such as "-" and "+" from y
        if xCompare.isdigit() == True and yCompare.isdigit() == True:                                       #Checking if the inputs were infact digits and not letters or symbols
            x = int(x)                                                                                      #Puts the value of x in to integar form
            y = int(y)                                                                                      #Puts the value of y in to integar form
            v = ans[ans.find(")") + 1::]                                                                    #Finds to see what the value of v is
            if v.isalpha() == False:                                                                        #Now checks to see if v is infact a letter
                print("Please make sure your V value is a letter and either A, B, C, D, or V. Please do not add more than 1 set of bracket!")             #Informs the user of their mistake
            else:
                if Ax <= x <= Cx and Ay <= y <= Cy:                                                         #Making sure the given x and y is within the rectangle
                    typeOfInput = False
                    print ("Your coordinates lies within this rectangle.")      #Indicating to the user that the position given is fine to proceed
                    if v == "A":        #Checking if v is vertice A
                        Vx = Ax
                        Vy = Ay
                    elif v == "B":      #Checking if v is vertice A
                        Vx = Bx
                        Vy = By
                    elif v == "C":      #Checking if v is vertice A
                        Vx = Cx
                        Vy = Cy
                    elif v == "D":      #Checking if v is vertice A
                        Vx = Dx
                        Vy = Dy
                    elif v == "V":      #Checking if v is V
                        typeOfInput = True
                        print ("The point of your choice (%i,%i), is closest to vertice %s." %(x, y, findClosestVertice(x, y)))                     #Giving the user the output of the closest Vertice
                    else:
                        typeOfInput = True
                        print ("However, your choice of a vertice was neither A, B, C, D or V (making sure it is caplized). Please try again.")     #Informing the user of their errors, asks to try again
                    if typeOfInput == False:
                        print ("The point of your choice (%i,%i), is %0.2f units away from vertice %s." %(x, y, pointsDistance(x, y, Vx, Vy), v))   #Giving the user the distance between their point and the vertice of choice
                else:
                    print ("Your coordinates does not lie within this rectangle.")  #Informing the user of they incorrect formating
        else:
            print ("Please input in the correct formating. (input x and y in terms of digits.)")                        #Informing the user of they incorrect formating
    else:
        print ("Please input in the format (x,y) V. Making sure to include brackets and commas.")                                #Informing the user of they incorrect formating
def pointsDistance(x1, y1, x2, y2):                 #Function to find distance between two points
    d = float(sqrt((x2 - x1)**2 + (y2 - y1)**2))    #Uses the formula to find out distance
    return d
def findClosestVertice(x1, y1):                 #Creating function to find the closest Vertice when V is given
    minDistance = pointsDistance(x1, y1, Ax, Ay)
    ans = "A"
    if minDistance > pointsDistance(x1, y1, Bx, By):
        minDistance = pointsDistance(x1, y1, Bx, By)
        ans = "B"
    if minDistance > pointsDistance(x1, y1, Cx, Cy):    
        minDistance = pointsDistance(x1, y1, Cx, Cy)
        ans = "C"        
    if minDistance > pointsDistance(x1, y1, Dx, Dy):    
        minDistance = pointsDistance(x1, y1, Dx, Dy)
        ans = "D"
    return ans                                  #Returns the shortest distance
Ax = -5          #Asigning the point for A
Ay = -5
length = 17     #Assigning the length of rectangle
width = 21      #Assigning the width of rectangle
Bx = Ax + length
By = Ay
Cx = Ax + length
Cy = Ay + width
Dx = Ax
Dy = Ay + width
print ("The rectangle has corners A(%i,%i), B(%i,%i), C(%i,%i), D(%i,%i)." %(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy))
XYVSeperation(input("Please enter the X and Y coordinates of your point, followed by a vertices of your choice in the form (x,y) V \n(V being either \"A, B, C, D or V\". Inputting V will result in the return of the closest vertice to your point): "))                                                                       #Excecutes the main program after assigning the rectangle
