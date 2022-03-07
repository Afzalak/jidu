#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def xyz():
    return render_template("xyz.html")
@app.route("/userdetail",methods=["GET","POST"])
def xy():
    if(request.method=="POST"):
        Name=request.form["a"]
        Email=request.form["b"]
        Gender=request.form["gen"]
        Curry=request.form["food1"]
        quantity1=request.form["quantity1"]
        Chapati=request.form["food2"]
        quantity2=request.form["quantity2"]
        print("Name:",Name)
        print("Email:",Email)
        print("Gender:",Gender)
        print("Curry=",Curry)
        print("quantity1=",quantity1)
        print("Chapati=",Chapati)
        print("quantity2=",quantity2)
        total=int(Curry)*int(quantity1)+int(Chapati)*int(quantity2)
        print("total=",total)
        import smtplib
        box=smtplib.SMTP_SSL("smtp.gmail.com",465)
        box.login("afzalkhanak000786@gmail.com","Afzal@1998")
        msg='Hi {} \n your total billing is {}'.format(Name,total)
        box.sendmail("afzalkhan000786@gmail.com",Email,msg)
        box.close()
        return render_template("xyz.html")
app.run()

