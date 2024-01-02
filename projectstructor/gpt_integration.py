from openai import OpenAI

class GPTIntegration:
    def __init__(self, api_key, model="gpt-3.5-turbo", temperature=0.7, max_tokens=150, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.client = OpenAI(api_key=self.api_key)

    def query_gpt(self, system_message, user_message):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model=self.model
        )
        return chat_completion
