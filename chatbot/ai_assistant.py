

class AI_Assistant:
    def __init__(self):
        self.user_name = None
        self.llm_model = None
        self.embedding_model = None
        self.expert_domain = None        
        self.chain = None
    
    def setup(self, session_data: dict):
        self.user_name = session_data["user_name"]
        self.llm_model = session_data["llm_model"]
        self.embedding_model = session_data["embedding_model"]
        self.expert_domain = session_data["expert_domain"]

    def chat(self, user_query: str):
        response = f"The length of your text is {len(user_query)}"
        references = {
            "message": user_query,
            "length": len(user_query),
            "user_name": self.user_name,
        }
        return response, references

    