import requests

url = "https://testposws.param.com.tr/turkpos.ws/service_turkpos_prod.asmx"


xml_data = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <TP_WMD_UCD xmlns="https://turkpos.com.tr/">
      <G>
        <CLIENT_CODE>10738</CLIENT_CODE>
        <CLIENT_USERNAME>Test</CLIENT_USERNAME>
        <CLIENT_PASSWORD>Test</CLIENT_PASSWORD>
      </G>
      <GUID>0c13d406-873b-403b-9c09-a5766840d98c</GUID>
      <KK_Sahibi>test</KK_Sahibi>
      <KK_No>4546711234567894</KK_No>
      <KK_SK_Ay>12</KK_SK_Ay>
      <KK_SK_Yil>2026</KK_SK_Yil>
      <KK_CVC>000</KK_CVC>
      <KK_Sahibi_GSM>5551231212</KK_Sahibi_GSM>
      <Hata_URL>https://dev.param.com.tr/en</Hata_URL>
      <Basarili_URL>https://dev.param.com.tr/tr</Basarili_URL>
      <Siparis_ID>TestsiparisId654654</Siparis_ID>
      <Siparis_Aciklama>a</Siparis_Aciklama>
      <Taksit>1</Taksit>
      <Islem_Tutar>100,00</Islem_Tutar>
      <Toplam_Tutar>100,00</Toplam_Tutar>
      <Islem_Hash>pF3hqdSXpRyIuWtVd+4DrGhVxKk=</Islem_Hash>
      <Islem_Guvenlik_Tip>NS</Islem_Guvenlik_Tip>
      <Islem_ID>654654</Islem_ID>
      <IPAdr>127.0.0.1</IPAdr>
      <Ref_URL>https://dev.param.com.tr/tr</Ref_URL>
      <Data1>a</Data1>
      <Data2>a</Data2>
      <Data3>a</Data3>
      <Data4>a</Data4>
      <Data5>a</Data5>
    </TP_WMD_UCD>
  </soap:Body>
</soap:Envelope>
"""

headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "https://turkpos.com.tr/TP_WMD_UCD"
}
# POST isteği gönder
response = requests.post(url, data=xml_data.encode("utf-8"), headers=headers)

print("Status Code:", response.status_code)
print("Gelen XML:", response.text)