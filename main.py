import math

# Atividade proposta
# função f
f = lambda x : ( math.e ** x ) + ( 2 ** -x ) + 2 * math.cos( x ) - 6
# defivada da função f
flin = lambda x : ( math.e ** x ) - math.log(2) * 2 ** (-x) - 2 * ( math.sin(x) )
# x inicial ( x0 )
xi = 1
# Erro / Precisão
precisao = 10 ** -5

# # Exercicio 1
# f = lambda x : (2 * x ** 3) + (3 * x ** 2) - 2
# flin = lambda x : (6 * x ** 2) + (6 * x)
# # x inicial ( x0 )
# xi = 0.5
# # Erro / Precisão
# precisao = 10 ** -3

# # Exercicio 2
# f = lambda x : ( x ** 3 ) - ( x ** 2) - 1
# flin = lambda x : ( 3 * x ** 2 ) - ( 2 * x )
# # x inicial ( x0 )
# xi = 1
# # Erro / Precisão
# precisao = 10 ** -2

# # Outro
# f = lambda x : ( 2.71 ** ( (-x) ** 2 ) ) - x
# flin = lambda x : ( (2 * x) + (2.71 ** (x ** 2)) ) / ( 2.71 ** ( x ** 2 ) )
# # x inicial ( x0 )
# xi = 1
# # Erro / Precisão
# precisao = 10 ** -8

# diferença 
dif = 1

# contador de iteraçao
cont = 1

while dif > precisao:
  # x da proxima iteração
  xp = xi - ( f( xi ) / flin( xi ) )
  # print( "x = ", xi, ", f(x) = ", f(xi), ", flin(x) = ", flin(xi), "dif: ", abs( xp - xi ) )
  print( "X", cont, " = ", xp )
  # diferença eh o modulo do x menos x anterior
  dif = abs( xp - xi )
  # atualiza o xi
  xi = xp
  # conta iteração
  cont += 1

print( "A raiz procurada é aproximadamente: x = ", xp )
# print( "f(x) = ", f(xp) )