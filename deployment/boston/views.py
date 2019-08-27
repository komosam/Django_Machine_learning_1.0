from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from boston.forms import VariableForm
import pickle 
import numpy as np


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    def prediction(self,inputs):
        model_file = staticfiles_storage.path('boston.pkl')
        with open(model_file, 'rb') as fid:
            lin_model = pickle.load(fid)
        predictions = lin_model.predict(inputs)
        return predictions
    
    def get(self,request):
        form=VariableForm()
        return render(request,self.template_name, {'form':form})
    
    
    def post(self,request):
        form=VariableForm(request.POST)
        if form.is_valid():
            #crim = form.cleaned_data['CRIM']
            variables = [i for i in form.cleaned_data.values()]
            variables = np.array(variables).astype('float').reshape(1,-1)
            pred = self.prediction(variables)
            pred = pred.item()
            #pred = 1000

        args = {'form':form,'predictions':pred}
        return render(request,self.template_name,args)