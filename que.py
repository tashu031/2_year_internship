queue = []
while(True):
    print("""
          1. Add element
          2. Remove element
          3. Display first 3 elements
          4. Display last 3 elements
          5. Display all elements
          6. Exit
          """)
    ch = int ( input("Enter your choice: "))
    if ch ==1:
        queue.append(int(input("enter a  number: ")))
    elif ch ==2:
        if queue:
            queue.pop(0)
        else:
            print("Queue is empty")
    elif ch ==3:
        if queue.count() <3:
            print("Queue has less than 3 elements")
        else:
            print("First 3 elements:", queue[:3])
    elif ch==4:
        if queue.count() <3:
            print("Queue has less than 3 elements")
        else:
            print("Last 3 elements:", queue[-3:])
    elif ch==5:
        print("All elements:", queue)
    elif ch==6:
        break
    else:
        print("Invalid choice : Please enter a valid choice(1-6)")
      