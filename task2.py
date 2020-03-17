import json

TASKS_FILE = 'tasks.json'
'''
Chapter II 
A script to manage the task list. 
Provides a text user interface with options to list, add, edit and delete tasks. 
The tasks are identified by a hash value calculated from its contents
'''

print('\t\t\t\tTask List Editor')
print('\nWelcome to Your Tasks.')
print('The following list can be readily edited.')
print('You can view, add, edit and remove the tasks with the following commands:')
print('\n')
print('     '+'View:    In order to view the list enter the following command:')
print('\n\t\t\t\t print_tasks()\n')
print('     '+'Add:     In order to add new element to the list enter the following command:')
print('\n\t\t\t\t add_task()\n')
print('     '+'Edit:    In order to edit a certain task from the list enter the following command:')
print('\n\t\t\t\t edit_task()\n')
print('     '+'Remove:  In order to remove a certain task from the list enter the following command:')
print('\n\t\t\t\t remove_task()\n')

tasks = [
  ['Code Python', '3', '15', '15', '10', 'Train necessary python skills to get the job and be successful'],
  ['Code Python', '3', '15', '15', '10', 'Train necessary python skills to get the job and be successful'],
  ['Meeting', '3', '17', '15', '10', 'group meeting'],
  ['Interview', '3', '20', '12', '20', 'Rise and shine, nail the interview'],
  ['Meeting', '4', '1', '17', '30','group meeting'],
  ['Interview', '4', '5', '8', '20', 'Rise and shine, nail the interview'],
  ['Job offer', '4', '6', '9', '45',  'Accept python Job offer at Gliwice'],
  ['Work', '5', '1', '10', '0', 'Work your ass off in Python and be succesful'],
  ['Cycling', '5', '2', '6', '10', 'Train to stay mentally and physically healthy'],
  ['Work', '5', '3', '10', '10', 'Work your ass off in Python and be succesful'],
  ['Cycling', '6', '1', '6', '05', 'Train to stay mentally and physically healthy'],
  ['Work', '6', '2', '10', '01', 'Work your ass off in Python and be succesful'],
  ['Cycling', '6', '3', '6', '01', 'Train to stay mentally and physically healthy'],
  ['Work', '6', '4', '10', '10', 'Work your ass off in Python and be succesful']]

  
with open(TASKS_FILE, 'w') as json_file:
  json.dump(tasks, json_file)
  
  
with open(TASKS_FILE) as f:
  tasks = json.load(f)
  
  
def print_tasks():
    """
    Print all the tasks for the given date from the given list of tasks.
    """
    print('List of current tasks:')
    count=0
    for task in tasks:
        count += 1
        num = str(count)
        print('                        '+'     Task number '+num)
        print('')
        print('  Task Name:        '+task[0])
        print('  Date and Time:    '+task[1]+'-'+task[2]+' at '+task[3]+':'+task[4])
        print('  Description:      '+task[5])
        print('')
        print('')
    print('End of the list.')
    
    
def add_task():
    '''
    Simple function adds another element to the Task list, requires input from the user.
    '''
    print('In order to add another task please fill in the following information')
    a = str(input('Step 1: Please write a name of the task: '))
    b = str(input('Step 2: Enter month: (1-12): '))
    c = str(input('Step 3: Enter day (between 1 and 31): '))
    d = str(input('Step 4: Please enter the deadline/appointed hour: (0-23) '))
    e = str(input('Step 5: Please enter the deadline/appointed minutes: (0-59)'))
    f = str(input('Step 6: Please write a short description of the task:'))

    if a and b and c and d and f:
        tasks.append([a,b,c,d,e,f])
    
    print('\n\t\tUPDATE! New task added: '+a+' - '+f+'\n\n') 
  
  
def edit_task():
    '''
    A task edtior function. Takes exising list element at a specified index and changes are aplied via user input.
    '''
    choose = 0
    print('In order to make edits to an exisitng task element please fill in the following information')
    while choose == 0:
        try:
            num = int(input('Step 1: Please choose the Number of the Task you wish to make changes to: '))
            if num in range(1,len(tasks)+1):
                choose = 1
        except ValueError:
            print('Please provide an integer! Try again..')
    n = num - 1
    en = str(num)
    tasks[n][0] = str(input('Step 1: Please write a new name of task '+en+': '))
    tasks[n][1] = str(input('Step 2: Enter month: (1-12): '))
    tasks[n][2] = str(input('Step 3: Enter day (between 1 and 31): '))
    tasks[n][3] = str(input('Step 4: Please enter the deadline/appointed hour: (0-23) '))
    tasks[n][4] = str(input('Step 5: Please enter the deadline/appointed minutes: (0-59)'))
    tasks[n][5] = str(input('Step 6: Please write a new description of the task '+en+': '))
        
    print('\n\t\tUPDATE! Task no.'+en+' has been succesfully changed!\n\n') 
    

def remove_task():
    '''
    A function that deletes an element at a specified index.
    '''
    choose = 0
    while choose == 0:
        try:
            d = int(input('Please enter the number of a Task You wish to delete: '))
            if d in range(1,len(tasks)+1):
                choose = 1
        except ValueError:
            print('Please provide an integer! Try again..')
    n = d-1
    no = str(d)
    del tasks[n]
    print('\n\t\tUPDATE! Task no. '+no+' has been succesfully deleted!\n\n') 
