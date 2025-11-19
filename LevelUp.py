import random

#DADOS USUÁRIO
usuarios = {}
usuario_atual = None

carreiras_escolhidas = {}
planos_estudo = {}

# CARREIRAS
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

def criar_usuario():
    print("\n=== CADASTRO ===")
    nome = input("Nome: ").strip()
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

    print(f"\nUsuário '{nome}' cadastrado com sucesso! Faça login com '{email}'.\n")
    return email


def entrar_usuario():
    print("\n=== LOGIN ===")
    email = input("Digite seu e-mail: ").strip().lower()
    if email not in usuarios:
        print("E-mail não encontrado. Cadastre-se primeiro.\n")
        return None
    print(f"\nBem-vindo(a), {usuarios[email]['nome']}!\n")
    return email


def criar_perfil(email):
    print("\n=== CRIAR/ATUALIZAR PERFIL ===")
    idade = input(f"Idade [{usuarios[email]['idade']}]: ").strip()
    if idade:
        usuarios[email]['idade'] = idade

    interesse = input(f"Interesse [{usuarios[email]['interesse']}]: ").strip().lower()
    if interesse:
        usuarios[email]['interesse'] = interesse

    hab = input("Habilidades (separe por vírgula) ou ENTER para manter: ").strip()
    if hab:
        usuarios[email]['habilidades'] = [h.strip().title() for h in hab.split(",") if h.strip()]

    print("\nPerfil atualizado com sucesso!\n")


def sugerir_carreira(email):
    interesse = usuarios[email]['interesse']
    if not interesse:
        print("Defina seu interesse no perfil primeiro.\n")
        return

    sugestoes = [c for c in carreiras.keys() if interesse in c.lower()]
    if not sugestoes:
        print("Nenhuma correspondência exata encontrada. Listando todas as carreiras.\n")
        sugestoes = list(carreiras.keys())

    print("\nCarreiras sugeridas:")
    for i, c in enumerate(sugestoes, 1):
        print(f"{i}. {c}")

    escolha = input("Escolha a carreira pelo número (ou 0 para cancelar): ").strip()
    if not escolha.isdigit():
        print("Entrada inválida.\n")
        return
    num = int(escolha)
    if num == 0:
        print("Operação cancelada.\n")
        return
    idx = num - 1
    if 0 <= idx < len(sugestoes):
        usuarios[email]['carreira'] = sugestoes[idx]
        usuarios[email]['plano'] = []  # limpa plano anterior
        print(f"\n✔ Carreira escolhida: {sugestoes[idx]}\n")
    else:
        print("Opção inválida.\n")


def gerar_plano(email):
    carreira = usuarios[email]['carreira']
    if not carreira:
        print("Escolha uma carreira primeiro.\n")
        return

    habilidades = carreiras[carreira]

    if not usuarios[email]['plano']:
        iniciais = random.sample(habilidades, k=min(2, len(habilidades)))
        usuarios[email]['plano'] = [{"tarefa": t, "feito": False} for t in iniciais]

    plano = usuarios[email]['plano']

    print("\n=== SEU PLANO DE ESTUDOS ===")
    for i, item in enumerate(plano, 1):
        status = "✔️" if item["feito"] else "❌"
        print(f"{i}. {item['tarefa']} [{status}]")

    marcar = input("\nDeseja marcar alguma tarefa como concluída? (s/n): ").strip().lower()
    if marcar != 's':
        return

    num = input("Número da tarefa: ").strip()
    if not num.isdigit():
        print("Entrada inválida.")
        return
    idx = int(num) - 1
    if idx < 0 or idx >= len(plano):
        print("Número inválido.")
        return

    if plano[idx]['feito']:
        print("Essa tarefa já está marcada como concluída.")
        return

    plano[idx]['feito'] = True
    print("✔ Tarefa marcada como concluída!")

    # LIBERAR NOVAS TAREFAS
    if all(t['feito'] for t in plano) and len(plano) < len(habilidades):
        restantes = [h for h in habilidades if h not in [p['tarefa'] for p in plano]]
        if restantes:
            nova = random.choice(restantes)
            plano.append({"tarefa": nova, "feito": False})
            print(f"🔓 Nova tarefa liberada: {nova}")


def ver_progresso(email):
    plano = usuarios[email]['plano']
    if not plano:
        print("Nenhum plano gerado ainda.\n")
        return

    total = len(plano)
    feitos = sum(1 for t in plano if t['feito'])
    barra = "#" * feitos + "-" * (total - feitos)
    print(f"\nProgresso: [{barra}] {feitos}/{total} concluídas\n")

    print("✔ Concluídas:")
    for t in plano:
        if t['feito']:
            print(f"- {t['tarefa']}")

    print("\n❌ Pendentes:")
    for t in plano:
        if not t['feito']:
            print(f"- {t['tarefa']}")
    print("")


def conectar_mentor(email):
    carreira = usuarios[email]['carreira']
    if not carreira:
        print("Escolha uma carreira primeiro.\n")
        return

    encontrados = [m for m in mentores if carreira.lower() in m['area'].lower()]
    print(f"\nMentores disponíveis para {carreira}:")
    if not encontrados:
        print("Nenhum mentor encontrado para esta área.\n")
        return
    for m in encontrados:
        print(f"- {m['nome']} ({m['area']})")
    print("")


def cadastrar_mentor():
    nome = input("Nome do mentor: ").strip()
    area = input("Área do mentor (ex: Desenvolvedor Backend): ").strip()
    if not nome or not area:
        print("Dados inválidos. Cancelado.")
        return
    mentores.append({"nome": nome, "area": area})
    print("Mentor cadastrado com sucesso!\n")


# MENU

def menu():
    global usuario_atual
    usuario_atual = None

    while True:
        print("\n=== LEVEL UP – ASSISTENTE DE CARREIRA ===")
        print("1. Cadastrar usuário")
        print("2. Login (por e-mail)")
        print("3. Criar/Atualizar Perfil")
        print("4. Sugestão de Carreira")
        print("5. Gerar Plano de Ação")
        print("6. Ver Progresso")
        print("7. Conectar com Mentor")
        print("8. Cadastrar Mentor Voluntário")
        print("9. Logout")
        print("0. Sair")

        opc = input("Escolha: ").strip()

        if opc == "1":
            usuario_atual = criar_usuario() or usuario_atual

        elif opc == "2":
            usuario_atual = entrar_usuario() or usuario_atual

        elif opc == "3":
            if usuario_atual:
                criar_perfil(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opc == "4":
            if usuario_atual:
                sugerir_carreira(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opc == "5":
            if usuario_atual:
                gerar_plano(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opc == "6":
            if usuario_atual:
                ver_progresso(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opc == "7":
            if usuario_atual:
                conectar_mentor(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opc == "8":
            cadastrar_mentor()

        elif opc == "9":
            if usuario_atual:
                print(f"Usuário {usuarios[usuario_atual]['nome']} desconectado.\n")
                usuario_atual = None
            else:
                print("Nenhum usuário está logado.\n")

        elif opc == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()
