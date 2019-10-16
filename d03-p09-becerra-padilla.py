#practica 09
#becerra gonzalez diego ivan
#padilla valdez gustavo

def descuento():#calcula el descuento total que se hace en un teatro
    boletos = [-2];#arreglo donde se guardara el descuento del boleto
    cat1 = 0;#guardara el numerode personas qde la categoria 1
    cat2 = 0;#guardara el numerode personas qde la categoria 2
    cat3 = 0;#guardara el numerode personas qde la categoria 3
    cat4 = 0;#guardara el numerode personas qde la categoria 4
    cat5 = 0;#guardara el numerode personas qde la categoria 5
    for i2 in boletos :#for que pedira la edad del cliente hasta que se indique lo contrario
        edad = str(input("Ingresa la edad del cliente(debe de ser mayor de 4 años) y -1 para mostrar el dinero no percibido "));
        try :#si ingreso un numero, entra
            edad = int(edad);
            if edad > 0 and edad < 5 :#si entra dentro del rango de personas no permitidas
                print("No se permiten menores de 5 años");
                boletos.append(-2);
            elif edad >= 5 and edad <= 14 :#si entra dentro de la categoria 1
                boletos.append(35);#se guarda la edad de la persona
                cat1 += 1;#se agrega a su categoria
            elif edad >= 15 and edad <= 19 :#si entra dentro de la categoria 2
                boletos.append(25);#se guarda la edad de la persona
                cat2 += 1;#se agrega a su categoria
            elif edad >= 20 and edad <= 45 :#si entra dentro de la categoria 3
                boletos.append(10);#se guarda la edad de la persona
                cat3 += 1;#se agrega a su categoria
            elif edad >= 46 and edad <= 65 :#si entra dentro de la categoria 4
                boletos.append(25);#se guarda la edad de la persona
                cat4 += 1;#se agrega a su categoria
            elif edad >= 66 and edad <= 120 :#si entra dentro de la categoria 5
                boletos.append(35);#se guarda la edad de la persona
                cat5 += 1;#se agrega a su categoria
            elif edad == -1 :#si ingresa la opcion de salida
                pass;
            else : #en caso de que ingrese cualquier otro numero no valido
                print("Debes ingresar una edad valida");
                boletos.append(-2);
        except :#en caso de que ingrese un caracter
            print("\nDebes de ingresar solo numeros");
            boletos.append(-2);

    costo = 100;#costo del boleto
    desc1 = (costo * 0.35)*cat1;#descuento de la categoria 1
    desc2 = (costo * 0.25)*cat2;#descuento de la categoria 2
    desc3 = (costo * 0.1)*cat3;#descuento de la categoria 3
    desc4 = (costo * 0.25)*cat4;#descuento de la categoria 4
    desc5 = (costo * 0.35)*cat5;#descuento de la categoria 5
    #se imprimen los datos
    print("El boleto cuesta 100");
    print("Personas de la categoria 1: ",cat1," y el dinero descontado en esa categoria ",desc1);
    print("Personas de la categoria 2: ",cat2," y el dinero descontado en esa categoria ",desc2);
    print("Personas de la categoria 3: ",cat3," y el dinero descontado en esa categoria ",desc3);
    print("Personas de la categoria 4: ",cat4," y el dinero descontado en esa categoria ",desc4);
    print("Personas de la categoria 5: ",cat5," y el dinero descontado en esa categoria ",desc5);
    
def e1():#funcion para el ejercicio 1
    print("\nEjercicio 1");
    descuento();

def neumaticos():#muestra un menu para ejecutar los ejercicios
        aumento = [0] ;#sera la variable que hace infinito el ciclo
        masafinal=0;
        masat=[];
        total_llantas = 0;
        promedio=0;
        for i in aumento :#se repetira hasta llegar a 1, al llegar a una opcion o validacion i se inicia en 0
                opcion = str(input("\nPresione 1 si quiere ingresar datos de la llanta, y 0 para salir y ver "));
                try :#si ingresa un numero, lo ejecuta
                        opcion = int(opcion);
                        if opcion < 0 or opcion > 1 :#si esta fuera del rango o es negativo
                                print("Debes ingresar 1 ó 0");
                                aumento.append(0); 
                        else :#en otro caso
                                if opcion == 1 :#Si elige meter datos
                                    
                                    aumentov=[0]; #Inicializara las tablas que se usan en caso de que el volumen y la presion sean negativas
                                    aumentop=[0];
                                    movil=str(input("Ingresa 1 para motocicleta y 2 para automovil ")); #Pregunta cual es su vehiculo
                                    if movil == "1": #Si elige moto
                                        
                                        for y in range(2) : #Hara un ciclo for para pedir los datos de las 2 llantas de la moto
                                            aumentop = [0];
                                            aumentov = [0]; #Reinicializara las tablas en 0
                                            presion=float(input("Dame la presion ")); 
                                            if presion < 0: #Si la presion no es un dato valido lo volvera a pedir
                                                print("La presion no puede ser menor a 0");
                                                for x in aumentop  : #Este for es equivalente a un while que no lo dejara salir hasta que la presion sea un dato valido
                                                    presion=float(input("Dame la presion "));
                                                    if presion < 0:
                                                        print("La presion no puede ser menor a 0");
                                                        aumentop.append(0);
                                                
                                               
                                            volumen=float(input("Dame el volumen "));
                                            if volumen <= 0: #Si el volumen no es un dato valido lo volvera a pedir
                                                print("El volumen no puede ser menor o igual  a 0");
                                                for x in aumentov  : #El equivalente al while hasta que el volumen sea valido
                                                    volumen=float(input("Dame el volumen "));
                                                    if volumen <= 0:
                                                        print("La presion no puede ser menor o igual  a 0");
                                                        aumentov.append(0);
                        
                                            temp=float(input("Dame la temperatura "));
                                            masa = (presion * volumen) / (0.37 * (temp+460)); #Calculara la masa
                                            masat.append(masa); #Añadira la masa en una lista con todas las masas
                                        total_llantas += 2; #Al total de llantas se le añaden 2 para calcular el promedio

                                    elif movil == "2": #Si elige auto
                                        
                                        for y in range(4) : #Hara un ciclo for para pedir los datos de las 4 llantas del auto
                                            aumentop = [0];
                                            aumentov = [0]; #Reinicializara las tablas en 0
                                            presion=float(input("Dame la presion ")); 
                                            if presion < 0: #Si la presion no es un dato valido lo volvera a pedir
                                                print("La presion no puede ser menor a 0");
                                                for x in aumentop  : #Este for es equivalente a un while que no lo dejara salir hasta que la presion sea un dato valido
                                                    presion=float(input("Dame la presion "));
                                                    if presion < 0:
                                                        print("La presion no puede ser menor a 0");
                                                        aumentop.append(0);
                                                
                                               
                                            volumen=float(input("Dame el volumen "));
                                            if volumen <= 0: #Si el volumen no es un dato valido lo volvera a pedir
                                                print("El volumen no puede ser menor o igual  a 0");
                                                for x in aumentov  : #El equivalente al while hasta que el volumen sea valido
                                                    volumen=float(input("Dame el volumen "));
                                                    if volumen <= 0:
                                                        print("La presion no puede ser menor o igual  a 0");
                                                        aumentov.append(0);
                        
                                            temp=float(input("Dame la temperatura "));
                                            masa = (presion * volumen) / (0.37 * (temp+460)); #Calculara la masa
                                            masat.append(masa); #Añadira la masa en una lista con todas las masas
                                        total_llantas += 4; #Al total de llantas se le añaden 4 para calcular el promedio
                                        

                                    else: 
                                        print("Ingresa un dato valido!");
                                    aumento.append(0);
                                        
                                if opcion == 0 :
                                        pass;#no se agrega nada para que termine el ciclo
                                
                except :#en caso de que ingrese un caracter
                        print("Debes un dato valido!(Abstengase de ingresar caracteres)");
                        aumento.append(0);

        if total_llantas > 0: #Se tendra que ingresar datos de llantas para evitar error de variables               
            for z in range(total_llantas) : #Este for suma todas las masas que estaban en la lista
                masafinal += masat[z];
            promedio = masafinal / total_llantas; #Calcula el promedio y despues lo imprime
        print("El promedio de la masa de aire de una llanta fue de: " , promedio);
    
    
def e2():#funcion para el ejercicio 2
    print("\nEjercicio 2");
    neumaticos();

def bachoco():#determina el promedio de calidad de n-gallinas y calcula el precio del kg de huevo
    aumento = [0];#lista para el for infinito
    aumento2 = [0];#otra lista para ciclos for internos
    calidades = [];#lista que  guardara la calidad de todas las gallinas
    contador = 0;#contara el numero de gallinas ingresadas
    print("Formula bachoco");
    for i in aumento:
        opcionBachoco = str(input("Ingresa 1 para ingresar los datos de una gallina y 2 para imprimir el precio por kg de huevo "));
        try:#entra si se puede hacer la conversion a numero
            opcionBachoco = int(opcionBachoco);
            if opcionBachoco < 1 or opcionBachoco > 2 :#si esta fuera del rango
                print("Debes ingresar una opcion valida");
                aumento.append(0);
            elif opcionBachoco == 1:#ingresa datos de la gallina
                for i2 in aumento2 :
                    peso = str(input("Ingresa el peso de la gallina en kg "));
                    try:#si ingreso un numero
                        peso = int(peso);
                    except:#si ingresa un caracter
                        print("Debes ingresar el peso con numeros");
                        aumento2.append(0);
                aumento2 = [0];#se vuelve a vaciar la lista
                for i2 in aumento2 :
                    altura = str(input("Ingresa la altura de la gallina  "));
                    try:#si ingreso un numero
                        altura = int(altura);
                    except:#si ingresa un caracter
                        print("Debes ingresar la altura con numeros");
                        aumento2.append(0);
                aumento2 = [0];#se vuelve a vaciar la lista
                for i2 in aumento2 :
                    huevos = str(input("Ingresa el numero de huevos que pone "));
                    try:#si ingreso un numero
                        huevos = int(huevos);
                    except:#si ingresa un caracter
                        print("Debes ingresar el dato usando numeros");
                        aumento2.append(0);
                        
                calidad = (peso*altura)/huevos;#calcula la calidad de la gallina
                calidades[i] = calidad;#guarda la calidad de la gallina
                contador += 1;#se aumenta el numero de gallinas
                aumento.append(0);
            elif opcionBachoco == 2 :
                sumatoria = 0;#guardara el valor de todas las calidades de las gallinas
                for i2 in calidades :#recorre la lista de calidad
                    sumatoria += calidades[i2];
                promedio = sumatoria/contador;#saca el promedio de calidad de las gallinas

                precioK = 0;#precio por kilo de huevo
                if promedio >= 15 :
                    precioK = promedio * 1.2;
                elif promedio > 8 and promedio < 15 :
                    precioK = promedio;
                elif promedio <= 8 :
                    precioK = promedio * 0.8;

                print("Se ingresaron los datos de ",contador," gallinas");
                print("El promedio de calidad es ",promedio);
                print("El precio por kg de huevo es ",precioK);
        except:#por si ingresa un caracter
            print("Solo se pueden ingresa numeros");
            aumento.append(0);

    

def e3():#funcion para el ejercicio 3
    print("\nEjercicio 3");
    bachoco();

def diputados():
        aumento = [0] ;#sera la variable que hace infinito el ciclo
        favor = 0; #Inicializo variables de votos para evitar errores
        contra = 0;
        abst = 0;
        diputados= 500;
        
        for i in aumento :#se repetira hasta llegar a 1, al llegar a una opcion o validacion i se inicia en 0
                print("\n-ENCUESTA DEL TRATADO DE LIBRE Y COMERCIO-"); 
                print("Ingrese 0 si esta en contra");
                print("Ingrese 1 si esta a favor");
                print("Ingrese 2 para salir")
                opcion = str(input("Digite su opcion: "));
                try :#si ingresa un numero, lo ejecuta
                        opcion = int(opcion);
                        if opcion < 0 or opcion > 2 :#si esta fuera del rango o es negativo
                                print("Debes ingresar una opcion valida");
                                aumento.append(0); 

                        else :#en otro caso
                            if diputados == 0:#Si ya no hay diputados que puedan votar
                                 pass; #No agregara nada, y el for terminara
                            elif opcion == 1 and diputados != 0:#Si elige la opcion 1 y todavia se puede votar
                                favor += 1; #Se le añadira 1 a favor
                                aumento.append(0);
                            elif opcion == 0 and diputados != 0: #En la opcion 0 y 1 se repite lo mismo que lo anterior
                                contra += 1;
                                aumento.append(0);
                            elif opcion == 2 and diputados != 0: #sale
                                pass;#no aumenta el limite, para salir
                        
                                
                                
                except :#en caso de que ingrese un caracter
                        print("\nDebes de ingresar solo numeros enteros para poder votar");
                        aumento.append(0);
                        
        total_votos = favor + contra; #Sacara el total de votos
        #Sacara el promedio de cada opcion
        promfavor= (favor / diputados) * 100; 
        promcontra= (contra / diputados) * 100;
        promabst = ((diputados - (favor+contra))/diputados)*100;
        #Y la mandara a imprimir
        print("El promedio de los votos a favor fue de %" , promfavor , "Con un total de votos de " , favor);
        print("El promedio de los votos en contra fue de %" , promcontra , "Con un total de votos de " , contra);
        print("El promedio de los votos abstenidos fue de %" , promabst);


def e4():#funcion para el ejercicio 4
    print("\nEjercicio 4");
    diputados();

def suma():
    aumento = [0] ;#sera la variable que hace infinito el ciclo
    aux=0; #Se necesitara una variable auxiliar para hacer calculos
    
    
    for i in aumento : #Se crea el for en caso de que ingrese un numero invalido
        numero= str(input("Ingresa el numero de donde empezara la suma: "));
        try:
            numero = int(numero);
            total=0; #Se inicializa el total
            if numero < 1: #Si ingresa algun valor menor a 1 no se hara ninguna suma
                print("Debes ingresar una opcion valida");
                aumento.append(0);
            else :
                #Se hara la impresion y la suma a traves del for
                print("-Suma en decimal-");
                for x in range(numero) : 
                    if numero-aux > 1: #El if-else, esta solo por el signo al final
                        print(numero-aux , end=" + ");
                        total += numero-aux; #El total va sumando todos los numeros en sucesion
                        aux += 1; #El auxiliar sirve para decrecer el numero de partida
                    else :
                        print(numero-aux , end=" = ");
                        total += numero-aux;
                        aux += 1;
                        
                print(total); #Imprime el total en decimal
                aux=0;
                total=0; #Reinicializa el auxiliar y el total para volverlo a utilizar en el hexadecimal
                print("-Suma en hexadecimal-"); #Hace lo mismo que en el for decimal, pero tratando el dato como hexadecimal
                for y in range(numero) :
                    if numero-aux > 1:
                        print(hex(numero-aux) , end=" + ");
                        total += numero-aux;
                        aux += 1;
                    else :
                        print(hex(numero-aux) , end=" = ");
                        total += numero-aux;
                        aux += 1;
                print(hex(total)); #Imprime el total en hexadecimal

        except:
            print("Ingresa un numero entero!");
            aumento.append(0);

def e5():#funcion para el ejercicio 5
    print("\nEjercicio 5");
    suma();

def python():
    aumento = [0] ; #Toda esta parte sera inicializacion de tablas y variables que se necesitaran
    aumentob = [0]; #Equivalente a hacer el ciclo while, en caso de que la calificacion de la materia este mal
    aumentocod = [0]; #Equivalente al while, pero para en caso de que el codigo este repetido
    alumnos=0; #Variable para contar el total de alumnos, y que servira a la hora de calcular el promedio
    cod_totales=0; #El total de codigos que existen, para compararlos y encontrar alguno igual
    pmax=0; #El promedio maximo, que se usara de auxiliar
    cmax=""; #El codigo del promedio maximo, que se usara de auxiliar
    empate=0; #Contador en caso de que haya en caso de empate, poder saber cuantos empataron
    pmaxs=[]; #Lista para guardar los promedios maximos
    cmaxs=[]; #Lista para guardar los codigos de los promedios maximos
    codigos=[]; #Lista para guardar codigos
    promedio=[]; #Lista para guardar promedios
    materia1=[]; #Listas para guardar calificaciones de materias
    materia2=[];
    materia3=[];
    
    print("\n-Programando en Python con Profesor Campos-"); 
    for i in aumento: #Se crea el ciclo for, para que se sigan subiendo datos de alumnos
        print("\nIngrese 1 si quiere ingresar datos del alumno");
        print("Ingrese 0 si ya se termino de registrar los alumnos");
        opcion = str(input("Digite su opcion: "));
        try :#si ingresa un numero, lo ejecuta
            opcion = int(opcion);
            
            if opcion < 0 or opcion > 1 :#si esta fuera del rango o es negativo te lo repite
                print("Debes ingresar 1 ó 0");
                aumento.append(0);
            else:
                if opcion==1: #Si elige meter datos
                    aumento.append(0);
                    alumnos +=1; 
                    aux= str(input("Dame tu codigo de alumno "));

                    for x in range(cod_totales):
                    #Este for sera para comprobar que el codigo no este registrado, comparandolo  con todos los de la lista
                        for z in aumentocod:
                            if aux == codigos[x]:
                                print("Codigo ya registrado! Ingrese otro: ", end="");
                                aux=str(input());
                                aumentocod.append(0);
                    
                    cod_totales+=1;
                    codigos.append(aux); #Agregara el codigo a la lista
                        
                    
                    for x in aumentob: #Los for in aumentob, sera para evitar calificaciones erroneas, en vez del while
                        error=1;
                        print("Dame la calificacion de tu materia #1" , end=" ");
                        auxm= str(input()); 
                        try:
                            auxm = int(auxm);
                            if auxm < 0 or auxm > 100: #Si no esta en el rango, pide la calificacion valida
                                print("Ingresa una calificacion valida!");
                                aumentob.append(0);
                            else: #Si todo esta bien ,lo agrega a la lista 
                                materia1.append(auxm);
                                aumentob = [0];

                        except:
                            print("Ingresa numero entero para la calificacion!");
                            aumentob.append(0);
                    for x in aumentob: #Mismo caso que el for anterior
                        print("Dame la calificacion de tu materia #2", end=" ");
                        auxm= str(input());
                        try:
                            auxm = int(auxm);
                            if auxm < 0 or auxm > 100:
                                print("Ingresa una calificacion valida!");
                                aumentob.append(0);
                            else:
                                materia2.append(auxm);
                                aumentob = [0];

                        except:
                            print("Ingresa numero entero para la calificacion!");
                            aumentob.append(0);
                    for x in aumentob: #Mismo caso que el for anterior
                        print("Dame la calificacion de tu materia #3" , end=" ");
                        auxm= str(input());
                        try:
                            auxm = int(auxm);
                            if auxm < 0 or auxm > 100:
                                print("Ingresa una calificacion valida!");
                                aumentob.append(0);
                            else:
                                materia3.append(auxm);
                                aumentob = [0];

                        except:
                            print("Ingresa numero entero para la calificacion!");
                            aumentob.append(0);
                if opcion==0: #Si decide salir
                    if alumnos > 0: #Tiene que haber alumnos para sacar promedios
                        for y in range(alumnos): #Con este for saca los promedios de cada alumno
                            mat1= materia1[y];
                            mat2= materia2[y];
                            mat3= materia3[y];
                            prom=(mat1+mat2+mat3)/3;
                            promedio.append(prom);
                        for y in range(alumnos): #Este for saca el promedio maximo
                            if promedio[y] > pmax: #Si es mayor al maximo, reinicializara el empate y la lista de promedios maximos
                                #Y solo se ingresara el nuevo promedio maximo
                                empate=0;
                                pmaxs=[];
                                cmaxs=[];
                                pmax=promedio[y];
                                cmax=codigos[y];
                                cmaxs.append(cmax);
                                pmaxs.append(pmax);
                            elif promedio[y]==pmax: #Si es igual al maximo, lo añadira a la lista de promedio maximos, y añadira 1 mas al caso de empate
                                empate+=1;
                                pmax=promedio[y];
                                cmax=codigos[y];
                                cmaxs.append(cmax);
                                pmaxs.append(pmax);
                        #If else para saber que mensaje imprimir en caso o no de empate
                        if empate != 0:
                                print("--Hubo ",empate+1," niños empatados con los promedios mas alto--");
                        else:
                            print("--Promedio mas alto--");
                            
                        for z in range(empate+1):#Imprime el o los promedios maximos
                            prom=pmaxs[z];
                            cod=cmaxs[z];
                            print("El alumno de codigo ",cod," obtuvo un promedio de ", prom);      
                    else: #Si no se registraron alumnos, no hace nada
                        print("No se registro ningun alumno");
                                                                                 
        except :#en caso de que ingrese un caracter
            print("\nDebes de ingresar solo numeros enteros para elegir su opcion");
            aumento.append(0);


        
def e6():#funcion para el ejercicio 6
    print("\nEjercicio 6");
    python();

def cajero():#calcula el total de una venta mas iva y el total de dinero en caja
    caja = 0;#el valor inicial de caja es uno
    subtotal = 0;
    iva = 0;
    total = 0;
    pago = 0;
    cambio = float(0);
    opcion = 0;
    aumento = [0];#lista para el for infinito
    #costo de algunos productos
    huevo = 10;
    leche = 15;
    frijol = 7;
    cheetos = 13;
    galletas = 10;
    producto = 0;#guardara la opcion de producto elegida
    for i in aumento:
        opcion = str(input("Ingresa 1 para ingresar un producto, 2 para terminar la venta, 3 para imprimir el total en caja y 4 para salir  "));
        try:#entra si ingreso un numero
            opcion = int(opcion);
            if opcion < 1 or opcion > 4 :#si ingreso un numero no valido
                print("Las opciones solo son numeros positivos");
                aumento.append(0);
            if opcion == 1:#ingresa un producto y se calcula el subtotal
                print("\n1.-kg huevo $",huevo);
                print("2.-lt leche $",leche);
                print("3.-kg frijol $",frijol);
                print("4.-paquete cheetos $",cheetos);
                print("5.-paquete galletas $",galletas);
                producto = str(input("Ingresa el numero de opcion del producto vendido "));
                try:#si ingreso un numero
                    producto = int(producto);
                    if producto < 1 or producto > 5:#si no esta dentro del rango
                        print("Se deben ingresar numeros dentro de las opciones");
                        aumento.append(0);
                    else :
                        if producto == 1:
                            subtotal += huevo;
                            aumento.append(0);
                        if producto == 2:
                            subtotal += leche;
                            aumento.append(0);
                        if producto == 3:
                            subtotal += frijol;
                            aumento.append(0);
                        if producto == 4:
                            subtotal += cheetos;
                            aumento.append(0);
                        if producto == 5:
                            subtotal += galletas;
                            aumento.append(0);
                except:# si no ingreso un numero
                    print("No elejiste un numero");
                    aumento.append(0);
            if opcion == 2:#imprime el total de la venta
                iva = subtotal * 0.16;
                total = subtotal + iva;
                print("Subtotal $",subtotal);
                print("IVA $", iva);
                print("Total $",total);
                pago = str(input("Ingresa la cantidad recibida del cliente "));
                try:#si ingreso un numero
                    pago = float(pago);
                    if pago < 1 :#si ingresa negativos
                        pago = str(input("La cantidad recibida debe ser un numero positivo"));
                        pago = float(pago);
                        cambio = pago - total;
                        print("Cambio $",cambio);
                        caja += total;
                        #las siguientes tres variables se reinician a 0
                        subtotal = 0;
                        iva = 0;
                        total = 0;
                        aumento.append(0);
                    else:
                        cambio = pago - total;
                        print("Cambio $",cambio);
                        caja += total;
                        #las siguientes tres variables se reinician a 0
                        subtotal = 0;
                        iva = 0;
                        total = 0;
                        aumento.append(0);
                except:#si no ingreso un numero
                    pago = str(input("La cantidad recibida debe ser un numero "));
                    pago = float(pago);
                    if pago < 1 :#si ingresa negativos
                        pago = str(input("La cantidad recibida debe ser un numero positivo"));
                        pago = float(pago);
                        cambio = pago - total;
                        print("Cambio $",cambio);
                        caja += total;
                        #las siguientes tres variables se reinician a 0
                        subtotal = 0;
                        iva = 0;
                        total = 0;
                        aumento.append(0);
                    else:
                        cambio = pago - total;
                        print("Cambio $",cambio);
                        caja += total;
                        #las siguientes tres variables se reinician a 0
                        subtotal = 0;
                        iva = 0;
                        total = 0;
                        aumento.append(0);
            if opcion == 3:#imprime el total en caja
                print("El dinero en caja es $",caja);
            if opcion == 4:#sale del for
                pass;
                
        except:#si ingreso un caracter
            print("Deberia de haber ingresado un numero");
            aumento.append(0);
            
def e7():#funcion para el ejercicio 7
    print("\nEjercicio 7");
    cajero();

def menu():#muestra un menu para ejecutar los ejercicios
        aumento = [0] ;#sera la variable que hace infinito el ciclo
        for i in aumento :#se repetira hasta llegar a 1, al llegar a una opcion o validacion i se inicia en 0
                opcion = str(input("\n-Ingresa el numero de ejercicio a ejecutar y 8 para salir- "));
                try :#si ingresa un numero, lo ejecuta
                        opcion = int(opcion);
                        if opcion < 1 or opcion > 8 :#si esta fuera del rango o es negativo
                                print("Debes ingresar un numero valido ");
                                aumento.append(0);
                                
                        else :#en otro caso
                                if opcion == 1 :#ejecuta el ejercicio 1
                                        e1();
                                        aumento.append(0);
                                if opcion == 2 :#ejecuta el ejercicio 2
                                        e2();
                                        aumento.append(0);
                                if opcion == 3 :#ejecuta el ejercicio 3
                                        e3();
                                        aumento.append(0);
                                if opcion == 4 :#ejecuta el ejercicio 4
                                        e4();
                                        aumento.append(0);
                                if opcion == 5 :#ejecuta el ejercicio 5
                                        e5();
                                        aumento.append(0);
                                if opcion == 6 :#ejecuta el ejercicio 6
                                        e6();
                                        aumento.append(0);
                                if opcion == 7 :#ejecuta el ejercicio 7
                                        e7();
                                        aumento.append(0);
                                if opcion == 8 :
                                        pass;#no se agrega nada para que termine el ciclo
                                
                except :#en caso de que ingrese un caracter
                        print("\nDebes de ingresar solo numeros menu");
                        aumento.append(0);
                        

menu();

print("\npractica 09");
print("becerra gonzalez diego ivan");
print("padilla valdez gustavo");
