# **Selenium IDE Komutları**

Selenium IDE yazılım bilgisine sahip olmadan dahi web otomasyonu yapmamızı sağlayan bir IDE’ dir. Bu  IDE’ nin kullanımı oldukça basit olmasına rağmen gayet yeterli bir hizmet sunuyor. IDE’ yi kullanırken bir proje oluşturup ardından test dosyası oluşturarak otomasyona başlayabilirsiniz. Öncelikle gitmek istediğimiz sayfanın URL’ sini vererek kayıta başlayabiliriz. Kayıt gerçek manada sizin yaptığınız her işlemi tıklamanızı, bir şeyler yazmanızı, sürükle bırak yapmanızı gibi bir çok aksiyonu otomatik olarak arka planda kaydeder. Siz yapmak istediğiniz otomasyonu bir kere manuel yapıyorsunuz ve ardından IDE aynı işlemleri kaydederek otomasyonunu size çıktı olarak veriyor. Selenium IDE komutlar üzerinde çalışan bir ortamdır ve bunu kullanıcı kayıt ederken otomatik olarak kendisi bu komutları oluşturur. Ancak bizim de komut eklememize veya çıkarmamıza olanak sağlar. Aşağıda Selenium IDE’ de en çok kullanılan komutları bulabilirsiniz.

* **Open:** Belirtilen URL'yi mevcut tarayıcı penceresinde açar.
  **Click:** Web sayfasındaki belirtilen bir öğeye tıklar.
  **Type:** Metin alanına veya metin kutusuna metin yazar.
  **Select:** Bir açılır listeden bir seçenek seçer.
  **Assert:** Belirli bir koşulun doğru olup olmadığını kontrol eder ve doğru değilse yürütmeyi durdurur.
  **Verify:** Assert'e benzer, ancak koşul yanlışsa bile yürütmeye devam eder.
  **Wait:** Belirtilen bir süre boyunca veya belirli bir koşul gerçekleşene kadar yürütmeyi duraklatır.
  **Store:** Daha sonra kullanmak üzere bir değeri kaydeder.
  **Echo:** Bir mesajı log çıktısına yazar console a yazdırmakla aynı işlemdir.
  **Pause:** Kullanıcı devam ettikçe test yürütme işlemini duraklatır.
  **MouseOver:** Belirtilen bir öğenin üzerine fare işaretçisini hareket ettirir.
  **dragAndDrop:** Bir öğeyi bir konumdan alır ve başka bir konuma bırakır.
  **waitForElementVisible:** Belirtilen bir öğe sayfada görüne kadar bekler.
  **store Text:** Belirtilen bir öğenin metnini alır ve bir değişkende saklar.
  **clickAndWait:** Bir öğeye tıklar ve sonraki sayfanın yüklenmesini bekler.
  **store Value:** Bir form alanının değerini alır ve bir değişkende saklar.
  **gotoIf:** Belirli bir koşul doğruysa belirtilen bir etikete atlar.
  **store Attribute:** Bir öğenin belirtilen bir özelliğinin değerini alır ve bir değişkende saklar.
  **assert Text:** Belirtilen bir öğenin metninin beklenen değere eşit olup olmadığını kontrol eder.

Bunlar sadece birkaç örnek, ve Selenium IDE birçok farklı işlemi gerçekleştirmek için çeşitli komutları destekler. Selenium IDE sıklıkla kendini günceller bu yüzden kendi [dokümantasyon](https://www.selenium.dev/selenium-ide/docs/en/api/commands) sayfasından takip edebilirsiniz.
