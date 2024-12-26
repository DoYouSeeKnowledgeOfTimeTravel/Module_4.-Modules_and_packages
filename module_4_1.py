from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(213, 5)
result2 = fake_divide(36, 0)
result3 = true_divide(1951, 56)
result4 = true_divide(7, 0)
print(result1)
print(result2)
print(result3)
print(result4)