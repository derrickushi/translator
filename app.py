from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    original_text = ""
    error_message = ""
    source_lang = "auto"
    target_lang = "kn" # Default target is Kannada
    
    try:
        languages = GoogleTranslator().get_supported_languages(as_dict=True)
    except Exception as e:
        languages = {'english': 'en', 'kannada': 'kn'} # Fallback

    if request.method == 'POST':
        original_text = request.form.get('text_to_translate', '')
        source_lang = request.form.get('source_lang', 'auto')
        target_lang = request.form.get('target_lang', 'kn')
        
        if original_text.strip():
            try:
                translator = GoogleTranslator(source=source_lang, target=target_lang)
                translated_text = translator.translate(original_text)
            except Exception as e:
                error_message = f"An error occurred during translation: {str(e)}"

    return render_template('index.html', 
                           translated_text=translated_text, 
                           original_text=original_text, 
                           error_message=error_message,
                           languages=languages,
                           source_lang=source_lang,
                           target_lang=target_lang)

@app.route('/api/translate', methods=['POST'])
def api_translate():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    original_text = data['text']
    source_lang = data.get('source_lang', 'auto')
    target_lang = data.get('target_lang', 'kn')
    
    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated_text = translator.translate(original_text)
        return jsonify({
            'original': original_text, 
            'translated': translated_text,
            'source_lang': source_lang,
            'target_lang': target_lang
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
