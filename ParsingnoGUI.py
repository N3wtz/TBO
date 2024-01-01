#CNF Rules
R= {
    "K": [["S", "P"], ["P1", "O"], ["P1", "Pel"], ["P1", "Ket"], ["P1", "P2"], ["P1", "P3"], ["P1", "P4"]],
    "P1": [["S", "P"]],
    "P2": [["O", "Pel"]],
    "P3": [["O", "Ket"]],
    "P4": [["P2", "Ket"]],

    "S": [["NP", "AdjP"], ["NumP","NP"], ["NP","Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["gagas"], ["alaya"], ["komodo"], ["surya"], ["duta"], ["krisna"], ["david"], ["nengah"], ["putu"], ["dika"], ["dewi"], ["siti"], ["rahayu"], ["ani"], ["adi"], ["santoso"], ["ratna"], ["hadi"], ["prayitno"], ["kiki"], ["sinta"], ["haryono"], ["baikal"], ["copacabana"], ["mediterania"], ["rio"], ["de"], ["janeiro"], ["bali"], ["bandung"], ["bogor"], ["monas"], ["denpasar"], ["surabaya"], ["jakarta"], ["jawa"], ["arab"], ["saudi"], ["jepang"], ["medan"], ["indonesia"], ["dia"], ["itu"], ["saya"], ["kita"], ["kami"], ["mereka"], ["anda"], ["ia"], ["aku"], ["tersebut"], ["ini"], ["kalian"], ["beliau"], ["nenek"], ["daun"], ["guru"], ["kepulauan"], ["ubi"], ["kebun"], ["orang"], ["acara"], ["mahasiswa"], ["kegiatan"], ["pengabdian"], ["dewasa"], ["wahana"], ["pemadam"], ["kebakaran"], ["waktu"], ["menyelamatkan"], ["penduduk"], ["desa"], ["anak"], ["laki-laki"], ["bermain"], ["taman"], ["kota"], ["ibu"], ["siswa"], ["perpustakaan"], ["kampus"], ["polisi"], ["ketertiban"], ["jalan"], ["burung"], ["merapati"], ["siang"], ["hari"], ["ikan"], ["koi"], ["kolam"], ["taman"], ["kuda"], ["pacuan"], ["lintasan"], ["pacu"], ["monyet"], ["kecil"], ["ranting"], ["pohon"], ["kelinci"], ["teman"], ["kebun"], ["lumba-lumba"], ["laut"], ["lepas"], ["kupu-kupu"], ["bunga"], ["sapi"], ["nektar"], ["lebah"], ["rumput"], ["padang"], ["buaya"], ["tepi"], ["danau"], ["kuliah"], ["seminar"], ["dr."], ["universitas"], ["pantai"], ["pemimpin"], ["proyek"], ["bu"], ["pemilik"], ["warung"], ["kopi"], ["prof."], ["pakar"], ["bidang"], ["ekologi"], ["juara"], ["lomba"], ["menyanyi"], ["pembicara"], ["tetangga"], ["dunia"], ["keindahan"], ["pantainya"], ["bukit"], ["tinggi"], ["pemandangan"], ["alam"], ["danau"], ["pantai"], ["ikon"], ["kota"], ["kulinernya"], ["hujan"], ["tengah"], ["budaya"], ["malam"], ["timur"], ["pentas"], ["ogoh-ogoh"], ["tahun"], ["baru"], ["saka"], ["negara"], ["pengahsil"], ["minyak"], ["pasang"], ["sepatu"], ["rak"], ["buah"], ["rumah"], ["tahap"], ["konstruksi"], ["ekor"], ["merpati"], ["buku"], ["suasana"], ["prestasi"], ["penghasil"], ["kucing"], ["belakang"], ["pengunjung"], ["kamar"], ["tidur"], ["pertunjukan"], ["teater"], ["mobil"], ["digunakan"], ["kotak"], ["pagi"], ["mainan"], ["anak-anak"], ["bungkus"], ["rokok"], ["sejarah"], ["kebudayaan"], ["bahasa"], ["asrama"], ["putri"], ["pemain"], ["sepak"], ["bola"], ["bapak"], ["kakek"], ["kursi"], ["rotan"], ["pelatih"], ["tari"], ["rencana"], ["perjalanan"], ["sangat"], ["pengembangan"], ["teknologi"], ["pesat"], ["gadis"], ["kecil"], ["boneka"], ["barunya"], ["air"], ["terjun"], ["pegunungan"], ["yang"], ["mekar"], ["kesegaran"], ["pikiran"], ["kebanggaan"], ["setia"], ["udara"], ["rasa"], ["cokelat"], ["rindang"], ["cita-cita"], ["pendorong"], ["kesuksesan"], ["pameran"], ["karya"], ["seni"], ["kontemporer"], ["lokal"], ["daya"], ["tarik"], ["wisata"], ["daerah"], ["hewan"], ["peliharaan"]],
    "P": [["Prep", "NP"],["Prep", "AdjP"], ["AdvP", "VP"], ["Adv", "AdjP"], ["mengambil"], ["menghadiri"], ["mengikuti"], ["menaiki"], ["mempunyai"], ["memasak"], ["makanan"], ["belajar"], ["menjaga"], ["membuat"], ["terbang"], ["berenang"], ["berlari"], ["bergelantungan"], ["melompat-lompat"], ["bermain"], ["hinggap"], ["mengumpulkan"], ["mengunyah"], ["adalah"], ["berjemur"], ["hadir"], ["memberikan"], ["berlibur"], ["merupakan"], ["menjadi"], ["membantu"], ["terkenal"], ["memiliki"], ["dikenal"], ["terletak"], ["ramai"], ["menyambut"], ["terpajang"], ["sedang"], ["hadir"], ["disiram"], ["berisi"], ["membeli"], ["meneliti"], ["kursus"], ["menyukai"], ["dua"], ["disusun"], ["berlangsung"], ["seni"], ["menampilkan"], ["keluarga"], ["hewan"]],
    "O": [["NP", "AdjP"], ["NumP", "NP"], ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["gagas"], ["alaya"], ["komodo"], ["surya"], ["duta"], ["krisna"], ["david"], ["nengah"], ["putu"], ["dika"], ["dewi"], ["siti"], ["rahayu"], ["ani"], ["adi"], ["santoso"], ["ratna"], ["hadi"], ["prayitno"], ["kiki"], ["sinta"], ["haryono"], ["baikal"], ["copacabana"], ["mediterania"], ["rio"], ["de"], ["janeiro"], ["bali"], ["bandung"], ["bogor"], ["monas"], ["denpasar"], ["surabaya"], ["jakarta"], ["jawa"], ["arab"], ["saudi"], ["jepang"], ["medan"], ["indonesia"], ["dia"], ["itu"], ["saya"], ["kita"], ["kami"], ["mereka"], ["anda"], ["ia"], ["aku"], ["tersebut"], ["ini"], ["kalian"], ["beliau"], ["nenek"], ["daun"], ["guru"], ["kepulauan"], ["ubi"], ["kebun"], ["orang"], ["acara"], ["mahasiswa"], ["kegiatan"], ["pengabdian"], ["dewasa"], ["wahana"], ["pemadam"], ["kebakaran"], ["waktu"], ["menyelamatkan"], ["penduduk"], ["desa"], ["anak"], ["laki-laki"], ["bermain"], ["taman"], ["kota"], ["ibu"], ["siswa"], ["perpustakaan"], ["kampus"], ["polisi"], ["ketertiban"], ["jalan"], ["burung"], ["merapati"], ["siang"], ["hari"], ["ikan"], ["koi"], ["kolam"], ["taman"], ["kuda"], ["pacuan"], ["lintasan"], ["pacu"], ["monyet"], ["kecil"], ["ranting"], ["pohon"], ["kelinci"], ["teman"], ["kebun"], ["lumba-lumba"], ["laut"], ["lepas"], ["kupu-kupu"], ["bunga"], ["sapi"], ["nektar"], ["lebah"], ["rumput"], ["padang"], ["buaya"], ["tepi"], ["danau"], ["kuliah"], ["seminar"], ["dr."], ["universitas"], ["pantai"], ["pemimpin"], ["proyek"], ["bu"], ["pemilik"], ["warung"], ["kopi"], ["prof."], ["pakar"], ["bidang"], ["ekologi"], ["juara"], ["lomba"], ["menyanyi"], ["pembicara"], ["tetangga"], ["dunia"], ["keindahan"], ["pantainya"], ["bukit"], ["tinggi"], ["pemandangan"], ["alam"], ["danau"], ["pantai"], ["ikon"], ["kota"], ["kulinernya"], ["hujan"], ["tengah"], ["budaya"], ["malam"], ["timur"], ["pentas"], ["ogoh-ogoh"], ["tahun"], ["baru"], ["saka"], ["negara"], ["pengahsil"], ["minyak"], ["pasang"], ["sepatu"], ["rak"], ["buah"], ["rumah"], ["tahap"], ["konstruksi"], ["ekor"], ["merpati"], ["buku"], ["suasana"], ["prestasi"], ["penghasil"], ["kucing"], ["belakang"], ["pengunjung"], ["kamar"], ["tidur"], ["pertunjukan"], ["teater"], ["mobil"], ["digunakan"], ["kotak"], ["pagi"], ["mainan"], ["anak-anak"], ["bungkus"], ["rokok"], ["sejarah"], ["kebudayaan"], ["bahasa"], ["asrama"], ["putri"], ["pemain"], ["sepak"], ["bola"], ["bapak"], ["kakek"], ["kursi"], ["rotan"], ["pelatih"], ["tari"], ["rencana"], ["perjalanan"], ["sangat"], ["pengembangan"], ["teknologi"], ["pesat"], ["gadis"], ["kecil"], ["boneka"], ["barunya"], ["air"], ["terjun"], ["pegunungan"], ["yang"], ["mekar"], ["kesegaran"], ["pikiran"], ["kebanggaan"], ["setia"], ["udara"], ["rasa"], ["cokelat"], ["rindang"], ["cita-cita"], ["pendorong"], ["kesuksesan"], ["pameran"], ["karya"], ["seni"], ["kontemporer"], ["lokal"], ["daya"], ["tarik"], ["wisata"], ["daerah"], ["hewan"], ["peliharaan"]],
    "Pel": [["NP", "AdjP"], ["NumP", "NP"], ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["gagas"], ["alaya"], ["komodo"], ["surya"], ["duta"], ["krisna"], ["david"], ["nengah"], ["putu"], ["dika"], ["dewi"], ["siti"], ["rahayu"], ["ani"], ["adi"], ["santoso"], ["ratna"], ["hadi"], ["prayitno"], ["kiki"], ["sinta"], ["haryono"], ["baikal"], ["copacabana"], ["mediterania"], ["rio"], ["de"], ["janeiro"], ["bali"], ["bandung"], ["bogor"], ["monas"], ["denpasar"], ["surabaya"], ["jakarta"], ["jawa"], ["arab"], ["saudi"], ["jepang"], ["medan"], ["indonesia"], ["dia"], ["itu"], ["saya"], ["kita"], ["kami"], ["mereka"], ["anda"], ["ia"], ["aku"], ["tersebut"], ["ini"], ["kalian"], ["beliau"], ["nenek"], ["daun"], ["guru"], ["kepulauan"], ["ubi"], ["kebun"], ["orang"], ["acara"], ["mahasiswa"], ["kegiatan"], ["pengabdian"], ["dewasa"], ["wahana"], ["pemadam"], ["kebakaran"], ["waktu"], ["menyelamatkan"], ["penduduk"], ["desa"], ["anak"], ["laki-laki"], ["bermain"], ["taman"], ["kota"], ["ibu"], ["siswa"], ["perpustakaan"], ["kampus"], ["polisi"], ["ketertiban"], ["jalan"], ["burung"], ["merapati"], ["siang"], ["hari"], ["ikan"], ["koi"], ["kolam"], ["taman"], ["kuda"], ["pacuan"], ["lintasan"], ["pacu"], ["monyet"], ["kecil"], ["ranting"], ["pohon"], ["kelinci"], ["teman"], ["kebun"], ["lumba-lumba"], ["laut"], ["lepas"], ["kupu-kupu"], ["bunga"], ["sapi"], ["nektar"], ["lebah"], ["rumput"], ["padang"], ["buaya"], ["tepi"], ["danau"], ["kuliah"], ["seminar"], ["dr."], ["universitas"], ["pantai"], ["pemimpin"], ["proyek"], ["bu"], ["pemilik"], ["warung"], ["kopi"], ["prof."], ["pakar"], ["bidang"], ["ekologi"], ["juara"], ["lomba"], ["menyanyi"], ["pembicara"], ["tetangga"], ["dunia"], ["keindahan"], ["pantainya"], ["bukit"], ["tinggi"], ["pemandangan"], ["alam"], ["danau"], ["pantai"], ["ikon"], ["kota"], ["kulinernya"], ["hujan"], ["tengah"], ["budaya"], ["malam"], ["timur"], ["pentas"], ["ogoh-ogoh"], ["tahun"], ["baru"], ["saka"], ["negara"], ["pengahsil"], ["minyak"], ["pasang"], ["sepatu"], ["rak"], ["buah"], ["rumah"], ["tahap"], ["konstruksi"], ["ekor"], ["merpati"], ["buku"], ["suasana"], ["prestasi"], ["penghasil"], ["kucing"], ["belakang"], ["pengunjung"], ["kamar"], ["tidur"], ["pertunjukan"], ["teater"], ["mobil"], ["digunakan"], ["kotak"], ["pagi"], ["mainan"], ["anak-anak"], ["bungkus"], ["rokok"], ["sejarah"], ["kebudayaan"], ["bahasa"], ["asrama"], ["putri"], ["pemain"], ["sepak"], ["bola"], ["bapak"], ["kakek"], ["kursi"], ["rotan"], ["pelatih"], ["tari"], ["rencana"], ["perjalanan"], ["sangat"], ["pengembangan"], ["teknologi"], ["pesat"], ["gadis"], ["kecil"], ["boneka"], ["barunya"], ["air"], ["terjun"], ["pegunungan"], ["yang"], ["mekar"], ["kesegaran"], ["pikiran"], ["kebanggaan"], ["setia"], ["udara"], ["rasa"], ["cokelat"], ["rindang"], ["cita-cita"], ["pendorong"], ["kesuksesan"], ["pameran"], ["karya"], ["seni"], ["kontemporer"], ["lokal"], ["daya"], ["tarik"], ["wisata"], ["daerah"], ["hewan"], ["peliharaan"], ["mengambil"], ["menghadiri"], ["mengikuti"], ["menaiki"], ["mempunyai"], ["memasak"], ["makanan"], ["belajar"], ["menjaga"], ["membuat"], ["terbang"], ["berenang"], ["berlari"], ["bergelantungan"], ["melompat-lompat"], ["bermain"], ["hinggap"], ["mengumpulkan"], ["mengunyah"], ["adalah"], ["berjemur"], ["hadir"], ["memberikan"], ["berlibur"], ["merupakan"], ["menjadi"], ["membantu"], ["terkenal"], ["memiliki"], ["dikenal"], ["terletak"], ["ramai"], ["menyambut"], ["terpajang"], ["sedang"], ["hadir"], ["disiram"], ["berisi"], ["membeli"], ["meneliti"], ["kursus"], ["menyukai"], ["dua"], ["disusun"], ["berlangsung"], ["seni"], ["menampilkan"], ["keluarga"], ["hewan"], ["lezat"], ["cepat"], ["indah"], ["terdalam"], ["terbesar"], ["nyaman"], ["besar"], ["hitam"], ["putih"], ["luas"], ["baik"], ["senang"], ["menghibur"], ["tua"], ["panjang"], ["sejuk"], ["kelemahannya"], ["kesejukan"], ["romantis"], ["manis"], ["tinggi"]],
    "Ket": [["PP", "NP"], ["Prep", "AdjP"], ["Adv", "AdjP"], ["Num", "NP"], ["sedikit"], ["banyak"], ["sekitar"], ["lima"], ["para"], ["seekor"], ["belas"], ["delapan"], ["dua"], ["sepuluh"], ["tujuh"], ["puluh"], ["setiap"], ["tiga"], ["lezat"], ["cepat"], ["indah"], ["terdalam"], ["terbesar"], ["nyaman"], ["besar"], ["hitam"], ["putih"], ["luas"], ["baik"], ["senang"], ["menghibur"], ["tua"], ["panjang"], ["sejuk"], ["kelemahannya"], ["kesejukan"], ["romantis"], ["manis"], ["tinggi"]],
    "NP": [["NP", "AdjP"], ["NumP","NP"], ["NP","Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["gagas"], ["alaya"], ["komodo"], ["surya"], ["duta"], ["krisna"], ["david"], ["nengah"], ["putu"], ["dika"], ["dewi"], ["siti"], ["rahayu"], ["ani"], ["adi"], ["santoso"], ["ratna"], ["hadi"], ["prayitno"], ["kiki"], ["sinta"], ["haryono"], ["baikal"], ["copacabana"], ["mediterania"], ["rio"], ["de"], ["janeiro"], ["bali"], ["bandung"], ["bogor"], ["monas"], ["denpasar"], ["surabaya"], ["jakarta"], ["jawa"], ["arab"], ["saudi"], ["jepang"], ["medan"], ["indonesia"], ["dia"], ["itu"], ["saya"], ["kita"], ["kami"], ["mereka"], ["anda"], ["ia"], ["aku"], ["tersebut"], ["ini"], ["kalian"], ["beliau"], ["nenek"], ["daun"], ["guru"], ["kepulauan"], ["ubi"], ["kebun"], ["orang"], ["acara"], ["mahasiswa"], ["kegiatan"], ["pengabdian"], ["dewasa"], ["wahana"], ["pemadam"], ["kebakaran"], ["waktu"], ["menyelamatkan"], ["penduduk"], ["desa"], ["anak"], ["laki-laki"], ["bermain"], ["taman"], ["kota"], ["ibu"], ["siswa"], ["perpustakaan"], ["kampus"], ["polisi"], ["ketertiban"], ["jalan"], ["burung"], ["merapati"], ["siang"], ["hari"], ["ikan"], ["koi"], ["kolam"], ["taman"], ["kuda"], ["pacuan"], ["lintasan"], ["pacu"], ["monyet"], ["kecil"], ["ranting"], ["pohon"], ["kelinci"], ["teman"], ["kebun"], ["lumba-lumba"], ["laut"], ["lepas"], ["kupu-kupu"], ["bunga"], ["sapi"], ["nektar"], ["lebah"], ["rumput"], ["padang"], ["buaya"], ["tepi"], ["danau"], ["kuliah"], ["seminar"], ["dr."], ["universitas"], ["pantai"], ["pemimpin"], ["proyek"], ["bu"], ["pemilik"], ["warung"], ["kopi"], ["prof."], ["pakar"], ["bidang"], ["ekologi"], ["juara"], ["lomba"], ["menyanyi"], ["pembicara"], ["tetangga"], ["dunia"], ["keindahan"], ["pantainya"], ["bukit"], ["tinggi"], ["pemandangan"], ["alam"], ["danau"], ["pantai"], ["ikon"], ["kota"], ["kulinernya"], ["hujan"], ["tengah"], ["budaya"], ["malam"], ["timur"], ["pentas"], ["ogoh-ogoh"], ["tahun"], ["baru"], ["saka"], ["negara"], ["pengahsil"], ["minyak"], ["pasang"], ["sepatu"], ["rak"], ["buah"], ["rumah"], ["tahap"], ["konstruksi"], ["ekor"], ["merpati"], ["buku"], ["suasana"], ["prestasi"], ["penghasil"], ["kucing"], ["belakang"], ["pengunjung"], ["kamar"], ["tidur"], ["pertunjukan"], ["teater"], ["mobil"], ["digunakan"], ["kotak"], ["pagi"], ["mainan"], ["anak-anak"], ["bungkus"], ["rokok"], ["sejarah"], ["kebudayaan"], ["bahasa"], ["asrama"], ["putri"], ["pemain"], ["sepak"], ["bola"], ["bapak"], ["kakek"], ["kursi"], ["rotan"], ["pelatih"], ["tari"], ["rencana"], ["perjalanan"], ["sangat"], ["pengembangan"], ["teknologi"], ["pesat"], ["gadis"], ["kecil"], ["boneka"], ["barunya"], ["air"], ["terjun"], ["pegunungan"], ["yang"], ["mekar"], ["kesegaran"], ["pikiran"], ["kebanggaan"], ["setia"], ["udara"], ["rasa"], ["cokelat"], ["rindang"], ["cita-cita"], ["pendorong"], ["kesuksesan"], ["pameran"], ["karya"], ["seni"], ["kontemporer"], ["lokal"], ["daya"], ["tarik"], ["wisata"], ["daerah"], ["hewan"], ["peliharaan"]],
    "VP": [["Prep", "NP"],["Prep", "AdjP"], ["AdvP", "VP"], ["Adv", "AdjP"], ["mengambil"], ["menghadiri"], ["mengikuti"], ["menaiki"], ["mempunyai"], ["memasak"], ["makanan"], ["belajar"], ["menjaga"], ["terbang"], ["berenang"], ["berlari"], ["membuat"], ["bergelantungan"], ["melompat-lompat"], ["bermain"], ["hinggap"], ["mengumpulkan"], ["mengunyah"], ["adalah"], ["berjemur"], ["hadir"], ["memberikan"], ["berlibur"], ["merupakan"], ["menjadi"], ["membantu"], ["terkenal"], ["memiliki"], ["dikenal"], ["terletak"], ["ramai"], ["menyambut"], ["terpajang"], ["sedang"], ["hadir"], ["disiram"], ["berisi"], ["membeli"], ["meneliti"], ["kursus"], ["menyukai"], ["dua"], ["disusun"], ["berlangsung"], ["seni"], ["menampilkan"], ["keluarga"], ["hewan"]],
    "PP": [["di"], ["itu"], ["tersebut"], ["saja"], ["untuk"], ["dari"], ["pada"], ["dalam"], ["dengan"], ["ini"], ["orang"], ["PP", "NP"], ["Prep","AdjP"]],
    "AdjP": [["lezat"], ["cepat"], ["indah"], ["terdalam"], ["terbesar"], ["nyaman"], ["besar"], ["hitam"], ["putih"], ["luas"], ["baik"], ["senang"], ["menghibur"], ["tua"], ["panjang"], ["sejuk"], ["kelemahannya"], ["kesejukan"], ["romantis"], ["manis"], ["tinggi"], ["Adv", "AdjP"]],
    "AdvP": [["jarang"], ["sering"], ["selalu"], ["sedang"], ["hanya"], ["diperbolehkan"], ["akan"], ["sangat"], ["dilakukan"], ["sudah"], ["lama"], ["harus"], ["Adv", "AdvP"]],
    "NumP": [["sedikit"], ["banyak"], ["sekitar"], ["lima"], ["para"], ["seekor"], ["belas"], ["delapan"], ["dua"], ["sepuluh"], ["tujuh"], ["puluh"], ["setiap"], ["tiga"], ["Num", "NumP"]],
    
    "PropNoun": [["gagas"], ["alaya"], ["komodo"], ["surya"], ["duta"], ["krisna"], ["david"], ["nengah"], ["putu"], ["dika"], ["dewi"], ["siti"], ["rahayu"], ["ani"], ["adi"], ["santoso"], ["ratna"], ["hadi"], ["prayitno"], ["kiki"], ["sinta"], ["haryono"], ["baikal"], ["copacabana"], ["mediterania"], ["rio"], ["de"], ["janeiro"], ["bali"], ["bandung"], ["bogor"], ["monas"], ["denpasar"], ["surabaya"], ["jakarta"], ["jawa"], ["arab"], ["saudi"], ["jepang"], ["medan"], ["indonesia"]],
    "Noun": [["nenek"], ["daun"], ["guru"], ["kepulauan"], ["ubi"], ["kebun"], ["orang"], ["acara"], ["mahasiswa"], ["kegiatan"], ["pengabdian"], ["dewasa"], ["wahana"], ["pemadam"], ["kebakaran"], ["waktu"], ["menyelamatkan"], ["penduduk"], ["desa"], ["anak"], ["laki-laki"], ["bermain"], ["taman"], ["kota"], ["ibu"], ["siswa"], ["perpustakaan"], ["kampus"], ["polisi"], ["ketertiban"], ["jalan"], ["burung"], ["merapati"], ["siang"], ["hari"], ["ikan"], ["koi"], ["kolam"], ["taman"], ["kuda"], ["pacuan"], ["lintasan"], ["pacu"], ["monyet"], ["kecil"], ["ranting"], ["pohon"], ["kelinci"], ["teman"], ["kebun"], ["lumba-lumba"], ["laut"], ["lepas"], ["kupu-kupu"], ["bunga"], ["sapi"], ["nektar"], ["lebah"], ["rumput"], ["padang"], ["buaya"], ["tepi"], ["danau"], ["kuliah"], ["seminar"], ["dr."], ["universitas"], ["pantai"], ["pemimpin"], ["proyek"], ["bu"], ["pemilik"], ["warung"], ["kopi"], ["prof."], ["pakar"], ["bidang"], ["ekologi"], ["juara"], ["lomba"], ["menyanyi"], ["pembicara"], ["tetangga"], ["dunia"], ["keindahan"], ["pantainya"], ["bukit"], ["tinggi"], ["pemandangan"], ["alam"], ["danau"], ["pantai"], ["ikon"], ["kota"], ["kulinernya"], ["hujan"], ["tengah"], ["budaya"], ["malam"], ["timur"], ["pentas"], ["ogoh-ogoh"], ["tahun"], ["baru"], ["saka"], ["negara"], ["pengahsil"], ["minyak"], ["pasang"], ["sepatu"], ["rak"], ["buah"], ["rumah"], ["tahap"], ["konstruksi"], ["ekor"], ["merpati"], ["buku"], ["suasana"], ["prestasi"], ["penghasil"], ["kucing"], ["belakang"], ["pengunjung"], ["kamar"], ["tidur"], ["pertunjukan"], ["teater"], ["mobil"], ["digunakan"], ["kotak"], ["pagi"], ["mainan"], ["anak-anak"], ["bungkus"], ["rokok"], ["sejarah"], ["kebudayaan"], ["bahasa"], ["asrama"], ["putri"], ["pemain"], ["sepak"], ["bola"], ["bapak"], ["kakek"], ["kursi"], ["rotan"], ["pelatih"], ["tari"], ["rencana"], ["perjalanan"], ["sangat"], ["pengembangan"], ["teknologi"], ["pesat"], ["gadis"], ["kecil"], ["boneka"], ["barunya"], ["air"], ["terjun"], ["pegunungan"], ["yang"], ["mekar"], ["kesegaran"], ["pikiran"], ["kebanggaan"], ["setia"], ["udara"], ["rasa"], ["cokelat"], ["rindang"], ["cita-cita"], ["pendorong"], ["kesuksesan"], ["pameran"], ["karya"], ["seni"], ["kontemporer"], ["lokal"], ["daya"], ["tarik"], ["wisata"], ["daerah"], ["hewan"], ["peliharaan"]],
    "Pronoun": [["dia"], ["itu"], ["saya"], ["kita"], ["kami"], ["mereka"], ["anda"], ["ia"], ["aku"], ["tersebut"], ["ini"], ["kalian"], ["beliau"]],
    "Verb": [["mengambil"], ["menghadiri"], ["mengikuti"], ["menaiki"], ["mempunyai"], ["memasak"], ["makanan"], ["belajar"], ["menjaga"], ["membuat"], ["terbang"], ["berenang"], ["berlari"], ["bergelantungan"], ["melompat-lompat"], ["bermain"], ["hinggap"], ["mengumpulkan"], ["mengunyah"], ["adalah"], ["berjemur"], ["hadir"], ["memberikan"], ["berlibur"], ["merupakan"], ["menjadi"], ["membantu"], ["terkenal"], ["memiliki"], ["dikenal"], ["terletak"], ["ramai"], ["menyambut"], ["terpajang"], ["sedang"], ["hadir"], ["disiram"], ["berisi"], ["membeli"], ["meneliti"], ["kursus"], ["menyukai"], ["dua"], ["disusun"], ["berlangsung"], ["seni"], ["menampilkan"], ["keluarga"], ["hewan"]],
    "Prep":[["di"], ["itu"], ["tersebut"], ["saja"], ["untuk"], ["dari"], ["pada"], ["dalam"], ["dengan"], ["ini"], ["orang"]],
    "Adv" : [["jarang"], ["sering"], ["selalu"], ["sedang"], ["hanya"], ["diperbolehkan"], ["akan"], ["sangat"], ["dilakukan"], ["sudah"], ["lama"], ["harus"]],
    "Adj" : [["lezat"], ["cepat"], ["indah"], ["terdalam"], ["terbesar"], ["nyaman"], ["besar"], ["hitam"], ["putih"], ["luas"], ["baik"], ["senang"], ["menghibur"], ["tua"], ["panjang"], ["sejuk"], ["kelemahannya"], ["kesejukan"], ["romantis"], ["manis"], ["tinggi"]],
    "Num": [["sedikit"], ["banyak"], ["sekitar"], ["lima"], ["para"], ["seekor"], ["belas"], ["delapan"], ["dua"], ["sepuluh"], ["tujuh"], ["puluh"], ["setiap"], ["tiga"]],
}

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
        print("True")
    else:
        print("False")

input_sentence = "air hujan membuat suasana romantis "
words = input_sentence.split()

cykParse(words)
