print('Расчёт ипотечной ставки')
name = input('Введите имя и фамилию: ')
while True:
    base_bet = int(17)
    region = input('Введите регион проживания: ')
    if region == 'Дальний Восток' or region == 'ДВ':
        print('Ваш регион проживания Дальний Восток, Вам предлагается особое предложение по государственной программе в виде ставки по ипотеке 2%')
        check_1 = input('Согласны ли вы с данным предложением? Введите \"да/нет\":')
        if check_1 == 'да':
            bet = 2
            print(f'Поздравляем! Ваша ипотечная ставка {bet}%!')
            break    
    else:
        print(f'Ваше регион проживания {region}')    
    kids = int(input('Введите количество детей в Вашей семье: ')) 
    if kids >= 3:
        bet_kids = base_bet - 1
        print('Ваша ипотечная ставка снижена на 1%')
    else:
        bet_kids = base_bet
    check_client = input('Имеется ли у Вас в нашем банке зарплатный проект (да/нет): ')
    if check_client == 'да':
        bet_check_client = bet_kids - 0.5
        print(f'Спасибо, {name}, что пользуетесь нашими услугами! Ваша ставка снижена на 0.5%!')
    else:
        bet_check_client = bet_kids
    check_insurance = str(input('Оформлена ли у Вас в нашем банке страховка (да/нет): '))
    if check_insurance == 'да':
        bet_check_insurance = bet_check_client - 1.5
        print(f'Спасибо, {name}, что пользуетесь нашими услугами! Ваша ставка снижена на 1.5%!')
    else:
        bet_check_insurance = bet_check_client
    print(f'Спасибо, {name}, что воспользовались нашим банком для оформления ипотеки!')
    print('')
    print(f'Ваша ипотечная ставка в регионе: {region} составляет {bet_check_insurance}%')
    break



 