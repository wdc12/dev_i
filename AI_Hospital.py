class ExpertSystem:
    def __init__(self):
        self.rules = []  # Knowledge base

    def add_rule(self, condition, action):
        self.rules.append((condition, action))

    def make_decision(self, symptoms):
        for condition, action in self.rules:
            if all(symptom in symptoms for symptom in condition):
                return action
        return "No diagnosis found"

# Example usage
if __name__ == "__main__":
    # Initialize the expert system
    expert_system = ExpertSystem()

    # Add rules to the knowledge base
    expert_system.add_rule(["fever", "cough"], "Diagnosis: Common cold")
    expert_system.add_rule(["fever", "shortness of breath"], "Diagnosis: Flu")

    # Get user input
    symptoms = input("Enter the symptoms (separated by commas): ").split(",")

    # Make a decision based on the given symptoms
    diagnosis = expert_system.make_decision(symptoms)
    print(diagnosis)
    
   
'''
A system that uses human expertise to make complicated decisions.Simulates reasoning by
applying knowledge and interfaces.Uses expert’s knowledge as rules and data within the
system.Models the problem solving ability of a human expert.
Components of an ES:
1. Knowledge Base
i. Represents all the data and information inputed by experts in the field.
ii. Stores the data as a set of rules that the system must follow to make decisions.
2. Reasoning or Inference Engine
i. Asks the user questions about what they are looking for.
ii. Applies the knowledge and the rules held in the knowledge base.
iii. Appropriately uses this information to arrive at a decision.
3. User Interface
i. Allows the expert system and the user to communicate.
ii. Finds out what it is that the system needs to answer.
iii. Sends the user questions or answers and receives their response.
4. Explanation Facility
i. Explains the systems reasoning and justifies its conclusions.
?- go.
Does the patient has the symptom headache? : y.
Does the patient has the symptom runny_nose? : |: n.
Does the patient has the symptom sore_throat? : |: n.
Does the patient has the symptom abdominal_pain? : |: y.
Does the patient has the symptom poor_appetite? : |: y.
Does the patient has the symptom fever? : |: y.
Advices and Sugestions:
1: Chloramphenicol
2: Amoxicillin
3: Ciprofloxacin
4: Azithromycin
Please do complete bed rest and take soft diet because
It is suggested that the patient has typhoid
true .
'''
