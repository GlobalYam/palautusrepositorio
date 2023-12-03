class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]

        # tarkista ovatko tasan
        if self.m_score1 == self.m_score2:
            # jos ovat tasan, niin score 1 ja score 2 ovat samat
            # täten valitaan scorenames listasta pisteiden perusteella
            if self.m_score1 < 3:
                score = f"{score_names[self.m_score1]}-All"
            else:
                score = "Deuce"
        
        # jos scoret eivät ole tasan niin tarkistetaan lisää ehtoja, kuten jos peli voi olla ohi
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score_difference = self.m_score1 - self.m_score2
            winning_player = f"player{1 if score_difference > 0 else 2}"
            
            #onko etu vai voitto?
            if abs(score_difference) == 1:
                score = f"Advantage {winning_player}"
            else:
                score = f"Win for {winning_player}"
        else:
            # jos peli ei ole lähellä loppua:
            score = f"{score_names[self.m_score1]}-{score_names[self.m_score2]}"

        return score