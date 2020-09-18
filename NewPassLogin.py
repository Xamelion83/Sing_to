MasZag = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
          'V', 'B', 'N', 'M']
MasMal = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
          'v', 'b', 'n', 'm']
MasChis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
MasSin = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?']

def ProverkaPass(ProvPass):
    Zag = 0
    Mal = 0
    Chis = 0
    Sin = 0
    for j in ProvPass:
        if j in MasZag:
            Zag += 1
        if j in MasMal:
            Mal += 1
        if j in MasChis:
            Chis += 1
        if j in MasSin:
            Sin += 1
    if Zag + Mal + Chis + Sin < 12:
        print('Пароль меньше 12 символов')
        ProvPass = (input('Введите пароль: '))
        ProverkaPass(ProvPass)
    elif (Zag < 1) or (Mal < 1) or (Chis < 1) or (Sin < 1):
        print('Пароль не содержит заглавную или маленькую букву или цифру или символ')
        ProvPass = (input('Введите пароль: '))
        ProverkaPass(ProvPass)
    else:
        BasePass = open('BasePass.txt','a')
        BasePass.write(ProvPass)
        BasePass.write('\n')
        BasePass.close()
    return (ProvPass)

with open('BaseLogin.txt') as BaseLoginF:
    LoginLines = BaseLoginF.readlines()
    LoginLines = [x.strip() for x in LoginLines]

def ProverkaLogin(ProvLogin):
    a = [ProvLogin]
    m = 0
    for i in a:
        if i in LoginLines:
            m += 1
    if m != 0:  
        print('Такой логин существует')
        ProvLogin = input('Введите свой логин: ')
        ProverkaLogin(ProvLogin)
    else:
        BaseLogin = open('BaseLogin.txt','a')
        BaseLogin.write(ProvLogin)
        BaseLogin.write('\n')
        BaseLogin.close()
    return (ProvLogin)
    
ProvLogin = (input('Введите свой логин: '))
ProverkaLogin(ProvLogin)
ProvPass = (input('Введите пароль: '))
ProverkaPass(ProvPass)
print('Пользователь зарегистрирован\n')
import Main
