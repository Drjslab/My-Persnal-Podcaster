from openai import OpenAI

class GenAI:
    def __init__(self, model="gpt-4", api_key=None):
        # Initialize with model selection and API key setup
        self.model = model
        self.client = OpenAI(api_key=api_key)
    
    
    def generate(self, prompt, max_tokens=2048, temperature=0.7, system_prompt):
        # Format the conversation as a list of messages with role and content
        conversation = [
            {"role": "system", "content": system_prompt},
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
    
    def textToAudio(self, text, model="tts-1", voice="alloy", audio_file="output.mp3"):
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text,
        )
        response.stream_to_file(audio_file)    

if __name__ == "__main__":
    # Example usage:
    gen_ai = GenAI(api_key="")
    result = gen_ai.generate("Write a creative opening line for a mystery novel.")
    print(result)
