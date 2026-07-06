# . Simple Commands (CRUD Operations)
# Add: A quick way to input a task (e.g., todo add "Math Homework" 2026-07-05).
# List: Display tasks in a clean, readable table.
# Complete: Check off a task using a simple ID number (e.g., todo done 3).
# Delete: Remove a task easily if created by mistake.

# Student-Specific Fields
# Course Tag: A simple flag to filter by class (e.g., --course CS101 or -c CS101).
# Due Date: Basic date input that defaults to "today" if left blank.
# Status Indicator: Clear visual markers like [ ] for pending and [X] for completed.
import json

class Task:
    def __init__(self):
        print("Task Manager Initialized")
       
        try:
            with open("task_data.txt", "r") as file:
                self.task_data = json.load(file)
                self.id = len(self.task_data[id]) + 1
        except json.JSONDecodeError:
            print("Error: task_data.txt is corrupted. An empty list is being created.")
            self.task_data = {}
            self.id = 1
        except Exception as e:
            print(f"An unexpected error occurred: {e}. An empty list is being created.")
            self.task_data = {}
            self.id = 1
        finally:
            print("Task Manager is ready to use.")

        
        
                
       
    def add_task(self,task_name , task_due_date = None, task_course_tag = None, task_status = "pending"):
       self.task_data[self.id]= {
           "name": task_name,
           "due_date": task_due_date,
           "course_tag": task_course_tag,
           "status": task_status
       }
       self.id +=1
       
       return self.task_data
    
    
    def list_task(self):
        print("\nTasks:")
        if not self.task_data:
            print("No tasks available.")
            return
        print("--------Your Tasks---------")
        for task_id, task_info in self.task_data.items():
            print(f"ID:\t{task_id}\nStatus:\t{task_info['status']}\nName:\t{task_info['name']}\nDue:\t{task_info['due_date']}\nCourse:\t{task_info['course_tag']}")
            print("----------------------------")

    def complete_task(self):
        while True:
            try:
                id = input("Enter task ID to complete: ")
                if id in self.task_data.keys():
                    self.task_data[id]["status"] = "completed"
                    break
                elif int(id) in self.task_data.keys():
                    self.task_data[int(id)]["status"] = "completed"
                    break
                else:
                    print(f"Task ID {id} does not exist. Please enter a valid task ID.")
            except (KeyError, ValueError) :
                print(f"Task ID {id} does not exist or is invalid. Please enter a valid task ID.")
            
        
            



       

    def delete_task(self):
         while True:
            try:
                id = input("Enter task ID to delete: ")
                if id in self.task_data.keys():
                    del self.task_data[id]
                    break
                elif int(id) in self.task_data.keys():
                    del self.task_data[int(id)]
                    break
                else:
                    print(f"Task ID {id} does not exist. Please enter a valid task ID.")
            except (KeyError, ValueError) :
                print(f"Task ID {id} does not exist or is invalid. Please enter a valid task ID.")
            except (KeyError, ValueError) :
                print(f"Task ID {id} does not exist or is invalid. Please enter a valid task ID.")
        
    def save_task(self):
        try:
            with open("task_data.txt", "w") as file:
                json.dump(self.task_data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving tasks: {e}")
          
def main():
    task_manager = Task()#here task_manager is an instance or an object of the Task class

    while True:
        print("\nStudent Task Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ").lower()
        

        if choice == '1':
            task_name = input("Enter task name: ").capitalize()
            task_due_date = input("Enter due date (YYYY-MM-DD) or leave blank for today: ")
            task_course_tag = input("Enter course tag (e.g., CS101): ").upper()
            if task_due_date == "":
                task_due_date = None
            if task_course_tag == "":
                task_course_tag = None
            task_manager.add_task(task_name, task_due_date, task_course_tag)
            print(f"Task '{task_name}' added successfully.")
            task_manager.save_task()  # Save after adding a task
    

        elif choice == '2':
            task_manager.list_task()
            task_manager.save_task()  # Save after listing tasks
           


        elif choice == '3':
            task_manager.complete_task()
            task_manager.save_task()  # Save after completing a task

        elif choice == '4':
            task_manager.delete_task()
            task_manager.save_task()  # Save after deleting a task
            

        elif choice == '5':
            task_manager.save_task()
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

main()
    