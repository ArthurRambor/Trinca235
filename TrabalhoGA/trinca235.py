def pertence_clube(n: int) -> bool:
    """
    Verifica se um número pertence ao 'clube 2, 3, 5',
    ou seja, se seus fatores primos são apenas 2, 3 e 5.
    """
    for fator in [2, 3, 5]:
        while n % fator == 0:  # enquanto for divisível, divide
            n //= fator
    return n == 1  # se no final sobrar 1, pertence ao clube


def encontrar_numero(posicao: int) -> int:
    """
    Encontra o número na posição desejada dentro da sequência.
    """
    contador = 0
    numero = 1

    while True:
        if pertence_clube(numero):
            contador += 1
            if contador == posicao:
                return numero
        numero += 1


# 🔹 Exemplo: encontrar o número na posição 1500
resultado = encontrar_numero(1500)
print(f"O número na posição 1500 é {resultado}")