class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_name=worker_num
        self.fname=fname
        self.lname=lname
        self.work_experience_company=work_experience_company
        self.salary=salary
        self.age=age
    def worker_information(self):
        print(f"Worker Number: {self.worker_num}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Work Experience in Company: {self.work_experience_company} years")
        print(f"Salary: {self.salary}")
        print(f"Age: {self.age}")
    def salary_bonus(self):
        if 5<self.work_experience_company<10:
            bonus=self.salary+0.015
        elif self.work_experience_company>10:
            bonus=self.salary*0.02
        else:
            bonus=self.salary*0.005
        return bonus
worker_list=[]
def search_my_num(worker_list, worker_num):
    for num in worker_list:
        if num.worker_num==worker_num:
            return True
        else:
            return False
def search_by_name_experience(worker_list, fname, worker_experience):
    result=[]
    for worker in worker_list:
        if worker.fname==fname and worker.worker_experience==worker_experience:
            result.append(worker)
    return result
def add_worker(worker_list, worker):
    worker_list.append(worker)
def remove_worker(worker_num):
    for worker in worker_list:
        if worker.worker_num==worker_num:
            worker_list.remove(worker)
            print("Information delete!")
        else:
            print("Wrong worker_num!")

num_workers = int(input("Enter the number of workers: "))
for i in range(num_workers):
    print(f"\n--- Enter information for worker {i+1} ---")
    worker_num = int(input(f"Enter worker number: "))
    fname = input(f"Enter first name: ")
    lname = input(f"Enter last name: ")
    work_experience_company = int(input(f"Enter work experience in company (years): "))
    salary = float(input(f"Enter salary: "))
    age = int(input(f"Enter age: "))
    worker=Worker(worker_num, fname, lname, work_experience_company, salary, age)
    add_worker(worker_list,worker)
print("______Worker Information______")
for worker in worker_list:
    worker.worker_information()
    print(f"Bonus: {worker.salary_bonus():.2f}")
    print("---------------------------")