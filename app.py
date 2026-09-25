from app import create_app
import glob

app = create_app()

if __name__ == '__main__':
    # Archivos extra que Flask debe vigilar para recargar
    extra_files = (
        glob.glob('app/templates/**/*.html', recursive=True) +
        glob.glob('app/static/**/*.css',     recursive=True) +
        glob.glob('app/static/**/*.js',      recursive=True)
    )
    app.run(host='0.0.0.0', port=5000, debug=True, extra_files=extra_files)
