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

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

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
    return render_template('admin/search-employee.html')

@app.route('/add-employee-save', methods=['POST'])
def add_employee_save():
    # This is a placeholder for processing the add employee form submission.
    # In a real application, you would validate and save the data here.
    empid = request.form.get('emp_id')
    name = request.form.get('full_name')
    email = request.form.get('email')
    mobile = request.form.get('phone')
    salary = request.form.get('salary')
    position = request.form.get('position')
    
    mysql = mysql_configuration
    mycursor = mysql.connection.cursor() # connection with db by cursor obj 

    # insert employee data into the database
    sql = "INSERT INTO employee_data(empid,name, email,mobile, salary, position) VALUES (%s, %s, %s, %s, %s, %s)"

    values = (empid, name, email, mobile, salary, position)

    mycursor.execute(sql, values) # query specification 

    mysql.connection.commit() # used for save data to db
    mycursor.close() # connection closs


    return render_template('admin/add-employee-result.html', empid=empid, name=name, email=email, mobile=mobile, salary=salary, position=position)

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
@app.route('/profile-page')
def profile_page():
    return render_template('admin/profile.html')


 
if __name__ == '__main__':
    app.run(debug=True)