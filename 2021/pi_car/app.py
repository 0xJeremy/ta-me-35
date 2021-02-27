from flask import Flask, Response, render_template, request
import serial
import cv2


try:
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import time

    serialPort = serial.Serial("/dev/serial0", baudrate=115200)
    camera = PiCamera()
    camera.resolution = (640, 480)
    time.sleep(2)
    rawCapture = PiRGBArray(camera, size=(640, 480))

    def gen_frames():
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            ret, buffer = cv2.imencode(".jpg", frame.array)
            frame = buffer.tobytes()
            rawCapture.truncate(0)
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


except Exception as E:
    print(E)

    serialPort = None
    cam = cv2.VideoCapture(2)

    def gen_frames():
        while True:
            success, frame = cam.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode(".jpg", frame)
                frame = buffer.tobytes()
                yield (
                    b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                )


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/cmd", methods=["POST"])
def cmd():
    global serialPort
    requestData = request.form["type"]
    print("Sending command to SPIKE: {}".format(requestData))
    if serialPort:
        serialPort.write(requestData.encode())
    return "Success!"


if __name__ == "__main__":
    app.run(debug=True)
