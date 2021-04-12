import math
# so i can use sqrt, pi, etc

import sys
#so I can use sys.exit


def com_area_triangle(xa, ya, xb, yb, xc, yc):
    # def a function that takes data from the vertexes of the triangle and calculates where the COM is
    # I consider point f[xf,yf] the center of mass
    global xf, yf, area, areaxf, areayf
    xf = (xa + xb + xc) / 3
    yf = (ya + yb + yc) / 3
    f = [xf, yf]

    # doint the area now
    a = math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2)
    b = math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)
    c = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    A = [xa, ya]
    B = [xb, yb]
    C = [xc, yc]

    # computing the area times the coordinae
    areaxf = area* xf
    areayf = area* yf

    print("The area of the triangle with verteces A", A, ", B", B, " and C", C, " is ", area)
    print("The center of mass is in point F", f)
    # definition of function over


def com_area_parallelogram(xa, ya, xb, yb, xc, yc, xd, yd):
    # def a function that calculates the com for a parallelogram
    # consider point F[xf,yf] to be COM
    global xf, yf, area, areaxf, areayf
    xf = (xa + xb + xc + xd) / 4
    yf = (ya + yb + yc + yd) / 4
    f = [xf, yf]

    # doing the area now
    a = math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2)
    b = math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)
    c = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    p = (a + b + c) / 2
    half_area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    area = 2 * half_area
    vertex_a = [xa, ya]
    vertex_b = [xb, yb]
    vertex_c = [xc, yc]
    vertex_d = [xd, yd]

    # computing the area times the coordinae
    areaxf = area * xf
    areayf = area * yf

    print("The area of the parallelogram with verteces A", vertex_a, ", B", vertex_b, ", C", vertex_c, " and D ",
          vertex_d, " is ", area)
    print("The center of mass is point e", f)
    # defined the f. that calculates the COM of a parallelogram


def com_area_circle(xc, yc, x1, y1, x2, y2):
    # a f. that calculates the COM of a circular shape using its center and two endpoints
    r1 = math.sqrt((x1 - xc) ** 2 + (y1 - yc) ** 2)
    r2 = math.sqrt((x2 - xc) ** 2 + (y2 - yc) ** 2)
    h = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    center = [xc, yc]

    # checking if they are points on a circle or not
    if (r1 == r2):
        radius = r1
        global xf, yf, area, areaxf, areayf
        if x1 == x2:
            yf = yc
            x_com = (2 * math.pi * math.sin(math.pi/2)) / (3 * math.pi/2)
            if y1 > yc or y2 > yc:
                xf = xc + x_com
            elif y1 < yc or y2 < yc:
                xf = xc - x_com
            else:
                print("Are you sure you introduced the coordinates right? Try again 1. alfa=PI/2. calc y")

        elif y1 == y1:
            xf = xc
            x_com = (2 * math.pi * math.sin(math.pi / 2)) / (3 * math.pi / 2)

            if x1 > xc or x2 > xc:
                yf = yc + x_com
            elif x1 < xc or x2 < xc:
                yf = yc - x_com
            else:
                print("Are you sure you introduced the coordinates right? Try again 1. alfa=PI/2. calc x")

        else:
            # declaring alfa to be 0 because it's simpler than unlocal-ing it for every if case
            alfa = 0

            #seeing which angle we are talking about
            t = input("Is it the smaller of the greater angle?"
                      "\nType s or g")

            if t == "s":
                alfa = (math.arcsin(h / radius)) / 2
            elif t == "g":
                alfa = math.pi + (math.arcsin(h / radius)) / 2
            else:
                print("Wrong letter")

            x_com = (2 * math.pi * math.sin(alfa)) / (3 * alfa)
            # because alfa is half of the total angle, y_com=x_com
            f_coord_no = x_com * math.cos(alfa)
            # checking where the points are

            if x1 > xc or x2 > xc:
                xf = xc + f_coord_no
            elif x1 < xc or x2 < xc:
                xf = xc - f_coord_no
            else:
                print("Are you sure you introduced the coordinates right? Try again 2.alfa = any PI.x")

            if y1 > yc or y2 > yc:
                yf = yc + f_coord_no
            elif y1 < yc or y2 < yc:
                yf = yc - f_coord_no
            else:
                print("Are you sure you introduced the coordinates right? Try again 2. alfa = any PI.y")
            # end of checking

        f = [xf, yf]
        area = area_circle * (alfa / (2 * math.pi))

        # computing the area times the coordinae
        areaxf = area * xf
        areayf = area * yf

        print("The are of the circular sector with the center in ", center, "radius ", radius," and angle ", alfa, " is ", area)
        print("The center of mass is F", f)

    else:
        print("These aren't points on the radius of the circle with the center in ", center)
    # end of defining

# defining the function for the program

def choice():
    q = int(input(
                  "Press 1 for triangles "
                  "\nPress 2 for parallelograms"
                  "\nPress 3 for circles and circular sectors"))
    if q == 1:
        print("You selected triangles")
        # input the coordinates
        xa = float(input("The x coordinate of point A is: "))
        ya = float(input("The y coordinate of point A is: "))
        xb = float(input("The x coordinate of point B is: "))
        yb = float(input("The y coordinate of point B is: "))
        xc = float(input("The x coordinate of point C is: "))
        yc = float(input("The y coordinate of point C is: "))

        # now we call the function
        com_area_triangle(xa, ya, xb, yb, xc, yc)


    elif q == 2:
        print("You selected parallelograms")
        xa = float(input("The x coordinate of point A is: "))
        ya = float(input("The y coordinate of point A is: "))
        xb = float(input("The x coordinate of point B is: "))
        yb = float(input("The y coordinate of point B is: "))
        xc = float(input("The x coordinate of point C is: "))
        yc = float(input("The y coordinate of point C is: "))
        xd = float(input("The x coordinate of point D is: "))
        yd = float(input("The y coordinate of point D is: "))

        # now we call the function
        com_area_parallelogram(xa, ya, xb, yb, xc, yc, xd, yd)

    elif q == 3:
        print("You selected circles and circular sectors")
        xc = float(input("The x coordinate of the center is : "))
        yc = float(input("The y coordinate of the center is : "))
        x1 = float(input("The x coordinate of point 1 is: "))
        y1 = float(input("The y coordinate of point 1 is: "))
        x2 = float(input("The x coordinate of point 2 is: "))
        y2 = float(input("The y coordinate of point 2 is: "))

        # now we call the function
        com_area_circle(xc, yc, x1, y1, x2, y2)

    else:
        raise Exception("Wrong number")


# starting the program. First finding how many bodies we have
n = int(input("How many bodies are there?"))

print("Welcome to Center of Mass Calculator v2")

for i in range (0, n):
    choice()
    j = i + 1
    # putting the data into a matrix
    data = []
    body = [area, xf, yf, areaxf, areayf]
    data.append(body)
    print("Body number: ", j, " ", data[i])
    # computing the sums for the formula x=sum(area*xi)/sum(area)

sum_area = sum(data[:,1])
sum_area_times_x = sum(data[:, 4])
sum_area_times_y = sum(data[:, 5])
# calculating the final center of mass
x_final = sum_area_times_x/sum_area
y_final = sum_area_times_y/sum_area
center_of_mass=[x_final, y_final]
print("The center of mass for this system of ",n," bodies is ", center_of_mass)




