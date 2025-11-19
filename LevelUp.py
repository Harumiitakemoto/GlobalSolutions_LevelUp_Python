import random

# DADOS USUÁRIO
usuarios = {}
usuario_atual = None

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
    print("\n=== CADASTRO ===")
    nome = input("Digite seu nome: ").lower()
    if not nome:
        print("Nome inválido.")
        return None

    while True:
        email = input("E-mail (será seu login): ").strip().lower()
        if not email:
            print("E-mail inválido. Tente novamente.")
            continue
        if email in usuarios:
            print("Este e-mail já está cadastrado. Use outro ou faça login.")
            return None
        break

    idade = input("Idade: ").strip()
    interesse = input("Área de interesse (ex: backend, dados, segurança): ").strip().lower()

    usuarios[email] = {
        "nome": nome,
        "idade": idade,
        "interesse": interesse,
        "habilidades": [],
        "carreira": None,
        "plano": []
    }

    print(f"\nUsuário {nome} cadastrado com sucesso! Faça login com '{email}'.\n")
    return email


def entrar_usuario():
    print("\n=== LOGIN ===")
    email = input("Digite seu e-mail: ").lower().strip()

    if email not in usuarios:
        print("E-mail não encontrado! Cadastre-se primeiro.\n")
        return None

    print(f"\nBem-vindo(a), {usuarios[email]['nome']}!\n")
    return email

def criar_perfil(email):
    print("\n=== Atualizar Perfil ===")
    usuarios[email]["idade"] = input("Idade: ")
    usuarios[email]["interesse"] = input("Área de interesse: ").lower()
    print("\nPerfil atualizado com sucesso!\n")


def sugerir_carreira(email):
    interesse = usuarios[email]["interesse"]

    if not interesse:
        print("\nCrie seu perfil primeiro.\n")
        return

    sugestoes = [c for c in carreiras if interesse in c.lower()]
    if not sugestoes:
        sugestoes = list(carreiras.keys())

    print("\nCarreiras sugeridas:")
    for i, c in enumerate(sugestoes, 1):
        print(f"{i}. {c}")

    escolha = int(input("\nEscolha pelo número: ")) - 1

    if 0 <= escolha < len(sugestoes):
        carreira = sugestoes[escolha]
        carreiras_escolhidas[email] = carreira
        print(f"\n✔ Carreira escolhida: {carreira}\n")
    else:
        print("Opção inválida!")


def gerar_plano(email):
    if email not in carreiras_escolhidas:
        print("\nEscolha uma carreira primeiro!\n")
        return

    carreira = carreiras_escolhidas[email]
    habilidades = carreiras[carreira]

    if email not in planos_estudo:
        iniciais = random.sample(habilidades, k=min(2, len(habilidades)))
        planos_estudo[email] = [{"tarefa": t, "feito": False} for t in iniciais]

    plano = planos_estudo[email]

    print("\n=== SEU PLANO DE ESTUDOS ===")
    for i, item in enumerate(plano, 1):
        status = "✔️" if item["feito"] else "❌"
        print(f"{i}. {item['tarefa']} [{status}]")

    if input("\nMarcar tarefa como concluída? (s/n): ").lower() == "s":
        num = int(input("Número da tarefa: ")) - 1

        if 0 <= num < len(plano):
            plano[num]["feito"] = True
            print("\n✔ Tarefa concluída!")

            # liberar próxima
            concluidas = all(t["feito"] for t in plano)
            if concluidas and len(plano) < len(habilidades):
                restantes = [
                    h for h in habilidades if h not in [t["tarefa"] for t in plano]
                ]
                nova = random.choice(restantes)
                plano.append({"tarefa": nova, "feito": False})
                print(f"Nova tarefa liberada: {nova}\n")


def ver_progresso(email):
    if email not in planos_estudo:
        print("\nGere um plano primeiro.\n")
        return

    plano = usuarios[usuario_atual]["plano"]

    if not plano:
        print("\nNenhum plano gerado.\n")
        return

    plano = planos_estudo[email]
    feitos = sum(t["feito"] for t in plano)
    total = len(plano)

    print(f"\nProgresso: {feitos}/{total} concluídas")
    print("Concluídas:")
    for t in plano:
        if t["feito"]:
            print("✔", t["tarefa"])
    print("\nPendentes:")
    for t in plano:
        if not t["feito"]:
            print("❌", t["tarefa"])


def conectar_mentor(email):
    if email not in carreiras_escolhidas:
        print("\nEscolha uma carreira primeiro!\n")
        return

    carreira = carreiras_escolhidas[email]

    print(f"\nMentores disponíveis para {carreira}:\n")

    encontrados = [
        m for m in mentores if carreira.lower() in m["area"].lower()
    ]

    if not encontrados:
        print("Nenhum mentor encontrado!\n")
        return

    for m in encontrados:
        print(f"- {m['nome']} ({m['area']})")
    print()


def cadastrar_mentor():
    nome = input("Nome do mentor: ").strip()
    area = input("Área do mentor (ex: Desenvolvedor Backend): ").strip()
    if not nome or not area:
        print("Dados inválidos. Cancelado.")
        return
    mentores.append({"nome": nome, "area": area})
    print("Mentor cadastrado com sucesso!\n")

#MENU
def menu():
    global usuario_atual
    usuario_atual = None

    while True:
            print("\n=== LEVEL UP – ASSISTENTE DE CARREIRA ===")
            print("1. Cadastrar usuário")
            print("2. Login")
            print("3. Criar/Atualizar Perfil")
            print("4. Sugestão de Carreira")
            print("5. Gerar Plano de Ação")
            print("6. Ver Progresso")
            print("7. Conectar com Mentor")
            print("8. Cadastrar Mentor Voluntário")
            print("9. Sair")

            opc = input("Escolha: ")

            if opc == "1":
                usuario_atual = cadastrar_usuario()

            elif opc == "2":
                usuario_atual = login()

            elif opc == "3":
                if usuario_atual:
                    criar_perfil(usuario_atual)
                else:
                    print("Faça login primeiro!")

            elif opc == "4":
                if usuario_atual:
                    sugerir_carreira(usuario_atual)
                else:
                    print("Faça login primeiro!")

            elif opc == "5":
                if usuario_logado:
                    gerar_plano(usuario_logado)
                else:
                    print("Faça login primeiro!")

            elif opc == "6":
                if usuario_atual:
                    ver_progresso(usuario_atual)
                else:
                    print("Faça login primeiro!")

            elif opc == "7":
                if usuario_atual:
                    conectar_mentor(usuario_atual)
                else:
                    print("Faça login primeiro!")

            elif opc == "8":
                cadastrar_mentor()

            elif opc == "9":
                print("Saindo...")
                break

            else:
                print("Opção inválida!\n")


    menu()