with open('BaseLogin.txt') as BaseLoginF:
    LoginAvtoLines = BaseLoginF.readlines()
    LoginAvtoLines = [x.strip() for x in LoginAvtoLines]
with open('BasePass.txt') as BasePassF:
    PassAvtoLines = BasePassF.readlines()
    PassAvtoLines = [x.strip() for x in PassAvtoLines]
    
def ProverLAP():
    Login = input('Введите ваш логин: ')
    Pass = input('Введите ваш пароль: ')
    a = [Login]
    b = [Pass]
    for i in a:
        if i in LoginAvtoLines:
            SravLodin = LoginAvtoLines.index(i)
        else:
            SravLodin = 0
    for j in b:
        if j in PassAvtoLines:
            SravPass = PassAvtoLines.index(j)
        else:
            SravPass = 0
    if SravLodin == SravPass and SravLodin != 0 and SravPass != 0:
        print('Вошли в сиcтему')
    else:
        print('Не верный логин или пароль')
        ProverLAP()
    return()
        
ProverLAP()


