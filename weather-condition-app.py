import requests#api'den veri çekmek için kütüphane

print("Sistemimize Hoşgeldiniz")

apikey = "ENTER_YOUR_API_KEY"

sorgulanansehirler = []

def menu():
    print("1-Şehir İsmiyle Hava Durumu Sorgula")
    print("2-Sorgulanan Şehirleri Yazdır")
    print("3-Çıkış Yap")


def havadurumual(sehir):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={apikey}&units=metric&lang=tr")
    #request.get ile api'dan veriyi çekiyoruz ve f {sehir} ile url'e sehir girdisini ekliyoruz
    #bu sayede sehir ismine gore hava durumu geliyor

    data = response.json() #response.json ile json gelen veri python sözlüğüne çevriliyor

    if response.status_code == 200:#200 kodu başarılı yanıt demek
        havadurumu = {
            "Şehir": sehir,
            "Hava Durumu": data['weather'][0]['description'],#openweathermap'in json data isimleri
            "Sıcaklık": data['main']['temp'],
            "Nem Oranı": data['main']['humidity']
            
        }
        sorgulanansehirler.append(sehir)
        return havadurumu
    
    elif response.status_code == 404:#404 bulunamadı kodu
        return ("Hata: Lütfen şehrin ismini doğru yazınız.")
    else:
        return (f"Hata kodu: {response.status_code}")


def sorgulanansehirleri_yazdir():
        print("Sorgulanan Şehirler:")
        print(sorgulanansehirler)

while True:
        menu()
        secim = input("Yapmak istediğiniz işlemin numarasını yazın: ")

        if secim == "1":
            sehir = input("Hava durumunu görmek istediğiniz şehri giriniz: ")
            havadurumu = havadurumual(sehir)
            print(havadurumu)
 
        elif secim == "2":
            sorgulanansehirleri_yazdir()

        elif secim == "3":
            print("Programdan çıkış yaptınız")
            break

        else:
            print("Geçersiz seçim yaptınız.")
