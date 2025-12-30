"""
Flask API for BMI Calculator.
"""
from flask import Flask, request, jsonify, render_template_string
from .calculator import calcular_imc, classificar_imc

app = Flask(__name__)

# Simple HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora de IMC</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .form-group {
            margin: 20px 0;
        }
        label {
            display: block;
            margin-bottom: 5px;
            color: #555;
            font-weight: bold;
        }
        input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        #result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            display: none;
        }
        .result-success {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
        }
        .result-error {
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            color: #721c24;
        }
        .api-docs {
            margin-top: 30px;
            padding: 20px;
            background-color: #e9ecef;
            border-radius: 5px;
        }
        .api-docs h2 {
            color: #333;
            font-size: 18px;
        }
        .api-docs code {
            background-color: #f8f9fa;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Calculadora de IMC</h1>
        <form id="imcForm">
            <div class="form-group">
                <label for="peso">Peso (kg):</label>
                <input type="number" step="0.01" id="peso" name="peso" required>
            </div>
            <div class="form-group">
                <label for="altura">Altura (m):</label>
                <input type="number" step="0.01" id="altura" name="altura" required>
            </div>
            <button type="submit">Calcular IMC</button>
        </form>
        <div id="result"></div>
        
        <div class="api-docs">
            <h2>API Documentation</h2>
            <p><strong>Endpoint:</strong> <code>POST /api/calcular</code></p>
            <p><strong>Body:</strong> <code>{"peso": 70, "altura": 1.75}</code></p>
            <p><strong>Response:</strong> <code>{"imc": 22.86, "classificacao": "Peso normal"}</code></p>
        </div>
    </div>
    
    <script>
        document.getElementById('imcForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const peso = parseFloat(document.getElementById('peso').value);
            const altura = parseFloat(document.getElementById('altura').value);
            
            try {
                const response = await fetch('/api/calcular', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ peso, altura }),
                });
                
                const data = await response.json();
                const resultDiv = document.getElementById('result');
                
                if (response.ok) {
                    resultDiv.className = 'result-success';
                    resultDiv.innerHTML = `
                        <strong>Resultado:</strong><br>
                        IMC: ${data.imc}<br>
                        Classificação: ${data.classificacao}
                    `;
                } else {
                    resultDiv.className = 'result-error';
                    resultDiv.innerHTML = `<strong>Erro:</strong> ${data.error}`;
                }
                
                resultDiv.style.display = 'block';
            } catch (error) {
                const resultDiv = document.getElementById('result');
                resultDiv.className = 'result-error';
                resultDiv.innerHTML = `<strong>Erro:</strong> ${error.message}`;
                resultDiv.style.display = 'block';
            }
        });
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    """Render the main web interface."""
    return render_template_string(HTML_TEMPLATE)


@app.route('/api/calcular', methods=['POST'])
def calcular():
    """
    API endpoint to calculate BMI.
    
    Expected JSON body:
    {
        "peso": float,
        "altura": float
    }
    
    Returns:
    {
        "imc": float,
        "classificacao": string
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "JSON body é obrigatório"}), 400
        
        peso = data.get('peso')
        altura = data.get('altura')
        
        if peso is None or altura is None:
            return jsonify({"error": "Campos 'peso' e 'altura' são obrigatórios"}), 400
        
        peso = float(peso)
        altura = float(altura)
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        return jsonify({
            "imc": imc,
            "classificacao": classificacao
        })
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200


def main():
    """Start the Flask application."""
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', '5000'))
    
    app.run(debug=debug_mode, host=host, port=port)


if __name__ == "__main__":
    main()
