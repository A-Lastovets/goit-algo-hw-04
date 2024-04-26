from pathlib import Path 

def total_salary(file_path) -> tuple:
    total_salary = 0
 
    try:
        file_path = Path("A:/Home_work/goit-algo-hw-04/salary_employees.txt")
        lines = ["Alex Korp,3000", "Nikita Borisenko,2000", "Sitarama Raju,1000"]
 
        with open(file_path, "w", encoding="utf-8") as file:
            file.write('\n'.join(lines))
        
        with open(file_path, "r", encoding="utf-8") as file:
                employeers = len(lines)
                for lines in file:
                    total = int(lines.split(",")[1])
                    total_salary += total

        average_salary = total_salary // employeers
 
        return (total_salary, average_salary)
    
    except FileNotFoundError:
        print("File not found or corrupted")

total_salary, average_salary = total_salary("salary_employees.txt")

print(f" Загальна сума заробітної плати: {total_salary}\n Середня заробітна плата: {average_salary}")