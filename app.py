def task():
    list_ = []
    print("---Well Come to the app task managment app---")
    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1 , total_task+1):
        task_name = input(f"Enter task {i} = ")
        list_.append(task_name)
    print(f"Todays task are\n{list_}")

    while True:
        operation  = int(input("Enter 1-Add\n2-Update\n3-Delete\n4View\n5-Exit/Stop = "))   
        if operation == 1:
            add = input("Enter task you want to add = ")
            list_.append(add)
            print(f"task {add} has been successfully added.. ")

        elif operation == 2:
            update_val = input("Enter the task name you want to update = ")
            if update_val in list_:
                up = input("Enter the new task = ")
                ind = list_.index(update_val)
                list_[ind] = up
                print(f"update task {up} ")  

        elif operation == 3:
            del_val = input("Which task you want to delete = ") 
            if del_val in list_:
                ind = list_.index(del_val)
                del list_[ind]
                print(f"task {del_val} has been deleted..")

        elif operation == 4:
            print(f"total task = {list_}")

        elif operation == 5:
            print("closing the program...")
            break 
        else:
            print("invalid input")     


task()                