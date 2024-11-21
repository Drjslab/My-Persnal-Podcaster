from openai import OpenAI

class GenAI:
    def __init__(self, model="gpt-4", api_key=None):
        # Initialize with model selection and API key setup
        self.model = model
        self.client = OpenAI(api_key=api_key)
        self.josnFormat = {
            'Idea': '',
            'Abstract': '',
            'Objectives': '',
            'Hypothesis': '',
            'Methodology': '',
            'Experimental_setup': '',
            'Conclusion': '',
            'Future_Study': '',
            'title': '',
            'emoji': 'only one related to topic'
        }


    
    def generate(self, prompt, max_tokens=2048, temperature=0.7):
        # Format the conversation as a list of messages with role and content
        conversation = [
            {"role": "system", "content": f"You are a helpful research assistant and only gives answer in JSON format {self.josnFormat} follwoing research idea."},
            {"role": "user", "content": prompt}
        ]
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=conversation,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    # Example usage:
    gen_ai = GenAI(api_key="")
    result = gen_ai.generate("Write a creative opening line for a mystery novel.")
    print(result)
