#Meu nome é menu
print('----- Bem-vindo à Loja de Marmitas do Arthur Yan Oliveira Silva -----')
print('------------------------------ Cardápio -----------------------------')

#Tabela de preços
print('-----| Tamanho |  Bife Acebolado (BA)  |  Filé de Frango (FF)  |-----')
print('-----|---------|-----------------------|-----------------------|-----')
print('-----|    P    |       R$ 16.00        |       R$ 15.00        |-----')
print('-----|    M    |       R$ 18.00        |       R$ 17.00        |-----')
print('-----|    G    |       R$ 22.00        |       R$ 21.00        |-----')
print('---------------------------------------------------------------------')
print()

total = 0 #Acumulador

#O while true vai repetir ate o final do pedido 
while True:
    #p/ escolher o sabor
    sabor = input('Entre com o sabor desejado (BA/FF): ')
    if sabor != 'BA' and sabor != 'FF':
        print("Sabor inválido. Tente novamente.")
        print()
        continue
       
    
    #p/ escolher o tamanho
    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print("Tamanho inválido. Tente novamente.")
        print()
        continue
    
    #Calcular preço é tamanho
    if sabor == 'BA':
        nomeSabor = 'Bife Acebolado'
        if tamanho == 'P':
            preco = 16.00
        elif tamanho == 'M':
            preco = 18.00
        elif tamanho == 'G':
            preco = 22.00
    elif sabor == 'FF':
        nomeSabor = 'Filé de Frango'
        if tamanho == 'P':
            preco = 15.00
        elif tamanho == 'M':
            preco = 17.00
        elif tamanho == 'G':
            preco = 21.00
    
    #p/ Total do pedido 
    total += preco
    print(f'Você pediu um {nomeSabor} no tamanho {tamanho}: R$ {preco:.2f}')
    print()
    #P/ saber se o cliente quer mais alguma coisa
    algoMais = input('Deseja mais alguma coisa? (S/N): ')
    if algoMais == 'N':
        break

#Total  a ser pago 
print()
print(f'O valor total a ser pago: R$ {total:.2f}')

