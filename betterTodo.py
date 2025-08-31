task = []
def load_todo():
    try:
        with open('tasks.txt', 'r')  as file:
            for line in file:
                task.append(line.strip())
    except FileNotFoundError:
        print("File not Found")           



def add_task():
    print(":::::::::::ADD TASKS:::::::::::")
    answer = input("Enter your Task: ")
    task.append(answer)

    with open("tasks.text", "a") as file: #to add the new answer to the file 
        file.write(answer + "\n")      
    print("Task Added Succesfully!!\n")

def view_task():
    print(":::::::::::VIEWING TASKS:::::::::::")
    for index, i in enumerate(task):
        print(f"{index + 1}. {i}\n")
     

def remove_task():
    print(":::::::::::REMOVING TASKS:::::::::::")
    answer = input("Enter name of task you want to enter: ")
    if answer in task:
        print(f"Removing task: {answer}")
        print("Please wait...")
        import time
        time.sleep(2)  # Simulate a delay for removing the task
        task.remove(answer)
        with open("tasks.txt", "w") as file:
            for t in task:                 #to update the deletion
                file.write(t + "\n")
        print("Task have been removed succesfully!\n")
    else:
       print("Task not found. Please enter a valid task name.")
       return

def Todo_menu():
        load_todo()
        while True:
            print(":::::::::::Welcome To My TODO App:::::::::::")
            print("-----What would you like to do?-----")
            print("1. Add Task")
            print("2. View Task")
            print("3. Remove Task")
            print("4. Quit")
            answer = input("Enter Your Choice: ")

            if answer == "1":
                add_task()
                
            elif answer == "2":
                view_task()
            elif answer == "3":
                remove_task() 
            elif answer =="4":
                print("Thank you for tasking with us. See you Later!!")
                quit()
            else:
                print("Incorrect choice")   
                continue 

Todo_menu()            
                        
                   
