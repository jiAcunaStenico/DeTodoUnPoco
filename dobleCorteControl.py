saldo = 0
total_c = 0
total_d = 0
flag = True

while True:
    sucursal = int (input(f"Ingrese sucursal: "))
    nro_cuenta = int (input(f"Ingrese Nro de cuenta: "))
    tipo =  input (f"Ingrese Tipo de Cuenta: ")
    monto = int (input(f"Ingrese Monto: ")) 

    if flag == True:
        flag = False
        aux_suc = sucursal
        aux_cliente = nro_cuenta
    
    if sucursal == aux_suc:
        if nro_cuenta == aux_cliente:
            
            if tipo == "c":
                saldo = saldo + monto
                total_c = total_c + monto
            else:
                 saldo = saldo - monto
                 total_d = total_d + monto
        else:
             print ("el cliente es" ,aux_cliente)
             print ("el saldo es",saldo)
             saldo = 0
             
             aux_cliente = nro_cuenta
             if tipo == "c":
                saldo = saldo + monto
                total_c = total_c + monto
             else:
                saldo = saldo - monto
                total_d = total_d + monto

    else:
        print ("el cliente",aux_cliente)
        print ("tiene de saldo ",saldo)
        saldo = 0
        print ("la sucursal es",aux_suc)
        print ("el debito es",total_d)
        print ("el credito es",total_c)
        total_c = 0
        total_d = 0
        

        aux_cliente = nro_cuenta
        aux_suc = sucursal
        if tipo == "c":
            saldo = saldo + monto
            total_c = total_c + monto
        else:
            saldo = saldo - monto
            total_d = total_d + monto
    
    if sucursal == 0:
        break