from flask import Flask, request, jsonify
from wtpsplit import SaT 
app = Flask(__name__)
sat = SaT("sat-3l-sm", style_or_domain="ud", language="en")


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})



@app.route('/split', methods=['POST'])
def split_text():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    result = sat.split(text)
    return jsonify({'sentences': result})

if __name__ == '__main__':
    app.run()
