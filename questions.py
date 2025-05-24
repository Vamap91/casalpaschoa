"""
Sistema de perguntas do jogo 10 Dates: Conexão Profunda
Organizadas por fase e ambiente para máxima personalização
"""

import random

# Estrutura: QUESTIONS[fase][ambiente] = [lista de perguntas]
QUESTIONS = {
    1: {  # Fase 1: Conectar - Perguntas profundas para casais maduros
        "intimidade": [
            {
                "text": "💕 Depois de todos esses anos juntos, qual é a coisa mais nova que você descobriu sobre mim recentemente?",
                "points": 3,
                "action": "Compartilhem essa descoberta beijando suavemente"
            },
            {
                "text": "🌟 Se pudéssemos reviver um momento dos nossos primeiros anos de relacionamento, qual você escolheria?",
                "points": 4,
                "action": "Recriem uma parte desse momento agora"
            },
            {
                "text": "💭 Qual é o medo que você tem sobre nosso futuro juntos que nunca me contou?",
                "points": 4,
                "action": "Segurem as mãos e prometam enfrentar juntos"
            },
            {
                "text": "🔥 Como nossa intimidade mudou ao longo dos anos? O que você mais sente falta?",
                "points": 4,
                "action": "Conversem sobre como podem resgatar isso"
            },
            {
                "text": "💔 Qual foi o momento mais difícil que passamos e como isso nos fortaleceu?",
                "points": 5,
                "action": "Abracem-se e celebrem a superação"
            },
            {
                "text": "🌙 Se tivéssemos que recomeçar nossa vida sexual do zero hoje, como seria?",
                "points": 4,
                "action": "Planejem esse 'recomeço' com carícias"
            },
            {
                "text": "💫 Qual sonho que tínhamos no início ainda não realizamos juntos?",
                "points": 3,
                "action": "Façam um plano real para realizar"
            },
            {
                "text": "🎭 Como você acha que eu mudei desde que nos conhecemos? E você?",
                "points": 3,
                "action": "Elogiem as mudanças positivas um do outro"
            },
            {
                "text": "🔒 Qual segredo sobre nosso relacionamento você guardaria por toda vida?",
                "points": 4,
                "action": "Sussurrem esse segredo no ouvido"
            },
            {
                "text": "💖 Se soubesse que teríamos mais 50 anos juntos, o que você mais gostaria de viver comigo?",
                "points": 4,
                "action": "Façam uma promessa de amor eterno"
            }
        ],
        "publico": [
            {
                "text": "👫 Olhando para outros casais aqui, o que eles têm que nós não temos? E o que nós temos que eles não têm?",
                "points": 3,
                "action": "Elogiem discretamente as qualidades únicas de vocês"
            },
            {
                "text": "💍 Se tivéssemos que renovar nossos votos hoje, o que você prometeria de diferente?",
                "points": 4,
                "action": "Façam essas promessas sussurrando"
            },
            {
                "text": "🔥 Qual é a fantasia sexual que você tem comigo que envolve um lugar público como este?",
                "points": 4,
                "action": "Planejem discretamente como seria"
            },
            {
                "text": "🌹 Se pudéssemos fugir juntos agora para qualquer lugar do mundo, onde iríamos?",
                "points": 2,
                "action": "Planejem essa fuga romântica"
            },
            {
                "text": "💭 Qual é o pensamento mais safado que você já teve sobre mim em um lugar público?",
                "points": 3,
                "action": "Contem sussurrando bem baixinho"
            },
            {
                "text": "👥 Como você acha que as pessoas nos veem como casal? Isso te incomoda?",
                "points": 2,
                "action": "Mostrem amor um pelo outro discretamente"
            },
            {
                "text": "🎭 Que papel nós fazemos na frente dos outros que é diferente de quando estamos sozinhos?",
                "points": 3
            },
            {
                "text": "💖 Se eu flertasse com você agora como se não nos conhecêssemos, como você reagiria?",
                "points": 3,
                "action": "Flirtem como se fosse a primeira vez"
            },
            {
                "text": "🌶️ Qual é a coisa mais ousada que já fizemos em público que ninguém sabe?",
                "points": 4,
                "action": "Relembrem com sorrisos cúmplices"
            },
            {
                "text": "💑 Se pudéssemos dar um conselho para casais mais jovens, qual seria?",
                "points": 3,
                "action": "Apliquem esse conselho em vocês mesmos agora"
            }
        ],
        "casa": [
            {
                "text": "🏠 Depois de tantos anos morando juntos, qual cantinho da casa ainda guarda memórias especiais nossas?",
                "points": 3,
                "action": "Vão até lá e criem uma nova memória"
            },
            {
                "text": "💑 Se pudéssemos redesenhar nossa rotina de casa para ter mais momentos íntimos, como seria?",
                "points": 4,
                "action": "Implementem uma mudança pequena agora"
            },
            {
                "text": "🔥 Qual foi a transa mais inesquecível que tivemos em casa e o que a tornou especial?",
                "points": 4,
                "action": "Vão ao local e relembrem com carinho"
            },
            {
                "text": "🌙 Como nossa vida íntima em casa mudou ao longo dos anos?",
                "points": 3,
                "action": "Conversem sobre como reacender a paixão"
            },
            {
                "text": "💖 Qual tradição nossa em casa você mais ama e nunca quer perder?",
                "points": 3,
                "action": "Pratiquem essa tradição agora"
            },
            {
                "text": "🛏️ Se pudéssemos transformar nosso quarto no paraíso romântico, o que mudaria?",
                "points": 3,
                "action": "Façam uma pequena mudança romântica agora"
            },
            {
                "text": "👫 Como equilibramos vida doméstica e romance depois de tanto tempo juntos?",
                "points": 2,
                "action": "Planejem mais momentos românticos em casa"
            },
            {
                "text": "🌹 Qual surpresa romântica em casa você gostaria de me fazer mas nunca fez?",
                "points": 4,
                "action": "Deem uma amostra dessa surpresa"
            },
            {
                "text": "💑 Se um casal jovem visitasse nossa casa, que conselho sobre amor duradouro daríamos?",
                "points": 3,
                "action": "Apliquem esse conselho fazendo algo romântico"
            },
            {
                "text": "🔮 Como você imagina que seremos daqui a 20 anos, ainda nesta casa?",
                "points": 3,
                "action": "Façam planos românticos para o futuro"
            }
        ],
        "distancia": [
            {
                "text": "💻 Qual é a coisa mais suja que você já pensou em fazer comigo através da tela?",
                "points": 4,
                "action": "Descrevam em detalhes sussurrando para a câmera"
            },
            {
                "text": "😈 Se eu aparecesse na sua porta agora, qual seria a primeira coisa que você faria comigo?",
                "points": 4,
                "action": "Mostrem através de gestos sensuais"
            },
            {
                "text": "🔥 Qual é a parte do meu corpo que você mais sente falta de tocar agora?",
                "points": 3,
                "action": "Toquem essa parte em vocês mesmos imaginando que é o outro"
            },
            {
                "text": "💀 Qual é o seu maior medo sobre nosso relacionamento à distância?",
                "points": 4
            },
            {
                "text": "📱 Qual foi a mensagem mais excitante que você já me mandou e se arrependeu depois?",
                "points": 3,
                "action": "Mandem algo ainda mais ousado agora"
            },
            {
                "text": "🌙 Em que você pensa quando se masturba pensando em mim?",
                "points": 4,
                "action": "Contem a fantasia em detalhes sensuais"
            },
            {
                "text": "💔 Você já se sentiu tentado(a) por outra pessoa durante nossa separação?",
                "points": 4,
                "action": "Sejam honestos e conversem sobre isso"
            },
            {
                "text": "🔮 Se pudesse me controlar à distância por 10 minutos, o que me faria fazer?",
                "points": 3,
                "action": "Façam esse comando agora pela tela"
            },
            {
                "text": "💣 Qual é a verdade mais pesada sobre nossa relação à distância que você nunca disse?",
                "points": 4
            },
            {
                "text": "🌡️ Descreva o reencontro sexual mais intenso que você imagina termos?",
                "points": 4,
                "action": "Planejem esse reencontro em detalhes"
            }
        ]
    },
    2: {  # Fase 2: Desejar - Romance maduro com sensualidade
        "intimidade": [
            {
                "text": "💕 Como nosso desejo um pelo outro evoluiu ao longo dos anos? O que mudou?",
                "points": 4,
                "action": "Mostrem como ainda se desejam com carícias"
            },
            {
                "text": "🔥 Qual foi a época da nossa vida em que mais fizemos amor? Sente falta?",
                "points": 4,
                "action": "Planejem como resgatar essa intensidade"
            },
            {
                "text": "💋 Se pudéssemos voltar à nossa lua de mel, o que faria diferente na cama?",
                "points": 3,
                "action": "Demonstrem com beijos apaixonados"
            },
            {
                "text": "🌹 Qual parte do meu corpo você ainda adora tocar como no primeiro dia?",
                "points": 3,
                "action": "Toquem essa parte com o mesmo desejo de antes"
            },
            {
                "text": "💫 Como posso seduzir você hoje do jeito que mais gosta depois de tanto tempo?",
                "points": 4,
                "action": "Ensinem um ao outro e pratiquem"
            },
            {
                "text": "🔮 Qual fantasia sexual nossa que ainda não realizamos você mais quer tornar real?",
                "points": 5,
                "action": "Planejem quando e como realizar"
            },
            {
                "text": "🌙 Em que momento do dia você mais sente vontade de fazer amor comigo?",
                "points": 3,
                "action": "Criem esse momento agora"
            },
            {
                "text": "💖 O que mais te excita em mim hoje que não existia quando éramos jovens?",
                "points": 4,
                "action": "Mostrem essa maturidade sendo sensuais"
            },
            {
                "text": "🔥 Como nossa intimidade sexual pode ficar ainda melhor nos próximos anos?",
                "points": 4,
                "action": "Façam uma promessa de paixão renovada"
            },
            {
                "text": "💕 Se tivéssemos que ensinar sobre amor maduro para um casal jovem, qual seria nosso segredo?",
                "points": 3,
                "action": "Pratiquem esse segredo agora mesmo"
            }
        ],
        "publico": [
            {
                "text": "😏 Se pudéssemos sair daqui agora, qual seria nosso destino romântico?",
                "points": 3,
                "action": "Planejem essa escapada romântica"
            },
            {
                "text": "💭 Qual é o pensamento mais romântico que você está tendo sobre mim agora?",
                "points": 3,
                "action": "Sussurrem discretamente no ouvido"
            },
            {
                "text": "🌹 Como você gostaria de me conquistar se nos conhecêssemos hoje?",
                "points": 3,
                "action": "Reconquistem um ao outro agora"
            },
            {
                "text": "🔥 Qual gesto meu te deixa mais apaixonado(a)?",
                "points": 2,
                "action": "Façam esse gesto agora"
            },
            {
                "text": "💋 Se eu te beijasse apaixonadamente agora, como você reagiria?",
                "points": 3,
                "action": "Testem com um beijo discreto mas intenso"
            },
            {
                "text": "😈 Qual é o seu plano de sedução para quando chegarmos em casa?",
                "points": 4
            },
            {
                "text": "🌶️ O que você mais quer me sussurrar no ouvido quando estivermos sozinhos?",
                "points": 3,
                "action": "Deem uma prévia bem baixinho"
            },
            {
                "text": "🔮 Como você está se sentindo pensando em nossa intimidade?",
                "points": 3,
                "action": "Expressem através de carícias discretas"
            },
            {
                "text": "💦 Qual é a coisa mais romântica que você quer fazer comigo hoje?",
                "points": 4
            },
            {
                "text": "🌡️ De 1 a 10, quanto você me deseja neste momento?",
                "points": 3,
                "action": "Mostrem a intensidade através do olhar"
            }
        ],
        "casa": [
            {
                "text": "🛏️ Nosso quarto ainda é um santuário de amor ou virou apenas lugar de dormir?",
                "points": 4,
                "action": "Transformem o quarto num ambiente romântico agora"
            },
            {
                "text": "🌙 Qual é o horário do dia que vocês mais faziam amor antes e por que parou?",
                "points": 4,
                "action": "Resgatem esse horário especial"
            },
            {
                "text": "💋 Se pudéssemos criar um ritual semanal de sedução em casa, como seria?",
                "points": 4,
                "action": "Iniciem esse ritual agora"
            },
            {
                "text": "🔥 Qual cômodo da casa tem o maior potencial romântico inexplorado?",
                "points": 3,
                "action": "Vão lá e explorem esse potencial"
            },
            {
                "text": "🛁 Como seria nosso banho romântico perfeito depois de tantos anos?",
                "points": 3,
                "action": "Planejem e preparem esse momento"
            },
            {
                "text": "🍷 Se criássemos uma noite temática romântica em casa, qual seria o tema?",
                "points": 3,
                "action": "Comecem a criar essa atmosfera"
            },
            {
                "text": "💕 Como podemos trazer mais espontaneidade para nossa vida íntima em casa?",
                "points": 4,
                "action": "Sejam espontâneos agora mesmo"
            },
            {
                "text": "🌹 Qual surpresa romântica caseira você gostaria de me fazer mas nunca fez?",
                "points": 4,
                "action": "Deem uma amostra dessa surpresa"
            },
            {
                "text": "🔮 Como você imagina nossa intimidade doméstica daqui a 10 anos?",
                "points": 3,
                "action": "Façam planos para manter a paixão acesa"
            },
            {
                "text": "💖 Qual é o maior mito sobre casais de longa data que nós quebramos?",
                "points": 3,
                "action": "Provem quebrando esse mito agora"
            }
        ],
        "distancia": [
            {
                "text": "💻 Como você gostaria de me seduzir através da tela?",
                "points": 4,
                "action": "Demonstrem agora de forma sensual"
            },
            {
                "text": "😈 Qual é a coisa mais romântica que você quer me dizer agora?",
                "points": 3,
                "action": "Digam olhando diretamente na câmera"
            },
            {
                "text": "🔥 Qual parte da nossa intimidade virtual você mais aprecia?",
                "points": 3
            },
            {
                "text": "💋 Como você imagina nosso próximo beijo quando nos encontrarmos?",
                "points": 4,
                "action": "Mandem um beijo intenso pela tela"
            },
            {
                "text": "🌙 Qual é a sua fantasia mais romântica sobre nosso reencontro?",
                "points": 4
            },
            {
                "text": "💫 O que mais te faz desejar minha presença física?",
                "points": 4
            },
            {
                "text": "🔮 Como você se sente quando me vê através da tela?",
                "points": 3,
                "action": "Expressem esse sentimento com gestos"
            },
            {
                "text": "🌹 Qual é a mensagem mais apaixonada que você quer me enviar?",
                "points": 3,
                "action": "Escrevam e mostrem na tela"
            },
            {
                "text": "💭 Em que você mais pensa quando sente saudade de mim?",
                "points": 4
            },
            {
                "text": "🔥 Como será nosso momento de reconexão física mais intenso?",
                "points": 5,
                "action": "Planejem esse momento em detalhes românticos"
            }
        ]
    },
    3: {  # Fase 3: Agir - Ações físicas e interações práticas
        "intimidade": [
            {
                "text": "💋 Beijem-se apaixonadamente por 1 minuto completo sem parar",
                "points": 4,
                "action": "Cronometrem e intensifiquem a cada segundo"
            },
            {
                "text": "🤗 Abracem-se pele com pele por 3 minutos em completo silêncio",
                "points": 4,
                "action": "Sintam o coração um do outro batendo"
            },
            {
                "text": "👁️ Olhem nos olhos um do outro por 5 minutos sem falar nem rir",
                "points": 5,
                "action": "Deixem as almas se conectarem através do olhar"
            },
            {
                "text": "💆 Façam massagem sensual um no outro por 10 minutos",
                "points": 4,
                "action": "Explorem cada parte do corpo com carinho"
            },
            {
                "text": "🌹 Sussurrem suas maiores verdades íntimas no ouvido",
                "points": 5,
                "action": "Compartilhem segredos que nunca contaram"
            },
            {
                "text": "💫 Dancem juntos uma música lenta completamente colados",
                "points": 3,
                "action": "Movam-se como se fossem um só corpo"
            },
            {
                "text": "🔥 Explorem-se através de carícias por 5 minutos",
                "points": 5,
                "action": "Descubram novas zonas erógenas um do outro"
            },
            {
                "text": "💋 Beijem 7 partes diferentes do corpo um do outro",
                "points": 4,
                "action": "Comecem suave e aumentem a intensidade"
            },
            {
                "text": "🌙 Respirem sincronizados por 5 minutos",
                "points": 3,
                "action": "Encostem as testas e encontrem o mesmo ritmo"
            },
            {
                "text": "💓 Coloquem as mãos no coração um do outro simultaneamente",
                "points": 4,
                "action": "Façam uma promessa de amor eterno"
            }
        ],
        "publico": [
            {
                "text": "🤝 Entrelacem os dedos e não se soltem por 10 minutos",
                "points": 3,
                "action": "Façam carícias discretas com os polegares"
            },
            {
                "text": "👂 Sussurrem suas maiores fantasias românticas no ouvido",
                "points": 4,
                "action": "Falem tão baixo que só vocês dois ouçam"
            },
            {
                "text": "😘 Troquem 15 beijos diferentes (testa, bochechas, lábios, mãos)",
                "points": 3,
                "action": "Sejam criativos mas discretos"
            },
            {
                "text": "📱 Tirem 10 selfies românticas em poses diferentes",
                "points": 2,
                "action": "Capturem a paixão de vocês"
            },
            {
                "text": "🎵 Cantem baixinho uma música especial só para vocês",
                "points": 2,
                "action": "Criem uma bolha romântica ao redor de vocês"
            },
            {
                "text": "👁️ Façam uma batalha de sedução apenas com o olhar",
                "points": 3,
                "action": "Quem desviar primeiro deve sussurrar 'eu te amo'"
            },
            {
                "text": "💌 Escrevam 'EU TE DESEJO' na palma da mão um do outro",
                "points": 3,
                "action": "Usem apenas o dedo indicador sensualmente"
            },
            {
                "text": "🌹 Alimentem um ao outro de forma sensual",
                "points": 3,
                "action": "Olhem nos olhos enquanto fazem isso"
            },
            {
                "text": "🤗 Abracem-se por baixo da mesa discretamente",
                "points": 2,
                "action": "Sintam o calor um do outro"
            },
            {
                "text": "💫 Façam promessas românticas sussurrando",
                "points": 4,
                "action": "Prometam coisas especiais para mais tarde"
            }
        ],
        "casa": [
            {
                "text": "🛋️ Assistam ao pôr do sol abraçados em silêncio completo",
                "points": 3,
                "action": "Apenas sintam a presença um do outro"
            },
            {
                "text": "🍳 Cozinhem algo juntos se alimentando mutuamente",
                "points": 2,
                "action": "Provem na boca um do outro carinhosamente"
            },
            {
                "text": "🛁 Preparem um banho romântico com velas",
                "points": 4,
                "action": "Relaxem juntos na água morna"
            },
            {
                "text": "💃 Dancem pela casa sem música, só no ritmo do coração",
                "points": 3,
                "action": "Deixem os corpos se guiarem"
            },
            {
                "text": "🕯️ Acendam velas e façam massagem com óleo",
                "points": 5,
                "action": "Revezem e explorem cada centímetro"
            },
            {
                "text": "🛏️ Deitem abraçados e compartilhem seus sonhos mais profundos",
                "points": 3,
                "action": "Falem olhando para o teto, bem juntinhos"
            },
            {
                "text": "📚 Leiam poesia romântica um para o outro na cama",
                "points": 2,
                "action": "Escolham versos que descrevam seu amor"
            },
            {
                "text": "🎨 'Desenhem' um no corpo do outro usando apenas as mãos",
                "points": 4,
                "action": "Criem arte com carícias suaves"
            },
            {
                "text": "☕ Preparem uma bebida quente e compartilhem a mesma xícara",
                "points": 2,
                "action": "Sintam o gosto nos lábios um do outro"
            },
            {
                "text": "🌙 Contem estrelas pela janela fazendo pedidos juntos",
                "points": 2,
                "action": "Cada estrela um desejo para vocês dois"
            }
        ],
        "distancia": [
            {
                "text": "👋 Mandem beijos e acenem por 2 minutos sem parar",
                "points": 2,
                "action": "Sejam criativos com poses e expressões"
            },
            {
                "text": "🎵 Cantem uma música especial juntos em sincronia perfeita",
                "points": 3,
                "action": "Escolham uma que represente vocês"
            },
            {
                "text": "💋 Criem 20 tipos diferentes de beijos pela tela",
                "points": 3,
                "action": "Sejam apaixonados e criativos"
            },
            {
                "text": "📱 Escrevam 'EU TE AMO' em idiomas diferentes simultaneamente",
                "points": 2,
                "action": "Mostrem na tela ao mesmo tempo"
            },
            {
                "text": "👁️ Façam uma sessão de 5 minutos apenas se olhando",
                "points": 4,
                "action": "Conectem-se através da tela em silêncio"
            },
            {
                "text": "🌙 Olhem para a lua/sol ao mesmo tempo por 3 minutos",
                "points": 3,
                "action": "Cada um na sua janela, conectados pelo céu"
            },
            {
                "text": "💌 Escrevam uma carta de amor de 5 linhas em tempo real",
                "points": 4,
                "action": "Cada um escreve e depois leem juntos"
            },
            {
                "text": "🕯️ Acendam uma vela cada um e façam um ritual",
                "points": 3,
                "action": "Criem um momento sagrado à distância"
            },
            {
                "text": "🤗 Abracem uma almofada por 3 minutos imaginando que é o outro",
                "points": 4,
                "action": "Fechem os olhos e sintam a presença"
            },
            {
                "text": "💭 Meditem juntos por 5 minutos respirando no mesmo ritmo",
                "points": 3,
                "action": "Sincronizem através da tela e se conectem espiritualmente"
            }
        ]
    }
}

def get_questions_by_phase_and_environment(phase, environment):
    """
    Retorna as perguntas para uma fase e ambiente específicos
    
    Args:
        phase (int): Fase do jogo (1, 2 ou 3)
        environment (str): Ambiente escolhido ('intimidade', 'publico', 'casa', 'distancia')
    
    Returns:
        list: Lista de perguntas embaralhadas para a fase e ambiente
    """
    if phase not in QUESTIONS:
        return []
    
    if environment not in QUESTIONS[phase]:
        return []
    
    questions = QUESTIONS[phase][environment].copy()
    random.shuffle(questions)  # Embaralha as perguntas para variedade
    
    return questions

def get_random_question(phase, environment):
    """
    Retorna uma pergunta aleatória para uma fase e ambiente específicos
    
    Args:
        phase (int): Fase do jogo (1, 2 ou 3)
        environment (str): Ambiente escolhido
    
    Returns:
        dict: Pergunta aleatória ou None se não encontrada
    """
    questions = get_questions_by_phase_and_environment(phase, environment)
    
    if questions:
        return random.choice(questions)
    
    return None

def get_total_questions_count(phase=None, environment=None):
    """
    Retorna o número total de perguntas disponíveis
    
    Args:
        phase (int, optional): Fase específica
        environment (str, optional): Ambiente específico
    
    Returns:
        int: Número total de perguntas
    """
    if phase and environment:
        return len(QUESTIONS.get(phase, {}).get(environment, []))
    elif phase:
        return sum(len(questions) for questions in QUESTIONS.get(phase, {}).values())
    else:
        total = 0
        for phase_questions in QUESTIONS.values():
            for env_questions in phase_questions.values():
                total += len(env_questions)
        return total

# Função para debug - lista todas as perguntas
def list_all_questions():
    """Lista todas as perguntas organizadas por fase e ambiente"""
    for phase, phase_data in QUESTIONS.items():
        phase_names = {1: "Conectar", 2: "Desejar", 3: "Agir"}
        print(f"\n=== FASE {phase}: {phase_names[phase]} ===")
        
        for env, questions in phase_data.items():
            env_names = {
                "intimidade": "Intimidade Total",
                "publico": "Espaço Público", 
                "casa": "Em Casa",
                "distancia": "À Distância"
            }
            print(f"\n--- {env_names.get(env, env)} ---")
            
            for i, question in enumerate(questions, 1):
                print(f"{i}. {question['text']} (Pontos: {question['points']})")
                if question.get('action'):
                    print(f"   Ação: {question['action']}")

if __name__ == "__main__":
    # Teste das funções
    print("=== TESTE DO SISTEMA DE PERGUNTAS ===")
    print(f"Total de perguntas: {get_total_questions_count()}")
    print(f"Perguntas Fase 1: {get_total_questions_count(1)}")
    print(f"Perguntas Fase 1 - Intimidade: {get_total_questions_count(1, 'intimidade')}")
    
    # Exemplo de pergunta aleatória
    print("\n=== PERGUNTA ALEATÓRIA ===")
    random_q = get_random_question(1, "intimidade")
    if random_q:
        print(f"Pergunta: {random_q['text']}")
        print(f"Pontos: {random_q['points']}")
        if random_q.get('action'):
            print(f"Ação: {random_q['action']}")
    
    # Descomentar para ver todas as perguntas  
    # list_all_questions()
