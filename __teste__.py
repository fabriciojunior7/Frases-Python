#Fabricio Junior
#Inicio: 07/07/2017
#Ultima Atualizacao: 07/07/2017
#Fim: ?

import os, random, time

os.system("cls")
os.system("color a")

txt = open("ai/teste/substantivos.txt", "r")
substantivos = txt.readlines()
txt.close()

txt = open("ai/teste/adjetivos.txt", "r")
adjetivos = txt.readlines()
txt.close()

txt = open("ai/teste/verbos-ligacao.txt", "r")
verbos_ligacao = txt.readlines()
txt.close()

txt = open("ai/teste/conjuncoes.txt", "r")
conjuncoes = txt.readlines()
txt.close()

save = open("Frases.txt", "a")

contador = 0

while(True):
	#time.sleep(5)
	
	frase = "%s %s %s" % (substantivos[random.randint(0, len(substantivos)-1)], verbos_ligacao[random.randint(0, len(verbos_ligacao)-1)], adjetivos[random.randint(0, len(adjetivos)-1)])
	frase = frase.split()
	frase = " ".join(str(e) for e in frase)

	frase2 = "%s %s %s" % (substantivos[random.randint(0, len(substantivos)-1)], verbos_ligacao[random.randint(0, len(verbos_ligacao)-1)], adjetivos[random.randint(0, len(adjetivos)-1)])
	frase2 = frase2.split()
	frase2 = " ".join(str(e) for e in frase2)

	conjuncao = conjuncoes[random.randint(0, len(conjuncoes)-1)]
	if("\n" in conjuncao):
		conjuncao = conjuncao[0:-1]

	#print(frase + "\n")
	#print(conjuncao + "\n")
	#print(frase2)
	#print("="*50)

	lista = [frase+"\n", conjuncao+"\n", frase2+"\n", ("="*20)+"\n"]

	save.writelines(lista)
	contador += 1
	if(contador > 10000): break

save.close()
os.system("start Frases.txt")
#os.system("shutdown /s /t 10")







