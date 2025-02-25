import json
import re
import torch
from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load Hugging Face NLP model for chatbot
chatbot_model = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def calculate_tax(income, deductions=0):
    taxable_income = max(0, income - deductions)
    tax = 0
    
    tax_slabs = [
        (250000, 0.05),
        (500000, 0.1),
        (750000, 0.15),
        (1000000, 0.2),
        (1250000, 0.25),
        (1500000, 0.3)
    ]
    
    prev_limit = 0
    for limit, rate in tax_slabs:
        if taxable_income > prev_limit:
            tax += (min(taxable_income, limit) - prev_limit) * rate
            prev_limit = limit
        else:
            break
    
    return tax

def get_deductions(details):
    deductions = 0
    if details.get("80C", 0) <= 150000:
        deductions += details.get("80C", 0)
    if details.get("80D", 0) <= 25000:
        deductions += details.get("80D", 0)
    if details.get("HRA", 0):
        deductions += details.get("HRA", 0)
    return deductions

@app.route('/calculate_tax', methods=['POST'])
def tax_api():
    try:
        data = request.get_json()
        income = data.get("income", 0)
        deductions = get_deductions(data.get("deductions", {}))
        tax = calculate_tax(income, deductions)
        return jsonify({"calculated_tax": tax})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_input = request.json.get("message", "").lower()
        response = chatbot_model(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
