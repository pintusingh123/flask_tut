from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
# MySQL configurations
app.secret_key = 'flask_project_secret_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'office_employee_management'
app.config['MYSQL_PORT'] = 3307
mysql_configuration = MySQL(app)



@app.route('/')
def home():
    # Landing page shows multiple sections (about/admin/contact) included as partials
    return render_template('landing.html')

@app.route('/home')
def index():
    # Keep original index available at /home
    return render_template('landing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin-login')
def admin_login():
    return render_template('admin-login.html')

@app.route('/blog')
def contactus():
    return render_template('blog.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_home():
    if request.method == 'POST':
        # Admin login form posts here. This is a placeholder for login validation.
        return render_template('admin/admin-home.html')
    return render_template('admin/admin-home.html')
@app.route('/admin-home')
def admin_home2():
    return render_template('admin/admin-home.html')

@app.route('/add-employee')
def add_employee():
    return render_template('admin/add-employee.html')

@app.route('/show-employees')
def show_employees():
    employees = []  # Will be populated from database
    mysql = mysql_configuration
    mycursor = mysql.connection.cursor() # connection with db by cursor obj
    mycursor.execute("SELECT * FROM employee_data")
    employees = mycursor.fetchall()
    mycursor.close()
    return render_template('admin/show-employee.html', employees=employees)

@app.route('/search-employee')
def search_employee():
    query = request.args.get('query', '').strip()
    employees = []

    if query:
        mysql = mysql_configuration
        mycursor = mysql.connection.cursor()
        like_query = f"%{query}%"
        sqlQuery = (
            "SELECT * FROM employee_data "
            "WHERE empid LIKE %s OR name LIKE %s OR email LIKE %s OR position LIKE %s"
        )
        mycursor.execute(sqlQuery, (like_query, like_query, like_query, like_query))
        employees = mycursor.fetchall()
        mycursor.close()

    return render_template('admin/search-employee.html', query=query, employees=employees)

@app.route('/add-employee-save', methods=['POST'])
def add_employee_save():
    # This is a placeholder for processing the add employee form submission.
    # In a real application, you would validate and save the data here.
    empid = (request.form.get('emp_id') or '').strip()
    name = (request.form.get('full_name') or '').strip()
    email = (request.form.get('email') or '').strip()
    mobile = (request.form.get('mobile') or '').strip()
    salary = (request.form.get('salary') or '').strip()
    position = (request.form.get('position') or '').strip()

    form = {
        "emp_id": empid,
        "full_name": name,
        "email": email,
        "mobile": mobile,
        "salary": salary,
        "position": position,
    }

    if not empid or not name or not email:
        return render_template(
            'admin/add-employee.html',
            error="Emp ID, Full Name, and Email are required.",
            form=form,
        )

    mysql = mysql_configuration
    mycursor = mysql.connection.cursor()  # connection with db by cursor obj

    try:
        sql = (
            "INSERT INTO employee_data(empid,name, email,mobile, salary, position) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        values = (empid, name, email, mobile or None, salary or None, position or None)
        mycursor.execute(sql, values)  # query specification
        mysql.connection.commit()  # used for save data to db
    except Exception as e:
        mysql.connection.rollback()
        return render_template(
            'admin/add-employee.html',
            error=f"Could not save employee. {e}",
            form=form,
        )
    finally:
        mycursor.close()  # connection close

    return render_template(
        'admin/add-employee-result.html',
        empid=empid,
        name=name,
        email=email,
        mobile=mobile,
        salary=salary,
        position=position,
    )

@app.route('/delete/<emp_id>' ,methods=['POST'])
def delete_employee(emp_id):
    mysql = mysql_configuration
    mycursor = mysql.connection.cursor()
    sqlQuery = "DELETE FROM employee_data WHERE empid = %s"
    id = emp_id
    mycursor.execute(sqlQuery, (id,))
    mysql.connection.commit()
    mycursor.close()
    return redirect('/show-employees')

# edit employee details
@app.route("/edit/<empid>")
def edit_employee(empid):
    mysql = mysql_configuration
    mycursor = mysql.connection.cursor()
    sqlQuery = "SELECT * FROM employee_data WHERE empid = %s"
    mycursor.execute(sqlQuery, (empid,))
    employee = mycursor.fetchone()
    mycursor.close()
    return render_template('admin/edit-employee.html', employee=employee)

# update form end point
@app.route("/update/<empid>", methods=['POST'])
def update_employee(empid):
    name = request.form.get('name')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    salary = request.form.get('salary')
    position = request.form.get('position')

    mysql = mysql_configuration
    mycursor = mysql.connection.cursor()
    sqlQuery = "UPDATE employee_data SET name=%s, email=%s, mobile=%s, salary=%s, position=%s WHERE empid=%s"
    values = (name, email, mobile, salary, position, empid)
    mycursor.execute(sqlQuery, values)
    mysql.connection.commit()
    mycursor.close()
    return redirect('/show-employees')

# exit update feature
@app.route('/profile-page')
def profile_page():
    return render_template('admin/profile.html')


 
if __name__ == '__main__':
    app.run(debug=True)
