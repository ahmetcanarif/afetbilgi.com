import sys
import json

basedir = "datasets"

if len(sys.argv) >= 2:
    basedir = sys.argv[1]

data_points = [
  { 'name_ar': 'ملاجئ مؤقتة', 'name_tr': 'Geçici Barınma Alanları', 'name_en': 'Temporary Accommodation Places', 'name_ku': 'Bicîhbûna Demkî', 'path': f'{basedir}/barinma.json' },
  { 'name_ar': 'مناطق تجميع آمنة', 'name_tr': 'Güvenli Toplanma Alanları', 'name_en': 'Safe Gathering Places', 'name_ku': 'Qadên Ewle Bo Kombûnê', 'path': f'{basedir}/toplanma.json' },
  { 'name_ar': 'المستشفيات الفعالة', 'name_tr': 'Aktif Hastaneler', 'name_en': 'Active Hospitals', 'name_ku': 'Nexweşxaneyên vekirî', 'path': f'{basedir}/hastane.json' },
  { 'name_ar': 'مواقع توصيل الطعام', 'name_tr': 'Yemek Dağıtım Yerleri', 'name_en': 'Food Distribution Center', 'name_ku': 'Cihên Belavkirina Xwarinê', 'path': f'{basedir}/yemek.json' },
  { 'name_ar': 'Services outside the disaster area' , 'name_tr': 'Afet bölgesi dışındaki hizmetler', 'name_en': 'Services outside the disaster area', 'name_ku': 'Services outside the disaster area', 'path': f'{basedir}/services.json'},
  { 'name_ar': "صيدليات الحاويات", "name_ku": "Dermanxaneyên Seyare", "name_en": "Container Pharmacies", "name_tr": 'Konteyner Eczaneler', 'path': f'{basedir}/eczane.json' },
  { 'name_ar': 'أرقام هواتف مهمة', 'name_tr': 'Önemli Telefon Numaraları', 'name_en': 'Crucial Phone Number', 'name_ku': 'Numareyên Girîng', 'path': f'{basedir}/telefon.json' },
  { 'name_ar': 'مُرْتَادِي الشَّبَكَة مهمة', 'name_tr': 'Önemli Web Siteleri', 'name_en': 'Useful Links', 'name_ku': ' Malperên Kêrhatî', 'path': f'{basedir}/faydali_linkler.json' },
  { 'name_ar': 'بَيَاطير', 'name_tr': 'Veterinerler', 'name_en': 'Veterinarians', 'name_ku': 'Veterîner', 'path': f'{basedir}/veteriner.json' },
  { 'name_ar': 'Digital Solidarity Campaigns' , 'name_tr': 'Dijital Yardımlaşma Seferberlikleri', 'name_en': 'Digital Solidarity Campaigns', 'name_ku': 'Digital Solidarity Campaigns', 'path': f'{basedir}/digital_platforms.json'},
  { 'name_ar': 'روابط التبرع بالمال' , 'name_tr': 'Para Bağışı Linkleri', 'name_en': 'Monetary Donation Links', 'name_ku': 'Lînkên bexşîna darayî', 'path': f'{basedir}/donation_links.json'},
  { 'name_ar': 'فرص التبرع بالعناصر', 'name_tr': 'Yardım Toplama Merkezleri','name_en': 'Other Donation', 'name_ku': 'Bexşkirina Tiştan', 'path': f'{basedir}/yardim_toplama_merkezleri.json' },
  { 'name_ar': 'نقاط الهلال الأحمر للتبرع بالدم', 'name_tr': 'Kızılay Kan Bağış Noktaları', 'name_en': 'Kızılay Blood Donation Places', 'name_ku': 'Cihên Xwîn Dayînê yên Kizilay/ Heyva Sor', 'path': f'{basedir}/blood.json' },
  { 'name_ar': 'نقاط التبرع بالخلايا الجذعية', 'name_tr': 'Kök Hücre Bağış Noktaları', 'name_en': 'Stem Cell Donation Points', 'name_ku': 'Cihên bo bexşîna xaneyî bineretiyê', 'path': f'{basedir}/kokhucre.json' },
  { 'name_ar': 'نصوص مفيدة', 'name_tr': 'Faydalı Yazılar', 'name_en': 'Useful Articles' , 'name_ku': 'Agahiyên Kêrhatî', 'path': f'{basedir}/yazilar.json' },
  { 'name_ar': 'نقاط الإخلاء', 'name_tr': 'Tahliye Noktaları', 'name_en': 'Evacuation Points', 'name_ku': 'Xalên valakirinê', 'path': f'{basedir}/tahliye.json' },
  { 'name_ar': 'مساعدات النقل', 'name_tr': 'Ulaşım Yardımları', 'name_en': 'Transportation Aid', 'name_ku': 'Alîkariya Veguhestinê', 'path': f'{basedir}/ulasim.json' },
  { 'name_ar': 'المحطة البنزين', 'name_tr': 'Benzin İstasyonları', 'name_en': 'Gas Stations', 'name_ku': 'Stasyona sotemeniyê', 'path': f'{basedir}/akaryakit.json' },
  { 'name_ar': 'المرحاض المتنقل', 'name_tr': 'Mobil Tuvaletler', 'name_en': 'Mobile Toilets', 'name_ku': 'Destavxaneyên mobîl', 'path': f'{basedir}/mobil_tuvalet.json' },
  { 'name_tr': 'Açık Eczaneler', 'name_en': 'Open Pharmacies', 'name_ku': 'Dermanxaneyên vekirî', "name_ar": "صيدليات مفتوحة", 'path': f'{basedir}/eczane_local.json' },

  # { 'name_tr': 'VPN', 'path': f'{basedir}/vpn.json' },
#   STAGING
#   { 'name': 'Kapalı Yollar', 'path': f'{basedir}/kapaliyollar.json' },

#   DEPRECATED
#   { 'name_tr': 'Para Bağışı İmkanları', 'name_en': 'Money Donation', 'path': 'datasets/bagis.json' },
]

result = {
    'type': 'question',
    'text_tr': 'Lütfen bilgi almak istediğiniz konuyu seçiniz.',
    'text_en': 'Please select a topic.',
    'text_ku': 'Ji kerema xwe mijara hûn dixwazin agahdariyê jê bigirin hilbijêrin',
    'text_ar': 'الرجاء تحديد الموضوع الذي تريد تلقي معلومات عنه',
    'options': []
}

for data_point in data_points:
    with open(f"{data_point['path']}", "r", encoding="utf-8") as f:
        try:
            text = f.read().encode("utf-8")

            data = json.loads(text)

            result['options'].append({
                **data_point,
                'value': data,
            })
        except Exception as e:
            print(f"Error reading {data_point['path']}: {e}")
            sys.exit(1)

print(json.dumps(result, ensure_ascii=False, allow_nan=False))

