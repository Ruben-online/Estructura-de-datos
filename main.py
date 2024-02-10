from linked_list import LinkedList, Customer, Product, Sale


users = {'user1': 'password1', 'user2': 'password2'}

def reg_user():
    username = input('Ingrese el usuario: ')

    if username in users:
        print('El usuario ya existe')
    else:
        password = input('Ingrese la contraseña: ')
        users[username] = password
        print('Registro excitoso')

def manage_costumers():
    pass

def manage_products():
    pass

def manage_sales():
    pass

def user_menu(username):
    while True:
        print('Accesorios OMEGA\n')
        print('1. Administrar clientes')
        print('2. Administrar productos')
        print('3. Administrar ventas')
        print('4. Salir')

        user_menu_option = input('Ingrese una opcion (1-4): ')

        if option == '1':
            manage_costumers()
        elif option == '2':
            manage_products()
        elif option == '3':
            manage_sales()
        elif option == '4':
            print('Saliendo del programa...')
            break
        else:
            print('Ingrese una opcion valida')

def login():
    username = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')

    if username in users and users[username] == password:
        print('Bienvenido')
    else:
        print('Intentelo de nuevo, usuario o contraseña incorrectas')

while True:
    print('Menu\n')
    print('1. Registrar un usuario')
    print('2. Login')
    print('3. Salir')

    option = input('Ingrese una opcion (1-3): ')

    if option == '1':
        reg_user()
    elif option == '2':
        login()
    elif option == '3':
        print('Saliendo del programa...')
        break
    else:
        print('Ingrese una opcion valida')