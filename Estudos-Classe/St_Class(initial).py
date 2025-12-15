class Employee:
    def __init__(self, name, job_pos, salary):
        self.name = name
        self.job_pos = job_pos
        self.salary = salary
dev_junior = Employee("Ericles", "Development Junior", 3500)
designer = Employee("Stephanie", "Designer", 3000)
data_engineer = Employee("Paco", "Data Engineer", 9000)
print(f"debug line testing - following the order | salary | name | job position |:")
print(f"| {dev_junior.salary} | {dev_junior.name} | {dev_junior.job_pos} |")
print(f"| {designer.salary} | {designer.name} | {designer.job_pos} |")
print(f"| {data_engineer.salary} | {data_engineer.name} | {data_engineer.job_pos} |")
print(f"{40 *"="}\nLast debug line, finished.\n{40 *"="}") 