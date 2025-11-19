import random

# DADOS USUÁRIO
usuarios = {}
usuario_atual = None   # guarda o nome do usuário logado

#  CARREIRAS

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

mentores = [
    {"nome": "Mateus Oliveira", "area": "Desenvolvedor Frontend"},
    {"nome": "Rogerio Nakata", "area": "Desenvolvedor Backend"},
    {"nome": "Camila Silva", "area": "Analista de Dados"},
    {"nome": "Pedro Costa", "area": "Cybersegurança"},
    {"nome": "Laura Puglli", "area": "Cientista de Dados"},
    {"nome": "Paulo Andrade", "area": "DevOps"},
    {"nome": "Marina Rossi", "area": "UX/UI Designer"},
]

#  FUNÇÕES DO SISTEMA

def criar_usuario():
    print("\n=== Criar Novo Usuário ===")
    nome = input("Digite seu nome: ").lower()

    if nome in usuarios:
        print("\nEste nome já está cadastrado.\n")
        return

    idade = input("Idade: ")
    interesse = input("Área da tecnologia que te interessa: ").lower()

    usuarios[nome] = {
        "idade": idade,
        "interesse": interesse,
        "habilidades": [],
        "carreira": None,
        "plano": []
    }

    print("\nUsuário criado com sucesso!\n")


def entrar_usuario():
    global usuario_atual

    print("\n=== Entrar ===")
    nome = input("Digite seu nome: ").lower()

    if nome not in usuarios:
        print("\nUsuário não encontrado. Crie um perfil.\n")
        return

    usuario_atual = nome
    print(f"\nBem-vindo(a), {usuario_atual.capitalize()}!\n")


def sugerir_carreira():
    global usuarios, usuario_atual

    if usuario_atual is None:
        print("\nEntre com um usuário primeiro.\n")
        return

    interesse = usuarios[usuario_atual]["interesse"]

    sugestoes = [c for c in carreiras if interesse in c.lower()]

    if not sugestoes:
        sugestoes = list(carreiras.keys())

    print("\nCarreiras sugeridas:")
    for i, c in enumerate(sugestoes, 1):
        print(f"{i}. {c}")

    escolha = int(input("\nEscolha pelo número: ")) - 1

    if 0 <= escolha < len(sugestoes):
        usuarios[usuario_atual]["carreira"] = sugestoes[escolha]
        print(f"\n✔ Carreira escolhida: {sugestoes[escolha]}\n")
    else:
        print("Opção inválida.")


def gerar_plano():
    global usuarios, usuario_atual

    if usuario_atual is None:
        print("\nEntre com um usuário primeiro.\n")
        return

    carreira = usuarios[usuario_atual]["carreira"]

    if not carreira:
        print("\nEscolha uma carreira primeiro.\n")
        return

    habilidades = carreiras[carreira]
    plano = usuarios[usuario_atual]["plano"]

    if not plano:
        iniciais = random.sample(habilidades, k=2)
        usuarios[usuario_atual]["plano"] = [{"tarefa": t, "feito": False} for t in iniciais]

    plano = usuarios[usuario_atual]["plano"]

    print("\n=== Plano de Ação ===")
    for i, item in enumerate(plano, 1):
        status = "✔️" if item["feito"] else "❌"
        print(f"{i}. {item['tarefa']} [{status}]")

    if input("\nConcluir tarefa? (s/n): ").lower() == "s":
        idx = int(input("Número da tarefa: ")) - 1

        if 0 <= idx < len(plano):
            plano[idx]["feito"] = True
            print("\n✔ Tarefa concluída!")

            if all(t["feito"] for t in plano) and len(plano) < len(habilidades):
                restantes = [h for h in habilidades if h not in [t["tarefa"] for t in plano]]
                nova = random.choice(restantes)
                plano.append({"tarefa": nova, "feito": False})
                print(f"\nNova tarefa liberada: {nova}")
        else:
            print("Número inválido.")


def ver_progresso():
    if usuario_atual is None:
        print("\nEntre com um usuário primeiro.\n")
        return

    plano = usuarios[usuario_atual]["plano"]

    if not plano:
        print("\nNenhum plano gerado.\n")
        return

    total = len(plano)
    feitos = sum(1 for t in plano if t["feito"])

    print(f"\nProgresso: {feitos}/{total} concluídas")
    print("Concluídas:")
    for t in plano:
        if t["feito"]:
            print("✔", t["tarefa"])
    print("\nPendentes:")
    for t in plano:
        if not t["feito"]:
            print("❌", t["tarefa"])


def conectar_mentor():
    if usuario_atual is None:
        print("\nEntre com um usuário primeiro.\n")
        return

    carreira = usuarios[usuario_atual]["carreira"]

    if not carreira:
        print("\nEscolha uma carreira primeiro.\n")
        return

    print(f"\nMentores em {carreira}:\n")

    disponiveis = [m for m in mentores if m["area"].lower() == carreira.lower()]

    if not disponiveis:
        print("Nenhum mentor disponível.")
    else:
        for m in disponiveis:
            print("-", m["nome"], f"({m['area']})")


def cadastrar_mentor():
    nome = input("\nNome do mentor: ")
    area = input("Área do mentor: ")

    mentores.append({"nome": nome, "area": area})
    print("\n✔ Mentor cadastrado!\n")

#  MENU

while True:
    print("\n=== LEVEL UP – SISTEMA DE MENTORIA ===")
    print("1. Criar Usuário")
    print("2. Entrar no Sistema")
    print("3. Sugestão de Carreira")
    print("4. Gerar Plano de Ação")
    print("5. Ver Progresso")
    print("6. Conectar com Mentor")
    print("7. Cadastrar Mentor Voluntário")
    print("8. Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        criar_usuario()
    elif opcao == "2":
        entrar_usuario()
    elif opcao == "3":
        sugerir_carreira()
    elif opcao == "4":
        gerar_plano()
    elif opcao == "5":
        ver_progresso()
    elif opcao == "6":
        conectar_mentor()
    elif opcao == "7":
        cadastrar_mentor()
    elif opcao == "8":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")
