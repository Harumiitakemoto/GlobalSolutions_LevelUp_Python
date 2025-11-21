import random

#DADOS USUÁRIO
usuarios = {}
usuario_atual = None

carreiras_escolhidas = {}
planos_estudo = {}


# CARREIRAS
carreiras = {
    "Desenvolvedor Frontend": [
        ("Ler artigo de HTML + tags principais", 10),
        ("Assistir aula de CSS e montar layout simples", 15),
        ("Criar página responsiva com Flexbox/Grid", 20),
        ("Estudar JavaScript básico e DOM", 25),
        ("Criar landing page completa", 30)
    ],

    "Desenvolvedor Backend": [
        ("Praticar lógica de programação com Python", 10),
        ("Criar funções, módulos e manipular arquivos", 15),
        ("Criar uma API simples com Flask ou FastAPI", 20),
        ("Aprender SQL e manipular banco de dados", 25),
        ("Criar um sistema completo API + Banco de Dados", 30)
    ],

    "Desenvolvedor Python": [
        ("Instalar Python e configurar ambiente", 10),
        ("Estudar 1h por dia sintaxe básica", 15),
        ("Criar 3 programas simples (calculadora, listas)", 20),
        ("Estudar módulos, funções e arquivos", 25),
        ("Criar um mini-projeto (API, CRUD ou jogo)", 30)
    ],

    "Desenvolvedor Java": [
        ("Revisar lógica e variáveis em Java", 10),
        ("Praticar if/else, loops e arrays", 15),
        ("Fazer exercícios de classes e objetos", 20),
        ("Criar projeto simples (sistema de login)", 25),
        ("Criar CRUD completo em Java", 30)
    ],

    "UX/UI Designer": [
        ("Estudar princípios de design", 10),
        ("Analisar 3 interfaces famosas", 15),
        ("Criar wireframes de um app", 20),
        ("Estudar prototipação no Figma", 25),
        ("Criar design completo de um app/site", 30)
    ],

    "Analista de Dados": [
        ("Estudar fundamentos de dados", 10),
        ("Aprender Excel intermediário", 15),
        ("Estudar SQL básico e fazer 10 consultas", 20),
        ("Aprender Pandas para análise", 25),
        ("Criar dashboard no Power BI ou Tableau", 30)
    ],

    "Cientista de Dados": [
        ("Relembrar Python e bibliotecas base", 10),
        ("Estudar estatística básica", 15),
        ("Aprender Numpy e Pandas", 20),
        ("Criar primeiros modelos com Scikit-Learn", 25),
        ("Criar modelo completo + relatório", 30)
    ],

    "QA / Teste de Software": [
        ("Estudar tipos de testes", 10),
        ("Criar casos de teste simples", 15),
        ("Estudar testes manuais na prática", 20),
        ("Aprender automação com Selenium", 25),
        ("Criar suíte de testes automatizados", 30)
    ],

    "DevOps / Cloud": [
        ("Estudar fundamentos de Cloud", 10),
        ("Aprender Linux básico", 15),
        ("Aprender Docker e criar containers", 20),
        ("Estudar CI/CD e pipelines", 25),
        ("Criar pipeline + deploy automatizado", 30)
    ],

    "Cybersecurity": [
        ("Estudar fundamentos de segurança", 10),
        ("Estudar ataques comuns (SQLi, XSS, CSRF)", 15),
        ("Praticar com Linux + Kali básico", 20),
        ("Aprender pentest em apps web", 25),
        ("Criar relatório completo de vulnerabilidades", 30)
    ],

    "Engenharia de Software": [
        ("Estudar requisitos e boas práticas", 10),
        ("Fazer diagrama simples (UML)", 15),
        ("Estudar arquitetura e padrões de projeto", 20),
        ("Criar módulo pequeno bem estruturado", 25),
        ("Desenvolver mini-sistema completo", 30)
    ]
}

# MENTORES
mentores = [
    {"nome": "Mateus Oliveira", "area": "Desenvolvedor Frontend"},
    {"nome": "Rogerio Nakata", "area": "Desenvolvedor Backend"},
    {"nome": "Renata Campos", "area": "Desenvolvedor Python"},
    {"nome": "Isabela Izumi", "area": "Desenvolvedor Java"},
    {"nome": "Camila Silva", "area": "Analista de Dados"},
    {"nome": "Pedro Costa", "area": "Cybersecurity"},
    {"nome": "Laura Puglli", "area": "Cientista de Dados"},
    {"nome": "Paulo Andrade", "area": "DevOps / Cloud"},
    {"nome": "Marina Rossi", "area": "UX/UI Designer"},
    {"nome": "Jonathan Soares", "area": "QA / Teste de Software"},
    {"nome": "Marcio Lopes", "area": "Engenharia de Software"},
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
        "plano": [],
        "pontos":0,
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

    # SE O USUÁRIO AINDA NÃO TEM PLANO
    if not usuarios[email]['plano']:
        iniciais = random.sample(habilidades, k=min(2, len(habilidades)))

        # Criar tarefas com pontos progressivos
        usuarios[email]['plano'] = []
        for t in iniciais:
            usuarios[email]['plano'].append({
                "tarefa": t,
                "feito": False,
                "pontos": random.choice([10, 20, 30])  # inicial simples
            })

        # Criar também o campo de pontuação total
        usuarios[email]['pontos'] = 0

    plano = usuarios[email]['plano']

    print("\n=== SEU PLANO DE ESTUDOS ===")
    for i, item in enumerate(plano, 1):
        status = "✔️" if item["feito"] else "❌"
        print(f"{i}. {item['tarefa']} [{status}]  (+{item['pontos']} pts)")

    print(f"\nPontos totais: {usuarios[email]['pontos']} pts")

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

    # MARCAR COMO FEITO
    plano[idx]['feito'] = True
    ganho = plano[idx]['pontos']
    usuarios[email]['pontos'] += ganho

    print(f"✔ Tarefa concluída! Você ganhou +{ganho} pontos!")
    print(f"🏆 Pontos totais agora: {usuarios[email]['pontos']} pts")

    # LIBERAR NOVAS TAREFAS
    if all(t['feito'] for t in plano) and len(plano) < len(habilidades):
        restantes = [h for h in habilidades if h not in [p['tarefa'] for p in plano]]
        if restantes:
            nova = random.choice(restantes)

            # Deixa novas tarefas mais difíceis terem mais pontos
            dificuldade = len(plano)  # quanto mais tarefas, mais difícil
            pontos = min(10 + dificuldade * 10, 50)

            plano.append({
                "tarefa": nova,
                "feito": False,
                "pontos": pontos
            })

            print(f"\nNova tarefa liberada: {nova} (+{pontos} pts)")

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

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            usuario_atual = criar_usuario() or usuario_atual

        elif opcao == "2":
            usuario_atual = entrar_usuario() or usuario_atual

        elif opcao == "3":
            if usuario_atual:
                criar_perfil(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opcao == "4":
            if usuario_atual:
                sugerir_carreira(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opcao == "5":
            if usuario_atual:
                gerar_plano(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opcao == "6":
            if usuario_atual:
                ver_progresso(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opcao == "7":
            if usuario_atual:
                conectar_mentor(usuario_atual)
            else:
                print("Faça login primeiro.\n")

        elif opcao == "8":
            cadastrar_mentor()

        elif opcao == "9":
            if usuario_atual:
                print(f"Usuário {usuarios[usuario_atual]['nome']} desconectado.\n")
                usuario_atual = None
            else:
                print("Nenhum usuário está logado.\n")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()
