from django.shortcuts import render
def calcs_Churn(request):
    InitialCust = int(request.POST.get('Initial_customer', 0)) if request.method == 'POST' else ''
    PresentCust = int(request.POST.get('Present_customer', 0)) if request.method == 'POST' else ''
    Churn = (InitialCust/PresentCust)*100 if request.method == 'POST' else ''
    print("Initial customer =",InitialCust)
    print("Present customer =",PresentCust)
    print("Churn rate =",Churn)
    return render(request, 'myapp/priya.html',{'InitialCust': InitialCust, 'PresentCust': PresentCust, 'Churn': Churn})