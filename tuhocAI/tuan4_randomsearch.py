
def generate_vector(n=10,m=8):
    vector =[[0]*n for _ in range(m)]
    for i in range (m):
        for j in range (n):
            if random.random()>=0.5:
                vector[i][j]=1
    return vector
