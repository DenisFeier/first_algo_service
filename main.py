from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    make_response,
    send_file
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    tasks = []
    with open('db.txt', 'r') as file:
        for line in file:
            tasks.append(line.strip())
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    with open("db.txt", 'a') as file:
        new_task = request.form.get('newTask')
        if new_task:
            file.write(new_task + '\n')
    return redirect(url_for('index'))


@app.route('/index.json', methods=['GET'])
def index_json():
    tasks = []
    with open('db.txt', 'r') as file:
        for line in file:
            tasks.append(line.strip())
    return make_response(jsonify(tasks), 200)


@app.route('/get_image', methods=['GET'])
def get_image():
    return send_file('static/cat.jpg')


@app.route("/something", methods=["GET"])
def get_random():
    return "HELLO"


@app.route("/something_html", methods=["GET"])
def get_random_html():
    return """
        <ul>
            <li>Hay</li>
            <li>silver</li>
            <li>elf</li>
        </ul>
    """


if __name__ == '__main__':
    app.run(debug=True)
