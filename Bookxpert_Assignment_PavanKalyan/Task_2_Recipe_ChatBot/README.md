# 🍳 AI Chef Master - Recipe Generator

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/FastAPI-0.68.0-green" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-1.10.0-FF4B4B" alt="Streamlit">
  
</div>

## 🌟 Introduction

AI Chef Master is an intelligent recipe generation system that helps you discover new recipes based on the ingredients you have. Whether you're a home cook looking for inspiration or a professional chef seeking new ideas, this application provides personalized recipe suggestions with beautiful, easy-to-follow instructions.

## ✨ Features

- **Smart Recipe Generation**: Get custom recipes based on available ingredients
- **Advanced Filtering**: Sort by meal categories, cooking time, and difficulty level
- **Beautiful UI**: Modern, responsive interface with smooth animations
- **Detailed Instructions**: Step-by-step cooking directions with professional tips
- **Nutritional Information**: Basic nutritional details for each recipe
- **Save & Share**: Save your favorite recipes or share them with friends

## 🛠️ Tech Stack

- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **AI/ML**: Hugging Face Transformers (GPT-2)
- **Database**: (Optional) SQLite for saved recipes
- **Deployment**: Docker (optional)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/recipe-chatbot.git
   cd recipe-chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

### 1. Start the Backend Server
```bash
cd server
uvicorn api_server:app --reload
```
The API will be available at `http://127.0.0.1:8000`

### 2. Start the Frontend
In a new terminal window:
```bash
cd ../ui
streamlit run app.py
```
The application will open in your default browser at `http://localhost:8501`

## 🎨 User Guide

### Home Screen
1. Enter your ingredients (comma-separated)
2. Select a meal category (optional)
3. Set maximum cooking time (optional)
4. Choose difficulty level (optional)
5. Click "Generate Recipe"

### Recipe View
- View the generated recipe with:
  - Preparation and cooking times
  - Detailed ingredient list
  - Step-by-step instructions
  - Chef's tips and serving suggestions

## 📚 Project Structure

```
recipe-chatbot/
├── server/
│   ├── api_server.py     # FastAPI application
│   ├── ai_generate.py    # Recipe generation logic
│   └── requirements.txt  # Backend dependencies
├── ui/
│   ├── app.py            # Streamlit UI
│   └── requirements.txt  # Frontend dependencies
├── test/                 # Test files
├── .gitignore
└── README.md
```

## 🧪 Testing

Run the test suite with:
```bash
cd test
pytest
```

## 🌐 API Documentation

Once the server is running, visit `http://127.0.0.1:8000/docs` for interactive API documentation.

### Endpoints
- `POST /generate`: Generate a new recipe
  - Parameters: `ingredients` (str), `category` (str, optional), `cooking_time` (int, optional), `difficulty` (str, optional)
  - Returns: JSON with the generated recipe

## 📸 Screenshots

<div align="center">
  <img src="screenshots/home.png" alt="Home Screen" width="45%">
  <img src="screenshots/recipe.png" alt="Generated Recipe" width="45%">
</div>

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- All the amazing open-source contributors

## 📧 Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com)

---

<div align="center">
  Made with ❤️ by Pavan Kalyan Neelam | 2025
</div>
