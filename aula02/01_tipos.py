#!/usr/bin/python3

type(1)
type(1.2)
type(2j)
type(True)

dir(1)

var = True
type(var)
var.numerator


type('Chocolate')
var = 'Chocolate'
var.upper()


var = ' curso python fundamentals     '
var.title()                 #Capitaliza as palavras
var.lower()                 #Converte para minúsculo
var.replace('e','&')        #Substituição
var.strip()                 #Trim
var.lstrip()                #LTrim
var.rstrip()                #RTrim
var.split()                 #Quebra em lista
var.startswith('c')         #Inicia c
var.startswith(' ')         #Inicia 
var.startswith(' c')        #Inicia 
var.strip().startswith('c') #Trim e Inicia com 'c' 
'.'.join(var)               #' .c.u.r.s.o. .p.y.t.h.o.n. .f.u.n.d.a.m.e.n.t.a.l.s. . . . . '



letras = ['a','b','c','d']
len(letras)     #Tamanho
letras[0]       #Posicao
letras[2]       #Posicao
letras[-1]      #Ultima Posição
letras[1:3]     #['b', 'c']
letras[0:-2]    #['a', 'b']

letras.append('e')      #Insere a letra 'e'
letras.insert(0,'a')    #Insere a letra 'a' na posição 0
letras.pop()            #Remove a ultima posição
letras.pop(0)           #Remove a posição informada

