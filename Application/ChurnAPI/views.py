from django.shortcuts import render
from . forms import ChurnForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import churn
from . serializers import churnsSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


class ChurnsView(viewsets.ModelViewSet):
	queryset = churn.objects.all()
	serializer_class = churnsSerializers

def ohevalue(df):
    ohe_col=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/allcol.pkl")
    cat_columns=['Gender','Married','Education','Self_Employed','Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict={}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i]=df_processed[i].values
        else:
            newdict[i]=0
    newdf=pd.DataFrame(newdict)
    return newdf
		
#@api_view(["POST"])
def churnreject(request):
	try:
		mdl=joblib.load("I:/esprit/4DS/Projet/ML/Churn/ChurnAPI/lgbm_cc.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		scalers=joblib.load("I:/esprit/4DS/Projet/ML/Churn/ChurnAPI/scaler.pkl")
		X=scalers.transform(unit)
		y_pred=mdl .predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Churn', False:'No Churn'})
		return JsonResponse('Your Status is {}'.format(newdf), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    
def cxcontact(request):
    if request.method=='POST':
        form=ChurnForm(request.POST)
        if form.is_valid():
            Firstname = form.cleaned_data['firstname']
            Lastname = form.cleaned_data['lastname']
            gender=form.cleaned_data['lastname']
            seniorCitizen=form.cleaned_data['seniorCitizen']
            partner=form.cleaned_data['partner']
            dependents=form.cleaned_data['dependents']
            phoneService=form.cleaned_data['phoneService']
            multipleLines=form.cleaned_data['multipleLines']
            internetService=form.cleaned_data['internetService']    
            onlineSecurity=form.cleaned_data['onlineSecurity']
            onlineBackup=form.cleaned_data['onlineBackup']
            deviceProtection=form.cleaned_data['deviceProtection']
            techSupport=form.cleaned_data['techSupport']
            streamingTv=form.cleaned_data['streamingTv']
            streamingMovies=form.cleaned_data['streamingMovies']
            contract=form.cleaned_data['contract']
            paperlessBilling=form.cleaned_data['paperlessBilling']
            paymentMethod=form.cleaned_data['paymentMethod']
            monthlyCharges=form.cleaned_data['monthlyCharges']
            totalCharges=form.cleaned_data['totalCharges']
            tenureMonths=form.cleaned_data['tenureMonths']
            myDict = (request.POST).dict()
            df=pd.DataFrame(myDict, index=[0])
            answer=churnreject(ohevalue(df))[0]
            Xscalers=churnreject(ohevalue(df))[1]
            print(Xscalers)
            messages.success(request,'Application Status: {}'.format(answer))

    form=ChurnForm()

    return render(request, 'myform/cxform.html', {'form':form})