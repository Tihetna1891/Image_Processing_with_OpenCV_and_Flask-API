from flask import Flask, render_template, request, redirect, url_for
import cv2
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process the image (convert to grayscale and detect edges)
        img = cv2.imread(filepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)

        # Save processed images
        gray_path = os.path.join(app.config['UPLOAD_FOLDER'], 'gray_' + file.filename)
        edges_path = os.path.join(app.config['UPLOAD_FOLDER'], 'edges_' + file.filename)
        cv2.imwrite(gray_path, gray)
        cv2.imwrite(edges_path, edges)

        return render_template('index.html', original=file.filename, gray='gray_' + file.filename, edges='edges_' + file.filename)

if __name__ == '__main__':
    app.run(debug=True)