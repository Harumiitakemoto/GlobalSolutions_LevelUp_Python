import random


# DADOS DO SISTEMA
usuario = {
    "nome": "",
    "habilidades": [],
    "interesses": [],
    "estilo": ""
}
carreira_escolhida = None
plano = []

# DICIONÁRIO COMPLETO DE CARREIRAS
carreiras = {

        "Desenvolvedor Backend": ["Python", "APIs", "Git", "Banco de Dados"],
        "Desenvolvedor Frontend": ["HTML", "CSS", "JavaScript", "Design Responsivo"],
        "Desenvolvedor Fullstack": ["HTML", "CSS", "JavaScript", "Python", "APIs"],
        "Cientista de Dados": ["Python", "Estatística", "Machine Learning", "Pandas"],
        "Analista de Dados": ["Excel", "SQL", "Python", "Dashboard"],
        "Engenheiro de Dados": ["Python", "SQL", "Pipelines", "Cloud"],
        "UX/UI Designer": ["Figma", "Design Thinking", "Prototipação"],
        "QA / Tester": ["Testes Automatizados", "Selenium", "Lógica"],
        "Cybersegurança": ["Redes", "Pentest", "Criptografia"],
        "DevOps": ["Cloud", "CI/CD", "Containers"],
        "Técnico de Informática": ["Hardware", "Manutenção", "Redes"],
        "Suporte Técnico": ["Atendimento", "Sistemas", "Resolução de Problemas"],
    }

# MENTORES

mentores = [
    {"nome": "Mateus Oliveira", "area": "Desenvolvedor Frontend"},
    {"nome": "Rogerio Nakata", "area": "Desenvolvedor Backend"},
    {"nome": "Camila Silva", "area": "Analista de Dados"},
    {"nome": "Pedro Costa", "area": "Cybersegurança"},
    {"nome": "Laura Puglli", "area": "Cientista de Dados"},
    {"nome": "Paulo Andrade", "area": "DevOps"},
    {"nome": "Marina Rossi", "area": "UX/UI Designer"},
]


# FUNÇÕES

def criar_perfil():
    usuario["nome"] = input("Digite seu nome: ")
    usuario["idade"] = input("Idade: ")
    usuario["interesse"] = input("Qual área da tecnologia mais te interessa? (ex: backend, dados, segurança): ").lower()
    print("\nPerfil criado com sucesso!\n")
#!!!falta add habilidades, verificar qnd possuir varios cadastratos!!!

def sugerir_carreira():
    global carreira_escolhida

    if "interesse" not in usuario or not usuario["interesse"]:
        print("\nCrie um perfil antes.\n")
        return None

    interesse = usuario["interesse"]

    # Filtra carreiras de acordo com o interesse
    sugestoes = [c for c in carreiras if interesse in c.lower()]

    # Se nada encontrado, mostra todas
    if not sugestoes:
        sugestoes = list(carreiras.keys())

    print("\nCarreiras recomendadas para você:")
    for i, c in enumerate(sugestoes, 1):
        print(f"{i}. {c}")

    escolha = int(input("\nEscolha uma carreira pelo número: ")) - 1

    if 0 <= escolha < len(sugestoes):
        carreira_escolhida = sugestoes[escolha]
        print(f"\n✔ Carreira escolhida: {carreira_escolhida}\n")
        return carreira_escolhida

    print("\nOpção inválida.\n")
    return None

def gerar_plano():
    global plano

    if not carreira_escolhida:
        print("\n⚠ Escolha uma carreira primeiro.\n")
        return

    habilidades = carreiras[carreira_escolhida]

    # Se o plano está vazio, gera 2 tarefas iniciais aleatórias
    if not plano:
        iniciais = random.sample(habilidades, k=min(2, len(habilidades)))
        plano = [{"tarefa": t, "feito": False} for t in iniciais]

    print("\nSeu plano de estudos:")
    for i, item in enumerate(plano, 1):
        status = "✔️" if item["feito"] else "❌"
        print(f"{i}. {item['tarefa']} [{status}]")

    concluir = input("\nMarcar tarefa como concluída? (s/n): ")

    if concluir.lower() == "s":
        indice = int(input("Qual número da tarefa? ")) - 1

        if 0 <= indice < len(plano):
            plano[indice]["feito"] = True
            print("Tarefa marcada como concluída! ✔")

            # Quando todas forem concluídas, liberar próxima
            if all(t["feito"] for t in plano) and len(plano) < len(habilidades):
                restantes = [h for h in habilidades if h not in [t["tarefa"] for t in plano]]
                nova = random.choice(restantes)
                plano.append({"tarefa": nova, "feito": False})
                print(f"\nNova tarefa desbloqueada: {nova}")

        else:
            print("Número inválido.")
def ver_progresso():
    if not plano:
        print("\nGere um plano primeiro.\n")
        return

    total = len(plano)
    feitos = sum(1 for t in plano if t["feito"])

    barra = "#" * feitos + "-" * (total - feitos)
    print(f"\nProgresso: [{barra}] {feitos}/{total} tarefas concluídas.\n")
#!!!mostrar o nome das tarefas a serem feitas  e as feitas com check!!!

def conectar_mentor():
    if not carreira_escolhida:
        print("\nEscolha uma carreira primeiro.\n")
        return

    print(f"\nMentores disponíveis para {carreira_escolhida}:\n")

    encontrados = [ m for m in mentores if carreira_escolhida.lower() in m["area"].lower()]

    if not encontrados:
        print("\nNenhum mentor disponível para esta área\n")
        return
    for m in encontrados:
        print(f"- {m['nome']} ({m['area']})")

    print()


def cadastrar_mentor():
    nome = input("\nDigite o nome do mentor: ")
    area = input("\nDigite o area do mentor: ")

    mentores.append({"nome": nome, "area": area})
    print("\nMentoria cadastrada com sucesso!\n")


# MENU

while True:
    print("=== LEVEL UP – ASSISTENTE DE CARREIRA ===")
    print("1. Criar Perfil")
    print("2. Sugestão de Carreira")
    print("3. Gerar Plano de Ação")
    print("4. Ver Progresso")
    print("5. Conectar com Mentor")
    print("6. Cadastrar Voluntariado Mentoria")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_perfil()
    elif opcao == "2":
        sugerir_carreira()
    elif opcao == "3":
        gerar_plano()
    elif opcao == "4":
        ver_progresso()
    elif opcao == "5":
        conectar_mentor()
    elif opcao == "6":
        cadastrar_mentor()
    elif opc == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")
