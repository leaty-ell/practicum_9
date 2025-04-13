for AB in range(10, 100):
    CAB = AB * AB
    if 100 <= CAB <= 999 and str(CAB)[1:] == str(AB):
        print(CAB)
        break
