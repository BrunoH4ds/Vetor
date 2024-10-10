Frutas = ["uva","Maça","Banana","abacaxi","morango"]
quant_Produtos = [20,15,10,30,5]

def atualicazao():
  quant_Produtos[0] -= 3
  quant_Produtos[3] -= 2
  print(quant_Produtos)
atualicazao();
def adicao():
  quant_Produtos[4] += 5
  print(quant_Produtos)
adicao();
def exibicao():
  for f, q in zip(Frutas, quant_Produtos):
        print(f"fruta: {f} quantidade: {q}")
exibicao();
