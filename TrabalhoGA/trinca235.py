def pertence_trinca(n: int) -> bool:
    
    """Verifica se fatores primos são apenas 2, 3 e 5."""
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
        if pertence_trinca(numero):
            contador += 1
            if contador == posicao:
                return numero
        numero += 1

posicao = 1500
# Encontrar posição 1500
resultado = encontrar_numero(posicao)
print(f"O número na posição {posicao}ª é {resultado}")