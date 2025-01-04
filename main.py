from faker import Faker
from colorama import Fore, Style, init
import os
from time import sleep

#Resetando a cor do prompt 
init(autoreset=True)

fake = Faker('pt_BR')

def prompt_cls():
    #limpa o terminal
    os.system('cls' if os.name== 'nt' else 'clear')
    
def main_menu():
    prompt_cls()
    print(Fore.BLUE + '''
  ______    _          _____    _ 
 |  ____|  | |        |_   _|  | |
 | |__ __ _| | _____    | |  __| |
 |  __/ _` | |/ / _ \   | | / _` |
 | | | (_| |   <  __/  _| || (_| |
 |_|  \__,_|_|\_\___| |_____\__,_|\n
''' + Fore.CYAN + 'Menu de opções:' + Fore.GREEN + '''
Digite a quantidade de pessoas fakes para gerar;
Digite "sair" para fechar o programa;
''' + Fore.CYAN + 'O que deseja:' )
    action= input()
    return action

def generator(n_ids):
    if n_ids > 0:
        prompt_cls()
        for i in range(n_ids):
            print(f"{Fore.CYAN + Style.BRIGHT + '=' * 110}\n{Fore.GREEN + Style.BRIGHT + f'Fake ID {i + 1}'.center(110)}\n{Fore.CYAN + Style.BRIGHT + '=' * 110}")
            print(Fore.GREEN + 'Nome:\n' + Fore.BLUE + f' {fake.name()}')
            print(Fore.GREEN + 'CPF:\n' + Fore.BLUE + f' {fake.cpf()}')
            print(Fore.GREEN + 'Email:\n' + Fore.BLUE + f' {fake.email()}')
            email= fake.address().replace('\n', ', ')
            print(Fore.GREEN + 'Endereço:\n' + Fore.BLUE + f' {email}')
            print(Fore.GREEN + 'Número de celular:\n' + Fore.BLUE + f' {fake.cellphone_number()}')
    else:
        print(Fore.RED + 'Esta opção não é válida. O número de pessoas geradas precisa ser maior que 0.')

if __name__ == '__main__':
    while True:
        action= main_menu()
        try:
            generator(int(action))
            input('Precione enter para voltar...')
        except:
            if action.lower() == 'sair':
                break
            else:
                print(Fore.RED + 'Esta opção não consta no programa.')
                sleep(2)