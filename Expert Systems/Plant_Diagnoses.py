# To install experta package, write: pip install experta
from experta import *

# Plant inherits from Fact class.
class Plant(Fact):
    """Info about the plant."""
    pass

# PlantDiagnoses inherits from KnowledgeEngine class.
class PlantDiagnoses(KnowledgeEngine):
    @Rule(Plant(temperature='high',humidity="normal",color= "reddish-brown"))
    def black_heart(self):
        print("The plant has black heart")

    @Rule(Plant(temperature='low', humidity="high", color="yellow"))
    def late_blight(self):
        print("The plant has late blight")

    @Rule(Plant(temperature='normal', humidity="normal", color="brown"))
    def early_blight(self):
        print("the plan has early blight")


# Take object from PlantDiagnoses class
engine = PlantDiagnoses()
engine.reset()

engine.declare(Plant(temperature="high",humidity="normal",color= "reddish-brown"))
engine.run()


