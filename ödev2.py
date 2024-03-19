def is_harf(character):
    """
    Belirli bir karakterin bir harf olup olmadığını kontrol eder.
    """
    if character.isalpha():
        return True
    else:
        return False

def kucuk_harf(character):
    """
    Belirli bir karakteri küçük harfe çevirir.
    """
    return character.lower()

def harf_sikliklari(metin):
    """
    Bir metinde harflerin kullanım sıklığını yüzdelik oranını hesaplar.
    """
    harf_sayaci = {}
    toplam_harf = 0
    for harf in metin:
        if is_harf(harf):
            harf = kucuk_harf(harf)  # Harfi küçük harfe çevir
            harf_sayaci[harf] = harf_sayaci.get(harf, 0) + 1
            toplam_harf += 1
    harf_sikliklari = {harf: (sayi / toplam_harf) * 100 for harf, sayi in harf_sayaci.items()}
    return toplam_harf, harf_sayaci, harf_sikliklari

def bilgi_ver():
    """
    Modülü kullanan kişiye bilgi verir.
    """
    print("Abdulkadir Canlı")
    print("211213001")
    print("Dünyaya vermek istediği not: 'Bilgi paylaştıkça çoğalır.'")


# Örnek kullanım
if __name__ == "__main__":
    metin = input("Lütfen bir metin girin: ")
    toplam_harf, harf_sayaci, metin_harf_sikliklari = harf_sikliklari(metin)

    print("Metnin tamami için harf sikliklari:")
    for harf, oran in metin_harf_sikliklari.items():
        print(f"{harf}: {oran:.2f}% ({harf_sayaci[harf]} adet)")
    print("\nToplam harf sayisi:", toplam_harf)

bilgi_ver()