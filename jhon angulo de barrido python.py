from cmu_graphics import *
Rect(0,0,400,400,relleno=gradiente('cian','agua'))
#Religiones
cristianismo = 2300
islam = 1900
hinduismo = 1200
budismo = 520
religionesTradicionalesChina = 394
religionesAfroamericanas = 100
personasNoReligiosas = 1200

sumaDeReligiones= cristianismo + islam + hinduismo + budismo + religionesTradicionalesChina + religionesAfroamericanas + personasNoReligiosas
print(sumaDeReligiones)
porcenteje1 = (cristianismo /sumaDeReligiones)
porcentaje2 = (islam /sumaDeReligiones)
porcentaje3 = (hinduismo /sumaDeReligiones)
porcentaje4 = (budismo /sumaDeReligiones)
porcentaje5 = (religionesTradicionalesChina /sumaDeReligiones)
porcentaje6 = (religionesAfroamericanas /sumaDeReligiones)
porcentaje7 = (personasNoReligiosas /sumaDeReligiones)

anguloDeBarrido1= int(porcenteje1*360)
anguloDeBarrido2= int(porcentaje2*360)
anguloDeBarrido3= int(porcentaje3*360)
anguloDeBarrido4= int(porcentaje4*360)
anguloDeBarrido5= int(porcentaje5*360)
anguloDeBarrido6= int(porcentaje6*360)
anguloDeBarrido7= int(porcentaje7*360)

print(porcenteje1)
print(porcentaje2)
print(porcentaje3)
print(porcentaje4)
print(porcentaje5)
print(porcentaje6)
print(porcentaje7)

print(anguloDeBarrido1)
print(anguloDeBarrido2)
print(anguloDeBarrido3)
print(anguloDeBarrido4)
print(anguloDeBarrido5)
print(anguloDeBarrido6)
print(anguloDeBarrido7)

Circle(130,240,120)
Arc(130,240,240,240,0,anguloDeBarrido1,fill='rojo')
Arc(130,240,240,240,108,anguloDeBarrido2,fill='amarillo')
Arc(130,240,240,240,197,anguloDeBarrido3,fill='azul')
Arc(130,240,240,240,253,anguloDeBarrido4,fill='blanco')
Arc(130,240,240,240,277,anguloDeBarrido5,fill='naranja')
Arc(130,240,240,240,295,anguloDeBarrido6,fill='verde')
Arc(130,240,240,240,299,anguloDeBarrido7,fill='gris')

Rect(260,40,10,10,fill='rojo')
Rect(260,60,10,10,fill='amarillo')
Rect(260,80,10,10,fill='azul')
Rect(260,100,10,10,fill='blanco')
Rect(260,20,10,10,fill='naranja')
Rect(260,120,10,10,fill='verde')
Rect(260,140,10,10,fill='gris')

Rotulo('cristianismo',310,42)
Rotulo('islam',310,62)
Rotulo('hinduismo',310,82)
Rotulo('budismo',310,102)
Rotulo('tradicionalesChina',330,22)
Rotulo('afroAmericanas',320,122)
Rotulo('personasNoReligiosas',338,142)

cmu_graphics.run()