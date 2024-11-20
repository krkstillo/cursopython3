"""
Pida al usuario la edad y el sexo, para que la computador le indique si ya puede 
jubilarse. Tome en cuenta que un hombre se puede jubilar cuando
tenga 60 anos o mas, en cambio, una mujer mayor se jubilara si tiene mas de 54 anos.
"""

edad = int(input('Ingrese su edad'))
sexo = input('Ingrese su sexo ')

if edad >= 60 and sexo == 'masculino':
    print('Puedes jubilarte')
elif edad >= 54 and sexo == 'femenino':
    print('Puedes jubilarte')
else:
    print('No puedes jubilarte aun')