from flask import Flask,render_template,request,jsonify,redirect,url_for
app = Flask(__name__) 

@app.route('/')
def hello():
   return redirect(url_for('login'))
   
@app.route('/login') 
def login(): 
   return render_template("login.html")
   
  
@app.route('/message',methods = ['POST']) 
def message():
   name=request.form.get("name")
   pw=request.form.get("password")
   d={}
   
   def validateString(s):
    letter_flag = False
    number_flag = False
    for i in s:
        if i.isalpha():
            letter_flag = True
        if i.isdigit():
            number_flag = True
    return letter_flag and number_flag 
    
   if(len(pw)<6):
      d={"status": 201,"msg": "Failure: password should be of length 6"}
   elif(not(validateString(pw))):
      d={"status": 202,"msg": "Failure: password to have 1 character and 1 number"} 
   elif(not(name.isalpha())):
      d={"status": 203,"msg": "Failure: only characters allowed in username"}  
   else:
      d={"status": 200,"msg": "Success"}
   
   return jsonify(d)
    
    
  
if __name__ == '__main__': 
   app.run(debug = True) 