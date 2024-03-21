import time

for c in range(10, -1, -1):
    time.sleep(1)
    print(f'Se prepara o foguete vai decolar! {c}')
    if c == 0:
        print("Buuuuuuuuuuuuum!")
