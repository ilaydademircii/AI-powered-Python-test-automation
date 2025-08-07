'''
Created on 2 Ağu 2024

@author: zehra
'''
import unittest
import io
import subprocess
import re

class RunResponseClass:

    def __init__(self, output_dosya_yolu):
        self.output_dosya_yolu = output_dosya_yolu

    def calistir(self):
        try:
            
            # Yazma işleminden sonra başka bir Python dosyasını çalıştır
            print("Yazma işleminden sonra  Python dosyasını çalıştır")
            result = subprocess.run(['python', self.output_dosya_yolu], capture_output=True, text=True)
            
            print("# Çıktıyı yazdır")
            # Çıktıyı yazdır
            print("Çıktı:")
            print(result.stdout)
            
            print("Hata varsa hata mesajını yazdır")
            # Hata varsa hata mesajını yazdır
            if result.stderr:
                print("Hata:")
                print(result.stderr)
            
            stdout = result.stdout
            stderr = result.stderr
            
            # Extract the class name dynamically from the file
            with open(self.output_dosya_yolu, 'r', encoding='utf-8') as file:
                content = file.read()
                class_name_match = re.search(r'class\s+(\w+)\s*\(.*\):', content)
                
                if not class_name_match:
                    return "Test sınıfı bulunamadı."
                
                class_name = class_name_match.group(1)
            
            output = io.StringIO()
            test_loader = unittest.TestLoader()
            test_suite = test_loader.loadTestsFromName(class_name, globals())
            runner = unittest.TextTestRunner(stream=output, verbosity=2)
            runner.run(test_suite)

            unittest_output = output.getvalue()

            final_output = stdout + unittest_output
            if stderr:
                final_output += "\nHata:\n" + stderr

            return final_output
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")
            return str(e)

