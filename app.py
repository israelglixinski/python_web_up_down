from flask import Flask, render_template, request, redirect, send_from_directory
import os

app = Flask(__name__)

# Configurações
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




# Página inicial
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

# Rota para upload de arquivo
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400
    
    file = request.files['file']
    if file.filename == '':
        return "Nenhum arquivo selecionado", 400
    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect('/')

# Rota para download de arquivo
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)




# Página inicial
@app.route('/playground1')
def index2():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

# Rota para upload de arquivo
@app.route('/playground1/upload', methods=['POST'])
def upload_file2():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400
    
    file = request.files['file']
    if file.filename == '':
        return "Nenhum arquivo selecionado", 400
    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect('/')

# Rota para download de arquivo
@app.route('/playground1/download/<filename>')
def download_file2(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)







if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5001')
