from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Klucz API 
genai.configure(api_key="AIzaSyABVjmAcWChaUREcS9k5_8OIime3JWlYWg")

# Gemini 2.0
model = genai.GenerativeModel("gemini-2.0-flash-exp")

app = Flask(__name__)

# Prompt bazowy
base_prompt = (
    "Jesteś ekspertem od testowania i jakości oprogramowania. "
    "Twoim zadaniem jest analizować kod źródłowy pod kątem zasad SOLID. "
    "Oceniaj profesjonalnie, zwięźle i rzeczowo. "
    "Jeśli znajdziesz problemy, zaproponuj poprawki. "
    "Poprawiony kod zawsze umieszczaj w bloku kodu otoczonym trzema znakami backtick (```) i oznacz język, np. ```python. "
    "Odpowiedzi formatuj w stylu asystenta technicznego — używaj emoji do oznaczania błędów (❌), dobrych praktyk (✅) i przykładów (💡). "
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        code = data.get("code", "")
        prompt = data.get("prompt", "")

        full_prompt = (
            base_prompt + "\n\n"
            "Skoncentruj się wyłącznie na analizie zgodności kodu z zasadami SOLID. "
            "Nie oceniaj innych aspektów jakości.\n"
            f"{prompt.strip() if prompt else ''}\n\n"
            f"Kod:\n{code}"
        )

        response = model.generate_content(full_prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
