import os
from flask import Flask, send_from_directory, request, send_file
from PIL import Image
import io

# Path to your frontend folder
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

app = Flask(
    __name__,
    static_folder=FRONTEND_FOLDER,   # serve CSS/JS from here
    static_url_path=''               # so /style.css maps to frontend/style.css
)

# Root route serves index.html from frontend/
@app.route('/')
def home():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

@app.route('/upload-image', methods=['POST'])
def upload_image():
    file = request.files.get('image')
    if not file:
        return "No file uploaded", 400

    # Compress into memory buffer
    img = Image.open(file.stream).convert('RGB')
    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=50, optimize=True)
    buf.seek(0)

    # Send as downloadable attachment
    return send_file(
        buf,
        mimetype='image/jpeg',
        as_attachment=True,
        download_name='compressed.jpg'
    )

if __name__ == '__main__':
    app.run(debug=True)
