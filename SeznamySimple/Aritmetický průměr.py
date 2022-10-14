def Average(seznam):
    return sum(seznam) / len(seznam)

seznam = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(seznam)

print("Aritmetický průměr je:", round(average, 2))
