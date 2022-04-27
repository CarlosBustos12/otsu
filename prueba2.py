
import random as rm

def imprimir(lista_final_no_da_mas):

    minimo = min(lista_final_no_da_mas)
    i_min = lista_final_no_da_mas.index(minimo)
    print(f" el menor valor de varianza  K={i_min+1} ya que dio {minimo}  \n {minimo*255}")

def resultado_seg(lista_w_o, lista_U_o, u_o_2, lista_w_1, lista_U_1, u_1_2):
    om=0
    lista_final_no_da_mas=[]
    for i in range(len(lista_w_1)):
        om=(lista_w_o[i]*u_o_2[i])+lista_w_1[i]*u_1_2[i]
        #print(lista_w_o[i],'x',u_o_2[i],'+',lista_w_1[i],'x',u_1_2[i],'= ', om)
        lista_final_no_da_mas.append(om)
    imprimir(lista_final_no_da_mas)  
def U_o_2(lista_caso1,lista_U_o,suma_caso1):
    lista_U_0_2=[]
    
    for i in range(len(lista_caso1)):
        mult=0
        for j in range(len(lista_caso1[i])):
            mult=((lista_caso1[i][j]*((j-lista_U_o[i])**2))/suma_caso1[i])+mult
        #print(lista_caso1[i][j],j,mult,suma_caso1[i])
        lista_U_0_2.append(mult)
    return lista_U_0_2
   
def U_1_2(lista_caso2,lista_U_1,suma_caso2):
    lista_U_1_2=[]
    
    for i in range(len(lista_caso2)):
        mult=0
        for j in range(len(lista_caso2[i])):
            mult=((lista_caso2[i][j]*((j-lista_U_1[i])**2))/suma_caso2[i])+mult
        #print(lista_caso1[i][j],j,mult,suma_caso1[i])
        lista_U_1_2.append(mult)
    return lista_U_1_2


def matematica(suma_caso1,suma_caso2,suma_total,lista_caso1,lista_caso2,lista_multi,lista_multi1):
    
    lista_w_o=[]
    lista_U_o=[]

    lista_w_1=[]
    lista_U_1=[]
        
    for i in range(len(lista_caso1)):
        mult=0
        mult2=0

        W_o=float(suma_caso1[i]/suma_total)
        lista_w_o.append(W_o)
        W_1=float(suma_caso2[i]/suma_total)
        lista_w_1.append(W_1)

        U_o=float((lista_multi[i][0])/suma_caso1[i])
        lista_U_o.append(U_o)
        U_1=float((lista_multi1[i][0])/suma_caso2[i])
        lista_U_1.append(U_1)
    
    u_o_2=U_o_2(lista_caso1,lista_U_o,suma_caso1)
    
    u_1_2=U_1_2(lista_caso2,lista_U_1,suma_caso2)
    
    resultado_seg(lista_w_o, lista_U_o, u_o_2, lista_w_1, lista_U_1, u_1_2)


def depurar(r_q,lista_caso1,lista_caso2):

    suma_total=sum(r_q)
    suma_caso1=[]
    suma_caso2=[]
    mult=0
    mult1=0
    lista_multi=[]
    lista_multi1=[]  

    for i in range(len(lista_caso1)):
        mult =0
        mult1=0
        suma_caso1.append(sum(lista_caso1[i]))
        suma_caso2.append(sum(lista_caso2[i]))

        for j in range(len(lista_caso1[i])):
            mult=j*lista_caso1[i][j]+mult
        
        for k in range(len(lista_caso2[i])):
            mult1=k*lista_caso2[k][j]+mult1
        lista_multi.append([mult])
        lista_multi1.append([mult1])
    print(suma_caso1,suma_caso2,suma_total,lista_caso1,lista_caso2,lista_multi,lista_multi1)
    matematica(suma_caso1,suma_caso2,suma_total,lista_caso1,lista_caso2,lista_multi,lista_multi1)
        

def inicio():
    r_q=[8,7,2,6,9,4]
    lista_caso1=[]
    lista_caso2=[]
    r_q=[elemento for elemento in r_q if elemento !=0]
    for i in range(len(r_q)+1):
        lista_caso1.append(r_q[:i])
        lista_caso2.append(r_q[i+1:])
    
    lista_caso1.pop(0)
    lista_caso2.pop(len(lista_caso2)-1)
    
    lista_caso1.pop(len(lista_caso1)-1)
    
    depurar(r_q,lista_caso1,lista_caso2)

inicio()
