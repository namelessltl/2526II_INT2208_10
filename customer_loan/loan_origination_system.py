from customer import Customer

class LoanOriginationSystem:
    def __init__(self, customer):
        self.customer = customer
        self.creditworthy = None
        self.loan_offer = None

    def check_valid_input(self):
        """Checks if the customer's input is valid."""
        if not isinstance(self.customer.age, int) or self.customer.age < 18 or self.customer.age > 65:
            raise ValueError("Invalid Input: Age must be an integer between 18 and 65.")
        
        if not isinstance(self.customer.income, (int, float)) or self.customer.income < 5 or self.customer.income > 500:
            raise ValueError("Invalid Input: Income must be a number between 5 and 500.")
        
        if not isinstance(self.customer.credit_score, int) or self.customer.credit_score < 300 or self.customer.credit_score > 850:
            raise ValueError("Invalid Input: Credit score must be an integer between 300 and 850.")
        
        if not isinstance(self.customer.employment, str) or self.customer.employment not in ['C', 'F']:
            raise ValueError("Invalid Input: Employment must be 'C' for contract or 'F' for freelance.")
        
        print("All inputs are valid.")
        return True
    
    def evaluate_creditworthiness(self):
        """Evaluates the customer's creditworthiness based on their input."""
        self.check_valid_input()
        
        if self.customer.credit_score >= 300 and self.customer.credit_score <= 500:
            self.creditworthy = "High"
        elif self.customer.credit_score >= 501 and self.customer.credit_score <= 700:
            self.creditworthy = "Medium"
        else:
            self.creditworthy = "Low"

        return self.creditworthy
    
    def generate_loan_offer(self):
        """Generates a loan offer based on the customer's info and creditworthiness."""
        evaluated_creditworthiness = self.evaluate_creditworthiness()
        
        if evaluated_creditworthiness == "High":
            self.loan_offer = "REJECT"
        elif evaluated_creditworthiness == "Medium":
            if self.customer.income < 15:
                self.loan_offer = "REJECT"
            else:
                if self.customer.employment == 'C':
                    self.loan_offer = "APPROVE"

                if self.customer.employment == 'F':
                    self.loan_offer = "MANUAL REVIEW"
        else:
            if self.customer.income < 15:
                if self.customer.employment == 'C':
                    self.loan_offer = "MANUAL REVIEW"
                else:
                    self.loan_offer = "REJECT"
            else:
                if self.customer.employment == 'C':
                    self.loan_offer = "APPROVE"

                if self.customer.employment == 'F':
                    self.loan_offer = "MANUAL REVIEW"
        
        return self.loan_offer