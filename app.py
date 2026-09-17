print("Bem vindo a companhia de sanemaento básico!") # saudação
while True:
    tipo = input("Digite o tipo de imóvel (comercial, casa, ou apartamento): ").lower() # entrada de dados, verifica se o que foi digitado esta correto, caso não, exibe a mensagem de erro e volta para o início
    if tipo in ["comercial", "casa", "apartamento"]:
        break
    else:
        print("Tipo de imóvel incorreto.") # coontinua o programa se estiver correto
 
consumo = float(input("Digite o consumo mensal de água em m³: ")) #
match tipo: #exibe o resultado de acordo com o tipo de imóvel e consumo
    case "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    case "casa":
        if (consumo <= 25):
            print("Consumo moderado – dentro do padrão residencial.")
        else: 
            print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
    case "apartamento":
        if (consumo < 10 ):
            print("Consumo econômico – excelente controle de água!")
        elif (consumo  <= 25):
            print("Consumo moderado – dentro do padrão residencial.")
        else:
            print("Consumo excessivo – adote medidas de economia e verifique vazamentos.") 


    