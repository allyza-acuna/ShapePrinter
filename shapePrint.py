def drawSquare(side):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawRectangle(length,width):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################	

def drawRightTriangle(height):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################

def drawDiamond(height):
	############################################################################
	# TODO: Implement this code segment                                        #
	############################################################################
	pass
	############################################################################
	# END CODE HERE					                                           #
	############################################################################
def drawClockwiseSpiral(side):
        arr = []
        direction = 0
        for i in range(0, side):
                sad = []
                for x in range(0, side):
                        sad.append(0)
                arr.append(sad)

        for i in range(0, side):
                arr[i][0] = 1
                arr[i][side-1] = 1
                arr[side-1][i] = 1
                
        op = 0 ##must go until 2, 2nd repeat
        di = 0 ##4 directions
        allowance = 0
        upall = 0
        dall = 0
        rightall = 0
        leftall = 2
        for i in range(side-2, 0, -2):
                for n in range(0,2):
                        for x in range(0, i):
                                if(di == 0):
                                        arr[side-upall-x-1][upall] = 1
                                elif(di == 1):
                                        arr[rightall+2][x+rightall] = 1
                                elif(di == 2):
                                        arr[dall+2+x][side-1-dall-2] = 1
                                else:
                                        arr[side-1-leftall][side-1-x-leftall] = 1
                        if(di == 0):
                                upall += 2
                        elif(di == 1):
                                rightall+=2
                        elif(di == 2):
                                dall+=2
                        else:
                                leftall+=2
                        di+=1
                        di = di%4
        for i in arr:
                l = ""
                for x in i:
                        if(x == 0):
                                l = l+" "
                        else:
                                l = l+"*"
                print(l)
print("----------------------------Shape Printer----------------------------")
while True:
	resp = 0
	while True:
		print("Which shape do you want to draw?")
		print("[1] - Square")
		print("[2] - Rectangle")
		print("[3] - Right Triangle")
		print("[4] - Diamond")
		print("[6] - Clockwise Spiral")
		print("[7] - Exit")
		try:
			resp = int(input("Response: "))
			if resp >= 1 and resp <= 6:
				break
			else:
				print("Response must be from 1 to 5")
		except ValueError:
			print("Input must be a number")

	if resp == 1:
		side = int(input("Enter side length: "))
		drawSquare(side)
	elif resp == 2:
		length = int(input("Enter length: "))
		width = int(input("Enter width: "))
		drawRectangle(length,width)
	elif resp == 3:
		height = int(input("Enter height: "))
		drawRightTriangle(height)
	elif resp == 4:
		height = int(input("Enter height: "))
		drawDiamond(height)
	elif resp == 6:
		height = int(input("Enter height: "))
		drawClockwiseSpiral(height)
	elif resp == 5:
		break

