import json
import os

# read, remove, write and list
def clear():
    os.system('cls')

def check():
    try:
        with open('data.json', 'r') as f:
            tasks = json.load(f)
            return tasks
    except FileNotFoundError:
        print("File not found. Creating a new one.") 
        return []
def add_task(task): 
    tasks = check ()
    ids_numero = []
    try:
        for t in tasks:
            p = int(t["id"])
            ids_numero.append(p)
        if len(ids_numero)<=0:
            numero = 1
        else:
            numero = max(ids_numero) + 1               
        id = f'{numero:05d}'
        tasks.append({"id": id, "task": task, "status": "Pendente"})
            
        with open('data.json', 'w') as f:
            json.dump(tasks, f)
    except:
        print ('Error, try again.')

def list_task():
    task = check()
    if len(task) <= 0:
        print ('The file does not exist or is empty.')

    else:
        for tarefa in task:
            print (f'{tarefa ["id"]} - {tarefa ["task"]} - {tarefa ["status"]}')
def remove_task(user_id):
    try:    
        task = check()  
        id_search = f'{user_id:05d}'
        for t in task:
            if t ['id'] == id_search:
                task.remove(t)
                break

        with open('data.json', 'w') as f:
            json.dump(task, f)
        print ('\nTask deleted successfully')
    except:
        print('Error, try again.')    
def switch(user_id):
    try:
        task = check()
        id_search = f'{user_id:05d}' 
        for t in task:
            if t ["id"] == id_search:
                if t["status"] == 'Pendente':
                    t["status"] = 'Concluido'    
                    break              
                else:
                    t["status"] = 'Pendente'
                    break             
        with open('data.json', 'w') as f:
            json.dump(task, f)
    except:
        print ('Error. Please try again')

while True:
    print ('\nHome\n')   
    print ( '1 - list task')
    print ('2 - Exit program')
    print ('3 - add task')
    print ('4 - remove task')
    print ('5 - switch task statuses')
    choise = input('\nWhich option do you choose? ')
    if choise == "1":
         clear()
         print ('\nlisting the tasks:\n') 
         list_task()        
    elif choise == '2':
         clear()
         print ('Exit')
         break
    elif choise == '3':
         clear()
         which = input ('Which task you wanna add ? ')
         add_task(which)
    elif choise == '4': 
         clear()
         print('\n')   
         list_task()
         id = int(input ('\nwhich one to exclude?'))
         remove_task(id)
    elif choise == '5':
         clear()
         list_task()
         id = int(input ('\nwhich one to alter?'))
         switch(id)
    else:
        print ('\noption invalid, try again.')
            



        


