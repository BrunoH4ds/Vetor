Frutas = ["uva","Maca","Banana","abacaxi","morango"]
quant_Produtos = [20,15,10,30,5]

#se eu quiser eu poderia fazer um sistema mais funcional 
#usando input e acrecesntando no valor de atualizacao e adicao usando booleanos 
#porem isso e so uma atv entao ta tranquilo

def atualicazao():
  quant_Produtos[0] -= 3
  quant_Produtos[3] -= 2
  print(quant_Produtos )
atualicazao();
def adicao():
  quant_Produtos[4] += 5
  print( quant_Produtos )
adicao();
def exibicao():
  print("\n Bem-Vindo ao Estoque")
  print("--------------------------------------------------------")
  for f, q in zip(Frutas, quant_Produtos):
        print(f"fruta: {f} quantidade: {q}")
        print("--------------------------------------------------------")
exibicao();
