
​‌‌‍⁡⁣⁢
𝘈͟𝘉͟𝘈͟𝘐͟𝘟͟𝘖, 𝘈͟𝘙͟𝘌͟𝘈 𝘋͟𝘌 𝘛͟𝘌͟𝘚͟𝘛͟𝘌 ͟𝘌 𝘈͟𝘗͟𝘙͟𝘌͟𝘕͟𝘋͟𝘐͟𝘡͟𝘈͟𝘋͟𝘖

#type() mostra o tipo de informação de codigo

#int.print(type(5))
#int (numero inteiro)

#str.print(type("oi"))
#str (string, texto)

#float.print(type(5.5))
#float (numero decimal)

# % mostra o resto de uma divisão
#print(f"seu nome é {nome}") f antes de ("") para formatação de texto, e {} para texto junto com variavel

​‌‌‍⁡⁢⁢⁢⁡⁢⁣⁢#͟𝙖͟𝙪͟𝙡͟𝙖 𝙙͟𝙚 𝙡͟𝙞͟𝙨͟𝙩͟𝙖͟𝙨​⁡

#frutas = [banana, maçã, pera, goiaba]
#isso é uma lista
#o primeiro item na regra index sempre começa com o espaço 0 (banana = 0, maçã = 1)

#print(frutas[1:3])
# [1:3] serve para mostras somente o item desejado da lista, ou seja mostra so de maçã ate pera (o numero apos : não segue a regra do index)

#print(len(frutas)) 
#o len() mostra quantos itens na lista (4 itens)

#print(frutas.count())
#count() sempre mostra quantas vezes um item se repete na lista

#print(frutas.index(pera))
#index() mostra em que posição o item esta (no caso de pera é 3 (regra index))

#if 'goiba' in frutas :
# print(" goiaba esta em frutas")
#else :
# print(' gaoiba não esta em frutas')
#verificar se a str(string) 'banana' esta na lista frutas

#frutas = [banana, maçã, pera, goiaba]
#print(frutas)
#adcionar_futas = input(" adiciona uma fruta")
#frutas.append(adcionar_frutas)
#print(frutas)
#append() vai adicionar um iten a ultima posição enquanto o codigo esta rodando (se eu colocar 'maracuja' ele sera adcionado apos goiaba)

#frutas = [banana, maçã, pera, goiaba]
#print(frutas)
#adcionar_futas = input(" adiciona uma fruta")
#frutas.insert(0, adcionar_frutas)
#print(frutas)
#insert() podemos adicionar um iten em qualquer posição enquanto o codigo esta rodando (o 0(ou outro numero) especifica a posição, ou seja se eu adicionar maracuja ele ficara na posição 0), a regra index valida 

#frutas.remove('pera')
#remove() vai tirar um item apos o codigo rodar
#pop() faz a mesma coisa do 'remove()' so que agora usando o index do item ( se eu quiser tirar pera eu escrevo frutas.pop.(2))

#clear() limpa uma lista

#lista_copia = frutas.copy()
#copy() cria uma copia diferente, podendo trabalhar com a copia ou a original individualmente

#numeros = [4, 7 , 8 ,0 ,2 ,3]
#numeros.sort()
#print(numeros)
#em uma lista numerica, o sort() ordena em ordem crescente, e em uma lista com letras ele ordena em ordem alfabetica
#sort(reverse=true)
#ordena em ordem decrescente ou de 'z' a 'a'

​‌‍‌⁡⁢⁢#t͟u͟p͟l͟a⁡​
#cores(azul, vermelho, verde)
#é uma lista que não pode ser alterada com codigos

#cores(azul, vermelho, verde)
#cores_lista = list(cores)
#transforma uma tupla em uma lista

#cores = [azul, vermelho, verde]
#cores_tupla = tuple(cores)
#transforma uma lista em tupla

#​‌‍‌⁡⁣⁢⁣dicionario⁡​
#gato = {'raça' = 'preto' 'nome' = 'beth'}
#mostra os itens referentes a uma propriedade

#print(gato['raça'])
#mostra o valor de uma chave
#get('raça', 'raça não encontrada')
#mostra o valor de uma chave, e se não encontrar pode exibir um texto

#a chave obrigatoriamente vai ser string mas pode colocar qualquer valor a chave ('chave' : [lista], texto, (tupla), 5 )

#gato['idade'] = 2
#adiciona uma chave e um valor ao dicionario (pode adcionar somente o valor também)