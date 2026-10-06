import easygui

# 1. Mensagem simples de boas-vindas
easygui.msgbox("Bem-vindo à aplicação com EasyGUI!", title="Início", ok_button="Começar")

# 2. Caixa de entrada para texto (Nome)
nome = easygui.enterbox("Qual é o seu nome?", title="Cadastro")

# Se o utilizador clicar em 'Cancel' ou deixar em branco, o programa termina
if not nome:
    easygui.msgbox("Nenhum nome introduzido. O programa será encerrado.", title="Aviso")
    exit()

# 3. Caixa de seleção de botões (Menu)
escolha = easygui.buttonbox(
    f"Olá, {nome}! Escolha uma das opções abaixo:",
    title="Menu Principal",
    choices=["Pedir Dados", "Escolher uma Cor", "Sair"]
)

# 4. Ações com base na escolha
if escolha == "Pedir Dados":
    # Entrada de número inteiro (Idade)
    idade = easygui.integerbox("Digite a sua idade:", title="Idade", lowerbound=1, upperbound=120)
    
    # Campo para palavra-passe
    senha = easygui.passwordbox("Crie uma palavra-passe:", title="Segurança")
    
    if idade and senha:
        easygui.msgbox(f"Dados guardados com sucesso!\nNome: {nome}\nIdade: {idade}", title="Sucesso")

elif escolha == "Escolher uma Cor":
    # Lista de escolha simples (Dropdown/Listbox)
    cor = easygui.choicebox("Selecione a sua cor preferida:", title="Cores", choices=["Azul", "Verde", "Vermelho", "Amarelo"])
    
    if cor:
        easygui.msgbox(f"A sua cor favorita é {cor}!", title="Resultado")

else:
    easygui.msgbox("A sair do programa...", title="Até breve")