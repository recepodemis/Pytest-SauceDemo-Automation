# Saucedemo Test Otomasyonu

Bu proje, [Saucedemo](https://www.saucedemo.com) sitesinde gerçekleştirilen bir dizi test otomasyonunu içermektedir. Proje, Python dili ve Selenium kütüphanesi kullanılarak geliştirilmiştir.

## Test Senaryoları

### 1. Ürünü Sepete Ekle ve Kontrol Et

Bu test senaryosu, kullanıcının sisteme başarılı bir şekilde giriş yaptıktan sonra bir ürünü sepete ekleyip, ardından bu ürünü sepette görüntüleyebildiğini kontrol eder.

    @pytest.mark.parametrize("username,password"[("standard_user","secret_sauce")])
	def test_checkToCard(self,username,password):
    # Test senaryosu kodu buraya gelecek

### 2. Ürünü Sepetten Kaldır ve Kontrol Et

Bu test senaryosu, kullanıcının sisteme başarılı bir şekilde giriş yaptıktan sonra bir ürünü sepete ekleyip, ardından bu ürünü sepette görüntüleyebildiğini, ürünü kaldırabildiğini ve alışverişe devam ederek ürünün sepette olmadığını kontrol eder.

    @pytest.mark.xfail
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_checkToCardRemoved(self,username,password):
        # Test senaryosu kodu buraya gelecek

### 3. Başarısız Giriş Kontrolü

Bu test senaryosu, sisteme yanlış kullanıcı adı ve şifre kombinasyonları ile giriş yapılamadığını kontrol eder.

    `@pytest.mark.parametrize("username,password",[("recepodemis","deneme"),("testrecep","secret_sauce"),("standard_user","test_password")])
    def test_failedLogin(self,username,password):
        # Test senaryosu kodu buraya gelecek`
## Çalıştırma

Projeyi çalıştırmak için terminal veya komut istemcisinde aşağıdaki komutu kullanabilirsiniz:

`pytest test_file.py` 

Bu komut, belirtilen test dosyasındaki tüm senaryoları çalıştıracaktır.
