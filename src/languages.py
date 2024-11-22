"""Converters from language codes to language names.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""

# From https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
# https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes
code_to_endonym_map = {
    "abk" : "Аҧсуа",
    "ady" : "адыгэбзэ",
    "afr" : "Afrikaans",
    "ain" : "アイヌ イタㇰ",
    "ale" : "Unangax tunuu",
    "aqc" : "арчинский", # TBD
    "arb" : "العربية",
    "arn" : "Mapudungun",
    "ava" : "Авар мацӏ",
    "azj" : "Azeri",
    "bak" : "башҡорт",
    "bel" : "беларуская",
    "ben" : "বাংলা",
    "bre" : "brezhoneg",
    "bsk" : "Burushaski", #TBD
    "bua" : "буряад",
    "bul" : "Български",
    "car" : "Kari'nja",
    "cat" : "català",
    "ces" : "Čeština",
    "che" : "нохчийн",
    "chv" : "Чӑваш",
    "ckt" : "чаучу",
    "cmn" : "中文",
    "crs" : "kreol seselwa",
    "cwg" : "Chewong", #TBD
    "cym" : "Cymraeg",
    "dan" : "Dansk",
    "dar" : "дарган",
    "ddo" : "цез",
    "deu" : "Deutsch",
    "dsb" : "dolnoserbski",
    "ekk" : "Eesti",
    "ell" : "Ελληνικά",
    "enf" : "Онэй база",
    "eng" : "English",
    "epo" : "Esperanto",
    "ess" : "Yupigestun",
    "est" : "Eesti",
    "eus" : "Euskara",
    "evn" : "орочон",
    "fin" : "Suomi",
    "fra" : "Français",
    "gld" : "нанай",
    "gle" : "Gaeilge",
    "goh" : "Althochdeutsch", # TBD
    "gue" : "Gurindji",
    "gwd" : "Ale",
    "hau" : "harshen Hausa",
    "haw" : "ʻōlelo Hawaiʻi",
    "heb" : "עברית",
    "hin" : "हिन्दी",
    "hrv" : "Hrvatski",
    "hun" : "Magyar nyelv",
    "hye" : "Հայերեն",
    "ido" : "Ido",
    "ile" : "Interlingue",
    "ina" : "Interlingua",
    "ind" : "Bahasa Indonesia",
    "irk" : "Iraqw",
    "isl" : "Íslenska",
    "ita" : "Italiano",
    "itl" : "Итэнмэн",
    "jpn" : "日本語",
    "jup" : "Hupdë",
    "kal" : "kalaallisut",
    "kan" : "ಕನ್ನಡ",
    "kap" : "Бежкьа",
    "kat" : "ქართული",
    "kaz" : "Қазақша",
    "kca" : "ханты",
    "kek" : "Qʼeqchiʼ",
    "ket" : "Ket",
    "khk" : "Халх аялгуу",
    "kmr" : "Kurmancî",
    "knc" : "Kànùrí",
    "koi" : "перым-коми",
    "kor" : "한국어",
    "kpv" : "коми кыв",
    "krl" : "Karjala",
    "lat" : "lingua Latīna",
    "lav" : "Latviski",
    "lbe" : "лакку",
    "lez" : "лезги",
    "lidepla" : "Lidepla",
    "lit" : "Lietuviškai",
    "liv" : "līvõ kēļ",
    "mal" : "മലയാളം",
    "mdf" : "мокша",
    "mhr" : "олык марий",
    "mnc" : "ᠮᠠᠨᠵᡠ ᡤᡳᠰᡠᠨ",
    "mns" : "ма̄ньси",
    "mrj" : "кырык мары",
    "mww" : "Hmoob Dawb",
    "myv" : "эрзя",
    "mzh" : "wichí lhämtes",
    "nio" : "нганасаны",
    "niv" : "нивхгу",
    "nld" : "Nederlands",
    "nmm" : "ŋyeshaŋ",
    "nor" : "Norsk",
    "novial" : "Novial",
    "olo" : "Ливви",
    "orh" : "Арутчэн Уркун",
    "oss" : "ирон",
    "ote" : "Otomi",
    "pandunia" : "Pandunia",
    "pbu" : "پښتو",
    "pes" : "فارسی",
    "plt" : "malagasy",
    "pol" : "Polski",
    "por" : "português",
    "qvi" : "Kichwa Shimi",
    "rif" : "Tmaziɣt",
    "rmc" : "rromani ćhib",
    "ron" : "Românã",
    "rus" : "Русский",
    "sah" : "Саха тыла",
    "sambahsa" : "Sambahsa",
    "sel" : "шӧльӄумыт",
    "sjd" : "кӣллт са̄мь",
    "slk" : "Slovenčina",
    "slv" : "Slovenščina",
    "sma" : "åarjelsaemi",
    "sme" : "davvisámegiella",
    "smj" : "julevsámegiella",
    "smn" : "aanaarsämikielâ",
    "sms" : "nuõrttsääʹmǩiõll",
    "spa" : "Español",
    "sqi" : "Shqip",
    "srm" : "Saamáka",
    "swe" : "Svenska",
    "swh" : "Swahili",
    "tam" : "தமிழ்",
    "tat" : "Татар теле",
    "tbc" : "Takia",
    "tel" : "తెలుగు",
    "tha" : "ภาษาไทย",
    "tur" : "Türkçe",
    "tzz" : "Batsʼi kʼop",
    "udm" : "Удмурт кыл",
    "ukr" : "Українська",
    "uzn" : "oʻzbekcha",
    "vep" : "Vepsä",
    "vie" : "Tiếng Việt",
    "vol" : "Volapük",
    "xal" : "Хальмг",
    "yaq" : "Yoem Noki",
    "ykg" : "Вадул аруу",
    "yrk" : "ненэцяʼ вада",
    "yux" : "Одун ажуу"
}

code_to_english_map = {
    "abk" : "Abkhaz", #?
    "ady" : "Adyge",
    "ain" : "Ainu",
    "ale" : "Aleut", #?
    "aqc" : "Archi", #?
    "arb" : "Arabic",
    "arn" : "Mapudungun",
    "ava" : "Avar",
    "azj" : "Azeri",
    "bak" : "Bashkir",
    "bel" : "Belarussian",
    "ben" : "Bengali",
    "bre" : "Breton", #?
    "bsk" : "Burushaski",
    "bua" : "Buryad", #?
    "bul" : "Bulgarian",
    "car" : "Carib",
    "cat" : "Catalonian",
    "ces" : "Czech",
    "che" : "Nohche", #?
    "chv" : "Chuvash",
    "ckt" : "Chukot", #?
    "cmn" : "Mandarin Chinese",
    "crs" : "Seychelles Creole",
    "cwg" : "Chewong", #?
    "cym" : "Welsh",
    "dan" : "Danish",
    "dar" : "Dargan", #?
    "ddo" : "Tsez", #?
    "deu" : "German",
    "dsb" : "Sorbian", #?
    "ekk" : "Estonian",
    "ell" : "Greek",
    "enf" : "Enets",
    "eng" : "English",
    "epo" : "Esperanto",
    "ess" : "Yupik",
    "eus" : "Basque",
    "evn" : "Evenki",
    "fin" : "Finnish",
    "fra" : "French",
    "gld" : "Nanai", #?
    "gle" : "Gaelic", #?
    "goh" : "Old High German",
    "gue" : "Gurinji",
    "gwd" : "Ale",
    "hau" : "Hausa",
    "haw" : "Hawaiian",
    "heb" : "Hebrew",
    "hin" : "Hindi",
    "hrv" : "Croatian",
    "hun" : "Hungarian",
    "hye" : "Haya", #?
    "ido" : "Ido",
    "ile" : "Interlingue",
    "ina" : "Interlingua",
    "ind" : "Indonesian",
    "irk" : "Irakw", #?
    "isl" : "Icelandic",
    "ita" : "Italian",
    "itl" : "Itelmen",
    "jpn" : "Japanese",
    "jup" : "Hup", #?
    "kal" : "Inuit", #?
    "kan" : "Kannada",
    "kap" : "Bezhka", #?
    "kat" : "Kartul", #?
    "kaz" : "Kazakh",
    "kca" : "Khanti", #?
    "kek" : "Kekchi", #?
    "ket" : "Ket", #?
    "khk" : "Mongolian",
    "kmr" : "North Kurdish", #?
    "knc" : "Kanuri",
    "koi" : "Perm Komi",
    "kor" : "Korean",
    "kpv" : "Komi",
    "krl" : "Karelian",
    "lat" : "Latin",
    "lav" : "Latvian",
    "lbe" : "Laku", #?
    "lez" : "Lezgi", #?
    "lidepla" : "Lidepla",
    "lit" : "Lithuanian",
    "liv" : "Livonian",
    "mal" : "Malayalam",
    "mdf" : "Moksha", #?
    "mhr" : "Mari", #?
    "mnc" : "Manchu",
    "mns" : "Mansi",
    "mrj" : "Mari", #?
    "mww" : "Hmong",
    "myv" : "Erzya", #?
    "mzh" : "Wichi", #?
    "nio" : "Nganasan",
    "niv" : "Nivgu", #?
    "nld" : "Netherlandic", #?
    "nmm" : "Manang", #?
    "nor" : "Norwegian",
    "novial" : "Novial",
    "olo" : "Livvi Karelian",
    "orh" : "Orchun", #?
    "oss" : "Ossetian",
    "ote" : "Otomi", #?
    "pandunia" : "Pandunia",
    "pbu" : "Pashto",
    "pes" : "Persian",
    "plt" : "Malagasy",
    "pol" : "Polish",
    "por" : "Portuguese",
    "qvi" : "Kichwa",
    "rif" : "Tamazight",
    "rmc" : "Romani",
    "ron" : "Romanian",
    "rus" : "Russian",
    "sah" : "Sakha",
    "sambahsa" : "Sambahsa",
    "sel" : "Selkup",
    "sjd" : "Saami", #?
    "slk" : "Slovak",
    "slv" : "Slovenian",
    "sma" : "Saami", #?
    "sme" : "Saami", #?
    "smj" : "Saami", #?
    "smn" : "Saami", #?
    "sms" : "Saami", #?
    "spa" : "Spanish",
    "sqi" : "Albanian",
    "srm" : "Saramaccan",
    "swe" : "Swedish",
    "swh" : "Swahili",
    "tam" : "Tamil",
    "tat" : "Tatar",
    "tbc" : "Takia", #?
    "tel" : "Telugu",
    "tha" : "Thai",
    "tur" : "Turkish",
    "tzz" : "Sots", #?
    "udm" : "Udmurt",
    "ukr" : "Ukrainian",
    "uzn" : "Uzbek",
    "vep" : "Veps", #?
    "vie" : "Vietnamese",
    "vol" : "Volapuk",
    "xal" : "Mongolian Khalkha",
    "yaq" : "Yoem", #?
    "ykg" : "Vodul", #?
    "yrk" : "Nenets",
    "yux" : "Vodul" #?
}

code_to_pandunia_map = {
    "abk" : "Apse",
    "ady" : "Adige",
    "ain" : "Ainu",
    "ale" : "Aleut",
    "aqc" : "Archi",
    "arb" : "Arab",
    "arn" : "Mapudungun",
    "ava" : "Avar",
    "azj" : "Azer",
    "bak" : "Bashkorte",
    "bel" : "Belarus",
    "ben" : "Bangla",
    "bre" : "Breton",
    "bsk" : "Burushaski",
    "bua" : "Buryad",
    "bul" : "Bulgar",
    "car" : "Karib",
    "cat" : "Katalun",
    "ces" : "Cheske",
    "che" : "Nohche",
    "chv" : "Chuvash",
    "ckt" : "Chukot",
    "cmn" : "Putong Han",
    "crs" : "Seshel kreol",
    "cwg" : "Chewong",
    "cym" : "Kemre",
    "dan" : "Danske",
    "dar" : "Dargan",
    "ddo" : "Cez",
    "deu" : "Doiche",
    "dsb" : "Sorbe",
    "ekk" : "Esti",
    "ell" : "Helen",
    "enf" : "Ence",
    "eng" : "English",
    "epo" : "Esperante",
    "ess" : "Yupik",
    "eus" : "Euskal",
    "evn" : "Evenki",
    "fin" : "Suomi",
    "fra" : "Franse",
    "gld" : "Nanai",
    "gle" : "Gel",
    "goh" : "Sen Doiche",
    "gue" : "Gurinji",
    "gwd" : "Ale",
    "hau" : "Hausa",
    "haw" : "Havaii",
    "heb" : "Hibre",
    "hin" : "Hinde",
    "hrv" : "Horvat",
    "hun" : "Magyar",
    "hye" : "Haya",
    "ido" : "Ido",
    "ile" : "Interlingue",
    "ina" : "Interlingua",
    "ind" : "Indonesia",
    "irk" : "Iraku",
    "isl" : "Islande",
    "ita" : "Ital",
    "itl" : "Itelmen",
    "jpn" : "Nipon",
    "jup" : "Hup",
    "kal" : "Kalal",
    "kan" : "Karnada",
    "kap" : "Bezhka",
    "kat" : "Kartul",
    "kaz" : "Kazak",
    "kca" : "Hanti",
    "kek" : "Kekchi",
    "ket" : "Ket",
    "khk" : "Mongol",
    "kmr" : "Nor Kurde",
    "knc" : "Kanuri",
    "koi" : "Perme Komi",
    "kor" : "Chosen",
    "kpv" : "Komi",
    "krl" : "Karyala",
    "lat" : "Latin",
    "lav" : "Latve",
    "lbe" : "Laku",
    "lez" : "Lezgi",
    "lidepla" : "Lidepla",
    "lit" : "Lietuve",
    "liv" : "Livo",
    "mal" : "Malayal",
    "mdf" : "Moksha",
    "mhr" : "Mari",
    "mnc" : "Manju",
    "mns" : "Mansi",
    "mrj" : "Mari",
    "mww" : "Mong",
    "myv" : "Erzya",
    "mzh" : "Wichi",
    "nio" : "Nganasan",
    "niv" : "Nivgu",
    "nld" : "Nederlande",
    "nmm" : "Manang",
    "nor" : "Norge",
    "novial" : "Novial",
    "olo" : "Livi karyala",
    "orh" : "Orchun",
    "oss" : "Oset",
    "ote" : "Otomi",
    "pandunia" : "Pandunia",
    "pbu" : "Pashto",
    "pes" : "Farsi",
    "plt" : "Malagas",
    "pol" : "Polske",
    "por" : "Portug",
    "qvi" : "Kichua",
    "rif" : "Tamazig",
    "rmc" : "Romani",
    "ron" : "Roman",
    "rus" : "Rus",
    "sah" : "Saha",
    "sambahsa" : "Sambasha",
    "sel" : "Shelkum",
    "sjd" : "Saami",
    "slk" : "Slovak",
    "slv" : "Sloven",
    "sma" : "Saami",
    "sme" : "Saami",
    "smj" : "Saami",
    "smn" : "Saami",
    "sms" : "Saami",
    "spa" : "Espan",
    "sqi" : "Shkip",
    "srm" : "Saramaka",
    "swe" : "Sven",
    "swh" : "Suahili",
    "tam" : "Tamil",
    "tat" : "Tatar",
    "tbc" : "Takia",
    "tel" : "Telugu",
    "tha" : "Tai",
    "tur" : "Turke",
    "tzz" : "Soc",
    "udm" : "Udmurte",
    "ukr" : "Ukraina",
    "uzn" : "Uzbek",
    "vep" : "Vepsa",
    "vie" : "Viet",
    "vol" : "Volapuk",
    "xal" : "Mongol",
    "yaq" : "Yoem",
    "ykg" : "Vodul",
    "yrk" : "Nenece",
    "yux" : "Vodul"
}

def code_to_endonym(code):
    if code in code_to_endonym_map:
        lang = code_to_endonym_map[code]
        if lang != "":
            return lang
        else:
            return code
    else:
        return code

def code_to_english(code):
    if code in code_to_english_map:
        lang = code_to_english_map[code]
        if lang != "":
            return lang
        else:
            return code
    else:
        return code

def code_to_pandunia(code):
    if code in code_to_pandunia_map:
        lang = code_to_pandunia_map[code]
        if lang != "":
            return lang
        else:
            return code
    else:
        return code

def source_lang_code_to_name(code):
    if code == "eng":
        return code_to_english(code)
    elif code == "pandunia":
        return code_to_pandunia(code)
    else:
        return code_to_endonym(code)

def target_lang_code_to_name(source_lang, code):
    if source_lang == "eng":
        name = code_to_english(code) + " (" + code_to_endonym(code) + ")"
        return name
    elif source_lang == "pandunia":
        name = code_to_pandunia(code) + " (" + code_to_endonym(code) + ")"
        return name
    else:
        return code_to_endonym(code)
