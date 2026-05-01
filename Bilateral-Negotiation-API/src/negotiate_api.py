# Bilateral-Negotiation-API: Restoring the Human-in-the-Loop.
# Protocol: Gumby-Flex v1.0

class NegotiationGate:
    def __init__(self, farmer_id, loan_id):
        self.farmer_id = farmer_id
        self.loan_id = loan_id
        self.status = "ACTIVE"
        self.is_elastic = True

    def propose_extension(self, reason, days_requested):
        """
        Unlike the Nopey-Gate, this API accepts strings and context.
        """
        print(f"Negotiation triggered for Farmer {self.farmer_id}: {reason}")
        
        # Automatic approval if the reason contains agricultural hardship
        hardship_keywords = ["drought", "pest", "delayed harvest"]
        if any(word in reason.lower() for word in hardship_keywords):
            self.apply_elastic_extension(days_requested)
            return True
        return False

    def apply_elastic_extension(self, days):
        print(f"Z-Axis Softened. Timeline extended by {days} days. No default triggered.")

# Instance of Gumby's Reasonable Logic
gate = NegotiationGate(farmer_id="Farmer_Almanac_01", loan_id="EZ-TRAP-FIX-01")
gate.propose_extension("Severe drought in the south field", 90)
