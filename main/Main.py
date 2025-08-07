
import PySimpleGUI as sg
from runtheresponse import RunResponse
from openaiIslemleri import OpenAIIslem


class Main:

    api_key = "***************"
  
    testcode_column = [
        [sg.Text("Test edilecek dosyayı seçin:"), sg.InputText(key="input_dosya_yolu"), sg.FileBrowse("Gözat")],
        [sg.Button("Test Üret")],
        [sg.Text("Test Kodları:", size=(40, 1))],
        [sg.Multiline(size=(80, 10), key="output_test_kodu")],
        [sg.Button("Testi Çalıştır")],
    ]
    
    testresult_column = [
        [sg.Text("", size=(40, 1))],
        [sg.Text("Test Sonucu:", size=(40, 1))],
        [sg.Multiline(size=(80, 10), key="output_test_sonucu")],
    ]
    
    layout = [
        [
            sg.Column(testcode_column),
            sg.VSeparator(),
            sg.Column(testresult_column),
        ]
    ]
    
    window = sg.Window("Test Üretme ve Çalıştırma", layout)
    
    # Pencere olay döngüsü
    while True:
        event, values = window.read()
        input_dosya_yolu = values["input_dosya_yolu"]
        output_dosya_yolu = "C:/Users/zehra/demo/Calistir.py"  # Çıktı dosyası yolu
        if event == sg.WIN_CLOSED:  # Pencereyi kapatma
            break
    
        if event == "Test Üret":
            
            # OpenAIIslemleri sınıfını kullanarak işlemleri gerçekleştirin
            openai_islemleri = OpenAIIslem.OpenAIIslemleri(api_key, input_dosya_yolu, output_dosya_yolu)
            openai_islemleri.openai_cevapla()
            
            # Dosyayı çalıştır ve sonucu al
            run_response = RunResponse.RunResponseClass(output_dosya_yolu)
            test_sonucu = run_response.calistir()
    
            # Sonuçları GUI'ye yazdır
    
            with open(output_dosya_yolu, 'r', encoding='utf-8') as output_file:
    
                test_kodu = output_file.read()
    
                window["output_test_kodu"].update(test_kodu)
    
                window["output_test_sonucu"].update(test_sonucu)
    
                sg.popup("Test  tamamlandı!", title="Başarılı")      
    
        if event == "Testi Çalıştır":
            test_kodu = values["output_test_kodu"]
            
            try:
                with open(output_dosya_yolu, 'w', encoding='utf-8') as outputdosya:
                        outputdosya.write(test_kodu)
            except Exception as e:
                print(f"Dosya yazma hatası: {e}")
            
            run_response = RunResponse.RunResponseClass(output_dosya_yolu)
            test_sonucu = run_response.calistir()
    
            with open(output_dosya_yolu, 'r', encoding='utf-8') as output_file:
                test_kodu = output_file.read()
                window["output_test_kodu"].update(test_kodu)
                window["output_test_sonucu"].update(test_sonucu)
            sg.popup("Test tamamlandı!", title="Başarılı")
            
    # Pencereyi kapatma
    window.close()
