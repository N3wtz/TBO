import streamlit as st

#Rule Of CNF By Gagas Keren
R = {
    "K": [["S", "P"], ["P1", "O"], ["P1", "Pel"], ["P1", "Ket"], ["P1", "P2"], ["P1", "P3"], ["P1", "P4"]],
    "P1": [["S", "P"]],
    "P2": [["O", "Pel"]],
    "P3": [["O", "Ket"]],
    "P4": [["P2", "Ket"]],

    "S": [["Gagas"], ["Surya"], ["Alex"], ["Wahyu"], ["Budi"], ["Alicia"], ["Pradipta"], ["David"], ["Krisna"], ["John"], ["Putu"], ["Komodo"], ["Buaya"], ["Siti"], ["Dika"], ["Duta"], ["Adi"], ["Dwipa"], ["Alaya"], ["Nengah"],
          ["saya"], ["kamu"], ["dia"], ["mereka"],
          ["rumah"], ["pohon"], ["kucing"], ["meja"], ["mobil"], ["perpustakaan"], ["polisi"], ["ayah"], ["dokter"], ["guru"], ["anjing"], ["petani"], ["pasien"], ["pelangi"], ["bola"], ["nasi"], ["buku"], ["desain"], ["murid"], ["lukisan"], ["koran"], ["mie"], ["penjahat"], ["padi"], ["komputer"], ["buku"], ["motor"], ["penyanyi"], ["kuda"], ["lagu"], ["ikan"], ["soto"], ["batu"], ["dapur"], ["pasar"], ["taman"], ["sekolah"], ["lapangan"], ["pertigaan"], ["sawah"], ["mawar"], ["kebanggaan"], ["pemandangan"], ["kesegaran"], ["pikiran"], ["penenang"], ["dunia"], ["orang tua"], ["suasana"], ["romantis"], ["hutan"], ["cita-cita"], ["kesuksesan"], ["pendorong"], ["kesabaran"], ["kunci"], ["keberhasilan"], ["cinta"], ["selalu"], ["abadi"], ["hewan"], ["kucing itu"], ["peliharaan"], ["idola"], ["keluarga"], ["mobil baru itu"], ["kendaraan"], ["listrik"],
          ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"]],
    "P": [["makan"], ["berbicara"], ["main"], ["minum"], ["tidur"], ["berlari"], ["melompat"], ["menulis"], ["membaca"], ["memakan"], ["memasak"], ["menggigit"], ["melompati"], ["bermain"], ["memiliki"], ["menangkap"], ["pergi"], ["memukul"], ["menendang"], ["merawat"], ["mengajar"], ["mengejar"], ["menggambar"], ["berlari"], ["menanam"], ["menjual"], ["menyukai"], ["membeli"], ["dikejar"], ["menunggu"], ["mengendarai"], ["melukis"], ["digigit"], ["menyanyikan"], ["memancing"], ["menabrak"], ["adalah"], ["akan"] ,["idola"], ["kendaraan"], ["hewan"],
          ["Verb", "NP"]],
    "O": [["Gagas"], ["Surya"], ["Alex"], ["Wahyu"], ["Budi"], ["Alicia"], ["Pradipta"], ["David"], ["Krisna"], ["John"], ["Putu"], ["Komodo"], ["Buaya"], ["Siti"], ["Dika"], ["Duta"], ["Adi"], ["Dwipa"], ["Alaya"], ["Nengah"],
          ["saya"], ["kamu"], ["dia"], ["mereka"],
          ["rumah"], ["pohon"], ["kucing"], ["meja"], ["mobil"], ["perpustakaan"], ["polisi"], ["ayah"], ["dokter"], ["guru"], ["anjing"], ["petani"], ["pasien"], ["pelangi"], ["bola"], ["nasi"], ["buku"], ["desain"], ["murid"], ["lukisan"], ["koran"], ["mie"], ["penjahat"], ["padi"], ["komputer"], ["buku"], ["motor"], ["penyanyi"], ["kuda"], ["lagu"], ["ikan"], ["soto"], ["batu"], ["dapur"], ["pasar"], ["taman"], ["sekolah"], ["lapangan"], ["pertigaan"], ["sawah"], ["mawar"], ["kebanggaan"], ["pemandangan"], ["kesegaran"], ["pikiran"], ["penenang"], ["dunia"], ["orang tua"], ["suasana"], ["romantis"], ["hutan"], ["cita-cita"], ["kesuksesan"], ["pendorong"], ["kesabaran"], ["kunci"], ["keberhasilan"], ["cinta"], ["selalu"], ["abadi"], ["hewan"], ["kucing itu"], ["peliharaan"], ["idola"], ["keluarga"], ["mobil baru itu"], ["kendaraan"], ["listrik"],
          ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"]],
    "Pel": [["Gagas"], ["Surya"], ["Alex"], ["Wahyu"], ["Budi"], ["Alicia"], ["Pradipta"], ["David"], ["Krisna"], ["John"], ["Putu"], ["Komodo"], ["Buaya"], ["Siti"], ["Dika"], ["Duta"], ["Adi"], ["Dwipa"], ["Alaya"], ["Nengah"],
            ["saya"], ["kamu"], ["dia"], ["mereka"],
            ["rumah"], ["pohon"], ["kucing"], ["meja"], ["mobil"], ["perpustakaan"], ["polisi"], ["ayah"], ["dokter"], ["guru"], ["anjing"], ["petani"], ["pasien"], ["pelangi"], ["bola"], ["nasi"], ["buku"], ["desain"], ["murid"], ["lukisan"], ["koran"], ["mie"], ["penjahat"], ["padi"], ["komputer"], ["buku"], ["motor"], ["penyanyi"], ["kuda"], ["lagu"], ["ikan"], ["soto"], ["batu"], ["dapur"], ["pasar"], ["taman"], ["sekolah"], ["lapangan"], ["pertigaan"], ["sawah"], ["mawar"], ["kebanggaan"], ["pemandangan"], ["kesegaran"], ["pikiran"], ["penenang"], ["dunia"], ["orang tua"], ["suasana"], ["romantis"], ["hutan"], ["cita-cita"], ["kesuksesan"], ["pendorong"], ["kesabaran"], ["kunci"], ["keberhasilan"], ["cinta"], ["selalu"], ["abadi"], ["hewan"], ["kucing itu"], ["peliharaan"], ["idola"], ["keluarga"], ["mobil baru itu"], ["kendaraan"], ["listrik"],
            ["makan"], ["berbicara"], ["main"], ["minum"], ["tidur"], ["berlari"], ["melompat"], ["menulis"], ["membaca"],
            ["sekarang"], ["kemarin"], ["besok"], ["sejak"], ["kelak"], ["saat"], ["kala"], ["sekali"], ["terus"], ["segera"], ["lambat"], ["juga"], ["hanya"], ["hampir"], ["sangat"], ["lebih"],
            ["cantik"], ["ganteng"], ["cerdas"], ["lucu"], ["bodoh"], ["lancar"], ["kaya"], ["miskin"], ["indah"], ["rumit"], ["tua"], ["muda"], ["jelek"], ["pahit"], ["asam"], ["manis"], ["pedas"], ["serius"], ["ringan"], ["berat"], ["luas"], ["sempit"], ["lembut"], ["kasar"], ["pendek"], ["tinggi"], ["cepat"], ["mahal"],
            ["di"], ["dengan"], ["atas"], ["ke"], ["bawah"], ["dari"], ["untuk"], ["dalam"], ["luar"], ["sekitar"], ["dekat"],
            ["Verb", "NP"],["Num", "NP"]],
    "Ket": [["Prep", "NP"], ["Prep"], ["VP"], ["Prep", "PP"],
            ["sekarang"], ["kemarin"], ["besok"], ["sejak"], ["kelak"], ["saat"], ["kala"], ["sekali"], ["terus"], ["segera"], ["lambat"], ["juga"], ["hanya"], ["hampir"], ["sangat"], ["lebih"],
            ["cantik"], ["ganteng"], ["cerdas"], ["lucu"], ["bodoh"], ["lancar"], ["kaya"], ["miskin"], ["indah"], ["rumit"], ["tua"], ["muda"], ["jelek"], ["pahit"], ["asam"], ["manis"], ["pedas"], ["serius"], ["ringan"], ["berat"], ["luas"], ["sempit"], ["lembut"], ["kasar"], ["pendek"], ["tinggi"], ["cepat"], ["mahal"],
            ["Gagas"], ["Surya"], ["Alex"], ["Wahyu"], ["Budi"], ["Alicia"], ["Pradipta"], ["David"], ["Krisna"], ["John"], ["Putu"], ["Komodo"], ["Buaya"], ["Siti"], ["Dika"], ["Duta"], ["Adi"], ["Dwipa"], ["Alaya"], ["Nengah"],
            ["saya"], ["kamu"], ["dia"], ["mereka"],
            ["rumah"], ["pohon"], ["kucing"], ["meja"], ["mobil"], ["perpustakaan"], ["polisi"], ["ayah"], ["dokter"], ["guru"], ["anjing"], ["petani"], ["pasien"], ["pelangi"], ["bola"], ["nasi"], ["buku"], ["desain"], ["murid"], ["lukisan"], ["koran"], ["mie"], ["penjahat"], ["padi"], ["komputer"], ["buku"], ["motor"], ["penyanyi"], ["kuda"], ["lagu"], ["ikan"], ["soto"], ["batu"], ["dapur"], ["pasar"], ["taman"], ["sekolah"], ["lapangan"], ["pertigaan"], ["sawah"], ["mawar"], ["kebanggaan"], ["pemandangan"], ["kesegaran"], ["pikiran"], ["penenang"], ["dunia"], ["orang tua"], ["suasana"], ["romantis"], ["hutan"], ["cita-cita"], ["kesuksesan"], ["pendorong"], ["kesabaran"], ["kunci"], ["keberhasilan"], ["cinta"], ["selalu"], ["abadi"], ["hewan"], ["kucing itu"], ["peliharaan"], ["idola"], ["keluarga"], ["mobil baru itu"], ["kendaraan"], ["listrik"],
            ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"]],

    "NP": [["Gagas"], ["Surya"], ["Alex"], ["Wahyu"], ["Budi"], ["Alicia"], ["Pradipta"], ["David"], ["Krisna"], ["John"], ["Putu"], ["Komodo"], ["Buaya"], ["Siti"], ["Dika"], ["Duta"], ["Adi"], ["Dwipa"], ["Alaya"], ["Nengah"],
          ["saya"], ["kamu"], ["dia"], ["mereka"],
          ["rumah"], ["pohon"], ["kucing"], ["meja"], ["mobil"], ["perpustakaan"], ["polisi"], ["ayah"], ["dokter"], ["guru"], ["anjing"], ["petani"], ["pasien"], ["pelangi"], ["bola"], ["nasi"], ["buku"], ["desain"], ["murid"], ["lukisan"], ["koran"], ["mie"], ["penjahat"], ["padi"], ["komputer"], ["buku"], ["motor"], ["penyanyi"], ["kuda"], ["lagu"], ["ikan"], ["soto"], ["batu"], ["dapur"], ["pasar"], ["taman"], ["sekolah"], ["lapangan"], ["pertigaan"], ["sawah"], ["mawar"], ["kebanggaan"], ["pemandangan"], ["kesegaran"], ["pikiran"], ["penenang"], ["dunia"], ["orang tua"], ["suasana"], ["romantis"], ["hutan"], ["cita-cita"], ["kesuksesan"], ["pendorong"], ["kesabaran"], ["kunci"], ["keberhasilan"], ["cinta"], ["selalu"], ["abadi"], ["hewan"], ["kucing itu"], ["peliharaan"], ["idola"], ["keluarga"], ["mobil baru itu"], ["kendaraan"], ["listrik"],
          ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"]],
    "VP": [["makan"], ["berbicara"], ["main"], ["minum"], ["tidur"], ["berlari"], ["melompat"], ["menulis"], ["membaca"], ["Verb", "NP"]],
    "PP": [["Prep", "NP"], ["Prep", "VP"], ["Prep", "PP"], ["cantik"], ["ganteng"], ["cerdas"], ["lucu"], ["bodoh"], ["lancar"], ["kaya"], ["miskin"], ["indah"], ["rumit"], ["tua"], ["muda"], ["jelek"], ["pahit"], ["asam"], ["manis"],
           ["pedas"], ["serius"], ["ringan"], ["berat"], ["luas"], ["sempit"], ["lembut"], ["kasar"], ["pendek"], ["tinggi"], ["sekarang"], ["kemarin"], ["besok"], ["sejak"], ["kelak"], ["saat"], ["kala"], ["sekali"], ["terus"], ["segera"],
           ["lambat"], ["juga"], ["hanya"], ["hampir"], ["sangat"], ["lebih"]],
    "NumP": [["Num", "NP"]],

    "Noun": [["rumah"], ["pohon"], ["kucing"], ["meja"], ["mobil"], ["perpustakaan"], ["polisi"], ["ayah"], ["dokter"], ["guru"], ["anjing"], ["petani"], ["pasien"], ["pelangi"], ["bola"], ["nasi"], ["buku"], ["desain"], ["murid"], ["lukisan"], ["koran"], ["mie"], ["penjahat"], ["padi"], ["komputer"], ["buku"], ["motor"], ["penyanyi"], ["kuda"], ["lagu"], ["ikan"], ["soto"], ["batu"], ["dapur"], ["pasar"], ["taman"], ["sekolah"], ["lapangan"], ["pertigaan"], ["sawah"], ["mawar"], ["kebanggaan"], ["pemandangan"], ["kesegaran"], ["pikiran"], ["penenang"], ["dunia"], ["orang tua"], ["suasana"], ["romantis"], ["hutan"], ["cita-cita"], ["kesuksesan"], ["pendorong"], ["kesabaran"], ["kunci"], ["keberhasilan"], ["cinta"], ["selalu"], ["abadi"], ["hewan"], ["kucing itu"], ["peliharaan"], ["idola"], ["keluarga"], ["mobil baru itu"], ["kendaraan"], ["listrik"]],
    "Pronoun": [["saya"], ["kamu"], ["dia"], ["mereka"]],
    "PropNoun": [["Gagas"], ["Surya"], ["Alex"], ["Wahyu"], ["Budi"], ["Alicia"], ["Pradipta"], ["David"], ["Krisna"], ["John"], ["Putu"], ["Komodo"], ["Buaya"], ["Siti"], ["Dika"], ["Duta"], ["Adi"], ["Dwipa"], ["Alaya"], ["Nengah"]],
    "Adj": [["cantik"], ["ganteng"], ["cerdas"], ["lucu"], ["bodoh"], ["lancar"], ["kaya"], ["miskin"], ["indah"], ["rumit"], ["tua"], ["muda"], ["jelek"], ["pahit"], ["asam"], ["manis"], ["pedas"], ["serius"], ["ringan"], ["berat"], ["luas"], ["sempit"], ["lembut"], ["kasar"], ["pendek"], ["tinggi"], ["cepat"], ["mahal"]],
    "Verb": [["makan"], ["berbicara"], ["main"], ["minum"], ["tidur"], ["berlari"], ["melompat"], ["menulis"], ["membaca"], ["memakan"], ["memasak"], ["menggigit"], ["melompati"], ["bermain"], ["memiliki"], ["menangkap"], ["pergi"], ["memukul"], ["menendang"], ["merawat"], ["mengajar"], ["mengejar"], ["menggambar"], ["berlari"], ["menanam"], ["menjual"], ["menyukai"], ["membeli"], ["dikejar"], ["menunggu"], ["mengendarai"], ["melukis"], ["digigit"], ["menyanyikan"], ["memancing"], ["menabrak"], ["adalah"], ["akan"]],
    "Adv": [["sekarang"], ["kemarin"], ["besok"], ["sejak"], ["kelak"], ["saat"], ["kala"], ["sekali"], ["terus"], ["segera"], ["lambat"], ["juga"], ["hanya"], ["hampir"], ["sangat"], ["lebih"]],
    "Num": [["beberapa"], ["satu"], ["dua"]],
    "Prep": [["di"], ["dengan"], ["atas"], ["ke"], ["bawah"], ["dari"], ["untuk"], ["dalam"], ["luar"], ["sekitar"],["dekat"]]
}



# Function to perform the CYK Algorithm
def cykParse(words):
    n = len(words)
    T = [[set([]) for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for lhs, rule in R.items():
            for rhs in rule:
                if len(rhs) == 1 and rhs[0] == words[j]:
                    T[j][j].add(lhs)

        for i in range(j - 1, -1, -1):
            for k in range(i, j):
                for lhs, rule in R.items():
                    for rhs in rule:
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)

    if "K" in T[0][n - 1]:
        return ":green[Kalimat Anda Benar.]"
    else:
        return ":red[Kalimat Anda Salah.]"

# Function to run CYK algorithm
def run_cyk(input_sentence):
    words = input_sentence.split()
    return cykParse(words)

# Streamlit app
def main():
    st.title("APAKAH :red[KALIMAT] ANDA BENAR ?")
    st.title("CEK :red[KALIMAT] ANDA DISINI")
    input_sentence = st.text_input(":green[ Contoh : Gagas makan Komodo kemarin]", placeholder="Masukan Kalimat Disini")

    if st.button("Lihat Hasil"):
        if input_sentence:
            st.write(f"Kalimat yang di cek : '{input_sentence}'")
            result = run_cyk(input_sentence)
            st.write(f"Hasilnya: {result}")
        else:
            st.write("Masukan Kalimat Terlebih Dahulu.")

if __name__ == "__main__":
    main()
