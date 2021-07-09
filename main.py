import torch
from IPython.display import Image, clear_output  # to display images
import os
import cv2
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


# routes
@app.route("/")
def main():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['file']
        img_path = "static/" + img.filename
        img.save("static/sample.jpeg")

        command = "python yolov5/detect.py --weights yolov5/best.pt --img 416 --conf 0.4 --source static/sample.jpeg"
        os.system(command)

        # ss = 'Welcome'
        return render_template("new.html")

#    return render_template("index-old.html", prediction=ss, img_path=img_path)

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       # create a secure filename
#       filename = secure_filename(f.filename)
#       print(filename)
#       # save file to /static/uploads
#       filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#       print(filepath)
#       f.save(filepath)
#       get_image(filepath, filename)


if __name__ == "__main__":
    app.run(debug=True)
