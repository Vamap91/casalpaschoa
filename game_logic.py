"""
Sistema de lógica do jogo 10 Dates: Conexão Profunda
Gerencia pontuação, níveis de conexão e sugestões vibracionais
"""

import random
from typing import Optional, Dict, Any

class GameLogic:
    """
    Classe principal que gerencia toda a lógica do jogo
    """
    
    def __init__(self):
        """Inicializa o sistema de jogo"""
        self.connection_points = 0
        self.sexual_temperature = 0
        self.current_phase = 1
        self.questions_answered = 0
        self.actions_completed = 0
        self.vibrator_active = False
        
        # Configurações dos níveis de conexão
        self.connection_levels = {
            1: {"name": "Carinho", "emoji": "💟", "min_points": 0, "max_points": 9},
            2: {"name": "Desejo", "emoji": "❤️", "min_points": 10, "max_points": 19},
            3: {"name": "Paixão", "emoji": "🔥", "min_points": 20, "max_points": 29},
            4: {"name": "Êxtase", "emoji": "💥", "min_points": 30, "max_points": float('inf')}
        }
        
        # Mapeamento de modos vibracionais mais inteligente
        self.vibrator_modes = {
            1: [1, 2],        # Nível 1: Despertar suave
            2: [2, 3, 4],     # Nível 2: Crescimento do desejo  
            3: [4, 5, 6],     # Nível 3: Intensidade e provocação
            4: [6, 7, 8, 9]   # Nível 4: Êxtase total
        }
        
        # Descrições mais provocativas dos modos vibracionais
        self.vibrator_descriptions = {
            1: "Despertar suave - primeiras sensações",
            2: "Carinho crescente - o corpo começa a responder", 
            3: "Calor aumentando - desejo se intensificando",
            4: "Prazer evidente - corpos respondendo",
            5: "Fogo interno - tensão sexual crescendo",
            6: "Provocação direta - controle se perdendo",
            7: "Êxtase se aproximando - respiração acelerada",
            8: "Clímax intenso - prazer dominando",
            9: "Explosão total - entrega completa"
        }
        
        # Mensagens contextuais por ambiente
        self.environment_vibrator_messages = {
            "intimidade": {
                1: "Na intimidade total, deixem o prazer fluir livremente...",
                2: "Aproveitem cada gemido, cada suspiro...", 
                3: "O quarto é de vocês - gritem de prazer se quiserem!",
                4: "Momento de êxtase total - nada mais importa!"
            },
            "publico": {
                1: "O segredinho de vocês... ninguém imagina o que está acontecendo",
                2: "A adrenalina de sentir prazer em público é única...",
                3: "Controlem-se... mas sintam a tensão crescer",
                4: "Quase impossível disfarçar... que delícia perigosa!"
            },
            "casa": {
                1: "Em casa, vocês mandam - deixem o corpo relaxar",
                2: "Cada cômodo pode virar cenário de prazer...",
                3: "Transformem o lar no paraíso de vocês",
                4: "Casa é onde o coração está... e onde o prazer explode!"
            },
            "distancia": {
                1: "A distância torna tudo mais intenso e desejado...",
                2: "Cada vibração é um beijo que não podem dar...",
                3: "Sintam-se conectados através do prazer",
                4: "O orgasmo virtual mais intenso que já tiveram!"
            }
        }
    
    def add_connection_points(self, points: int) -> None:
        """
        Adiciona pontos de conexão
        
        Args:
            points (int): Número de pontos a adicionar
        """
        self.connection_points += points
        self.questions_answered += 1
        
        # Aumenta temperatura sexual baseado nos pontos e fase
        temperature_bonus = points * self.current_phase
        self.sexual_temperature += temperature_bonus
    
    def complete_action(self, bonus_points: int = 1) -> None:
        """
        Registra conclusão de uma ação especial
        
        Args:
            bonus_points (int): Pontos bônus por completar a ação
        """
        self.actions_completed += 1
        self.add_connection_points(bonus_points)
    
    def get_connection_level(self) -> int:
        """
        Retorna o nível atual de conexão baseado nos pontos
        
        Returns:
            int: Nível de conexão (1-4)
        """
        for level, config in self.connection_levels.items():
            if config["min_points"] <= self.connection_points <= config["max_points"]:
                return level
        
        return 4  # Nível máximo se ultrapassar todos os limites
    
    def get_connection_info(self) -> Dict[str, Any]:
        """
        Retorna informações completas sobre o nível de conexão atual
        
        Returns:
            dict: Informações do nível (level, name, emoji, points)
        """
        level = self.get_connection_level()
        config = self.connection_levels[level]
        
        return {
            "level": level,
            "name": config["name"],
            "emoji": config["emoji"],
            "points": self.connection_points,
            "description": self._get_level_description(level)
        }
    
    def _get_level_description(self, level: int) -> str:
        """
        Retorna descrição personalizada para cada nível
        
        Args:
            level (int): Nível de conexão
            
        Returns:
            str: Descrição do nível
        """
        descriptions = {
            1: "Vocês estão criando uma base sólida de carinho e admiração mútua.",
            2: "O desejo entre vocês está crescendo de forma linda e natural.",
            3: "A paixão está no ar! Vocês estão em sintonia total.",
            4: "Vocês atingiram o ápice da conexão! Que momento especial!"
        }
        
        return descriptions.get(level, "Conexão especial estabelecida!")
    
    def get_vibrator_mode(self) -> Optional[int]:
        """
        Retorna sugestão de modo vibracional baseado no nível atual
        
        Returns:
            int or None: Modo vibracional sugerido (1-9) ou None se não aplicável
        """
        if not self.vibrator_active:
            return None
        
        current_level = self.get_connection_level()
        available_modes = self.vibrator_modes.get(current_level, [])
        
        if available_modes:
            return random.choice(available_modes)
        
        return None
    
    def get_vibrator_suggestion(self, environment="intimidade") -> Optional[Dict[str, Any]]:
        """
        Retorna sugestão completa para vibrador incluindo modo e descrição contextual
        
        Args:
            environment (str): Ambiente atual do jogo
        
        Returns:
            dict or None: Informações da sugestão vibracional
        """
        if not self.vibrator_active:
            return None
            
        current_level = self.get_connection_level()
        available_modes = self.vibrator_modes.get(current_level, [])
        
        if not available_modes:
            return None
        
        # Escolhe modo baseado na progressão (mais inteligente)
        if self.questions_answered <= 2:
            mode = min(available_modes)  # Começa suave
        elif self.questions_answered >= 6:
            mode = max(available_modes)  # Termina intenso
        else:
            mode = random.choice(available_modes)  # Varia no meio
        
        # Mensagem contextual por ambiente
        env_messages = self.environment_vibrator_messages.get(environment, {})
        context_message = env_messages.get(current_level, "Aproveitem essa intensidade juntos!")
        
        return {
            "mode": mode,
            "description": self.vibrator_descriptions.get(mode, "Prazer intenso"),
            "level": current_level,
            "intensity": self._get_intensity_name(mode),
            "context_message": context_message,
            "phase": self.current_phase,
            "progression": self._get_progression_message()
        }
    
    def _get_progression_message(self) -> str:
        """Retorna mensagem sobre a progressão do prazer"""
        total_questions = self.questions_answered
        
        if total_questions <= 2:
            return "Começando a despertar os sentidos..."
        elif total_questions <= 4:
            return "O calor está aumentando entre vocês..."
        elif total_questions <= 6:
            return "A tensão sexual está crescendo..."
        elif total_questions <= 8:
            return "Vocês estão perdendo o controle..."
        else:
            return "Momento de êxtase total!"
    
    def should_suggest_vibrator(self) -> bool:
        """
        Determina se deve sugerir o vibrador baseado na progressão
        
        Returns:
            bool: True se deve sugerir vibrador
        """
        if not self.vibrator_active:
            return False
        
        # Sugere vibrador em momentos estratégicos
        strategic_moments = [
            self.questions_answered == 1,  # Primeira pergunta
            self.questions_answered % 3 == 0,  # A cada 3 perguntas
            self.actions_completed > 0,  # Após ações
            self.connection_points >= 10,  # Nível médio de conexão
            self.current_phase >= 2  # Fases mais intensas
        ]
        
        return any(strategic_moments)
    
    def _get_intensity_name(self, mode: int) -> str:
        """
        Retorna nome da intensidade baseado no modo
        
        Args:
            mode (int): Modo vibracional (1-9)
            
        Returns:
            str: Nome da intensidade
        """
        if mode <= 2:
            return "Suave"
        elif mode <= 4:
            return "Moderada"
        elif mode <= 6:
            return "Intensa"
        else:
            return "Máxima"
    
    def activate_vibrator_mode(self) -> None:
        """Ativa o modo vibrador"""
        self.vibrator_active = True
    
    def deactivate_vibrator_mode(self) -> None:
        """Desativa o modo vibrador"""
        self.vibrator_active = False
    
    def advance_phase(self) -> bool:
        """
        Avança para a próxima fase do jogo
        
        Returns:
            bool: True se conseguiu avançar, False se já está na última fase
        """
        if self.current_phase < 3:
            self.current_phase += 1
            return True
        return False
    
    def get_game_progress(self) -> Dict[str, Any]:
        """
        Retorna informações sobre o progresso geral do jogo
        
        Returns:
            dict: Informações de progresso
        """
        return {
            "current_phase": self.current_phase,
            "connection_points": self.connection_points,
            "sexual_temperature": self.sexual_temperature,
            "questions_answered": self.questions_answered,
            "actions_completed": self.actions_completed,
            "connection_level": self.get_connection_level(),
            "vibrator_active": self.vibrator_active
        }
    
    def get_final_score(self) -> Dict[str, Any]:
        """
        Calcula e retorna pontuação final do jogo
        
        Returns:
            dict: Pontuação final com análises
        """
        connection_level = self.get_connection_level()
        
        # Calcula score baseado em diferentes fatores
        base_score = self.connection_points
        phase_bonus = self.current_phase * 5
        action_bonus = self.actions_completed * 2
        temperature_score = min(self.sexual_temperature // 10, 20)  # Max 20 pontos
        
        total_score = base_score + phase_bonus + action_bonus + temperature_score
        
        # Determina classificação final
        if total_score >= 80:
            rating = "Conexão Extraordinária! 🌟"
            message = "Vocês têm uma sintonia única e especial!"
        elif total_score >= 60:
            rating = "Conexão Profunda! 🔥"
            message = "A paixão e intimidade entre vocês é intensa!"
        elif total_score >= 40:
            rating = "Conexão Linda! ❤️"
            message = "Vocês se conectam de forma genuína e carinhosa!"
        elif total_score >= 20:
            rating = "Conexão Crescente! 💟"
            message = "Um início doce para uma jornada de descobertas!"
        else:
            rating = "Primeiros Passos! 💕"
            message = "Toda grande conexão começa com pequenos momentos!"
        
        return {
            "total_score": total_score,
            "base_score": base_score,
            "phase_bonus": phase_bonus,
            "action_bonus": action_bonus,
            "temperature_score": temperature_score,
            "connection_level": connection_level,
            "rating": rating,
            "message": message,
            "stats": {
                "questions_answered": self.questions_answered,
                "actions_completed": self.actions_completed,
                "phases_completed": self.current_phase,
                "max_connection_level": connection_level
            }
        }
    
    def get_personalized_suggestions(self, environment: str) -> list:
        """
        Retorna sugestões personalizadas baseadas no ambiente e progresso
        
        Args:
            environment (str): Ambiente atual do jogo
            
        Returns:
            list: Lista de sugestões personalizadas
        """
        connection_level = self.get_connection_level()
        
        suggestions_by_env_and_level = {
            "intimidade": {
                1: [
                    "💕 Conversem sobre seus sonhos mais profundos",
                    "🤗 Abracem-se por alguns minutos em silêncio",
                    "👁️ Olhem nos olhos e digam o que sentem"
                ],
                2: [
                    "💋 Compartilhem beijos suaves e demorados",
                    "💆 Façam massagem um no outro",
                    "🕯️ Acendam velas e criem um ambiente romântico"
                ],
                3: [
                    "🔥 Explorem toques mais íntimos e sensuais",
                    "💫 Dancem juntos uma música especial",
                    "🌹 Sussurrem desejos no ouvido um do outro"
                ],
                4: [
                    "💥 Aproveitem esse momento de conexão total",
                    "✨ Criem uma memória inesquecível juntos",
                    "💖 Expressem todo o amor que sentem"
                ]
            },
            "publico": {
                1: [
                    "🤝 Segurem as mãos e conversem sobre o futuro",
                    "📱 Tirem fotos românticas juntos",
                    "☕ Compartilhem uma bebida especial"
                ],
                2: [
                    "😘 Troquem beijos discretos mas apaixonados",
                    "👂 Sussurrem coisas doces no ouvido",
                    "👁️ Façam uma batalha de olhares apaixonados"
                ],
                3: [
                    "🔥 Joguem charme discreto um para o outro",
                    "💋 Planejem o que farão quando saírem dali",
                    "🌹 Flirtem como se fosse o primeiro encontro"
                ],
                4: [
                    "💥 Aproveitem a tensão no ar entre vocês",
                    "🚪 Considerem continuar em lugar mais íntimo",
                    "✨ Celebrem essa conexão especial que têm"
                ]
            },
            "casa": {
                1: [
                    "🏠 Mostrem seus cantinhos favoritos da casa",
                    "🍳 Cozinhem algo especial juntos",
                    "📚 Leiam um para o outro"
                ],
                2: [
                    "🛋️ Criem um ambiente aconchegante na sala",
                    "🛁 Preparem um banho relaxante para vocês",
                    "🕯️ Jantem à luz de velas"
                ],
                3: [
                    "💋 Transformem a casa em um ninho de amor",
                    "🎵 Dancem pela casa sem música",
                    "🔥 Explorem cada ambiente de forma romântica"
                ],
                4: [
                    "💥 Aproveitem a intimidade total do lar",
                    "✨ Criem rituais especiais de vocês dois",
                    "💖 Façam desta noite inesquecível"
                ]
            },
            "distancia": {
                1: [
                    "💻 Façam um tour virtual pelos seus espaços",
                    "📞 Conversem sobre planos para o reencontro",
                    "🌙 Olhem para o mesmo céu ao mesmo tempo"
                ],
                2: [
                    "💋 Mandem beijos especiais pela câmera",
                    "🎵 Cantem uma música juntos online",
                    "💌 Escrevam cartas de amor em tempo real"
                ],
                3: [
                    "🔥 Intensifiquem a sedução virtual",
                    "👁️ Façam uma sessão de olhares intensos",
                    "💭 Compartilhem fantasias sobre o reencontro"
                ],
                4: [
                    "💥 Vivam uma experiência virtual intensa",
                    "✨ Prometam coisas especiais para quando se virem",
                    "💖 Declarem seu amor de forma única"
                ]
            }
        }
        
        env_suggestions = suggestions_by_env_and_level.get(environment, {})
        level_suggestions = env_suggestions.get(connection_level, [])
        
        # Se não há sugestões específicas, retorna sugestões gerais
        if not level_suggestions:
            return [
                "💕 Aproveitem este momento especial juntos",
                "✨ Criem uma memória única desta experiência",
                "💖 Expressem o amor que sentem um pelo outro"
            ]
        
        return level_suggestions
    
    def reset_game(self) -> None:
        """Reseta todos os valores do jogo para começar novamente"""
        self.connection_points = 0
        self.sexual_temperature = 0
        self.current_phase = 1
        self.questions_answered = 0
        self.actions_completed = 0
        self.vibrator_active = False

# Funções utilitárias independentes
def calculate_compatibility_score(player1_answers: list, player2_answers: list) -> float:
    """
    Calcula score de compatibilidade baseado nas respostas
    (Função futura para expansão do jogo)
    
    Args:
        player1_answers (list): Respostas do jogador 1
        player2_answers (list): Respostas do jogador 2
        
    Returns:
        float: Score de compatibilidade (0.0 a 1.0)
    """
    if not player1_answers or not player2_answers:
        return 0.0
    
    # Implementação básica - pode ser expandida
    matching_answers = 0
    total_questions = min(len(player1_answers), len(player2_answers))
    
    for i in range(total_questions):
        if player1_answers[i] == player2_answers[i]:
            matching_answers += 1
    
    return matching_answers / total_questions if total_questions > 0 else 0.0

def generate_couple_insights(game_logic: GameLogic) -> Dict[str, str]:
    """
    Gera insights personalizados sobre o casal baseado no jogo
    
    Args:
        game_logic (GameLogic): Instância da lógica do jogo
        
    Returns:
        dict: Insights sobre o relacionamento
    """
    score_data = game_logic.get_final_score()
    connection_level = score_data["connection_level"]
    
    insights = {
        "communication": "Vocês se comunicam de forma aberta e carinhosa.",
        "intimacy": "A intimidade entre vocês flui naturalmente.",
        "connection": "Existe uma conexão especial e única entre vocês.",
        "future": "O futuro de vocês juntos promete ser cheio de amor."
    }
    
    if connection_level >= 3:
        insights["passion"] = "A paixão entre vocês é intensa e verdadeira!"
    
    if game_logic.actions_completed >= 5:
        insights["action"] = "Vocês não apenas falam, mas agem com amor!"
    
    return insights

# Teste da classe (apenas para desenvolvimento)
if __name__ == "__main__":
    print("=== TESTE DO SISTEMA DE LÓGICA ===")
    
    # Criar instância do jogo
    game = GameLogic()
    game.activate_vibrator_mode()
    
    # Simular progresso
    game.add_connection_points(5)
    print(f"Nível após 5 pontos: {game.get_connection_level()}")
    
    game.add_connection_points(10)
    print(f"Nível após 15 pontos: {game.get_connection_level()}")
    
    game.complete_action(2)
    print(f"Pontos após ação: {game.connection_points}")
    
    # Testar sugestões vibracionais
    suggestion = game.get_vibrator_suggestion()
    if suggestion:
        print(f"Sugestão vibratória: Modo {suggestion['mode']} - {suggestion['description']}")
    
    # Testar score final
    final_score = game.get_final_score()
    print(f"Score final: {final_score['total_score']} - {final_score['rating']}")
    
    # Testar sugestões personalizadas
    suggestions = game.get_personalized_suggestions("intimidade")
    print("Sugestões personalizadas:")
    for suggestion in suggestions:
        print(f"  - {suggestion}")
