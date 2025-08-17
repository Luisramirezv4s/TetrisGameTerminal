from enum import Enum
import keyboard

class Move(Enum): #Para definir los tipos de movimiento, asignamos una clase llamada Move
    #Estos movimiento son especificos, es decir que podemos consiferarlos como constantes
    DOWN = 1 #por implementacion con python tenemos que asignarles un identificador
    RIGHT = 2
    LEFT = 3
    ROTATE = 4
def tetris(): #definimos la funcion de juego
    #podemos reprentar el panel del juego como una matriz bidimensional
    #Cada lista representa una fila del juego
    #Posteriormente agrupar cada uno de las listas en una sola
    #Asignamos la variable screen como el conjunto de arrays

    screen = [['🐊', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🐊', '🐊', '🐊', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
              ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲']]
   
    printScreen(screen) #En diferentes sitios de la aplicacion se necesita continuamente imprimir la pantalla

    rotation = 0 #19. Definimos en que rotacion se encuentran los objetos
                    #Por cada iteracion ademas va a devorlver el parametro de rotacion
    while(True): 
        event = keyboard.read_event()

        if event.name == 'esc':
            break #Detener la ejecucion del programa
        elif event.event_type == keyboard.KEY_DOWN: #20.Definimos el controlador de eventos del programa
            if event.name == 'down':
                (screen, rotation) = movePiece(screen, Move.DOWN, rotation)
            elif event.name == 'right':
                (screen, rotation) = movePiece(screen, Move.RIGHT, rotation)
            elif event.name == 'left':
                (screen, rotation) = movePiece(screen, Move.LEFT, rotation)
            elif event.name == 'space':
                (screen, rotation) = movePiece(screen, Move.ROTATE, rotation)
  
def movePiece(screen: list, movement: Move, rotation: int) -> (list, int):#8. Asignarle el valor del screen a la funcion #18. Definimos el parametro de rotacion 
    #1. Definir los tipos de movimiento. Si solo existen una serie de parametros con valores concretos. Podemos utilizar enumerados, en python esta es una biblioteca que tenemos que importar: enum  
    #2. Es decir, el parametro Move le indica a la funcion movePiece los movimientos especificos que puede realizar
    newScreen = [['🔲'] * 10 for i in range (10)] #11. Para actualizar el movimiento del objeto podemos reconstruirlo o visualizarlo como un screen en blanco

    rotationItem = 0 #15. Definimos cual es el objeto a rotar por medio un contador
    rotations = [[(+1, +1), (0, 0), (-2, 0), (-1, -1)], #14. Definimos las coordenadas de movimiento de rotacion de cada elemento. En este caso, rotaran 90 grados
                 [(0, +1), (-1, 0), (0, -1), (+1, -2)],
                 [(0, +2), (+1, +1), (-1, +1), (-2, 0)],
                 [(0, +1), (+1, 0), (+2, -1), (+1, -2)]]
    newRotation = rotation
    if movement is Move.ROTATE: 
        newRotation = 0 if rotation == 3 else rotation + 1
    

    for rowIndex, row in enumerate(screen): #Enumerate() permite acceder al index de cada elemento del screen
        for columnIndex, item in enumerate(row):

            if item  == '🐊':   #9. Es el objeto al que se le asignan las instrucciones de movimiento

                newRowIndex = 0 #10. Cada vez que se ejecute un movimiento se tiene que calcular el valor del nuevo indice
                newColumnIndex = 0 

                match movement: #3. Match movement: Para analisis de movimiento 
                    case Move.DOWN: #4. case, podemos verla como una clausula para acceder a los tipos de movimiento  
                        newRowIndex = rowIndex + 1 
                        newColumnIndex = columnIndex
                    case Move.RIGHT: #5. Podemos interpretar esto como una estructura if. 
                        newRowIndex = rowIndex
                        newColumnIndex = columnIndex + 1   
                        
                    case Move.LEFT:  #6. Una manera de interpretar el movimiento del objeto, es viendolo como un cambio de posicion en la matriz en el que cada cambio esta determinado por un par de coordenadas. En este caso el par de coordenadas esta dado por la fila y la columna
                        newRowIndex = rowIndex
                        newColumnIndex = columnIndex - 1 #7, Cada movimiento tiene un patron determinado
                        
                        
                    case Move.ROTATE:
                        newRowIndex = rowIndex + rotations[newRotation][rotationItem][0] #17. Definimos que la rotacion esta dada por el indice del par coordenado en ese momento
                        newColumnIndex = columnIndex + rotations[newRotation][rotationItem][1] #Y la modificacion de rotacion, rotations[Nos da el par coordenado que modificara el indice actual], rotationItem[nos dice en que elemento nos encontramos][elemento coordenado que se modificara]
                        rotationItem += 1 #16. Cada vez que se le agrege una unidad al contador, cambiamos el objeto a rotar
                
                if newRowIndex > 9 or newColumnIndex > 9 or newColumnIndex <0:
                    print('\nno se puede realizar el movimiento\n')
                    return (screen, rotation)
                else:
                    newScreen[newRowIndex][newColumnIndex] = '🐊' #11. Asignarle que coordenadas debe tomar nuestro item despues de un evento

    printScreen(newScreen) #12. newScreen funciona como el argumeto de la funcion printScreen(). 
                            #Es decir que el argumento de la funcion, variable screen inicial, se le asigna el valor de newScreen, una nueva matriz con elementos '🔲' pero con las coordenadas de nuestros items '🔳'
    return (newScreen, newRotation) #13. Una vez asignado el valor de newScreen a nuestra funcion printScreen(). Se retorna el valor de nuestra nueva matriz, o sea, del new screen
                    #Es decir, cada que se ejecute la funcion movePiece(). Una vez imprima el valor del newScreen y actualizara los cambios para una nueva ejecucion

def printScreen(screen: list):
    print('\nPantalla Tetris:\n')
    for row in screen: #Por cada ciclo se imprime un elemento de screen 
        print(''.join(map(str, row))) # .join() permite concatenar todos los elementos separados por un espacio vacio o 'n'
                                      # map() permite transformar un iterable completo usando otra funcion(cualquiera. map(inserte funcion, inserte iterable o cadena iterable)
                                      # Es decir. la funcion map() nos ahorra la necesidad de iterar cada uno de los elementos a la vez. Optimizando el codigo y ahorrando memoria
                                      #En este caso le estamos pidiendo que convierta en valores de tipo string los elementos de cada fila o row. El ciclo for es para iterar sobre cada elemento del screen

tetris()