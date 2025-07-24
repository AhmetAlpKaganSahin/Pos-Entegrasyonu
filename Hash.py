import hashlib
import base64

# Parametreler (dokümana göre, kendi verilerine göre güncelle)
CLIENT_CODE = "10738"
GUID = "0c13d406-873b-403b-9c09-a5766840d98c"
Taksit = "1"
Islem_Tutar = "100,00"
Toplam_Tutar = "100,00"
Siparis_ID = "TestsiparisId654654"

#Komple bir string elde etmek için
Islem_Guvenlik_Str = CLIENT_CODE + GUID + Taksit + Islem_Tutar + Toplam_Tutar + Siparis_ID


encoded_str = Islem_Guvenlik_Str.encode('ISO-8859-9')

sha1_hash = hashlib.sha1(encoded_str).digest()

Islem_Hash = base64.b64encode(sha1_hash).decode('utf-8')

print("Islem_Hash:", Islem_Hash)