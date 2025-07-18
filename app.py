from flask import Flask, render_template, request, jsonify
from agents.linkedin_summary_agent import generate_profile_summary
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        details = data.get('details', '').strip()
        
        if not name:
            return jsonify({'error': 'Name is required'}), 400
        
        summary, profile_image_url = generate_profile_summary(name, details, mock=False)
        
        result = {
            'summary': summary.summary if hasattr(summary, 'summary') else str(summary),
            'facts': summary.facts if hasattr(summary, 'facts') else [],
            'profile_image_url': profile_image_url,
            'name': name
        }
        
        return jsonify(result)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)