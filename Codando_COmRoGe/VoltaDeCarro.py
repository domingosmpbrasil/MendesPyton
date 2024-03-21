primeira_volta = float(input("Digite quantos segundos foi a primeira volta:"))
segunda_volta = float(input("Digite quantos segundos foi a segunda volta:"))
terceira_volta = float(input("Digite quantos segundos foi a terceira volta:"))

    if (primeira_volta < segunda_volta and primeira_volta < terceira_volta):
    print("A volta mais rápida foi a Primeira volta! 👏👏👏👏👏")
elif (segunda_volta < primeira_volta and segunda_volta < terceira_volta):
    print("A volta mais rápida foi a segunda volta! ")
else:
    print("A volta mais rápida foi a terceira volta!")
