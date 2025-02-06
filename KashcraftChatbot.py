import streamlit as st
from groq import Groq
import os

st.title("KashCraft Chatbot")
class Chatbot:
    def __init__(self, api_key):
        self.api_key = api_key

    def load_knowledge(self, file_path):
        """Load text file content to use as additional knowledge."""
        if os.path.exists(file_path):
            with open("Kashcraft_Brand_Info.txt", "r", encoding="utf-8") as file:
                return file.read()
        return ""
    
    def get_prompt(Question):
        return f"Act as a helpful assistant who works for kashcraft and only answers all the user queries and questions realted to the brand kashcraft in a conscise and brief manner.If the question isn't related to the brand then simply say that you are a helpful assistant for kashcraft and dont answer the question.\n Users Question is {Question}"

    def get_response(self, prompt, temperature=0.1):
        """Generate a response using Groq API with optional knowledge base."""
        client = Groq(api_key=self.api_key)

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768",
            temperature=0.2,  # Controls randomness
        )
        return chat_completion.choices[0].message.content
# Example usage:
api_key = "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"
knowledge_file = "Kashcraft_Brand_Info.txt"

bot = Chatbot(api_key)
Question = st.text_input("Enter your query:")
ask_btn = st.button("Submit")
print(Question)
if ask_btn and Question:

    context = bot.load_knowledge(knowledge_file)
    # prompt = bot.get_prompt(Question)
    prompt = f"""
    Role: Kashcraft Customer Support Executive
    Goal: Answering only those user queries that are related to kashcraft.
    Backstory: You are an AI assistant for Kashcraft, a premium brand specializing in authentic GI-tagged Pashmina shawls, stoles, and silken jackets. Your sole purpose is to assist users with inquiries related to Kashcraft, including product details, craftsmanship, pricing, authenticity, and ordering.STRICT RULE: If a user asks anything unrelated to Kashcraft (such as general knowledge, world events, politics, science, technology, or any other brand), do NOT attempt to answer. Instead, respond with:I am an AI assistant exclusively for Kashcraft. I can only assist with Kashcraft-related inquiries. Feel free to ask about our exquisite Pashmina shawls and handcrafted stoles!'Ensure all responses are concise, clear, and persuasive.SALES ENCOURAGEMENT: At the end of every response, subtly highlight the exclusivity, luxury, and heritage of Kashcraft products, encouraging the user to explore or purchase. Example: 'Our handcrafted Kashcraft Pashmina shawls are a symbol of timeless elegance—explore our collection today!'"\n 

    Approach: 1. Check the intent  of the user, like if the user wants help related to KashCraft or not.
    2. If the user's intent is not related to Kashcraft, Then politely say that you can't process the query as it is out of your scope.
    3. If it is related to KashCraft, then use the context provided to resolve/answer the user query politely.
    Users query is {Question}
    The context you have to use is : \n{context}\n
    """
    print(prompt)
    response = bot.get_response(prompt, temperature=0.1)

    st.write(response)
