# Indian Tax Assistant

## Overview
The **Indian Tax Assistant** is a Python-based web API that simplifies tax calculations under Indian tax laws and provides an AI-powered chatbot for tax-related queries. It utilizes **Flask** for the API and integrates Hugging Face's **DialoGPT** for natural language interactions.

## Features
- **Income Tax Calculation**: Computes tax based on Indian tax slabs, incorporating deductions like 80C, 80D, and HRA.
- **AI Chatbot**: Uses Hugging Face's DialoGPT to provide conversational tax-related assistance.
- **API-Based Interface**: Accepts JSON inputs and returns structured responses.

## Technologies Used
- **Flask** (for API development)
- **Hugging Face Transformers (DialoGPT)** (for AI chatbot functionality)
- **PyTorch** (for deep learning model execution)

## Installation
### Prerequisites
Ensure you have Python (>=3.8) installed along with the required libraries:
```sh
pip install flask torch transformers
```

## Usage
### Running the Application
```sh
python app.py
```

### API Endpoints
#### 1. Tax Calculation (`/calculate_tax`)
- **Method**: `POST`
- **Request Format (JSON)**:
  ```json
  {
    "income": 800000,
    "deductions": {
      "80C": 100000,
      "80D": 20000,
      "HRA": 50000
    }
  }
  ```
- **Response Format (JSON)**:
  ```json
  {
    "calculated_tax": 25000.0
  }
  ```

#### 2. AI Chatbot (`/chatbot`)
- **Method**: `POST`
- **Request Format (JSON)**:
  ```json
  {
    "message": "How much tax do I need to pay?"
  }
  ```
- **Response Format (JSON)**:
  ```json
  {
    "response": "Please provide your income and deductions to calculate your tax."
  }
  ```

## Future Enhancements
- Integration with government tax APIs for real-time data.
- More advanced NLP models for better chatbot responses.
- Support for additional tax deduction categories.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

