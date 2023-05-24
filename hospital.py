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
