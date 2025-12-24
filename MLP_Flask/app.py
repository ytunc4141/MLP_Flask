from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

cpu_labels = {
    1: "Giriş Seviye (i3 / Ryzen 3)",
    2: "Orta Seviye (i5 / Ryzen 5)",
    3: "Yüksek Seviye (i7 / Ryzen 7)",
    4: "Ultra Seviye (i9 / Ryzen 9)"
}

gpu_labels = {
    1: "Giriş (GTX 1650 vb.)",
    2: "Orta-Giriş (RTX 3050 / RX 6600)",
    3: "Orta (RTX 3060 / 4060)",
    4: "Yüksek (RTX 4070 / 3080)",
    5: "Ultra (RTX 4080 / 4090)"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:

        marka_val = int(request.form['Marka'])
        islemci_val = int(request.form['Islemci_Model'])
        ram = float(request.form['RAM_GB'])
        ssd = float(request.form['SSD_GB'])
        gpu_val = int(request.form['Ekran_Karti'])
        vram = float(request.form['VRAM_GB'])


        features = np.array([[marka_val, islemci_val, ram, ssd, gpu_val, vram]])
        prediction = model.predict(features)
        fiyat = int(prediction[0])

        if fiyat < 20000:
            fiyat = 20000 + abs(fiyat) % 5000

        marka_txt = "Intel" if marka_val == 1 else "AMD"
        islemci_txt = cpu_labels.get(islemci_val, "Bilinmiyor")
        gpu_txt = gpu_labels.get(gpu_val, "Bilinmiyor")

        return render_template('index.html', 
                               prediction_text=f'{fiyat}',
                               details={
                                   'marka': marka_txt,
                                   'islemci': islemci_txt,
                                   'ram': int(ram),
                                   'ssd': int(ssd),
                                   'gpu': gpu_txt,
                                   'vram': int(vram)
                               })
    
    except Exception as e:
        return render_template('index.html', error_text=f'Hata: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)