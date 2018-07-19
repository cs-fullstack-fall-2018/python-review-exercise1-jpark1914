#====Phase 0======
#
# print("loop")
#
# #====Phase 1=====
#
# def printLoop():
#
#     userInput = input("Enter something here")
#     print("loop")
# printLoop()
# #====Phase 2=====
#
# def printLoop2():
#     userInput2 = input("Enter something here")
#     print(userInput2)
# printLoop2()
#
# #====Phase 3=====

# def printLoop3():
#     userInput3 = input("Enter something or press 'q' or 0 to quit")
#
#     while(userInput3 != 'q' and userInput3 != 0):
#         print("whooptidy scoop loop")
#         userInput3 = input("Enter something again or press 'q' or 0 to quit")
# printLoop3()

#====Phase 4====

# def printLoop4():
#     userInput4 = input("Enter '1', '2', '3', or press 'q' to quit")
#
#     while( userInput4 != 'q'):
#         print("Please enter '1' '2' '3' or 'q' to quit")
#         userInput4 = input("Enter here")
#         if(userInput4 == '1'):
#             print("1")
#             continue
#         elif(userInput4 == '2'):
#             print('2')
#             continue
#         elif(userInput4 == '3'):
#             print('3')
#             continue
#         else:
#             print("Error")
#
# printLoop4()

#====Phase 5====
def printNumber(number):
    print(number)

def printLoop5():
    userInput5 = input("Enter '1', '2', '3', or press 'q' to quit")

    while( userInput5 != 'q'):
        print("Please enter '1' '2' '3' or 'q' to quit")
        userInput5 = input("Enter here")
        if(userInput5 == '1'):
            printInput()
            continue
        elif(userInput5 == '2'):
            print('2')
            continue
        elif(userInput5 == '3'):
            print('3')
            continue
        else:
            print("Error")
printLoop5()