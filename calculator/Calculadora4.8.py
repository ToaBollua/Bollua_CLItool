class Funciones:
    def suma(self):
        sum1 = float(input('Ingrese un número: '))
        sum2 = float(input('Ingrese otro número: '))
        res = (sum1 + sum2)
        if res.is_integer():
            res = int(res)
        print((sum1), '+', (sum2))
        if sum1 == 1 and sum2 == 1:
            print('El resultado es: Soprole')
        elif res == 13:
            print('Entre más me la mamas más me crece')
        elif res == 11:
            print('Chupalo entonces')
        else:
            print(f'El resultado es: {res}')
    def resta(self):
        sus1 = float(input('Ingrese un número: '))
        sus2 = float(input('Ingrese otro número: '))
        res = float(sus1 - sus2)
        if res.is_integer():
            res = int(res)
        print(sus1, '-', sus2)
        if res == 13:
            print('Entre más me la mamas más me crece')
        elif res == 11:
            print('Chupalo entonces')
        else:
            print(f'Tu resultado es: {res}')
    def mult(self):
        mult1 = float(input('Ingrese un número: '))
        mult2 = float(input('Ingrese otro número: '))
        res = float(mult1 * mult2)
        if res.is_integer():
            res = int(res)
        print(mult1, '*', mult2)
        if res == 13:
            print('Entre más me la mamas más me crece')
        elif res == 11:
            print('Chupalo entonces')
        elif mult1 == 8 and mult2 == 8:
            print('El resultado es: Super 8')
        else:
            print(f'El resultado es: {res}')
    def div(self):
        div1 = float(input('Ingrese un número: '))
        div2 = float(input('Ingrese otro número: '))
        print(div1, '/', div2)
        if div1 == 0 or div2 == 0:
            print("No se puede dividir entre 0.")
            return
        else:
            res = float(div1 / div2)
            if res.is_integer():
                res = int(res)
            if res == 13:
                print('Entre más me la mamas más me crece')
            elif res == 11:
                print('Chupalo entonces')
                print(f'El resultado es: {res}')
    def tabla(self):
        tab1 = int(input('Ingrese un número: '))
        for i in range (13):
            print(f"{tab1} x {i} = {tab1 * i}")

def usumenu():
    Funcion_1 = Funciones()
    menu = True
    while menu: 
        opt = input('1) Suma \n2) Resta \n3) Multiplicación \n4) División \n5) Tablas \n6) Salir \n¿Qué operación desea realizar?: ')
        if opt == '1':
            Funcion_1.suma()
            print('Reiniciando...')
            return
        elif opt == '2':
            Funcion_1.resta()
            print('Reiniciando...')
            return
        elif opt == '3':
            Funcion_1.mult()
            print('Reiniciando...')
            return
        elif opt == '4':
            Funcion_1.div()
            print('Reiniciando...')
            return
        elif opt == '5':
            Funcion_1.tabla()
            print('Reiniciando...')
            return
        elif opt == '6':
            print('Cerrando programa... \n~CHUPA productions~')
            quit()
        else:
            print('Respuesta invalida. Reintentando...')
            return

follow = True
while follow:
    keep = input('¿Desea comenzar? (s/n) > ')
    keep = keep.lower()
    if keep == 's':
        usumenu()
        continuar_bool = True
        while continuar_bool:
            continuar = input('¿Desea continuar? (s/n) > ')
            if continuar == 's':
                usumenu()
            elif continuar == 'n':
                continuar_bool = False
                follow = False
                print('Cerrando programa... \n~CHUPA productions~')
                quit()
            else:
                print('Respuesta invalida. Reintentando... ')
    elif keep == 'n':
        follow = False
        print('Cerrando programa... \n~CHUPA productions~')
        quit()
    else:
        print('Respuesta invalida. Reintentando... ')