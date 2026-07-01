from flask import Flask, render_template, request, send_file
from recon.aggregator import run_recon
from recon.report_writer import write_report
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    target = request.form.get("target", "").strip()

    if not target:
        return render_template("index.html", error="Please enter a URL or IP address.")

    data = run_recon(target)
    filepath = write_report(data, target)

    return render_template("result.html", data=data, target=target, filename=os.path.basename(filepath))


@app.route("/download/<filename>")
def download(filename):
    filepath = os.path.join("reports", filename)
    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
