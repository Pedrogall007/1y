import json
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check():
    try:
        with open('data.json', 'r') as f:
            tasks = json.load(f)
            return tasks
    except FileNotFoundError:
        print("File not found. Creating a new one.") 
        return []

def add_task(task_name): 
    tasks = check()
    id_numbers = []
    
    try:
        for t in tasks:
            p = int(t["id"])
            id_numbers.append(p)
            
        if len(id_numbers) <= 0:
            new_number = 1
        else:
            new_number = max(id_numbers) + 1              
            
        new_id = f'{new_number:05d}'
        tasks.append({"id": new_id, "task": task_name, "status": "Pending"})
            
        with open('data.json', 'w') as f:
            json.dump(tasks, f, indent=4)
            
        print('\nTask added successfully!')
    except Exception:
        print('Error. Please try again.')

def list_task():
    tasks = check()
    if len(tasks) <= 0:
        print('The file does not exist or is empty.')
    else:
        for task_item in tasks:
            print(f'{task_item["id"]} - {task_item["task"]} - Status: {task_item["status"]}')

def remove_task(user_id):
    try:    
        tasks = check()  
        id_search = f'{user_id:05d}'
        
        for t in tasks:
            if t['id'] == id_search:
                tasks.remove(t)
                break 

        with open('data.json', 'w') as f:
            json.dump(tasks, f, indent=4)
            
        print('\nTask deleted successfully')
    except Exception:
        print('Error. Please try again.')    

def switch(user_id):
    try:
        tasks = check()
        id_search = f'{user_id:05d}' 
        
        for t in tasks:
            if t["id"] == id_search:
                if t["status"] == 'Pending':
                    t["status"] = 'Completed'    
                else:
                    t["status"] = 'Pending'
                break             
                
        with open('data.json', 'w') as f:
            json.dump(tasks, f, indent=4)
            
        print('\nTask status changed successfully')
    except Exception:
        print('Error. Please try again.')

def main():
    while True:
        print('\n--- TO-DO LIST ---')   
        print('1 - List tasks')
        print('2 - Add task')
        print('3 - Remove task')
        print('4 - Switch task status')
        print('5 - Exit program')
        
        choice = input('\nWhich option do you choose? ')
        
        if choice == "1":
            clear()
            print('\nListing tasks:\n') 
            list_task()        
            
        elif choice == '2':
            clear()
            which_task = input('Which task do you want to add? ')
            add_task(which_task)
            
        elif choice == '3': 
            clear()
            list_task()
            try:
                task_id = int(input('\nWhich ID do you want to remove? '))
                remove_task(task_id)
            except ValueError:
                print('\nInvalid input! Please enter a number.')
                
        elif choice == '4':
            clear()
            list_task()
            try:
                task_id = int(input('\nWhich ID do you want to alter? '))
                switch(task_id)
            except ValueError:
                print('\nInvalid input! Please enter a number.')
                
        elif choice == '5':
            clear()
            print('Exiting program...')
            break
            
        else:
            print('\nInvalid option, try again.')

main()            

