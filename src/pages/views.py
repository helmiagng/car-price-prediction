from django.shortcuts import render
from .form import PredictCarForm
from .models import PredictPrice
import pickle
import pandas as pd
# Create your views here.

def preprocessing_and_ml_model(df):
    cat_col=['fueltype','aspiration','carbody','drivewheel','enginelocation','enginetype',
                'fuelsystem']

    enc_filename='ml_model/ohe_car_prediction.sav'
    scaler_filename='ml_model/scaler_car_prediction.sav'
    model_filename='ml_model/car_price_predictor_best_model.sav'
    enc_load=pickle.load(open(enc_filename,'rb'))
    scaler_load=pickle.load(open(scaler_filename,'rb'))
    model_load=pickle.load(open(model_filename,'rb'))
                
    ohe_df=pd.DataFrame(enc_load.transform(df[cat_col]).toarray())
    df=df.join(ohe_df)
    df.drop(columns=cat_col,inplace=True)
    
    df['cylindernumber']=pd.to_numeric(df['cylindernumber'],errors='coerce')

    if df['wheelbase'][0] < 95.7:
        df['wheelbase'] = 1
        
    elif df['wheelbase'][0]> 95.7 and df['wheelbase'][0] < 99.367:
        df['wheelbase'] = 2
    else:
        df['wheelbase'] = 3

    if  df['stroke'][0] < 3.153:
        df['stroke'] = 1
        
    elif df['stroke'][0]> 3.153 and df['stroke'][0] < 3.39:
        df['stroke'] = 2
    else:
        df['stroke'] = 3
        
        
    if  df['horsepower'][0] < 69.0:
        df['horsepower'] = 1
        
    elif df['horsepower'][0]> 69.0 and df['horsepower'][0] < 97.0:
        df['horsepower'] = 2
        
    elif df['horsepower'][0]> 97.0 and df['horsepower'][0] < 123.0:
        df['horsepower']= 3
        
    else:
        df['horsepower'] = 4

    df['citympg'] = df['citympg']//10
    print(df)
    df=scaler_load.transform(df)
    
    pred=model_load.predict(df)

    return pred[0]
    
def home_view(request):
    
    my_form=PredictCarForm()
    pred_price=PredictPrice()
    car_price_prediction=0
    if request.method=='POST':
        my_form=PredictCarForm(request.POST)
        if my_form.is_valid():
            
            #now data is good
            data_dict=my_form.cleaned_data
            #print(my_form.cleaned_data)
            PredictPrice.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
            
        
        #my_form=PredictCarForm()
        
            
        data_list=[[data_dict['fuel_types'],data_dict['aspiration'],data_dict['doornumber'],
                        data_dict['carbody'],data_dict['drivewheel'],
                        data_dict['enginelocation'],data_dict['wheelbase'],data_dict['carlength'],
                        data_dict['carwidth'],data_dict['carheight'],data_dict['curbweight'],
                        data_dict['enginetype'],data_dict['cylindernumber'],data_dict['enginesize'],
                        data_dict['fuelsystem'],data_dict['boreratio'],
                        data_dict['stroke'],data_dict['compressionratio'],data_dict['horsepower'],
                        data_dict['peakrpm'],data_dict['citympg'],data_dict['highwaympg']]]
            
        col=['fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel',
            'enginelocation', 'wheelbase', 'carlength', 'carwidth', 'carheight',
            'curbweight', 'enginetype', 'cylindernumber', 'enginesize',
            'fuelsystem', 'boreratio', 'stroke', 'compressionratio', 'horsepower',
            'peakrpm', 'citympg', 'highwaympg']
                
        df=pd.DataFrame(data=data_list,columns=col)
        
        car_price_prediction=preprocessing_and_ml_model(df)
        
        #print(car_price_prediction)
        #my_form=PredictCarForm()
    context={
            "form":my_form,
            "pred_price":car_price_prediction
                
            }
    return render(request,"home.html",context)