
def f(P_ust, P, H):
    if P > P_ust:
        return 2
    elif P < P_ust:
        return 1
    elif P == P_ust:
        return 0
    elif H < 10 and H > 90:
        return 0
    
print(f(1, 2, 3))