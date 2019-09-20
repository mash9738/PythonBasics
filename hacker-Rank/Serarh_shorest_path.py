H_SA = 2
H_SB = 3
H_IN = 4
SA_SB = 2
SA_H = 2
SB_SL = 2
SL_SB = 2
SL_IN = 2
IN_SL = 2

H_SL1 = H_SA + SA_SB + SB_SL
H_SL2 = H_SB + SB_SL
H_SL3 = H_IN + IN_SL

f_MAX = max(H_SL1, H_SL2, H_SL3)
f_MIN = min(H_SL1, H_SL2, H_SL3)

print(f_MAX, f_MIN)
