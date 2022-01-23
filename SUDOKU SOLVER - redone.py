#pos confirmar que funciona devemos
# melhorar a eficiencia e reduzir linhas desnecessarias
matr = [0]*81    #9x9
matp = [str()]*81    #9x9
ocux,ocuy,ocuz = [str()]*9,[str()]*9,[str()]*9
vacax,vacay,vacaz = str(),str(),str()
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
pos1="1,2,3,4,5,6,7,8,9"
pos2=str()
#pos1 devera sempre conter todos os nove lugares e se algum numero n poder constar
#devera vir NA   
num=1
v=1
def locf(x,y):
    coor=abs(((x+1)*9)-(9-(y+1)))-1
    return coor
#................................................................
#   Preencher o sudoku com os numeros usando a lista.
#   as outras partes comentadas sao para no caso de ter de receber as posicoes
#   como input
#while v<2:
for i in range(1,10):
    #pos=str(input("positions :"))#
    print(len(pos[i-1]))
    #num=input("num : ")#
    pos2=pos[num-1]
    x = y = t = int(0)
    for w in range(0,int(len(pos[num-1])/2)):
        x=int(pos2[t])
        y=int(pos2[t+1])
        matr[locf(x,y)]=num
        t+=2
   #v=int(input("type 2 to stop and 1 to add new number"))
    num+=1
# #.................................................................
# #   imprime o sudoku de uma forma facil de ver os nonantes
for x in range (0,9):
    if ((x==3)or(x==6)):
        print("")
    for y in range (0,9):
        print(matr[locf(x,y)], end=(""))
        if ((y==2)or(y==5)or(y==8)):
            print("  ", end=(""))
    print("")
# #.................................................................
# #   preenche a matrix ocup com as posicoes ocupadas
for x in range (0,9):
    for y in range (0,9):
        if matr[locf(x,y)]!=0:
            num = matr[locf(x,y)]
            ocux[num-1]+=str(x)
            ocuy[num-1]+=str(y)
            if x in range(0,3):
                if y in range(0,3):
                    ocuz[num-1]+=str(1)
                elif y in range(3,6):
                    ocuz[num-1]+=str(2)
                else:
                    ocuz[num-1]+=str(3)
            elif x in range(3,6):
                if y in range(0,3):
                    ocuz[num-1]+=str(4)
                elif y in range(3,6):
                    ocuz[num-1]+=str(5)
                else:
                    ocuz[num-1]+=str(6)
            else:
                if y in range(0,3):
                    ocuz[num-1]+=str(7)
                elif y in range(3,6):
                    ocuz[num-1]+=str(8)
                else:
                    ocuz[num-1]+=str(9)  
for num in range (1,10):
    print(num)
    print(" ",ocux[num-1],"\n ",ocuy[num-1],"\n ",ocuz[num-1]) 
# #................................................................
# # preenche as var vacax,y,z com as pos vagas
for x in range (0,9):
    for y in range (0,9):
        if matr[locf(x,y)]==0:
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
# #imprime a quantidade e as posicoes vagas de uma forma bm compreensivel
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
# #...................................................................
# #preenche a matr de possibilidades cell por cell
xx=yy=nn=num=int(0)
def fun():
    for num in range(1,10):
        if(str(num) in pos1)==True:
            if (str(nn) in ocuz[num-1])==False:
                if (str(xx) in ocux[num-1])==False:
                    if(str(yy) in ocuy[num-1])==False:
                        if (str(num) in matp[locf(xx,yy)]) == False:
                            matp[locf(xx,yy)] += str(num)
        elif (str(num) in pos1)==False:
            if (str(num) in matp[locf(xx,yy)]) == False:
                matp[locf(xx,yy)] += str(num)                
    return matp[locf(xx,yy)]
for xx in range(0,9):
    for yy in range (0,9):
        if xx in range(0,3):
            if yy in range(0,3):
                nn=1
                matp[locf(xx,yy)]=fun()
            elif yy in range(3,6):
                nn=2
                matp[locf(xx,yy)]=fun()
            else:
                nn=3
                matp[locf(xx,yy)]=fun()
        elif xx in range(3,6):
            if yy in range(0,3):
                nn=4
                matp[locf(xx,yy)]=fun()
            elif yy in range(3,6):
                nn=5
                matp[locf(xx,yy)]=fun()
            else:
                nn=6
                matp[locf(xx,yy)]=fun()
        else:
            if yy in range(0,3):
                nn=7
                matp[locf(xx,yy)]=fun()
            elif yy in range(3,6):
                nn=8
                matp[locf(xx,yy)]=fun()
            else:
                nn=9
                matp[locf(xx,yy)]=fun()
print("")
# #.................................................................
# #   imprime o matp de uma forma facil de ver os nonantes
#(cada um dos 9 quadrados 3x3 do sudoku)
for x in range (0,9):
    if ((x==3)or(x==6)):
        print(""*6,)
    print(" ", end=(""))
    for y in range (0,9):
        print(" ", end=(""))
        print(matp[locf(x,y)],end=(""))
        print("_"*(9-len(matp[locf(x,y)])), end=(""))
        if ((y==2)or(y==5)or(y==8)):
            print(" "*3, end=(""))
    print("")
print("")
# #.................................................................


# #.................................................................