# Universal Translator

A modern, web-based translation application built with Flask and `deep-translator`. This app features a sleek, glassmorphism UI and supports translation across over 100 languages.

## Features
- **Dynamic Language Support:** Automatically fetches all supported languages from the backend.
- **Auto-Detection:** Option to auto-detect the source language.
- **Modern UI:** Responsive, aesthetic interface featuring glassmorphism and a dark mode color palette.
- **Copy to Clipboard:** One-click copy for the translated text.

## Tech Stack
- **Backend:** Python, Flask, `deep-translator`
- **Frontend:** HTML, CSS (Vanilla with modern variables), FontAwesome icons

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/derrickushi/translator.git
   cd translator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000/`.

## API Endpoint
You can also use the translation service programmatically via the API endpoint:
- **URL:** `/api/translate`
- **Method:** `POST`
- **Body JSON:** `{"text": "Hello world", "source_lang": "en", "target_lang": "fr"}`

Example response:
```json
{
  "original": "Hello world",
  "translated": "Bonjour le monde",
  "source_lang": "en",
  "target_lang": "fr"
}
```
