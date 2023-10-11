print("Beräknar differensen av jämna/udda tal...")
even = 0
odd = 0
for i in range(1, 2001):
    if (i % 2 == 0):
        even += i
    elif (i % 2 != 0):
        odd += i
print(f'Differensen: {even - odd}')