import random
n=20        # size of invididual
m=10
def generate_random_value(): # tạo random value
    return  random.randint(0,1)
def compute_fitness(individual): # tính toán fitness
    return sum(gen for gen in individual)
def create_individual():    # tạo cá nhân
    return [generate_random_value() for _ in range(n)]
def selection(sorted_old_population):
    index1=random.randint(0,m-1)
    while True:
        index2=random.randint(0,m-1)
        if(index2!=index1):
            break
