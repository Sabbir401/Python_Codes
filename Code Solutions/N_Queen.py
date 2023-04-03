N = int(input("Enter number of queen: "))

arr = [[0]*N for i in range(N)]

def is_attack(i, j):
    # Checking Row & Column
    for k in range(N):
        if arr[i][k] == 1 or arr[k][j] == 1:
            return True

    # Checking Diagonals
    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j):
                if arr[k][l] == 1:
                    return True
    return False

# Handling N-Queens
def N_queen(n):
    # If n==0, No Queen Left
    if n == 0:
        return True

    for i in range(N):
        for j in range(N):
            if (not (is_attack(i, j))) and (arr[i][j] != 1):
                arr[i][j] = 1

                if N_queen(n - 1) == True:
                    return True
                arr[i][j] = 0
    return False

N_queen(N)

# Printing the Chessboard
for i in arr:
  print(i)
print("\n\n")