def trinca_235(n):
    # lista dos números da trinca
    trinca = [1]
    i2 = i3 = i5 = 0  # índices para os múltiplos de 2, 3 e 5
    
    for _ in range(1, n):  # já temos o 1 na posição inicial
        next2 = trinca[i2] * 2
        next3 = trinca[i3] * 3
        next5 = trinca[i5] * 5
        
        proximo = min(next2, next3, next5)
        trinca.append(proximo)
        
        if proximo == next2:
            i2 += 1
        if proximo == next3:
            i3 += 1
        if proximo == next5:
            i5 += 1
            
    return trinca[-1]

# Exemplo:
posicao = 1500
numero = trinca_235(posicao)
print(f"O número na posição {posicao} é {numero}")
c