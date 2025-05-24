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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');
    
    /* Reset e base */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
    }
    
    /* Container principal */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 24px;
        padding: 2rem;
        margin: 1rem auto;
        max-width: 800px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Títulos */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
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
        line-height: 1.5;
    }
    
    /* Cards de ambiente */
    .environment-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .environment-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        border: 3px solid transparent;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .environment-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 107, 107, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .environment-card:hover::before {
        left: 100%;
    }
    
    .environment-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(255, 107, 107, 0.2);
        border-color: #ff6b6b;
    }
    
    .environment-card.selected {
        border-color: #ff6b6b;
        background: linear-gradient(135deg, #fff5f5, #ffffff);
        transform: scale(1.05);
    }
    
    /* Ícones de ambiente */
    .env-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
    }
    
    .env-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .env-description {
        color: #6c757d;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    /* Cards de pergunta */
    .question-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border-radius: 24px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .question-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .question-card:hover::before {
        opacity: 1;
    }
    
    .question-text {
        font-size: 1.5rem;
        font-weight: 500;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    .question-action {
        background: rgba(255, 255, 255, 0.15);
        padding: 1.5rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .question-action strong {
        display: block;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }
    
    /* Fase atual */
    .phase-indicator {
        background: linear-gradient(90deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 30px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    /* Nível de conexão */
    .connection-level {
        background: rgba(255, 107, 107, 0.1);
        border: 2px solid #ff6b6b;
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .connection-level:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.2);
    }
    
    .connection-hearts {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        display: block;
        animation: heartbeat 2s infinite;
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .connection-text {
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.2rem;
    }
    
    /* Vibrator mode card */
    .vibrator-card {
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 15px 35px rgba(255, 107, 107, 0.4);
        animation: pulse 3s infinite;
        position: relative;
        overflow: hidden;
    }
    
    .vibrator-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .vibrator-card h4 {
        margin-bottom: 1rem;
        font-size: 1.3rem;
        position: relative;
        z-index: 1;
    }
    
    .vibrator-card p {
        margin: 0;
        font-size: 1.1rem;
        position: relative;
        z-index: 1;
    }
    
    /* Botões */
    .stButton > button {
        width: 100%;
        border-radius: 16px;
        border: none;
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
        font-weight: 600;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(255, 107, 107, 0.4);
    }
    
    /* Progresso do jogo */
    .game-progress {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .progress-bar {
        background: #e9ecef;
        border-radius: 12px;
        height: 12px;
        overflow: hidden;
        margin: 1rem 0;
        position: relative;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #ff6b6b, #ee5a52);
        height: 100%;
        border-radius: 12px;
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .progress-fill::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        animation: progressShine 2s infinite;
    }
    
    @keyframes progressShine {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    /* Cards de resultado final */
    .final-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border-radius: 24px;
        padding: 3rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 20px 50px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .final-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 10s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .final-card > * {
        position: relative;
        z-index: 1;
    }
    
    .score-display {
        font-size: 4rem;
        font-weight: 700;
        margin: 1.5rem 0;
        text-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Checkbox personalizado para vibrador */
    .vibrator-option {
        background: rgba(255, 107, 107, 0.1);
        border: 2px solid #ff6b6b;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .vibrator-option:hover {
        background: rgba(255, 107, 107, 0.15);
        transform: translateY(-2px);
    }
    
    /* Sugestões finais */
    .final-suggestions {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .final-suggestions h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-size: 1.4rem;
    }
    
    .final-suggestions ul {
        list-style: none;
        padding: 0;
    }
    
    .final-suggestions li {
        padding: 0.75rem 0;
        border-bottom: 1px solid #eee;
        font-size: 1.1rem;
        color: #495057;
    }
    
    .final-suggestions li:last-child {
        border-bottom: none;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .main-container {
            margin: 0.5rem;
            padding: 1.5rem;
        }
        
        .main-title {
            font-size: 2.2rem;
        }
        
        .question-text {
            font-size: 1.3rem;
        }
        
        .env-icon {
            font-size: 3rem;
        }
        
        .environment-grid {
            grid-template-columns: 1fr;
        }
        
        .score-display {
            font-size: 3rem;
        }
    }
    
    /* Esconder elementos do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
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
            "description": "Motel, quarto - momento só de vocês dois"
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
    st.markdown('<div class="environment-grid">', unsafe_allow_html=True)
    
    cols = st.columns(2)
    env_keys = list(environments.keys())
    
    for i, env_key in enumerate(env_keys):
        with cols[i % 2]:
            env = environments[env_key]
            selected_class = "selected" if st.session_state.environment == env_key else ""
            
            if st.button(
                f"{env['icon']} {env['title']}", 
                key=f"env_{env_key}",
                help=env['description'],
                use_container_width=True
            ):
                st.session_state.environment = env_key
                st.session_state.environment_name = env['title']
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Opção de vibrador
    st.markdown("### 🔥 Modo Extra (Opcional)")
    
    st.markdown("""
        <div class="vibrator-option">
            <h4>💖 Vibrador Inteligente</h4>
            <p>Quer usar um vibrador durante o jogo? O app sugerirá modos conforme a intensidade emocional aumenta!</p>
        </div>
    """, unsafe_allow_html=True)
    
    use_vibrator = st.checkbox("✨ Sim, vamos usar!", key="vibrator_checkbox")
    
    if use_vibrator:
        st.markdown("""
            <div style="background: rgba(255, 107, 107, 0.1); padding: 1.5rem; border-radius: 16px; margin: 1rem 0; border: 2px solid #ff6b6b;">
                <p style="margin: 0; color: #2c3e50; font-size: 1.1rem; text-align: center;">
                    🔥 Perfeito! O jogo sugerirá modos de vibração conforme vocês se conectam mais profundamente.
                    <br><strong>Você ativará manualmente no app do seu brinquedo.</strong>
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Botão para começar
    if st.session_state.environment:
        st.session_state.use_vibrator = use_vibrator
        
        # Ativa o modo vibrador na lógica do jogo
        if use_vibrator:
            if 'game_logic' not in st.session_state:
                st.session_state.game_logic = GameLogic()
            st.session_state.game_logic.activate_vibrator_mode()
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 Começar nossa Jornada", type="primary", use_container_width=True):
            st.session_state.game_started = True
            st.session_state.current_questions = get_questions_by_phase_and_environment(
                st.session_state.current_phase, 
                st.session_state.environment
            )
            st.rerun()
    else:
        st.markdown("""
            <div style="text-align: center; color: #6c757d; margin: 2rem 0;">
                👆 Escolha um ambiente para começar
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_game_screen():
    """Tela principal do jogo"""
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Header com progresso
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        phase_names = {1: "Conectar", 2: "Desejar", 3: "Agir"}
        phase_name = phase_names.get(st.session_state.current_phase, "Conectar")
        st.markdown(f'<div class="phase-indicator">Fase {st.session_state.current_phase}: {phase_name}</div>', unsafe_allow_html=True)
    
    with col2:
        if st.session_state.current_questions:
            progress = (st.session_state.question_index + 1) / len(st.session_state.current_questions)
            st.markdown(f"""
                <div class="game-progress">
                    <div style="font-weight: 600; color: #2c3e50; margin-bottom: 0.5rem;">
                        Progresso da Fase
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {progress * 100}%"></div>
                    </div>
                    <small style="color: #6c757d;">Pergunta {st.session_state.question_index + 1} de {len(st.session_state.current_questions)}</small>
                </div>
            """, unsafe_allow_html=True)
    
    with col3:
        connection_level = st.session_state.game_logic.get_connection_level()
        level_names = {1: "Carinho", 2: "Desejo", 3: "Paixão", 4: "Êxtase"}
        level_name = level_names.get(connection_level, "Carinho")
        hearts = "💟" if connection_level == 1 else "❤️" if connection_level == 2 else "🔥" if connection_level == 3 else "💥"
        
        st.markdown(f"""
            <div class="connection-level">
                <span class="connection-hearts">{hearts}</span>
                <div class="connection-text">Nível {connection_level}<br><small>{level_name}</small></div>
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
                <div class="question-action">
                    <strong>💫 Ação Especial:</strong>
                    <div>{current_question['action']}</div>
                </div>
            """, unsafe_allow_html=True)
        
        # Botões de ação
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("😊 Respondemos juntos!", key="answered", use_container_width=True):
                st.session_state.game_logic.add_connection_points(current_question.get('points', 1))
                next_question()
        
        with col2:
            if st.button("⏭️ Próxima pergunta", key="skip", use_container_width=True):
                next_question()
        
        # Sugestão de vibrador se ativado - Sistema Inteligente
        if st.session_state.use_vibrator and st.session_state.game_logic.should_suggest_vibrator():
            vibrator_suggestion = st.session_state.game_logic.get_vibrator_suggestion(st.session_state.environment)
            if vibrator_suggestion:
                
                st.markdown(f"""
                    <div class="vibrator-card">
                        <h4>🔥 Controle do Vibrador - Modo {vibrator_suggestion['mode']}/9</h4>
                        <div style="font-size: 1.2rem; margin: 1rem 0; font-weight: 600;">
                            {vibrator_suggestion['progression']}
                        </div>
                        <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 12px; margin: 1rem 0;">
                            <strong>💫 {vibrator_suggestion['description']}</strong>
                        </div>
                        <p style="font-size: 1rem; font-style: italic; opacity: 0.9;">
                            {vibrator_suggestion['context_message']}
                        </p>
                        <div style="margin-top: 1rem; text-align: center;">
                            <small>🎯 <strong>Dica Pro:</strong> Ajustem a intensidade conforme as emoções de vocês crescem!</small>
                        </div>
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
    
    phase_messages = {
        1: "Vocês criaram uma base sólida de conexão emocional! 💕",
        2: "O desejo entre vocês está crescendo beautifully! 🔥", 
        3: "Chegaram ao ápice da intimidade e conexão! 💥"
    }
    
    message = phase_messages.get(st.session_state.current_phase, "")
    
    st.markdown(f"""
        <div class="final-card">
            <h2>🎉 Fase {st.session_state.current_phase}: {current_phase_name} Concluída!</h2>
            <p style="font-size: 1.2rem; margin: 1.5rem 0;">{message}</p>
            <div style="font-size: 1.1rem; opacity: 0.9;">
                Pontos de conexão nesta fase: <strong>{st.session_state.game_logic.connection_points}</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.current_phase < 3:
        if st.button("🔥 Próxima Fase - Vamos mais fundo!", type="primary", use_container_width=True):
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
    
    # Mensagens personalizadas baseadas na pontuação
    if total_score >= 40:
        result_message = "Vocês têm uma conexão extraordinária! 🌟"
        result_emoji = "💥"
    elif total_score >= 30:
        result_message = "Sua conexão é profunda e intensa! 🔥"
        result_emoji = "🔥"
    elif total_score >= 20:
        result_message = "Vocês se conectam de forma linda! ❤️"
        result_emoji = "❤️"
    else:
        result_message = "Um começo doce para sua jornada! 💟"
        result_emoji = "💟"
    
    st.markdown(f"""
        <div class="final-card">
            <h1>💕 Jornada Concluída!</h1>
            <div class="score-display">{result_emoji}</div>
            <h2>{total_score} Pontos de Conexão</h2>
            <h3>Nível Final: {final_level}</h3>
            <p style="font-size: 1.3rem; margin: 1.5rem 0;">{result_message}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sugestões finais personalizadas por ambiente
    environment_suggestions = {
        "intimidade": [
            "💋 Compartilhem um beijo longo e apaixonado",
            "✍️ Escrevam uma carta de amor um para o outro",
            "🕯️ Acendam velas e continuem se conectando",
            "💭 Digam três coisas que mais amam um no outro",
            "🤗 Abracem-se em silêncio por 30 segundos"
        ],
        "publico": [
            "📱 Tirem uma selfie para lembrar deste momento",
            "🌹 Planejem um encontro ainda mais especial",
            "💌 Enviem uma mensagem romântica um para o outro",
            "☕ Brindem a conexão de vocês",
            "🚶 Caminhem juntos sob as estrelas"
        ],
        "casa": [
            "🍽️ Preparem uma refeição especial juntos",
            "🛋️ Assistam ao pôr do sol abraçados",
            "📚 Leiam um para o outro",
            "🎵 Dancem sua música favorita",
            "🛁 Relaxem juntos em um banho romântico"
        ],
        "distancia": [
            "💻 Marquem um encontro virtual especial",
            "📦 Enviem uma surpresa um para o outro",
            "🌙 Olhem para a mesma lua ao mesmo tempo",
            "📞 Façam uma ligação de boa noite",
            "💌 Escrevam uma carta digital especial"
        ]
    }
    
    suggestions = environment_suggestions.get(st.session_state.environment, environment_suggestions["casa"])
    
    st.markdown(f"""
        <div class="final-suggestions">
            <h3>💌 Finalizem essa experiência especial:</h3>
            <ul>
    """, unsafe_allow_html=True)
    
    for suggestion in suggestions:
        st.markdown(f"<li>{suggestion}</li>", unsafe_allow_html=True)
    
    st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Despedida com vibrador se ativado
    if st.session_state.use_vibrator:
        final_messages = {
            "intimidade": "Para um gran finale inesquecível, ativem o Modo 9 e explorem todos os prazeres que descobriram juntos! 🔥💥",
            "publico": "Agora que estão indo para casa... Modo 9 os espera para uma noite épica! 😈🔥",
            "casa": "Em casa, vocês mandam! Modo 9 para uma celebração íntima e explosiva! 🏠💥",
            "distancia": "Mesmo à distância, conectem-se no Modo 9 e tenham o orgasmo virtual mais intenso! 💻🔥"
        }
        
        env_message = final_messages.get(st.session_state.environment, "Modo 9 para celebrar essa conexão única!")
        
        st.markdown(f"""
            <div class="vibrator-card">
                <h4>🔥 Grande Final - Modo 9</h4>
                <p style="font-size: 1.2rem;">{env_message}</p>
                <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.9;">
                    <strong>🎯 Vocês merecem essa explosão de prazer!</strong><br>
                    Todo o tesão que construíram durante o jogo culmina agora... ✨
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Botão para reiniciar
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Nova Jornada", type="primary", use_container_width=True):
            # Reset do jogo
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    with col2:
        if st.button("💕 Finalizar", use_container_width=True):
            st.markdown("""
                <div style="text-align: center; margin: 2rem 0;">
                    <h2>Obrigado por fortalecer a conexão de vocês! 💕</h2>
                    <p>Que esta seja apenas uma das muitas jornadas especiais juntos.</p>
                </div>
            """, unsafe_allow_html=True)

def main():
    """Função principal do app"""
    initialize_game_state()
    
    if not st.session_state.game_started:
        show_welcome_screen()
    else:
        show_game_screen()

if __name__ == "__main__":
    main()
