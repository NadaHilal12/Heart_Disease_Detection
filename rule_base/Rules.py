from experta import *

class HeartExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.score = 0

    @Rule(Fact(age=P(lambda x:x > 50))&
          Fact(chol=P(lambda x:x >240)))
    def high_risk(self):
        self.score += 1

    @Rule(Fact(age=P(lambda x:x > 50)))
    def age_risk(self):
        self.score += 1
    
    @Rule(Fact(exang=1))
    def angina(self):
        self.score += 1
    
    @Rule(Fact(age=P(lambda x:x < 40))&
          Fact(chol=P(lambda x:x <200))&
          Fact(trestbps=P(lambda x:x <120)))
    def low_risk(self):
        self.score += 1

    @Rule(Fact(ca=P(lambda x: x > 1)))
    def vessels(self):
        self.score += 1
    
    @Rule(Fact(thalach=P(lambda x: x < 120)))
    def low_hr(self):
        self.score += 1

    @Rule(Fact(oldpeak=P(lambda x:x >2)))
    def oldpeak_risk(self):
        self.score += 1

    @Rule(Fact(age=P(lambda x: x > 50)) &
        Fact(trestbps=P(lambda x: x >= 140)))
    def age_bp(self):
        self.score += 1

    @Rule(Fact(cp=P(lambda x: x >= 2)))
    def chest_pain(self):
        self.score += 1

    @Rule(Fact(fbs=1))
    def sugar(self):
        self.score += 1
    
    @Rule(Fact(exang=1) &
    Fact(oldpeak=P(lambda x: x > 2)) &
    Fact(thalach=P(lambda x: x < 120)))
    def heart_attack_risk(self):
        self.score += 1

    def get_result(self):
        if self.score >= 3:
            return 1
        else:
            return 0