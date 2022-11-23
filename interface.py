from flask import Flask ,render_template,jsonify,request
from project_data.utils import Bank
import config
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] ="root123"
app.config["MYSQL_DB"] = "Bank"
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")
    # return "We are in Flask"




def Initiate():
    return "Project Started"
    
@app.route("/pred",methods =['GET','POST'])
def get_predict():
    data = request.form 

    age       =  eval(data['age'])
    job       =  str(data['job'])       
    marital   =  str(data['marital'])          
    education =  str(data['education'])    
    default   =   str(data['default'])             
    housing   =  str(data['housing'])               
    loan      =   str(data['loan'])              
    contact   =   str(data['contact'])
    month     =     str(data['month'])
    day_of_week =     str(data['day_of_week'])
    duration   =       eval(data['duration'])
    campaign    =    eval(data['campaign'])
    pdays       =   eval(data['pdays'])
    previous    =      eval(data['previous'])
    poutcome    =    str(data['poutcome'])
    emp_var_rate  =     eval(data['emp_var_rate'])
    cons_price_idx  =    eval(data['cons_price_idx'])
    cons_conf_idx   =     eval(data['cons_conf_idx'])
    euribor3m       =     eval(data['euribor3m'])
    nr_employed     =   eval(data['nr_employed'])

    dt_model = Bank(age,job,marital,education,default,housing,loan,contact,month,day_of_week,duration,campaign,pdays,previous,poutcome,
                 emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m,nr_employed)


    r = dt_model.Bank_predict()

    if r==1:
        result="Yes, Your loan is approved"
    else:
        result="No,Your loan is declined"

    cursor = mysql.connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS loan_db(age VARCHAR(30),job VARCHAR(30),marital VARCHAR(30),education VARCHAR(30),default_ VARCHAR(30),housing VARCHAR(30),loan VARCHAR(30),contact VARCHAR(30),month_ VARCHAR(30),day_of_week VARCHAR(30),duration VARCHAR(30),campaign VARCHAR(30),pdays VARCHAR(30),previous VARCHAR(30),poutcome VARCHAR(30),emp_var_rate VARCHAR(30),cons_price_idx VARCHAR(30),cons_conf_idx VARCHAR(30),euribor3m VARCHAR(30),nr_employed VARCHAR(30),result VARCHAR(30))'
    cursor.execute(query)
    cursor.execute('INSERT INTO loan_db(age,job,marital,education,default_,housing,loan,contact,month_,day_of_week,duration,campaign,pdays,previous,poutcome,emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m,nr_employed,result)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(age,job,marital,education,default,housing,loan,contact,month,day_of_week,duration,campaign,pdays,previous,poutcome,emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m,nr_employed,result))

    mysql.connection.commit() 
    cursor.close()
    return render_template("index1.html",result=result)

    # return jsonify({'prediction':f"The elisibility of a customer :{result}"})
    
    




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)