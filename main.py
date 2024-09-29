from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below
Here is a conversation history;{context}
Question :{question}
Answer:

"""

model = OllamaLLM(model ="Meditron")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("welcome to the ai chatbot. Type 'exit' to quit")
    while True:
        user_input = input("you:")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)
        
        context += f"\n user:{user_input} \n ai: {result}"

if __name__ == "__main__":
    handle_conversation()