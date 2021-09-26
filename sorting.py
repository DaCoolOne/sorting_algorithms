
def insertion(A: list) -> None:
    for i in range(len(A) - 1):
        j = i
        while j >= 0 and A[j] > A[j+1]:
            A[j+1], A[j] = A[j], A[j+1] # swap
            j -= 1




