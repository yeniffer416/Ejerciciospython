#funcion para sacar la nomina sin los aportes y los parafiscales
def nomina(cedula,nombre_empleado,salario_basico,dias_laborados,ventas_vendedor,prestamos):
    
    #impresiones de informacion basica cedula,nombre,salario basico
    print(f'cedula: {cedula}')
    print(f'nombre de empleado: {nombre_empleado}')
    print(f'salario basico es:{salario_basico}')
    
    #sueldo devengado
    sueldo_devengado=salario_basico*dias_laborados/30
    
    
    #if para determinar si tiene o no auxilio de transporte
    if salario_basico>=1000000 and salario_basico <=2000000:
        auxilio_transporte=117112*dias_laborados/30
        print(f'auxilio de transporte:{auxilio_transporte}')
    
    else:
        auxilio_transporte=0
        print(f'Auxilio de transporte:{auxilio_transporte}')
    
    #comision de ventas
    comision_ventas=ventas_vendedor*0.02
    print(f'comision={comision_ventas}')
    print(f'prestamos= {prestamos}')
    
    #total devengando por el empleado
    total_devengado=sueldo_devengado+comision_ventas
    
    #deducciones
    total_deducciones=prestamos
    
    #el valor del salario neto
    salario_neto=total_devengado-total_deducciones+auxilio_transporte
    
    print(f'salario a recibir: {salario_neto}')
    
    
    


#codigo principal
cedula=int(input('digite la cedula del empleado: '))
nombre_empleado=str(input('coloque el nombre del empleado: '))
salario_basico=int(input('ingrese el salario del empleado: '))
dias_laborados=int(input('digite los dias laborados : '))
ventas_vendedor=int(input('ingrese el valor de las ventas del mes del vendedor: '))
prestamos=int(input('ingrese el valor del prestamo si no tiene prestamos ingrese el valor 0: '))

#llamar funcion
nomina(cedula,nombre_empleado,salario_basico,dias_laborados,ventas_vendedor,prestamos)
