print('Выбирите\n','1-Авторизация\n','2-Новый_Пользователь\n')
a = int(input())
if a == 1:
    import LoginAndPass
elif a == 2:
    import NewPassLogin
else:
    print('Нет такого пункта')
