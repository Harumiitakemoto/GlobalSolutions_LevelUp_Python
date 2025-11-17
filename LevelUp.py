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
    "Tecnologia": {
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
    },

    "Marketing e Comunicação": {
        "Analista de Marketing": ["SEO", "Copywriting", "Social Media", "Analytics"],
        "Produtor de Conteúdo": ["Roteiro", "Edição de Vídeo", "Storytelling"],
        "Designer Gráfico": ["Photoshop", "Illustrator", "Composição"],
        "Fotógrafo": ["Iluminação", "Edição", "Composição"],
        "Jornalista": ["Redação", "Entrevista", "Investigação"],
        "Publicitário": ["Criação", "Campanhas", "Branding"],
    },

    "Gestão e Negócios": {
        "Administrador": ["Gestão", "Finanças", "Estratégia"],
        "Gerente de Projetos": ["Scrum", "Kanban", "Liderança"],
        "Product Manager": ["Pesquisa", "Roadmap", "Visão de Produto"],
        "Marketing": ["Branding", "SEO", "Redes Sociais"],
        "Vendas / SDR": ["CRM", "Prospecção", "Negociação"],
        "Analista de RH": ["Recrutamento", "Entrevistas", "Treinamento"],
        "Assistente Administrativo": ["Excel", "Organização", "Comunicação"],
        "Auxiliar de Escritório": ["Rotinas Administrativas", "Digitação"],
        "Logística": ["Armazenamento", "Transportes", "Processos"],
        "Administração Pública": ["Políticas Públicas", "Documentação", "Gestão Pública"],
    },

    "Saúde": {
        "Médico": ["Clínica Geral", "Anatomia", "Diagnósticos"],
        "Enfermeiro": ["Cuidados", "Procedimentos", "Medicações"],
        "Técnico de Enfermagem": ["Atendimento", "Procedimentos", "Biossegurança"],
        "Psicólogo": ["Psicologia Clínica", "Atendimento", "Psiquiatria Básica"],
        "Nutricionista": ["Dietas", "Análise Nutricional", "Atendimento"],
        "Farmacêutico": ["Fármacos", "Manipulação", "Regulamentação"],
        "Fisioterapeuta": ["Reabilitação", "Avaliação Física", "Terapias"],
        "Esteticista": ["Limpeza de Pele", "Aparelhos", "Tratamentos", "Cuidados com a Pele"],
    },

    "Engenharias e Exatas": {
        "Engenheiro Civil": ["AutoCAD", "Cálculo", "Estruturas"],
        "Engenheiro Mecânico": ["Termodinâmica", "Materiais", "Projetos 3D"],
        "Engenheiro Elétrico": ["Circuitos", "Potência", "Eletrônica"],
        "Engenheiro de Produção": ["Lean", "Processos", "Gestão"],
        "Engenheiro Químico": ["Processos Industriais", "Termodinâmica"],
        "Analista de Qualidade": ["ISO", "Documentação", "Processos"],
        "Analista de Produção": ["Excel", "Lean", "Otimização"],
        "Engenheiro de Software": ["Cloud", "Arquitetura", "DevOps"],
    },

    "Humanas e Educação": {
        "Advogado": ["Direito Civil", "Penal", "Processos"],
        "Professor": ["Didática", "Planejamento", "Avaliação"],
        "Pedagogo": ["Educação Infantil", "Planejamento", "Psicopedagogia"],
        "Assistente Social": ["Atendimento", "Políticas Públicas", "Relatórios"],
        "Coach de Carreira": ["Escuta Ativa", "Planejamento", "Comunicação"],
        "Mentor Educacional": ["Orientação", "Didática", "Acompanhamento"],
    }
}

# MENTORES

mentores = [
    {"nome": "Mateus Oliveira", "area": "Desenvolvedor ", "categoria": "Tecnologia"},
    {"nome": "Camila Silva", "area": "Analista de Dados", "categoria": "Tecnologia"},
    {"nome": "Pedro Costa", "area": "Cybersegurança", "categoria": "Tecnologia",},

    {"nome": "Mariana Akemi", "area": "Analista de Marketing", "categoria": "Marketing e Comunicação",},
    {"nome": "Sophia Ramos", "area": "Designer Gráfico", "categoria": "Marketing e Comunicação",},

    {"nome": "Carlos Almeida", "area": "Administrador", "categoria": "Gestão e Negócios",},
    {"nome": "Vanessa Bianco", "area": "Gerente de Projetos", "categoria": "Gestão e Negócios",},

    {"nome": "Dra. Alice Mendes", "area": "Médico", "categoria": "Saúde",},
    {"nome": "Dr. Mario Antunes", "area": "Psicólogo", "categoria": "Saúde",},

    {"nome": "Bruno Ferreira", "area": "Engenheiro Civil", "categoria": "Engenharias e Exatas",},
    {"nome": "Eduardo Toshio", "area": "Engenheiro Mecânico", "categoria": "Engenharias e Exatas",},
    {"nome": "Jefferson Moreira", "area": "Engenheiro de Produção", "categoria": "Engenharias e Exatas"},

    {"nome": "Dra. Patrícia Kobayashi", "area": "Advogado", "categoria": "Humanas e Educação",},
    {"nome": "Gisele Alves", "area": "Professor", "categoria": "Humanas e Educação",},
    {"nome": "Renata Pereira", "area": "Assistente Social", "categoria": "Humanas e Educação",}
]

# FUNÇÕES


def criar_perfil():
    usuario["nome"] = input("\nDigite seu nome: ")
    usuario["habilidades"] = [h.strip().title() for h in input("Habilidades (separadas por vírgula): ").split(",")]
    usuario["interesses"] = [i.strip().title() for i in input("Interesses: ").split(",")]
    usuario["estilo"] = input("Como você se define? (analítico, criativo, comunicador): ")

    print("\nPerfil criado com sucesso!\n")


def sugerir_carreira():
    global carreira_escolhida

    habilidades = usuario["habilidades"]
    opcoes = []

    # varre categorias
    for categoria, areas in carreiras.items():
        for carreira, skills in areas.items():
            for h in habilidades:
                if h in skills:
                    opcoes.append(carreira)
                    break

    if not opcoes:
        print("\nNenhuma carreira compatível encontrada.\n")
        return None

    print("\nCarreiras compatíveis com você:\n")
    for i, c in enumerate(opcoes, 1):
        print(f"{i}. {c}")

    escolha = int(input("\nEscolha sua carreira pelo número: ")) - 1

    if escolha < 0 or escolha >= len(opcoes):
        print("Opção inválida!\n")
        return None

    carreira_escolhida = opcoes[escolha]
    print(f"\n✔ Carreira escolhida: {carreira_escolhida}\n")

    return carreira_escolhida


def gerar_plano():
    global plano

    if not carreira_escolhida:
        print("\n⚠ Sugira e escolha uma carreira primeiro.\n")
        return

    # recuperar habilidades específicas dessa carreira
    habilidades = None
    for categoria, areas in carreiras.items():
        if carreira_escolhida in areas:
            habilidades = areas[carreira_escolhida]

    if habilidades is None:
        print("Erro ao encontrar habilidades da carreira.\n")
        return

    if not plano:
        tarefas_iniciais = random.sample(habilidades, k=min(2, len(habilidades)))
        plano = [{"tarefa": t, "feito": False} for t in tarefas_iniciais]

    print("\nSeu plano de ação:")
    for i, item in enumerate(plano, 1):
        status = "✔️" if item["feito"] else "❌"
        print(f"{i}. {item['tarefa']} [{status}]")

    if input("\nDeseja marcar tarefa como concluída? (s/n): ").lower() == "s":
        indice = int(input("Digite o número: ")) - 1
        if 0 <= indice < len(plano):
            plano[indice]["feito"] = True
            print("Tarefa concluída!")

            concluidas = all(t["feito"] for t in plano)
            ainda_faltam = len(plano) < len(habilidades)

            if concluidas and ainda_faltam:
                restantes = [h for h in habilidades if h not in [t["tarefa"] for t in plano]]
                nova = random.choice(restantes)
                plano.append({"tarefa": nova, "feito": False})
                print(f"\n🎉 Nova tarefa desbloqueada: {nova}")
        else:
            print("Número inválido!")


def ver_progresso():
    if not plano:
        print("\n⚠ Gere um plano primeiro.\n")
        return

    total = len(plano)
    feitos = sum(1 for t in plano if t["feito"])

    barra = "#" * feitos + "-" * (total - feitos)
    print(f"\nProgresso: [{barra}] {feitos}/{total} tarefas concluídas.\n")


def conectar_mentor():
    if not carreira_escolhida:
        print("\n⚠ Escolha uma carreira primeiro.\n")
        return

    print(f"\nMentores disponíveis para {carreira_escolhida}:\n")

    if carreira_escolhida in mentores:
        for m in mentores[carreira_escolhida]:
            print(f"- {m}")
    else:
        print("Nenhum mentor disponível para esta carreira.")

    print()



# MENU


while True:
    print("=== LEVEL UP – ASSISTENTE DE CARREIRA ===")
    print("1. Criar Perfil")
    print("2. Sugestão de Carreira")
    print("3. Gerar Plano de Ação")
    print("4. Ver Progresso")
    print("5. Conectar com Mentor")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_perfil()
    elif opcao == "2":
        sugerir_carreira()
    elif opcao == "3":
        gerar_plano()

    elif opc == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")
