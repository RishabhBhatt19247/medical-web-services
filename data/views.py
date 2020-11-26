from django.shortcuts import render,HttpResponse
from data.models import Detail

# Create your views here.
def alldetail(request):
    if request.method=='POST':
        name= request.POST['name']
        age= request.POST['age']
        date= request.POST['date']
        time= request.POST['time']
        problem= request.POST['problem']
        place= request.POST['place']
        email= request.POST['email']
        detail= Detail(name=name,age=age,date=date,time=time,problem=problem,place=place,email=email)   
        detail.save()
        if problem=='Overweight and Obesity':
            doctor="Raju Pokhral(Overweight specialist)"
        elif problem=='Hiv/Aids':
            doctor="Samay Srivastava(Reseacher on Hiv vaccine)"
        elif problem=='Corona Virus':
            doctor="Vaibhava Trivedi(Researcher on corona vaccine )"
        elif problem=='Mental Health':
            doctor="Aadarsh Srivastava(Mental Health Specialist)"
        elif problem=='Injury':
            doctor="Faisal Khan(Surgeon)"  
        elif problem=='Heart Problems':
            doctor="Kaushal Tondon(Cardiac Specialist)"  
        elif problem=='Bones Problems':
            doctor="Divya Kumari(Bone Specialist)"
        elif problem=='Eye and ear Problems':
            doctor=="Mahira Khan(Eye and ear Specialist)"
        else:
            doctor="Unknown"  
        params={'NAME':name,'AGE':age,'DATE':date,'TIME':time,'PROBLEM':problem,'PLACE':place,'EMAIL':email,'DOCTOR':doctor}
        return render(request,'letter.html',params)  
    else:
        return HttpResponse("Technical error occur")
            