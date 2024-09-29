from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_ollama import OllamaLLM

app = FastAPI()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Initialize your LangChain Ollama model
model = OllamaLLM(model_name="Meditron")

# Define request model
class UserInput(BaseModel):
    input_text: str

# Define a route to handle requests
@app.post("/chat/")
async def chat(user_input: UserInput):
    try:
        # Use LangChain + Ollama model to generate response
        response = model.generate(user_input.input_text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

