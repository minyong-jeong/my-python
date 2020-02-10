from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def render_file():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Upload</title>
    </head>
    <body>
        <form action="http://localhost:5000/fileUpload" method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit">
        </form>
    </body>
    </html>"""

@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        path = "D:/" + secure_filename(f.filename)
        f.save(path)
        return '%s -> File upload complete' % path

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)