import logging
logging.basicConfig(level=logging.INFO)

def calculation():
    print('Witam w programie kalkulator.')
    print('Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:')
    selected_program = int(input())
    
    if selected_program == 1:
        more_arg = input('Czy potrzebujesz większej ilości argumentów [Y/N]: ')
        if more_arg == 'Y':
            num_of_arg = int(input('Podaj docelową ilość argumentów: '))
            if num_of_arg:
                components = []
                print('Podaj składniki: ')
                for i in range(0,int(num_of_arg)):
                    components.append(float(input()))
                    i += 1
                print(f'Wprowadzone skłądniki to {components}')
                logging.info(f'Dodaję wszystkie podane liczby: ')
                sum = 0
                for i in components:
                    sum = sum + i
                print(f'Wynik to {sum}')
            else:
                pass

        else:
            first_component = float(input('Podaj pierwszy składnik: '))
            second_component = float(input('Podaj drugi składnik: '))
            logging.info(f'Dodaję {first_component} i {second_component}')
            sum = float(first_component + second_component)
            print(f'Wynik to {sum} ')
        
    elif selected_program == 2:
        first_component = float(input('Podaj pierwszy składnik: '))
        second_component = float(input('Podaj drugi składnik: '))
        logging.info(f'Odejmuję {first_component} i {second_component}')
        subtraction = float(first_component - second_component)
        print(f'Wynik to {subtraction}')
    
    elif selected_program == 3:

        more_arg = input('Czy potrzebujesz większej ilości argumentów [Y/N]: ')
        if more_arg == 'Y':
            num_of_arg = int(input('Podaj docelową ilość argumentów: '))
            if num_of_arg:
                components =[]
                print('Podaj składniki: ')
                for i in range(0,int(num_of_arg)):
                    
                    components.append(float(input()))
                    i += 1
                print(f'Wprowadzone skłądniki to {components}')
                logging.info(f'Mnożę wszystkie podane liczby: ')
                multiplication = 1
                
                for i in components:
                    multiplication = multiplication * i  
                    
                print(f'Wynik to {multiplication}')
                
            else:
                pass
        else:
            first_component = float(input('Podaj pierwszy składnik: '))
            second_component = float(input('Podaj drugi składnik: '))
            logging.info(f'Mnożę {first_component} i {second_component}')
            multiplication = float(first_component * second_component)
            print(f'Wynik to {multiplication}')

    elif selected_program == 4:
        first_component = float(input('Podaj pierwszy składnik: '))
        second_component = float(input('Podaj drugi składnik: '))
        logging.info(f'Dzielę {first_component} i {second_component}')
        div = float(first_component/ second_component)
        print(f'Wynik to {div}')

    elif selected_program > 4:
        logging.info('Błędnie wpisana wartość')
        

calculation()

#PS: Myślę że wszystko jest w porządku. Miłej kalkulacji :)
