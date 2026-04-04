from app import create_app

# Itt hívjuk meg a factory függvényt
app = create_app()

if __name__ == '__main__':
    # Csak fejlesztéskor fut ez a blokk (gunicorn/uwsgi nem ezt használja)
    app.run(debug=True)