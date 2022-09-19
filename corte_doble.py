sucursal = 0
nro_cuenta = 0
tipo = ""
monto = 0 
saldo = 0
total_c = 0
total_d = 0
aux_suc = 0
aux_cliente = 0
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
             print (aux_cliente)
             print (aux_suc)
             print (saldo)
             saldo = 0
             
             aux_cliente = nro_cuenta
             if tipo == "c":
                saldo = saldo + monto
                total_c = total_c + monto
             else:
                saldo = saldo - monto
                total_d = total_d + monto

        
        print (aux_cliente)
        print (aux_suc)
        print (saldo)
        saldo = 0
        print (aux_suc)
        print (total_d)
        print (total_c)
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
        break;
