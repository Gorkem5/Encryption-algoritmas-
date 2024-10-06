import tkinter as tk
from tkinter import messagebox, ttk

def turkish_caesar_cipher(text, shift, decrypt=False):
    """
    Türkçe karakter destekli Caesar şifreleme ve deşifreleme.

    Bu fonksiyon verilen metni belirli bir miktarda kaydırarak şifreler veya deşifre eder.
    Deşifre işlemi için 'decrypt' parametresi True olarak kullanılır.

    Parametreler:
        text (str): Şifrelenecek veya deşifrelenecek metin.
        shift (int): Her karakteri kaydırmak için kullanılan pozisyon sayısı.
        decrypt (bool): Metnin deşifre edilip edilmeyeceğini belirtir. (Varsayılan: False)

    Döndürür:
        str: Şifrelenmiş veya deşifrelenmiş metin.
    """
    # Türkçe karakterleri de içeren alfabeyi tanımlayın
    chars = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcdefghijklmnopqrstuvwxyzçşğıöü'
    result = []  # Sonuç metnini tutacak liste

    # Deşifre işlemi için kaydırma yönünü tersine çevir
    shift = -shift if decrypt else shift

    for char in text:
        # Eğer karakter alfabede varsa kaydır
        if char in chars:
            shifted_index = (chars.index(char) + shift) % len(chars)
            result.append(chars[shifted_index])
        else:
            # Alfabe dışında kalan karakterleri olduğu gibi ekle
            result.append(char)

    return ''.join(result)  # Listeyi birleştirerek metin olarak döndür

def xor_cipher(text, key, decrypt=False):
    """
    Basit bir XOR şifreleme ve çözme fonksiyonu.

    Bu fonksiyon verilen metne XOR işlemi uygulayarak şifreler veya deşifre eder.

    Parametreler:
        text (str): Şifrelenecek veya deşifrelenecek metin.
        key (int): XOR işlemi için anahtar.
        decrypt (bool): Kullanılmıyor, tutarlılık için dahil edilmiştir. (Varsayılan: False)

    Döndürür:
        str: Şifrelenmiş veya deşifrelenmiş metin.
    """
    result = [chr(ord(char) ^ key) for char in text]  # Her karakteri XOR işlemi uygulayıp listeye ekle
    return ''.join(result)  # Listeyi birleştirerek metin olarak döndür

def encrypt_text():
    """
    Girdi metninin seçilen şifreleme yöntemine göre şifrelenmesini sağlar.

    Bu fonksiyon girdi metnini, seçilen şifreleme yöntemini ve gerekli parametreleri
    (shift veya key) alır, şifreleme işlemini gerçekleştirir ve sonucu çıktı alanında gösterir.
    """
    text = input_text.get("1.0", tk.END).strip()  # Girdi metnini al
    method = method_selection.get()  # Seçilen yöntemi al
    encrypted_text = ''  # Şifrelenmiş metni tutacak değişken

    if method == "Caesar":
        shift = _retrieve_shift_value()  # Shift değerini al
        if shift is not None:
            encrypted_text = turkish_caesar_cipher(text, shift)  # Caesar şifrelemesi yap
        else:
            return  # Shift değeri geçersizse fonksiyondan çık
    elif method == "XOR":
        key = _retrieve_key_value()  # XOR anahtarını al
        if key is not None:
            encrypted_text = xor_cipher(text, key)  # XOR şifrelemesi yap
        else:
            return  # Anahtar değeri geçersizse fonksiyondan çık
    else:
        messagebox.showerror("Error", "Geçersiz şifreleme yöntemi seçildi.")  # Geçersiz bir yöntem seçildiyse hata göster
        return

    _display_output_text(encrypted_text)  # Şifrelenmiş metni çıktı alanında göster

def decrypt_text():
    """
    Şifrelenmiş metnin seçilen şifreleme yöntemine göre deşifrelenmesini sağlar.

    Bu fonksiyon şifrelenmiş metni, seçilen deşifreleme yöntemini ve gerekli parametreleri
    (shift veya key) alır, deşifreleme işlemini gerçekleştirir ve sonucu çıktı alanında gösterir.
    """
    text = output_text.get("1.0", tk.END).strip()  # Şifrelenmiş metni çıktı alanından al
    method = method_selection.get()  # Seçilen yöntemi al
    decrypted_text = ''  # Deşifre edilmiş metni tutacak değişken

    if method == "Caesar":
        shift = _retrieve_shift_value()  # Shift değerini al
        if shift is not None:
            decrypted_text = turkish_caesar_cipher(text, shift, decrypt=True)  # Caesar deşifrelemesi yap
        else:
            return  # Shift değeri geçersizse fonksiyondan çık
    elif method == "XOR":
        key = _retrieve_key_value()  # XOR anahtarını al
        if key is not None:
            decrypted_text = xor_cipher(text, key, decrypt=True)  # XOR deşifrelemesi yap
        else:
            return  # Anahtar değeri geçersizse fonksiyondan çık
    else:
        messagebox.showerror("Error", "Geçersiz deşifreleme yöntemi seçildi.")  # Geçersiz bir yöntem seçildiyse hata göster
        return

    _display_output_text(decrypted_text)  # Deşifre edilmiş metni çıktı alanında göster


def _retrieve_shift_value():
    """
    Kullanıcının girdiği shift değerini alır ve doğrular.

    Bu fonksiyon shift değerinin geçerli bir tamsayı olup olmadığını kontrol eder.
    Geçersiz ise bir hata mesajı gösterir.

    Döndürür:
        int: Geçerli ise shift değeri, değilse None.
    """
    try:
        return int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift değeri bir tamsayı olmalıdır.")
        return None

def _retrieve_key_value():
    """
    Kullanıcının girdiği XOR anahtarını alır ve doğrular.

    Bu fonksiyon anahtarın geçerli bir tamsayı olup olmadığını kontrol eder.
    Geçersiz ise bir hata mesajı gösterir.

    Döndürür:
        int: Geçerli ise anahtar değeri, değilse None.
    """
    try:
        return int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Anahtar değeri bir tamsayı olmalıdır.")
        return None

def _display_output_text(output_text_value):
    """
    Çıktı metin kutusunu günceller ve yeni metni ekler.

    Bu fonksiyon önce çıktı metin kutusunu temizler, ardından yeni metni ekler.

    Parametreler:
        output_text_value (str): Gösterilecek metin.
    """
    output_text.delete("1.0", tk.END)  # Eski çıktıyı temizle
    output_text.insert("1.0", output_text_value)  # Yeni çıktıyı ekle

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Şifreleme Aracı")  # Ana pencerenin başlığı

# Girdi metin kutusu için etiket oluştur ve pencereye ekle
tk.Label(root, text="Girdi Metni").pack()
# Kullanıcının metin girmesi için metin kutusu oluştur ve pencereye ekle
input_text = tk.Text(root, height=10, width=40)
input_text.pack()

# Şifreleme yöntemi seçimi için etiket oluştur ve pencereye ekle
tk.Label(root, text="Şifreleme Yöntemini Seçin").pack()
# Kullanıcının şifreleme yöntemini seçmesi için combobox oluştur
method_selection = ttk.Combobox(root, values=["Caesar", "XOR"])
method_selection.set("Caesar")  # Varsayılan değer olarak "Caesar" seçildi
method_selection.pack()

# Caesar şifrelemesi için kaydırma değeri girişi etiketi oluştur ve pencereye ekle
tk.Label(root, text="Shift (Caesar için)").pack()
# Kullanıcının kaydırma değerini girmesi için giriş kutusu oluştur ve pencereye ekle
shift_entry = tk.Entry(root)
shift_entry.pack()

# XOR şifrelemesi için anahtar girişi etiketi oluştur ve pencereye ekle
tk.Label(root, text="Key (XOR için)").pack()
# Kullanıcının XOR anahtarını girmesi için giriş kutusu oluştur ve pencereye ekle
key_entry = tk.Entry(root)
key_entry.pack()

# Çıktı metin kutusu için etiket oluştur ve pencereye ekle
tk.Label(root, text="Çıktı Metni").pack()
# Şifrelenmiş veya deşifre edilmiş metin için metin kutusu oluştur ve pencereye ekle
output_text = tk.Text(root, height=10, width=40)
output_text.pack()

# Şifreleme butonu oluştur ve pencereye ekle
encrypt_button = tk.Button(root, text="Şifrele", command=encrypt_text)
encrypt_button.pack()

# Deşifre butonu oluştur ve pencereye ekle
decrypt_button = tk.Button(root, text="Deşifrele", command=decrypt_text)
decrypt_button.pack()

# Tkinter ana döngüsünü başlat
root.mainloop()