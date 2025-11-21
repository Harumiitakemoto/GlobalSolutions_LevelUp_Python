import random

#DADOS USUÁRIO
usuarios = {}
usuario_atual = None

carreiras_escolhidas = {}
planos_estudo = {}

# CARREIRAS
carreiras = {
    "Desenvolvedor Backend": [
        "Estudar 1h por dia os fundamentos de Python",
        "Criar um pequeno projeto CRUD usando Python",
        "Assistir uma videoaula sobre APIs REST",
        "Ler um artigo sobre boas práticas de Git",
        "Criar um banco de dados simples e conectar ao Python",
        "Fazer um projeto de API usando Flask ou FastAPI",
    ],

    "Desenvolvedor Frontend": [
        "Praticar 1h de HTML por dia criando pequenas páginas",
        "Assistir uma videoaula sobre CSS Flexbox e Grid",
        "Criar um site simples responsivo",
        "Ler um artigo sobre boas práticas de design responsivo",
        "Criar um mini projeto usando JavaScript puro",
        "Reproduzir o layout de um site famoso no Figma",
    ],

    "Desenvolvedor Fullstack": [
        "Estudar fundamentos de HTML, CSS e JS por 1h/dia",
        "Criar um projeto simples Fullstack (frontend + API)",
        "Ler um artigo sobre autenticação JWT",
        "Criar backend em Python com Flask/FastAPI",
        "Criar frontend com HTML/CSS/JS consumindo a API",
        "Subir o projeto no GitHub",
    ],

    "Cientista de Dados": [
        "Estudar 1h por dia de Python focado em análise",
        "Assistir uma aula introdutória de Machine Learning",
        "Criar um notebook analisando um dataset do Kaggle",
        "Ler um artigo sobre estatística descritiva",
        "Criar gráficos usando Pandas e Matplotlib",
        "Fazer um mini projeto de previsão (regressão simples)",
    ],

    "Analista de Dados": [
        "Estudar SQL por 1h por dia",
        "Criar dashboards simples no Power BI ou Looker",
        "Assistir uma videoaula sobre ETL",
        "Ler um artigo sobre KPIs",
        "Criar consultas SQL resolvendo problemas reais",
        "Analisar um dataset público e gerar insights",
    ],

    "Engenheiro de Dados": [
        "Estudar fundamentos de Python e SQL diariamente",
        "Assistir uma aula sobre arquitetura de pipelines",
        "Criar um pipeline simples com arquivos CSV",
        "Ler um artigo sobre Data Lakes e Data Warehouses",
        "Criar um script de ETL automatizado",
        "Estudar conceitos básicos de Cloud (AWS ou GCP)",
    ],

    "UX/UI Designer": [
        "Estudar fundamentos de design no Figma por 1h/dia",
        "Criar um wireframe de um app simples",
        "Assistir videoaula de prototipação",
        "Ler artigo sobre heurísticas de Nielsen",
        "Criar uma landing page no Figma",
        "Refazer o design de um app famoso com melhorias",
    ],

    "QA / Tester": [
        "Estudar lógica de testes por 1h/dia",
        "Assistir uma videoaula de testes automatizados",
        "Criar casos de teste para um site real",
        "Ler artigo sobre testes funcionais vs unitários",
        "Instalar o Selenium e testar um site simples",
        "Criar relatório de bugs fictícios",
    ],

    "Cybersegurança": [
        "Estudar fundamentos de redes por 1h/dia",
        "Assistir videoaula sobre pentest",
        "Ler um artigo sobre OWASP Top 10",
        "Testar segurança de uma aplicação simples (simulação)",
        "Aprender a usar ferramentas como Nmap",
        "Criar relatório de vulnerabilidades básicas",
    ],

    "DevOps": [
        "Estudar fundamentos de Cloud por 1h/dia",
        "Assistir videoaula de CI/CD",
        "Criar um pipeline simples no GitHub Actions",
        "Ler artigo sobre containers com Docker",
        "Containerizar um pequeno projeto",
        "Criar deploy básico em cloud free-tier",
    ],

    "Técnico de Informática": [
        "Estudar hardware por 1h/dia",
        "Assistir videoaula de manutenção preventiva",
        "Abrir um computador e identificar peças (simulado)",
        "Ler artigo sobre redes básicas",
        "Resolver problemas simulados de atendimento",
        "Criar checklist de manutenção",
    ],

    "Suporte Técnico": [
        "Estudar atendimento ao cliente 1h/dia",
        "Assistir videoaula de troubleshooting",
        "Ler artigo sobre documentação de problemas",
        "Resolver simulações de problemas comuns",
        "Estudar sistemas operacionais (Win/Linux)",
        "Criar um guia de soluções frequentes",
    ],
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
