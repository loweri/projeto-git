import pandas as pd

class Employee:
    def __init__(self, name, job_pos, salary):
        self.name = name
        self.job_pos = job_pos
        self.salary = salary
dev_junior = Employee("Ericles", "Development Junior", 3500)
designer = Employee("Stephanie", "Designer", 3000)
data_engineer = Employee("Paco", "Data Engineer", 9000)
hrdata = []
dev_junior_dict = {
    "name": dev_junior.name,
    "job_pos": dev_junior.job_pos,
    "salary": dev_junior.salary
}
designer_dict = {
    "name": designer.name,
    "job_pos": designer.job_pos,
    "salary": designer.salary
}
data_engineer_dict = {
    "name": data_engineer.name,
    "job_pos": data_engineer.job_pos,
    "salary": data_engineer.salary
}
hrdata.append(dev_junior_dict)
hrdata.append(designer_dict)
hrdata.append(data_engineer_dict)
#
df_rh = pd.DataFrame(hrdata)
salary_avg = df_rh['salary'].mean()
print(f"\n{df_rh}")
print(f"\n{salary_avg}")
#
dev_filter = (df_rh['job_pos'] != 'Designer') #variavel criada pra filtrar tudo que não for "Designer"
df_dev = df_rh[dev_filter] #selecionamos só as linhas Verdadeiras
new_avg = df_dev['salary'].mean() #calculo da média em cima das linhas filtradas
print(df_dev)
print(new_avg)