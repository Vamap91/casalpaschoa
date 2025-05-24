import streamlit as st
import random
from questions import get_questions_by_phase_and_environment
from game_logic import GameLogic

# Configuração da página
st.set_page_config(
    page_title="10 Dates: Conexão Profunda 💕",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado para design UX perfeito
st.markdown("""
<style>
    /* Importar fontes modernas */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Reset e base */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Container principal */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 24px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Títulos */
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #6c757d;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Cards de ambiente */
    .environment-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        border: 2px solid transparent;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .environment-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.15);
        border-color: #ff6b6b;
    }
    
    .environment-card.selected {
        border-color: #ff6b6b;
        background: linear-gradient(135deg, #fff5f5, #ffffff);
    }
    
    /* Ícones de ambiente */
    .env-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
    }
    
    .env-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .env-description {
        color: #6c757d;
        text-align: center;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    
    /* Cards de pergunta */
    .question-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
        text-align: center;
    }
    
    .question-text {
        font-size: 1.4rem;
        font-weight: 500;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    /* Fase atual */
    .phase-indicator {
        background: linear-gradient(90deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
        font-size: 0.9rem;
    }
    
    /* Nível de conexão */
    .connection-level {
        background: rgba(255, 107, 107, 0.1);
        border: 2px solid #ff6b6b;
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    .connection-hearts {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .connection-text {
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.1rem;
    }
    
    /* Vibrator mode card */
    .vibrator-card {
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    /* Botões */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4);
    }
    
    /* Toggle switch para vibrador */
    .toggle-switch {
        position: relative;
        display: inline-block;
        width: 60px;
        height: 34px;
        margin: 1rem;
    }
    
    /* Progresso do jogo */
    .game-progress {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    .progress-bar {
        background: #e9ecef;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #ff6b6b, #ee5a52);
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
    
    /* Cards de resultado final */
    .final-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
    }
    
    .score-display {
        font-size: 3rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .main-container {
            margin: 0.5rem;
            padding: 1.5rem;
        }
        
        .main-title {
            font-size: 2rem;
        }
        
        .question-text {
            font-size: 1.2rem;
        }
        
        .env-icon {
            font-size: 2.5rem;
        }
    }
    
    /* Esconder elementos do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def initialize_game_state():
    """Inicializa o estado do jogo"""
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'environment' not in st.session_state:
        st.session_state.environment = None
    if 'use_vibrator' not in st.session_state:
        st.session_state.use_vibrator = False
    if 'current_phase' not in st.session_state:
        st.session_state.current_phase = 1
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
    if 'game_logic' not in st.session_state:
        st.session_state.game_logic = GameLogic()
    if 'current_questions' not in st.session_state:
        st.session_state.current_questions = []

def show_welcome_screen():
    """Tela de boas-vindas"""
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="main-title">10 Dates: Conexão Profunda</div>
        <div class="subtitle">Um jogo interativo para fortalecer a conexão emocional e física entre vocês 💕</div>
    """, unsafe_allow_html=True)
    
    # Escolha do ambiente
    st.markdown("### 🗺️ Escolha seu ambiente")
    
    environments = {
        "intimidade": {
            "icon": "🛏️",
            "title": "Intimidade Total",
            "description": "Motel, quarto - momento só de vocês"
        },
        "publico": {
            "icon": "🕯️",
            "title": "Espaço Público",
            "description": "Restaurante, café - diversão discreta"
        },
        "casa": {
            "icon": "🏠",
            "title": "Em Casa",
            "description": "Conforto do lar - ambiente relaxado"
        },
        "distancia": {
            "icon": "🎧",
            "title": "À Distância",
            "description": "Vídeo chamada - amor sem fronteiras"
        }
    }
    
    # Grid de ambientes
    cols = st.columns(2)
    env_keys = list(environments.keys())
    
    for i, env_key in enumerate(env_keys):
        with cols[i % 2]:
            env = environments[env_key]
            if st.button(f"{env['icon']} {env['title']}", key=f"env_{env_key}", help=env['description']):
                st.session_state.environment = env_key
                st.session_state.environment_name = env['title']
                st.rerun()
    
    # Opção de vibrador
    st.markdown("### 🔥 Modo Extra (Opcional)")
    use_vibrator = st.checkbox("💖 Usar vibrador inteligente durante o jogo", key="vibrator_checkbox")
    
    if use_vibrator:
        st.markdown("""
            <div style="background: rgba(255, 107, 107, 0.1); padding: 1rem; border-radius: 12px; margin: 1rem 0;">
                <p style="margin: 0; color: #2c3e50;">
                    ✨ Perfeito! O jogo sugerirá modos de vibração conforme a intensidade emocional aumenta.
                    Você ativará manualmente no app do seu brinquedo.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.environment:
        st.session_state.use_vibrator = use_vibrator
        if st.button("🚀 Começar o Jogo", type="primary"):
            st.session_state.game_started = True
            st.session_state.current_questions = get_questions_by_phase_and_environment(
                st.session_state.current_phase, 
                st.session_state.environment
            )
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_game_screen():
    """Tela principal do jogo"""
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Header com progresso
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown(f'<div class="phase-indicator">Fase {st.session_state.current_phase}</div>', unsafe_allow_html=True)
    
    with col2:
        progress = (st.session_state.question_index + 1) / len(st.session_state.current_questions) if st.session_state.current_questions else 0
        st.markdown(f"""
            <div class="game-progress">
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {progress * 100}%"></div>
                </div>
                <small>Pergunta {st.session_state.question_index + 1} de {len(st.session_state.current_questions)}</small>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        connection_level = st.session_state.game_logic.get_connection_level()
        hearts = "💟" if connection_level == 1 else "❤️" if connection_level == 2 else "🔥" if connection_level == 3 else "💥"
        st.markdown(f"""
            <div class="connection-level">
                <div class="connection-hearts">{hearts}</div>
                <div class="connection-text">Nível {connection_level}</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Pergunta atual
    if st.session_state.current_questions and st.session_state.question_index < len(st.session_state.current_questions):
        current_question = st.session_state.current_questions[st.session_state.question_index]
        
        st.markdown(f"""
            <div class="question-card">
                <div class="question-text">{current_question['text']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Ações da pergunta
        if current_question.get('action'):
            st.markdown(f"""
                <div style="background: rgba(255, 255, 255, 0.2); padding: 1rem; border-radius: 12px; margin: 1rem 0; text-align: center; color: white;">
                    <strong>💫 Ação especial:</strong> {current_question['action']}
                </div>
            """, unsafe_allow_html=True)
        
        # Botões de ação
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("😊 Responderam juntos", key="answered"):
                st.session_state.game_logic.add_connection_points(current_question.get('points', 1))
                next_question()
        
        with col2:
            if st.button("⏭️ Pular pergunta", key="skip"):
                next_question()
        
        # Sugestão de vibrador se ativado
        if st.session_state.use_vibrator:
            vibrator_mode = st.session_state.game_logic.get_vibrator_mode()
            if vibrator_mode:
                st.markdown(f"""
                    <div class="vibrator-card">
                        <h4>🔥 Sugestão Vibracional</h4>
                        <p>Ative o <strong>Modo {vibrator_mode}</strong> no outro celular e aproveitem essa intensidade juntos!</p>
                    </div>
                """, unsafe_allow_html=True)
    
    else:
        # Fim da fase atual
        show_phase_completion()
    
    st.markdown('</div>', unsafe_allow_html=True)

def next_question():
    """Avança para a próxima pergunta"""
    st.session_state.question_index += 1
    st.rerun()

def show_phase_completion():
    """Mostra conclusão da fase"""
    phase_names = {1: "Conectar", 2: "Desejar", 3: "Agir"}
    current_phase_name = phase_names.get(st.session_state.current_phase, "Conectar")
    
    st.markdown(f"""
        <div class="final-card">
            <h2>🎉 Fase {st.session_state.current_phase}: {current_phase_name} Concluída!</h2>
            <p>Vocês estão se conectando cada vez mais profundamente.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.current_phase < 3:
        if st.button("🔥 Próxima Fase", type="primary"):
            st.session_state.current_phase += 1
            st.session_state.question_index = 0
            st.session_state.current_questions = get_questions_by_phase_and_environment(
                st.session_state.current_phase, 
                st.session_state.environment
            )
            st.rerun()
    else:
        show_final_results()

def show_final_results():
    """Mostra resultados finais do jogo"""
    total_score = st.session_state.game_logic.connection_points
    final_level = st.session_state.game_logic.get_connection_level()
    
    st.markdown(f"""
        <div class="final-card">
            <h1>💕 Jogo Concluído!</h1>
            <div class="score-display">{total_score} pontos</div>
            <h3>Nível Final de Conexão: {final_level} {"💥" if final_level == 4 else "🔥" if final_level == 3 else "❤️" if final_level == 2 else "💟"}</h3>
            <p>Vocês criaram uma conexão ainda mais profunda!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sugestões finais
    st.markdown("""
        <div style="background: white; border-radius: 16px; padding: 2rem; margin: 1rem 0;">
            <h3>💌 Finalize essa experiência especial:</h3>
            <ul style="text-align: left;">
                <li>✍️ Escrevam uma carta um para o outro para ler amanhã</li>
                <li>📸 Compartilhem uma memória especial desta noite</li>
                <li>🤗 Se abracem por 20 segundos em silêncio</li>
                <li>💭 Digam três coisas que amam um no outro</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.use_vibrator:
        st.markdown("""
            <div class="vibrator-card">
                <h4>🔥 Despedida Especial</h4>
                <p>Para finalizar, ativem o <strong>Modo 9</strong> e celebrem essa conexão única que vocês têm! 💕</p>
            </div>
        """, unsafe_allow_html=True)
    
    if st.button("🔄 Jogar Novamente", type="primary"):
        # Reset do jogo
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

def main():
    """Função principal do app"""
    initialize_game_state()
    
    if not st.session_state.game_started:
        show_welcome_screen()
    else:
        show_game_screen()

if __name__ == "__main__":
    main()
