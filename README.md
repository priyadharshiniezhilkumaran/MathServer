# Ex.03 Design a Website for Server Side Processing
## Date:11/11/2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
priya.html

<html>
    <head>
        <title>CHURN RATE CALCULATION</title>
    </head>
    <body bgcolor="lightblue">
        <h3 align="center">CHURN RATE CALCULATION</h3>
        <h5 align="center">Priyadharshini E (26013770)</h5>
        <form method="POST">
            {%csrf_token%}
            <label>Initial customer:<label>
            <input type="number" value="{{InitialCust}}" name="Initial_customer"><br><br>
            <label>present customer:</label>
            <input type="number" value="{{PresentCust}}" name="Present_customer"><br><br>
            <input type="submit" value="Calculate"><br><br>
            <label>Churn rate:</label>
            <input type="number" value="{{Churn}}"><br><br>
        </form>
    </body>
</html>

views.py

from django.shortcuts import render
def calcs_Churn(request):
    InitialCust = int(request.POST.get('Initial_customer', 0)) if request.method == 'POST' else ''
    PresentCust = int(request.POST.get('Present_customer', 0)) if request.method == 'POST' else ''
    Churn = (InitialCust/PresentCust)*100 if request.method == 'POST' else ''
    print("Initial customer =",InitialCust)
    print("Present customer =",PresentCust)
    print("Churn rate =",Churn)
    return render(request, 'myapp/priya.html',{'InitialCust': InitialCust, 'PresentCust': PresentCust, 'Churn': Churn})

utls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [path('', views.calcs_Churn, name='calcs_Churn'),]

```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (27).png>)


## OUTPUT - WEBPAGE:
![alt text](<Screenshot (26).png>)


## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
