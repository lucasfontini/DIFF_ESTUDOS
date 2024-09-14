from flask import Flask, render_template, request
import json
from deepdiff import DeepDiff

app = Flask(__name__)

def read_json_file(file_path):
    """Lê um arquivo JSON e retorna seu conteúdo."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def compare_json_files(file1, file2):
    """Compara dois arquivos JSON usando DeepDiff."""
    json1 = read_json_file(file1)
    json2 = read_json_file(file2)

    # Usando DeepDiff para comparar os JSONs
    diff = DeepDiff(json1, json2, ignore_order=True)
    
    # Converta o resultado do diff em um JSON formatado
    return json.dumps(diff, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        file1 = 'arquivo1.json'
        file2 = 'arquivo2.json'
        result = compare_json_files(file1, file2)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
