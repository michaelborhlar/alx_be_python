task = str(input("Enter your task: "))

task_priority = str(input("Priority (high/medium/low): "))

time_bound = str(input("Is it time-bound? (yes/no): "))


match task_priority:
    case 'high':
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {task_priority} priority task. Consider completing it when you have free time.")
            
        
    case 'medium':
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {task_priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
        else:   
            print(f"Note: '{task}' is a {task_priority} priority task. Consider completing it when you have free time.")
        
        
        


