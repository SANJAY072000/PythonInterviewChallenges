from db_helper import *
create_table()
while 1:
    print("\n 1. Insert new task in todo list")
    print("\n 2. View the todo list")
    print("\n 3. Delete the task from todo list")
    print("\n 4. Exit")
    ch = int(input("\n Enter your choice : "))
    if ch == 1:
        task = input("\n Enter your todo : ")
        data_entry(task)
    elif ch == 2:
        print_data()
    elif ch == 3:
        index = int(input("\n Enter the index of the task to delete : "))
        delete_task(index)
    elif ch == 4:
        break
    else:
        print("\n Invalid choice")
close_cursor()













