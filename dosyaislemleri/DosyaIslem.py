'''
Created on 31 Tem 2024

@author: zehra
'''


# DosyaIslemleri sınıfını kullanarak dosya okuma ve yazma işlemleri yapın
class DosyaIslemleri:

    def __init__(self, input_dosya_yolu, output_dosya_yolu):
        self.input_dosya_yolu = input_dosya_yolu
        self.output_dosya_yolu = output_dosya_yolu

    def dosya_oku(self):
        try:
            with open(self.input_dosya_yolu, 'r', encoding='utf-8') as inputdosya:
                return inputdosya.read()
        except FileNotFoundError:
            return "Input dosyası bulunamadı."
        except Exception as e:
            return f"Dosya okuma hatası: {e}"

    def dosya_kontrol(self):
        try:
            with open(self.output_dosya_yolu, 'r', encoding='utf-8') as inputdosya:
                return inputdosya.read()
        except FileNotFoundError:
            return "Input dosyası bulunamadı."
        except Exception as e:
            return f"Dosya okuma hatası: {e}"

    def dosya_yaz(self, veri):
        try:
            with open(self.output_dosya_yolu, 'w', encoding='utf-8') as outputdosya:
                outputdosya.write(veri)
            return "Dosya başarıyla yazıldı."
        except Exception as e:
            return f"Dosya yazma hatası: {e}"

