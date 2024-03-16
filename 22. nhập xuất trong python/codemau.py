from time import sleep

your_name = "Hiếu"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.2)
print()
