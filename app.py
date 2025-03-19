from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Invalid input. Please enter valid numbers."
    
    # A simple HTML form using render_template_string.
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Simple Calculator</title>
    </head>
    <body>
      <h1>Calculator</h1>
      <form method="post">
        <input type="text" name="num1" placeholder="Enter first number" required>
        <select name="operation">
          <option value="add">+</option>
          <option value="subtract">-</option>
          <option value="multiply">*</option>
          <option value="divide">/</option>
        </select>
        <input type="text" name="num2" placeholder="Enter second number" required>
        <input type="submit" value="Calculate">
      </form>
      {% if result is not none %}
        <h2>Result: {{ result }}</h2>
      {% endif %}
    </body>
    </html>
    '''
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#this is a test cal app