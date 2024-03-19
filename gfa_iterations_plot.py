import matplotlib.pyplot as plt

file_path = r'C:\Users\zemskov\.anyLogistix3\alx.log'
results_path = r'C:\Users\zemskov\Downloads\GFA test\iterations.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    file.close()
iterations = []
values = []
for line in lines:
    if not line.__contains__("#"):
        continue
    parts = line.split(' ')
    iterations.append(int(parts[7].split('#')[1].split(':')[0].strip()))
    values.append(float(parts[8].strip()))
total_iterations = len(values)
final_iteration = total_iterations
for i in range(total_iterations - 1, 0, -1):
    if values[i] != values[total_iterations - 1]:
        final_iteration = i + 2
        print("Baseline: ", values[total_iterations - 1])
        print("Last wrong: ", values[i])
        break
# values2 = []
# iterations2 =[]
# for i in range(1, total_iterations - 1):
#     if i < 25:
#         continue
#     iterations2.append(iterations[i])
#     values2.append(values[i])
print("Meaningful iterations: ", final_iteration)
# print("Total iterations: ", total_iterations)
plt.plot(iterations, values, marker='o')
plt.xlabel('Номер итерации')
plt.ylabel('Значение целевой функции')
plt.title('График значений итераций')
plt.grid(True)
plt.show()
with open(file_path, 'w') as file:
    file.seek(0)
    file.close()
with open(results_path, 'a') as file:
    file.write("Meaningful iterations: " + str(final_iteration) + "\n")