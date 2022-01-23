import numpy as np
matr = np.zeros([9,9], dtype=int)
matp = np.zeros([9,9], dtype="|S9")
ocup = np.zeros([3,9], dtype="|S9")
ocux,ocuy,ocuz = "","",""
vacax,vacay,vacaz = "","",""
## matr -- a matrix principal que contem os valores do sudoku, cada posicao
##        pode ter apenas um valor
##        
## matp -- matrix das possibilidades ou seja contem todas as
##        possiveis posicoes de todos os numeros, de tal forma q em cada
##        posicao vc pode ter no max 9 valores
##        
## ocup -- matrix das listas das posicoes/coordenadas ocupadas(ou seja dif de 0)
##        x, y e quadrad
##        
## oocux,ocuy,ocuz -- por alguma razao o array do numpy
##        do tipo str "ocup" n tava a receber os valores um por um entao
##        tive de colocar um por um primeiro nessas var e dps mandas para "ocup"
##
## vacax,vacay,vacaz -- vars q contem as posicoes desocupadas(=0) 
#................................................................
#   lista da posicoes dos numeros no sudoku, a fila um é do 1 e assim por...
   # de modo a facilitar o trabalho do programa toda a lista pos deve conter
   # todos os numeros para cada linha mas quando um numero nao estiver na matrix
   # na sua linha deve vir NA, adicionalmente o primeiro num de cada é o indicador

pos=["07245348",
    "153088",
    "211668",
    "001381",
    "4337",
    "2234466580",
    "52387084",
    "2064",
    "41"]
pos1=[int(1),int(2),int(3),int(4),int(5),int(6),int(7),int(8),int(9)]
#pos1 devera sempre conter todos os nove lugares e se algum numero n poder constar
#devera vir NA
    
num=1
v=1
#................................................................
#   Preencher o sudoku com os numeros usando a lista.
#   as outras partes comentadas sao para no caso de ter de receber as posicoes
#   como input

#while v<2:#
for i in range(1,10):
    #pos=str(input("positions :"))#
    print(len(pos[i-1]))
    #num=input("num : ")#
    f=int(0)
    pos2=pos[num-1]
    g=int(0)
    t=int(0)
    for w in range(0,int(len(pos[num-1])/2)):
        f=int(pos2[t])
        g=int(pos2[t+1])
        matr[f,g]=num
        t+=2
   #v=int(input("type 2 to stop and 1 to add new number"))
    num+=1
#.................................................................
#   imprime o sudoku de uma forma facil de ver os quadrados
for x in range (0,9):
    if ((x==3)or(x==6)):
        print("")
    for y in range (0,9):
        print(matr[x,y], end=(""))
        if ((y==2)or(y==5)or(y==8)):
            print("  ", end=(""))
    print("")
#.................................................................
#   preenche a matrix ocup com as posicoes
for num in range(1,10):
    ocux,ocuy,ocuz="","",""
    print(ocux,ocuy,ocuz)
    for x in range (0,9):
        for y in range (0,9):
            if matr[x,y]==num:
                ocux+=str(x)
                ocuy+=str(y)
                if x in range(0,3):
                    if y in range(0,3):
                        ocuz+=str(1)
                    elif y in range(3,6):
                        ocuz+=str(2)
                    else:
                        ocuz+=str(3)
                elif x in range(3,6):
                    if y in range(0,3):
                        ocuz+=str(4)
                    elif y in range(3,6):
                        ocuz+=str(5)
                    else:
                        ocuz+=str(6)
                else:
                    if y in range(0,3):
                        ocuz+=str(7)
                    elif y in range(3,6):
                        ocuz+=str(8)
                    else:
                        ocuz+=str(9)  
    print(num)
    print(" ",ocux,"\n ",ocuy,"\n ",ocuz)
    ocup[0,num-1],ocup[1,num-1],ocup[2,num-1] = ocux,ocuy,ocuz

# print(ocup) 
#................................................................
# # preenche as var vacax,y,z com as pos desocupadas
for x in range (0,9):
    for y in range (0,9):
        if matr[x,y]==0:
            vacax+=str(x)
            vacay+=str(y)
            if x in range(0,3):
                if y in range(0,3):
                    vacaz+="1"
                elif y in range(3,6):
                    vacaz+="2"
                else:
                    vacaz+="3"
            elif x in range(3,6):
                if y in range(0,3):
                    vacaz+="4"
                elif y in range(3,6):
                    vacaz+="5"
                else:
                    vacaz+="6"
            else:
                if y in range(0,3):
                    vacaz+="7"
                elif y in range(3,6):
                    vacaz+="8"
                else:
                    vacaz+="9"
# #................................................................
# #   imprime a quantidade e as posicoes vagas de uma forma bm compreensivel
print("")
print(" posicoes vagas ou seja = 0 ")
print(len(vacax))
print("x - ",end="")
for i in range(0,len(vacax)):
    print(vacax[i],end=(""))
print("")
print("y - ",end="")
for i in range(0,len(vacay)):
    print(vacay[i],end=(""))
print("")
print("q - ",end="")
for i in range(0,len(vacaz)):
    print(vacaz[i],end=(""))   
print("")
t=1 
# #................................................................
# ## work in progresss... ps: i have no idea what this is                    
# ##            
# ##for num in range(1,10):
# ##    ocup1 = ocup[2,num-1]
# ##    ocup1[0],ocup1[1] = "",""
# ##    print(ocup1)
# ##    ocup2 = ocup[1,num-1]
# ##    ocup2[0],ocup2[1],ocup2[str(len(ocup3))-1] = "","",""
# ##    print(ocup2)
# ##    
# ##    ocup3 = ocup[2,num-1]
# ##    ocup3[0],ocup3[1],ocup3[str(len(ocup3))-1] = "","",""
# ##    print(ocup3)
# ##    
# ####    for a in range(1,len(vacaz)):
# ####        for b in range(1,len(ocup[2,num-1])):
# ## ...................................................................
# ## ordena os numeros presentes no sudoku de forma decrescente em relacao
# ## ao quao presentes na matriz sao, para dps poder comecar a preencher a mtr das possibilidades
# # print(pos)
# # print(pos1)
# # posd = pos
# # posd1 = pos1
# # #posd-posicao decrescente
# # for a in range (0,int(len(posd))):
    # # for b in range (a+1,int(len(posd))):
        # # if (len(posd[a])<len(posd[b])):
            # # posd[a],posd[b]=posd[b],posd[a]
            # # posd1[a],posd1[b]=posd1[b],posd1[a]
# # print(pos)
# # print(posd) 
# # print(pos1)
# # print(posd1)
# # por alguma razao embora funcione esta ordem ordena n so posd e posd1 mas
# # tbm pos e pos1 q embora seja uma propriedade util neste momente nao e o desejado
# #jpara alem disso na parte abaixo ordenar os nums deixou de ser necessario ou util sendo\
# #q agr seram preenchidos n numero por numero mas sim cell por cell
# #...................................................................
# #preenche a matr de possibilidades cell por cell
# x,xx=int(0),int(0)
# y,yy=int(0),int(0)
# n,nn=int(0),int(0)
# matp1=str()
# ocux,ocuy,ocuz=str(0),str(0),str(0)
# num=int(0)
# print(ocup)
# for xx in range(0,9):
    # matp1=str()
    # for yy in range (0,9):
        # matp1=str()
        # if xx in range(0,3):
            # if yy in range(0,3):
                # nn=1
                # for num in range(1,10):
                    # if(num in pos1)==True:
                        # ocux=ocup[0,num-1]
                        # ocuy=ocup[1,num-1]
                        # ocuz=ocup[2,num-1]
                        # if (nn in ocuz)==False:
                            # print(nn in ocuz)
                            # if (xx in ocux)==False:
                                # print(xx in ocux)
                                # if(yy in ocuy)==False:
                                    # print(yy in ocuy)
                                    # matp1 = matp1+str(num)
                    # elif (num in pos)==False:
                        # matp1 = matp1+str(num)                
                # matp[xx,yy]=matp1
            # elif yy in range(3,6):
                # nn=2

            # else:
                # nn=3

        # elif xx in range(3,6):
            # if yy in range(0,3):
                # nn=4

            # elif yy in range(3,6):
                # nn=5
                
            # else:
                # nn=6

        # else:
            # if yy in range(0,3):
                # nn=7

            # elif yy in range(3,6):
                # nn=8

            # else:
                # nn=9

# print(matp)

# #so this seams like it would have worked but cuz we cant concat these np arrays we 
# # are gonna have to go for filing every cell in the mtr one at a time insted of every possibility for
# # for a given number one at a time like when im playing on my phone but the end result is the same  i guess
# # for w in range (0,len(posd1)):
# # #   num=posd1[w]("do not uncoment this line")
    # # ocuz=ocup[2,posd1[w]-1]
    # # ocux=ocup[0,posd1[w]-1]
    # # ocuy=ocup[1,posd1[w]-1] 
    # # for n in range (1,10):
        # # if (n in ocuz)==False:
            # # for x in range (0,9):
                # # if (x in ocux)==False:
                    # # for y in range (0,9):
                        # # if (y in ocuy)==False:
                            # # matp[x,y]== matp[x,y]+posd1[w]

  

