import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 10, 1) #0,1,2,3,4,5,6,7,8,9
y=x**2-5*x+6
plt.figure(facecolor='lightblue')
plt.title("Jooniese pealkiri")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)
plt.plot(x, y, color='blue', linestyle='-', marker='D', markersize=8, label="Joonise joon")
plt.show()

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [16, 9, 4, 1, 0]

plt.plot(x, y1, linestyle='-', marker='o', color='blue',
                 markersize=8, markerfacecolor='lightblue', label="Tõusev joon")
plt.plot(x, y2, linestyle='--', marker='x', color='green',
                 markersize=8, label="Laskuv joon")

plt.title("Kahe joone näide")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.legend()
plt.grid(True)
plt.show()


x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
# plt.plot(x, y)
plt.title("Kahe joone näide")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.legend()
plt.grid(True)
plt.show()

while True:
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]

    plt.title("Kahe joone näide")
    plt.xlabel("x telg")
    plt.ylabel("y telg")

    choice = int(input("putting into work: "))
    if choice == 1:
        plt.plot(x, y)
        plt.show
        continue

    elif choice == 2:
        plt.scatter(x, y)
        plt.show()
        continue

    elif choice == 3:

        plt.bar(x, y)
        plt.show()
        continue

    elif choice == 4:

        plt.hist(x, y)
        plt.show()
        continue

    elif choice == 5:

        plt.pie(x, y)
        plt.show
        continue

# plt.figure(facecolor='lightblue')
# plt.title("Jooniese pealkiri")
# plt.xlabel("x telg")
# plt.ylabel("y telg")
# plt.grid(True)

# x=0
# x1=9
# y=2/27*x**2-3
# y1=2/27*x1**2-3
# plt.plot(x, y, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")
# plt.plot(x1, y1, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")
# plt.show()

# esimene ülasane
    elif choice == 6:
        x=np.arange(0, 10)
        y=2/27*x**2-3
        plt.plot(x, y, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

        x1=np.arange(-10, 1)
        y1=0.04*x1**2-3
        plt.plot(x1, y1, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

        x2=np.arange(-9, -2)
        y2=2/9*(x2+6)**2+1
        plt.plot(x2, y2, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

        x3=np.arange(-3, 10)
        y3=-1/12*(x3-3)**2+6
        plt.plot(x3, y3, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

        x4=np.arange(5, 9.3).round(1) # puts into place normally ig (spoiler: it doesnt)
        y4=1/9*(x4-5)**2+2
        plt.plot(x4, y4, color='red', linestyle='-', marker='o', markersize=8, label="Joonise joon")

        x5=np.arange(5, 9.5).round(1) # puts into place normally ig
        y5=1/8*(x5-7)**2+1.5
        plt.plot(x5, y5, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

        x6=np.arange(-13, -8)
        y6=-0.75*(x6+11)**2+6
        plt.plot(x6, y6, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

        x7=np.arange(-15, -12)
        y7=-0.5*(x7+13)**2+3
        plt.plot(x7, y7, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")
        # plt.show()

        x8=np.arange(-15, -9, 1)
        solvingproblem1=x8-x8
        y8=1+solvingproblem1
        plt.plot(x8, y8, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

        x9=np.arange(3, 5, 1)
        solvingproblem2=x9-x9
        y9=3+solvingproblem2
        plt.plot(x9, y9, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")
        plt.show()
        continue
    else:
        print("Bye bye! :3")
        break


# x8 = np.arange(-15, -10, 1)
# x9 = np.arange(3, 4, 1)
# y8 = [3]
# y9 = [1]

# plt.plot(x8, y8, linestyle='-', marker='o', color='blue',
#                  markersize=8, markerfacecolor='lightblue', label="Joonise joon")
# plt.plot(x9, y9, linestyle='--', marker='x', color='green',
#                  markersize=8, label="Joonise joon")
# plt.show()


# x8=np.arange(-15, -10, 1)
# y8=1
# plt.plot(x8, y8, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

# x9=np.arange(3, 4, 1)
# y9=3
# plt.plot(x9, y9, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")
# plt.show()

