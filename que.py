# queue = []
# while(True):
#     print("""
#           1. Add element
#           2. Remove element
#           3. Display first 3 elements
#           4. Display last 3 elements
#           5. Display all elements
#           6. Exit
#           """)
#     ch = int ( input("Enter your choice: "))
#     if ch ==1:
#         queue.append(int(input("enter a  number: ")))
#     elif ch ==2:
#         if queue:
#             queue.pop(0)
#         else:
#             print("Queue is empty")
#     elif ch ==3:
#         if queue.count() <3:
#             print("Queue has less than 3 elements")
#         else:
#             print("First 3 elements:", queue[:3])
#     elif ch==4:
#         if queue.count() <3:
#             print("Queue has less than 3 elements")
#         else:
#             print("Last 3 elements:", queue[-3:])
#     elif ch==5:
#         print("All elements:", queue)
#     elif ch==6:
#         break
#     else:
#         print("Invalid choice : Please enter a valid choice(1-6)")
      


l = []
while True :
    print("""
            1. Add element
            2. Remove element
            3. Peek (Top element)
            4. Display all elements
            5. Exit
          """)
 
    ch = int(input("Enter your choice: "))
    if ch ==1 :
        l.append(int(input("Enter a number: ")))
        print("Element added successfully")
    elif ch ==2 :
        if  l ==[] :
            print("Stack is empty")
        else:
            l.pop()
            print("Element removed successfully")
    elif ch ==3 :
        if l:
            print("Top element :" ,l[-1])
        else:
            print("Stack is empty")
    elif ch ==4 :
        print("All elements:", l)
    elif ch ==5 :
        break
    else:
        print("Invalid choice : Please enter a valid choice(1-5)")  

