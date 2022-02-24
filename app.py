#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == "POST":
        Age = request.form.get("Age")
        Loan = request.form.get("Loan")
        Income = request.form.get("Income")
        print(Age, Loan, Income)
        model1 = joblib.load("defaultXGBoost")
        pred = model1.predict([[float(Income), float(Age), float(Loan)]])
        if (str(pred) == "[0]"):
            prediction = "No"
        else:
            prediction = "Yes"
        s = "The predicted default is : " + prediction
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Cannot reach"))        


# In[ ]:


if __name__ =="__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




