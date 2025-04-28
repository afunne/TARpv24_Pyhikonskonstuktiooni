import matplotlib.pyplot as plt
import numpy as np
# x=np.arange(0, 10, 1) #0,1,2,3,4,5,6,7,8,9
# y=x**2-5*x+6
# plt.figure(facecolor='lightblue')
# plt.title("Jooniese pealkiri")
# plt.xlabel("x telg")
# plt.ylabel("y telg")
# plt.grid(True)
# plt.plot(x, y, color='blue', linestyle='-', marker='D', markersize=8, label="Joonise joon")
# plt.show()

# x = [0, 1, 2, 3, 4]
# y1 = [0, 1, 4, 9, 16]
# y2 = [16, 9, 4, 1, 0]

# plt.plot(x, y1, linestyle='-', marker='o', color='blue',
#                  markersize=8, markerfacecolor='lightblue', label="Tõusev joon")
# plt.plot(x, y2, linestyle='--', marker='x', color='green',
#                  markersize=8, label="Laskuv joon")

# plt.title("Kahe joone näide")
# plt.xlabel("x telg")
# plt.ylabel("y telg")
# plt.legend()
# plt.grid(True)
# plt.show()


# x = [0, 1, 2, 3, 4]
# y = [0, 1, 4, 9, 16]
# # plt.plot(x, y)
# plt.title("Kahe joone näide")
# plt.xlabel("x telg")
# plt.ylabel("y telg")
# plt.legend()
# plt.grid(True)
# plt.show()

# while True:
#     x = [0, 1, 2, 3, 4]
#     y = [0, 1, 4, 9, 16]

#     plt.title("Kahe joone näide")
#     plt.xlabel("x telg")
#     plt.ylabel("y telg")

#     choice = int(input("putting into work: "))
#     if choice == 1:
#         plt.plot(x, y)
#         plt.show
#         continue

#     elif choice == 2:
#         plt.scatter(x, y)
#         plt.show()
#         continue

#     elif choice == 3:

#         plt.bar(x, y)
#         plt.show()
#         continue

#     elif choice == 4:

#         plt.hist(x, y)
#         plt.show()
#         continue

#     elif choice == 5:

#         plt.pie(x, y)
#         plt.show
#         continue
#     else:
#         print("Bye bye! :3")
#         break


plt.figure(facecolor='lightblue')
plt.title("Jooniese pealkiri")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)

# x=0
# x1=9
# y=2/27*x**2-3
# y1=2/27*x1**2-3
# plt.plot(x, y, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")
# plt.plot(x1, y1, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")
# plt.show()

# esimene ülasane 

x=np.arange(0, 9, 1)
y=2/27*x**2-3
plt.plot(x, y, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

x1=np.arange(-10, 0, 1)
y1=0.04*x1**2-3
plt.plot(x1, y1, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")

x2=np.arange(-9, -3, 1)
y=2/9(x2+6)**2+1
plt.plot(x, y, color='blue', linestyle='-', marker='o', markersize=8, label="Joonise joon")
plt.show()