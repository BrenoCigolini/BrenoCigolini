n = int(input('Digite um número: '))
print('Escolha uma das opções para conversão:')
print('[1] para binário')
print('[2] para octal')
print('[3] para hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}.'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}.'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')
