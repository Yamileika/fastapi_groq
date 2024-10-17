import os
from fastapi import FastAPI, HTTPException
from groq import Groq
import uvicorn 

app = FastAPI()

client = Groq(
    api_key=os.environ.get("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"),
)

@app.get("/pregunta")
async def groq(pregunta: str):
    try:
        chat = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": pregunta,
                }
            ],
            model="llama3-8b-8192",
        )

        response_message = chat.choices[0].message.content

        return {"respuesta": response_message}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000)) 
    uvicorn.run(app, host="0.0.0.0", port=port)