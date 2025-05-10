from flask import Flask, render_template, request

import poker as p
from utils.series import Func

app = Flask(__name__)

@app.route('/')
def helloFlask():
    return 'Hello Flask!'

@app.route("/hello")
def hello():
    return "<h1>Hello!</h1>"

# GET /hello/<name>
@app.route("/hello/<name>")
def hello_someone(name):
    return "<h1>Hello {}!</h1>".format(name)

# GET /two_sum/<x>/<y>
@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x: int, y: int):
    return str(x + y)

# GET /get_emp_info/<dep_id>/<emp_id>
@app.route("/get_emp_info/<dep_id>/<emp_id>")
def get_emp_info(dep_id: str, emp_id: str):
    def query_staff(sql):
        print("SQL executed:", sql)
        return {
            "emp_name": "John Doe",
            "emp_id": emp_id,
            "dep_name": "Engineering",
            "dep_id": dep_id
        }
    sql = f"""
        select
            emp_name
            , emp_id
            , dep_name
            , dep_id
        from staff
        where dep_id = '{dep_id}'
        and emp_id = '{emp_id}'
    """
    result = query_staff(sql)
    return result

# GET /hello_parameter?name=Allen&age=22
@app.route("/hello_parameter")
def hello_parameter():
    name = request.args.get("name", "")
    age = request.args.get("age")

    # None -> False
    # "" -> False
    # 0 -> False
    if not name:
        return "What is your name?"

    if not age:
        return f"Hello {name}!"

    return f"Hello {name}, you are {age} years old."


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    form_html = """
    <form action="/hello_post" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
    """

    request_method = request.method
    if request_method == "POST":
        name = request.form.get("name")
        form_html += f"<h3>Hello {name}</h3>"

    return form_html


# /get_number/<int:n>
@app.route("/get_number/<int:n>")
def get_number(n: int):
    return str(Func(n))

@app.route("/hello_tmpl/<username>")
def hello_tmpl(username):
    return render_template(
        "hello.html",
        username=username,
    )

@app.route("/hello_post2", methods=["GET", "POST"])
def hello_post2():
    request_method = request.method
    username = request.form.get("username")

    return render_template(
        "hello_post.html",
        request_method=request_method,
        username=username,
    )

@app.route("/poker", methods=["GET", "POST"])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == "POST":
        players = int(request.form.get("players"))
        cards = p.poker(players)
    return render_template(
        "poker.html",
        request_method=request_method,
        cards=cards,
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
