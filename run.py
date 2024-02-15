from app import app  # Apenas importe o aplicativo, não é necessário importar db

if __name__ == '__main__':
    app.run(debug=True)