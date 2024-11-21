from openai import OpenAI
import base64

class GenAI:
    def __init__(self, model="gpt-4o", api_key=None):
        # Initialize with model selection and API key setup
        self.model = model
        self.client = OpenAI(api_key=api_key)
    
    
    def generate(self, prompt, max_tokens=2048, temperature=0.7, system_prompt="You are helpful chatbot."):
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
    
    def textToAudio(self, text, model="tts-1", voice="shimmer", audio_file="output.mp3", system_prompt="You are helpful chatbot."):
        completion = self.client.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": voice, "format": "wav"},
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        
        wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
        with open(audio_file, "wb") as f:
            f.write(wav_bytes)    

if __name__ == "__main__":
    # Example usage:
    gen_ai = GenAI(api_key="")
    result = gen_ai.generate("Write a creative opening line for a mystery novel.")
    print(result)
