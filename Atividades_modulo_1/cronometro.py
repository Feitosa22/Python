import time

def contador(segundos):
    for i in range(segundos):
        min, seg = divmod(segundos-i, 60)
        texto = f"{min:02d}:{seg:02d}"
        print(texto, end="\r") 
        time.sleep(1)

contador(10)