def pertence_clube(n: int) -> bool:
    """Verifica se seus fatores primos são apenas 2, 3 e 5."""
    for fator in [2, 3, 5]:
        while n % fator == 0:  # enquanto for divisível, divide
            n //= fator
    return n == 1  # se no final sobrar 1, pertence ao clube


def encontrar_numero(posicao: int) -> int:

    contador = 0
    numero = 1

    while True:
        if pertence_clube(numero):
            contador += 1
            if contador == posicao:
                return numero
        numero += 1

posicao = 1500
# número na posição desejada
resultado = encontrar_numero(posicao)
print(f"O número na {posicao} posição  é {resultado}")