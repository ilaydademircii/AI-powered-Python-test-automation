'''
Created on 2 Ağu 2024

@author: zehra
'''
import openai
from dosyaislemleri import DosyaIslem


class OpenAIIslemleri:

    def __init__(self, api_key, input_dosya_yolu, output_dosya_yolu):
        self.dosya_islemleri = DosyaIslem.DosyaIslemleri(input_dosya_yolu, output_dosya_yolu)
        self.output_dosya_yolu = output_dosya_yolu
        self.input_dosya_yolu = input_dosya_yolu
        self.endpoint_url = "https://api.openai.com/v1/chat/completions"
        openai.api_key = api_key
        
    def openai_cevapla(self):
        try:
            print("Dosya okuma işlemi başlatıldı.")
            veri = self.dosya_islemleri.dosya_oku()
            print(f"Dosya okuma başarılı. Okunan veri:\n{veri}")

            print("OpenAI ChatCompletion API'sini kullanarak cevap alın")
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                   
                    {"role": "system", "content": "Sen bir yazılım testi geliştiricisisin. Sana gönderilen mesajda test edeceğin kod bulunmakta. Bununla ilgili gerçek bir yazılım testi yazmalısın.  Fakat verdiğin cevapta AÇIKLAMA YAPMADAN DİREKT KODU VER. YAZACAĞIN CEVAPTA KOD DIŞINDA HİÇBİR ŞEY SÖYLEME. PYTHON ETİKETİ(```python) DE BULUNMASIN. SADECE KOD. Verdiğin METİN, komple bir .py dosyasına yapıştırılıp direkt çalıştırılabilir halde olsun. herhangi bir etiket veya kod olmayan bir satır olmasın. Yazacaksan da yorum satırı olarak yaz. Test sonucu gerçek test çıktısı gibi olsun. Test sonucu print olarak yazdırılsın. YAZACAĞIN CEVAPTA KOD DIŞINDA HİÇBİR ŞEY SÖYLEME. Kodun çıktısı bu şekilde olsun ------- Ran 1 test in 0.000s. Verilen dosya yolunda testler sınıfı paketin adı oluyor. from testler import.. py dosyasının adını koyacaksın"},
                    {"role": "user", "content": "Dosya yolu: " + self.input_dosya_yolu + veri}
                ]
            )

            try:
                
                cevap = response.choices[0].message['content'].strip()
                print(f"API cevabı başarıyla alındı. Alınan cevap:\n{cevap}")
                
            except openai.error.APIConnectionError as api_error:
                print(f"API bağlantı hatası: {api_error}")
            except openai.error.RateLimitError as limit_error:
                print(f"API çağrı limiti aşıldı: {limit_error}")

            # Veriyi başka bir dosyaya yazın
            print("Veriyi başka bir dosyaya yazın")
            yazma_sonucu = self.dosya_islemleri.dosya_yaz(cevap)
            print(yazma_sonucu)
            
            kontrol = self.dosya_islemleri.dosya_kontrol()
            print("Dosya kontrolü tamamlandı, içerik:")
            print(kontrol)
            
        except Exception as e:
            print(f"API çağrısı sırasında bir hata oluştu: {e}")
