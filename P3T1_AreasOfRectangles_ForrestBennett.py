#Areas Of Rectangles
#09/24/18
#CTI-110 P3T1 - Areas of Rectangles
#Forrest Bennett

#Find the Length of Rectangle 1.
Length_Rect1 = int(input('enter the length of rectangle 1:'))

#Find the Width of Rectangle 1.

Width_Rect1 = int(input('enter the width of rectangle 1:'))

#Find the Area for Rectangle 1.

Area_Rect1 = Length_Rect1 * Width_Rect1

#Display the Area for Rectancgle 1.

print(' The area of Rectangle 1 is', Area_Rect1) 

#Find the Length of Rectangle 2.

Length_Rect2 = int(input('Enter the length of rectangle 2:'))

#Find the width of Rectangle 2.

Width_Rect2 = int(input('Enter the width of rectangle 2:'))

#Find the Area of Rectangle 2.
Area_Rect2 = Length_Rect2 * Width_Rect2

#Display the Area of Rectangle 2.

print(' The area of Rectangle 2 is', Area_Rect2)

#Display if the Rectangles are less than, greater than, or equal to each other.
if Area_Rect1 > Area_Rect2:
    print('Rectangle 1 has more area')

elif Area_Rect1 < Area_Rect2:
    print('Rectangle 2 has more area')

else:
    print(' The rectangles are equal!')
