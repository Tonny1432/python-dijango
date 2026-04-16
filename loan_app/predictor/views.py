from django.shortcuts import render
import pickle
import numpy as np
import os

# LOAD MODEL PROPERLY
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, 'train.pkl'), 'rb'))
encoders = pickle.load(open(os.path.join(BASE_DIR, 'encoders.pkl'), 'rb'))

# SAFE TRANSFORM (🔥 prevents crash)
def safe_transform(encoder, value):
    value = value.strip().lower()
    if value in encoder.classes_:
        return encoder.transform([value])[0]
    else:
        return 0  # fallback


def predict(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))

        job = request.POST.get('job')
        housing = request.POST.get('housing')
        personal = request.POST.get('personal')
        poutcome = request.POST.get('poutcome')
        camping = int(request.POST.get('camping'))

        # 🔥 SAFE ENCODING
        job_value = safe_transform(encoders['job'], job)
        housing_value = safe_transform(encoders['housing'], housing)
        personal_value = safe_transform(encoders['loan'], personal)
        poutcome_value = safe_transform(encoders['poutcome'], poutcome)

        data = np.array([[age, job_value, housing_value, personal_value, poutcome_value, camping]])

        pred = model.predict(data)

        if pred[0] == 1:
            result = "You are eligible for the loan"
        else:
            result = "You are not eligible for the loan"

        return render(request, "predictor/final.html", {"result": result})

    return render(request, "predictor/pre.html")