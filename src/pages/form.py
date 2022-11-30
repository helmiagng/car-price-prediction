from django import forms
from .models import PredictPrice

class PredictCarForm(forms.Form):     
     
    FUEL_TYPES_OPTION=(
        ("diesel","diesel"),
        ("gas","gas"),
    ) 
     
    ASPIRATION_OPTION=(
        ("std","std"),
        ("turbo","turbo"),
    )

    CARBODY_OPTION=(
        ("sedan","sedan"),
        ("wagon","wagon"),
        ("hatchback","hatchback"),
        ("hardtop","hardtop"),
        ("convertible","convertible"),
    )

    DRIVEWHEEL_OPTION=(
        ("rwd","rwd"),
        ("rwd","rwd"),
        ("4wd","4wd"),
    )

    ENGINE_LOCATION_OPTION=(
        ("front","front"),
        ("rear","rear"),

    )

    ENGINE_TYPE_OPTION=(
        ("ohc","ohc"),
        ("l","l"),
        ("ohcf","ohcf"),
        ("dohc","dohc"),
        ("rotor","rotor"),
        ("ohcv","ohcv"),
        ("dohcv","dohcv"),
    )

    FUEL_SYSTEM_OPTION=(
        ("idi","idi"),
        ("mpfi","mpfi"),
        ("2bbl","2bbl"),
        ("1bbl","1bbl"),
        ("mfi","mfi"),
        ("4bbl","4bbl"),
        ("spdi","spdi"),
        ("spfi","spfi"),
    )

    CYLINDER_NUMBER_OPTION=(
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("8","8"),
        ("12","12"),
    )

    fuel_types         = forms.ChoiceField(required=True,choices=FUEL_TYPES_OPTION,label='Fuel type')
    aspiration         = forms.ChoiceField(required=True,choices=ASPIRATION_OPTION,label='Aspiration')
    carbody            = forms.ChoiceField(required=True,choices=CARBODY_OPTION,label='Car body')
    drivewheel         = forms.ChoiceField(required=True,choices=DRIVEWHEEL_OPTION,label='Drivewheel')
    enginelocation     = forms.ChoiceField(required=True,choices=ENGINE_LOCATION_OPTION,label='Engine location')
    enginetype         = forms.ChoiceField(required=True,choices=ENGINE_TYPE_OPTION,label='Engine type')
    fuelsystem         = forms.ChoiceField(required=True,choices=FUEL_SYSTEM_OPTION,label='Fuel system')                                         
   
    car_type           = forms.CharField(required= True,
                                         label='Car Type',
                                         widget=forms.TextInput(attrs={
                                            "placeholder":"Enter car type"
                                                                    }))



    doornumber         = forms.IntegerField(required=True,label='Door Number',
                                            widget=forms.TextInput(attrs={
                                                                      "placeholder": "How many door you have in your car?"
                                                                    }))
    wheelbase          = forms.FloatField(required=True,label='Wheel Base',
                                            widget=forms.TextInput(attrs={
                                                                      "placeholder":"Enter wheel base"
                                                                    }))
    carlength          = forms.FloatField(required=True,label='Car Length',
                                            widget=forms.TextInput(attrs={
                                                                      "placeholder":"Enter car length"
                                                                    }))
    carwidth           = forms.FloatField(required=True,label='Car Width',
                                            widget=forms.TextInput(attrs={
                                                                      "placeholder":"Enter car width"
                                                                    }))
    carheight           = forms.FloatField(required=True,label='Car Height',
                                            widget=forms.TextInput(attrs={
                                                                      "placeholder":"Enter car height"
                                                                    }))
    curbweight         = forms.IntegerField(required=True,label='Curb Weight',
                                            widget=forms.TextInput(attrs={
                                                                        "placeholder":"enter curb weight"
                                                                     }))
    cylindernumber     = forms.ChoiceField(required=True,choices=CYLINDER_NUMBER_OPTION,label='Cylinder Number')
    enginesize         = forms.IntegerField(required=True,label='Engine Size',
                                            widget=forms.TextInput(attrs={
                                                                        "placeholder":"Enter engine size"
                                            }))
    boreratio          = forms.FloatField(required=True,label='Bore ratio',
                                            widget=forms.TextInput(attrs={
                                                                      "placeholder":"Enter bore ratio"
                                                                    }))
    stroke             = forms.FloatField(required=True,label='Stroke',
                                            widget=forms.TextInput(attrs={
                                                                      "placeholder":"Enter stroke"
                                                                    }))
    compressionratio   = forms.FloatField(required=True,label='Compression ratio',
                                            widget=forms.TextInput(attrs={
                                                                      "placeholder":"Enter compression ratio"
                                                                    }))
    horsepower         = forms.IntegerField(required=True,label='Horsepower',
                                            widget=forms.TextInput(attrs={
                                                "placeholder":"Enter horsepower"
                                            }))     
    peakrpm          = forms.IntegerField(required=True,label='Peak RPM',widget=forms.TextInput(attrs={
                                                "placeholder":"Enter peak rpm"
                                            }))                                 
    citympg            = forms.IntegerField(required=True,label='City MPG',widget=forms.TextInput(attrs={
                                                "placeholder":"Enter city mpg"
                                            }))              
    highwaympg          = forms.IntegerField(required=True,label='Highway MPG',widget=forms.TextInput(attrs={
                                                "placeholder":"Enter highwaympg"
                                            }))                                               
    class Meta:
        model=PredictPrice
        fields=[
            'fuel_types',
            'aspiration',
            'carbody',
            'drivewheel',
            'enginelocation',
            'enginetype',
            'fuelsystem',
            'cartype',
            'doornumber',
            'carlength',
            'wheelbase',
            'carlength',
            'carwidth',
            'carheight',
            'curbweight',
            'cylindernumber',
            'enginesize',
            'boreratio',
            'stroke',
            'compressionratio',
            'horsepower',
            'citympg',
            'highwaympg'
        ]
    