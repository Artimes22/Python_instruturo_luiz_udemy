for i in range(10):
    if i == 2:
        print('I é 2, pulando...')
        continue

    if i == 8:
        print('I é 8, seu else não executaá')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('FOR completo com sucesso!')        
