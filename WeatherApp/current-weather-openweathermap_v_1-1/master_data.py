
# match_country_name()
# match_city()
# get_citys()

###


def match_country_name():

    name = {'AW': 'Aruba',
            'AF': 'Afghanistan',
            'AO': 'Angola',
            'AL': 'Albania',
            'AD': 'Andorra',
            'AE': 'United Arab Emirates',
            'AR': 'Argentina',
            'AM': 'Armenia',
            'AS': 'American Samoa',
            'AG': 'Antigua and Barbuda',
            'AU': 'Australia',
            'AT': 'Austria',
            'AZ': 'Azerbaijan',
            'BI': 'Burundi',
            'BE': 'Belgium',
            'BJ': 'Benin',
            'BF': 'Burkina Faso',
            'BD': 'Bangladesh',
            'BG': 'Bulgaria',
            'BH': 'Bahrain',
            'BS': 'Bahamas, The',
            'BA': 'Bosnia and Herzegovina',
            'BY': 'Belarus',
            'BZ': 'Belize',
            'BM': 'Bermuda',
            'BO': 'Bolivia',
            'BR': 'Brazil',
            'BB': 'Barbados',
            'BN': 'Brunei Darussalam',
            'BT': 'Bhutan',
            'BW': 'Botswana',
            'CF': 'Central African Republic',
            'CA': 'Canada',
            'CH': 'Switzerland',
            'CL': 'Chile',
            'CN': 'China',
            'CI': "Cote d'Ivoire",
            'CM': 'Cameroon',
            'CD': 'Congo, Dem. Rep.',
            'CG': 'Congo, Rep.',
            'CO': 'Colombia',
            'KM': 'Comoros',
            'CV': 'Cabo Verde',
            'CR': 'Costa Rica',
            'CU': 'Cuba',
            'CW': 'Curacao',
            'KY': 'Cayman Islands',
            'CY': 'Cyprus',
            'CZ': 'Czech Republic',
            'DE': 'Germany',
            'DJ': 'Djibouti',
            'DM': 'Dominica',
            'DK': 'Denmark',
            'DO': 'Dominican Republic',
            'DZ': 'Algeria',
            'EC': 'Ecuador',
            'EG': 'Egypt, Arab Rep.',
            'ER': 'Eritrea',
            'ES': 'Spain',
            'EE': 'Estonia',
            'ET': 'Ethiopia',
            'FI': 'Finland',
            'FJ': 'Fiji',
            'FR': 'France',
            'FO': 'Faroe Islands',
            'FM': 'Micronesia, Fed. Sts.',
            'GA': 'Gabon',
            'GB': 'United Kingdom',
            'GE': 'Georgia',
            'GH': 'Ghana',
            'GN': 'Guinea',
            'GM': 'Gambia, The',
            'GW': 'Guinea-Bissau',
            'GQ': 'Equatorial Guinea',
            'GR': 'Greece',
            'GD': 'Grenada',
            'GL': 'Greenland',
            'GT': 'Guatemala',
            'GU': 'Guam',
            'GY': 'Guyana',
            'HN': 'Honduras',
            'HR': 'Croatia',
            'HT': 'Haiti',
            'HU': 'Hungary',
            'ID': 'Indonesia',
            'IM': 'Isle of Man',
            'IN': 'India',
            'IE': 'Ireland',
            'IR': 'Iran, Islamic Rep.',
            'IQ': 'Iraq',
            'IS': 'Iceland',
            'IT': 'Italy',
            'JM': 'Jamaica',
            'JO': 'Jordan',
            'JP': 'Japan',
            'KZ': 'Kazakhstan',
            'KE': 'Kenya',
            'KG': 'Kyrgyz Republic',
            'KH': 'Cambodia',
            'KI': 'Kiribati',
            'KN': 'St. Kitts and Nevis',
            'KR': 'Korea, Rep.',
            'KW': 'Kuwait',
            'LA': 'Lao PDR',
            'LB': 'Lebanon',
            'LR': 'Liberia',
            'LY': 'Libya',
            'LC': 'St. Lucia',
            'LI': 'Liechtenstein',
            'LK': 'Sri Lanka',
            'LS': 'Lesotho',
            'LT': 'Lithuania',
            'LU': 'Luxembourg',
            'LV': 'Latvia',
            'MF': 'St. Martin (French part)',
            'MA': 'Morocco',
            'MC': 'Monaco',
            'MD': 'Moldova',
            'MG': 'Madagascar',
            'MV': 'Maldives',
            'MX': 'Mexico',
            'MH': 'Marshall Islands',
            'MK': 'North Macedonia',
            'ML': 'Mali',
            'MT': 'Malta',
            'MM': 'Myanmar',
            'ME': 'Montenegro',
            'MN': 'Mongolia',
            'MP': 'Northern Mariana Islands',
            'MZ': 'Mozambique',
            'MR': 'Mauritania',
            'MU': 'Mauritius',
            'MW': 'Malawi',
            'MY': 'Malaysia',
            'NC': 'New Caledonia',
            'NE': 'Niger',
            'NG': 'Nigeria',
            'NI': 'Nicaragua',
            'NL': 'Netherlands',
            'NO': 'Norway',
            'NP': 'Nepal',
            'NR': 'Nauru',
            'NZ': 'New Zealand',
            'OM': 'Oman',
            'PK': 'Pakistan',
            'PA': 'Panama',
            'PE': 'Peru',
            'PH': 'Philippines',
            'PW': 'Palau',
            'PG': 'Papua New Guinea',
            'PL': 'Poland',
            'PR': 'Puerto Rico',
            'KP': 'Korea, Dem. People’s Rep.',
            'PT': 'Portugal',
            'PY': 'Paraguay',
            'PF': 'French Polynesia',
            'QA': 'Qatar',
            'RO': 'Romania',
            'RU': 'Russian Federation',
            'RW': 'Rwanda',
            'SA': 'Saudi Arabia',
            'SD': 'Sudan',
            'SN': 'Senegal',
            'SG': 'Singapore',
            'SB': 'Solomon Islands',
            'SL': 'Sierra Leone',
            'SV': 'El Salvador',
            'SM': 'San Marino',
            'SO': 'Somalia',
            'RS': 'Serbia',
            'SS': 'South Sudan',
            'ST': 'Sao Tome and Principe',
            'SR': 'Suriname',
            'SK': 'Slovak Republic',
            'SI': 'Slovenia',
            'SE': 'Sweden',
            'SZ': 'Eswatini',
            'SX': 'Sint Maarten (Dutch part)',
            'SC': 'Seychelles',
            'SY': 'Syrian Arab Republic',
            'TC': 'Turks and Caicos Islands',
            'TD': 'Chad',
            'TG': 'Togo',
            'TH': 'Thailand',
            'TJ': 'Tajikistan',
            'TM': 'Turkmenistan',
            'TL': 'Timor-Leste',
            'TO': 'Tonga',
            'TT': 'Trinidad and Tobago',
            'TN': 'Tunisia',
            'TR': 'Turkey',
            'TV': 'Tuvalu',
            'TZ': 'Tanzania',
            'UG': 'Uganda',
            'UA': 'Ukraine',
            'UY': 'Uruguay',
            'US': 'United States',
            'UZ': 'Uzbekistan',
            'VC': 'St. Vincent and the Grenadines',
            'VE': 'Venezuela, RB',
            'VG': 'British Virgin Islands',
            'VI': 'Virgin Islands (U.S.)',
            'VN': 'Vietnam',
            'VU': 'Vanuatu',
            'WS': 'Samoa',
            'XK': 'Kosovo',
            'YE': 'Yemen, Rep.',
            'ZA': 'South Africa',
            'ZM': 'Zambia',
            'ZW': 'Zimbabwe'}

    return name


def match_icon(icons):

    icon = {"01d": "wi wi-day-clear",
            "01n": "wi wi-night-clear",
            "02d": "wi wi-day-cloudy",
            "02n": "wi wi-night-cloudy",
            "03d": "wi wi-day-cloudy",
            "03n": "wi wi-night-cloudy",
            "09d": "wi wi-day-showers",
            "09n": "wi wi-night-showers",
            "10d": "wi wi-day-rain",
            "10n": "wi wi-night-rain",
            "11d": "wi wi-day-thunderstorm",
            "11n": "wi wi-night-thunderstorm",
            "13d": "wi wi-day-snow",
            "13n": "wi wi-night-snow",
            "50d": "wi wi-day-sunny-overcast",
            }

    if icons in icon:
        icons_class = icon[icons]
    else:
        icons_class = "wi wi-day-sunny"

    return icons_class

def match_icon_animate(icons):
    
    icon = {"01d": "day",
            "01n": "night",
            "02d": "cloudy-day-1",
            "02n": "cloudy-night-1",
            "03d": "cloudy-day-2",
            "03n": "cloudy-night-2",
            "04d": "cloudy-day-3",
            "04n": "cloudy-night-3",
            "09d": "rainy-1",
            "09n": "rainy-4",
            "10d": "rainy-3",
            "10n": "rainy-7",
            "11d": "thunder",
            "11n": "thunder",
            "13d": "snowy-3",
            "13n": "snowy-6",
            "50d": "weather",
            "50n": "weather",
            
            }

    if icons in icon:
        icons_class = icon[icons]
    else:
        icons_class = "weather"

    return icons_class

def match_city():

    city = {'Oranjestad': 'AW',
            'Kabul': 'AF',
            'Luanda': 'AO',
            'Tirane': 'AL',
            'Andorra la Vella': 'AD',
            'Abu Dhabi': 'AE',
            'Buenos Aires': 'AR',
            'Yerevan': 'AM',
            'Pago Pago': 'AS',
            "Saint John's": 'AG',
            'Canberra': 'AU',
            'Vienna': 'AT',
            'Baku': 'AZ',
            'Bujumbura': 'BI',
            'Brussels': 'BE',
            'Porto-Novo': 'BJ',
            'Ouagadougou': 'BF',
            'Dhaka': 'BD',
            'Sofia': 'BG',
            'Manama': 'BH',
            'Nassau': 'BS',
            'Sarajevo': 'BA',
            'Minsk': 'BY',
            'Belmopan': 'BZ',
            'Hamilton': 'BM',
            'La Paz': 'BO',
            'Brasilia': 'BR',
            'Bridgetown': 'BB',
            'Bandar Seri Begawan': 'BN',
            'Thimphu': 'BT',
            'Gaborone': 'BW',
            'Bangui': 'CF',
            'Ottawa': 'CA',
            'Bern': 'CH',
            'Santiago': 'CL',
            'Beijing': 'CN',
            'Yamoussoukro': 'CI',
            'Yaounde': 'CM',
            'Kinshasa': 'CD',
            'Brazzaville': 'CG',
            'Bogota': 'CO',
            'Moroni': 'KM',
            'Praia': 'CV',
            'San Jose': 'CR',
            'Havana': 'CU',
            'Willemstad': 'CW',
            'George Town': 'KY',
            'Nicosia': 'CY',
            'Prague': 'CZ',
            'Berlin': 'DE',
            'Djibouti': 'DJ',
            'Roseau': 'DM',
            'Copenhagen': 'DK',
            'Santo Domingo': 'DO',
            'Algiers': 'DZ',
            'Quito': 'EC',
            'Cairo': 'EG',
            'Asmara': 'ER',
            'Madrid': 'ES',
            'Tallinn': 'EE',
            'Addis Ababa': 'ET',
            'Helsinki': 'FI',
            'Suva': 'FJ',
            'Paris': 'FR',
            'Torshavn': 'FO',
            'Palikir': 'FM',
            'Libreville': 'GA',
            'London': 'GB',
            'Tbilisi': 'GE',
            'Accra': 'GH',
            'Conakry': 'GN',
            'Banjul': 'GM',
            'Bissau': 'GW',
            'Malabo': 'GQ',
            'Athens': 'GR',
            "Saint George's": 'GD',
            'Nuuk': 'GL',
            'Guatemala City': 'GT',
            'Agana': 'GU',
            'Georgetown': 'GY',
            'Tegucigalpa': 'HN',
            'Zagreb': 'HR',
            'Port-au-Prince': 'HT',
            'Budapest': 'HU',
            'Jakarta': 'ID',
            'Douglas': 'IM',
            'New Delhi': 'IN',
            'Dublin': 'IE',
            'Tehran': 'IR',
            'Baghdad': 'IQ',
            'Reykjavik': 'IS',
            'Rome': 'IT',
            'Kingston': 'JM',
            'Amman': 'JO',
            'Tokyo': 'JP',
            'Astana': 'KZ',
            'Nairobi': 'KE',
            'Bishkek': 'KG',
            'Phnom Penh': 'KH',
            'Tarawa': 'KI',
            'Basseterre': 'KN',
            'Seoul': 'KR',
            'Kuwait City': 'KW',
            'Vientiane': 'LA',
            'Beirut': 'LB',
            'Monrovia': 'LR',
            'Tripoli': 'LY',
            'Castries': 'LC',
            'Vaduz': 'LI',
            'Colombo': 'LK',
            'Maseru': 'LS',
            'Vilnius': 'LT',
            'Luxembourg': 'LU',
            'Riga': 'LV',
            'Marigot': 'MF',
            'Rabat': 'MA',
            'Monaco': 'MC',
            'Chisinau': 'MD',
            'Antananarivo': 'MG',
            'Male': 'MV',
            'Mexico City': 'MX',
            'Majuro': 'MH',
            'Skopje': 'MK',
            'Bamako': 'ML',
            'Valletta': 'MT',
            'Naypyidaw': 'MM',
            'Podgorica': 'ME',
            'Ulaanbaatar': 'MN',
            'Saipan': 'MP',
            'Maputo': 'MZ',
            'Nouakchott': 'MR',
            'Port Louis': 'MU',
            'Lilongwe': 'MW',
            'Kuala Lumpur': 'MY',
            "Noum'ea": 'NC',
            'Niamey': 'NE',
            'Abuja': 'NG',
            'Managua': 'NI',
            'Amsterdam': 'NL',
            'Oslo': 'NO',
            'Kathmandu': 'NP',
            'Yaren District': 'NR',
            'Wellington': 'NZ',
            'Muscat': 'OM',
            'Islamabad': 'PK',
            'Panama City': 'PA',
            'Lima': 'PE',
            'Manila': 'PH',
            'Koror': 'PW',
            'Port Moresby': 'PG',
            'Warsaw': 'PL',
            'San Juan': 'PR',
            'Pyongyang': 'KP',
            'Lisbon': 'PT',
            'Asuncion': 'PY',
            'Papeete': 'PF',
            'Doha': 'QA',
            'Bucharest': 'RO',
            'Moscow': 'RU',
            'Kigali': 'RW',
            'Riyadh': 'SA',
            'Khartoum': 'SD',
            'Dakar': 'SN',
            'Singapore': 'SG',
            'Honiara': 'SB',
            'Freetown': 'SL',
            'San Salvador': 'SV',
            'San Marino': 'SM',
            'Mogadishu': 'SO',
            'Belgrade': 'RS',
            'Juba': 'SS',
            'Sao Tome': 'ST',
            'Paramaribo': 'SR',
            'Bratislava': 'SK',
            'Ljubljana': 'SI',
            'Stockholm': 'SE',
            'Mbabane': 'SZ',
            'Philipsburg': 'SX',
            'Victoria': 'SC',
            'Damascus': 'SY',
            'Grand Turk': 'TC',
            "N'Djamena": 'TD',
            'Lome': 'TG',
            'Bangkok': 'TH',
            'Dushanbe': 'TJ',
            'Ashgabat': 'TM',
            'Dili': 'TL',
            "Nuku'alofa": 'TO',
            'Port-of-Spain': 'TT',
            'Tunis': 'TN',
            'Ankara': 'TR',
            'Funafuti': 'TV',
            'Dodoma': 'TZ',
            'Kampala': 'UG',
            'Kiev': 'UA',
            'Montevideo': 'UY',
            'Washington D.C.': 'US',
            'Tashkent': 'UZ',
            'Kingstown': 'VC',
            'Caracas': 'VE',
            'Road Town': 'VG',
            'Charlotte Amalie': 'VI',
            'Hanoi': 'VN',
            'Port-Vila': 'VU',
            'Apia': 'WS',
            'Pristina': 'XK',
            "Sana'a": 'YE',
            'Pretoria': 'ZA',
            'Lusaka': 'ZM',
            'Harare': 'ZW'}
    return city


def get_citys():

    data = {'Oranjestad, Aruba': 'Oranjestad,AW',
            'Kabul, Afghanistan': 'Kabul,AF',
            'Luanda, Angola': 'Luanda,AO',
            'Tirane, Albania': 'Tirane,AL',
            'Andorra la Vella, Andorra': 'Andorra la Vella,AD',
            'Abu Dhabi, United Arab Emirates': 'Abu Dhabi,AE',
            'Buenos Aires, Argentina': 'Buenos Aires,AR',
            'Yerevan, Armenia': 'Yerevan,AM',
            'Pago Pago, American Samoa': 'Pago Pago,AS',
            "Saint John's, Antigua and Barbuda": "Saint John's,AG",
            'Canberra, Australia': 'Canberra,AU',
            'Vienna, Austria': 'Vienna,AT',
            'Baku, Azerbaijan': 'Baku,AZ',
            'Bujumbura, Burundi': 'Bujumbura,BI',
            'Brussels, Belgium': 'Brussels,BE',
            'Porto-Novo, Benin': 'Porto-Novo,BJ',
            'Ouagadougou, Burkina Faso': 'Ouagadougou,BF',
            'Dhaka, Bangladesh': 'Dhaka,BD',
            'Sofia, Bulgaria': 'Sofia,BG',
            'Manama, Bahrain': 'Manama,BH',
            'Nassau, Bahamas, The': 'Nassau,BS',
            'Sarajevo, Bosnia and Herzegovina': 'Sarajevo,BA',
            'Minsk, Belarus': 'Minsk,BY',
            'Belmopan, Belize': 'Belmopan,BZ',
            'Hamilton, Bermuda': 'Hamilton,BM',
            'La Paz, Bolivia': 'La Paz,BO',
            'Brasilia, Brazil': 'Brasilia,BR',
            'Bridgetown, Barbados': 'Bridgetown,BB',
            'Bandar Seri Begawan, Brunei Darussalam': 'Bandar Seri Begawan,BN',
            'Thimphu, Bhutan': 'Thimphu,BT',
            'Gaborone, Botswana': 'Gaborone,BW',
            'Bangui, Central African Republic': 'Bangui,CF',
            'Ottawa, Canada': 'Ottawa,CA',
            'Bern, Switzerland': 'Bern,CH',
            'Santiago, Chile': 'Santiago,CL',
            'Beijing, China': 'Beijing,CN',
            "Yamoussoukro, Cote d'Ivoire": 'Yamoussoukro,CI',
            'Yaounde, Cameroon': 'Yaounde,CM',
            'Kinshasa, Congo, Dem. Rep.': 'Kinshasa,CD',
            'Brazzaville, Congo, Rep.': 'Brazzaville,CG',
            'Bogota, Colombia': 'Bogota,CO',
            'Moroni, Comoros': 'Moroni,KM',
            'Praia, Cabo Verde': 'Praia,CV',
            'San Jose, Costa Rica': 'San Jose,CR',
            'Havana, Cuba': 'Havana,CU',
            'Willemstad, Curacao': 'Willemstad,CW',
            'George Town, Cayman Islands': 'George Town,KY',
            'Nicosia, Cyprus': 'Nicosia,CY',
            'Prague, Czech Republic': 'Prague,CZ',
            'Berlin, Germany': 'Berlin,DE',
            'Djibouti, Djibouti': 'Djibouti,DJ',
            'Roseau, Dominica': 'Roseau,DM',
            'Copenhagen, Denmark': 'Copenhagen,DK',
            'Santo Domingo, Dominican Republic': 'Santo Domingo,DO',
            'Algiers, Algeria': 'Algiers,DZ',
            'Quito, Ecuador': 'Quito,EC',
            'Cairo, Egypt, Arab Rep.': 'Cairo,EG',
            'Asmara, Eritrea': 'Asmara,ER',
            'Madrid, Spain': 'Madrid,ES',
            'Tallinn, Estonia': 'Tallinn,EE',
            'Addis Ababa, Ethiopia': 'Addis Ababa,ET',
            'Helsinki, Finland': 'Helsinki,FI',
            'Suva, Fiji': 'Suva,FJ',
            'Paris, France': 'Paris,FR',
            'Torshavn, Faroe Islands': 'Torshavn,FO',
            'Palikir, Micronesia, Fed. Sts.': 'Palikir,FM',
            'Libreville, Gabon': 'Libreville,GA',
            'London, United Kingdom': 'London,GB',
            'Tbilisi, Georgia': 'Tbilisi,GE',
            'Accra, Ghana': 'Accra,GH',
            'Conakry, Guinea': 'Conakry,GN',
            'Banjul, Gambia, The': 'Banjul,GM',
            'Bissau, Guinea-Bissau': 'Bissau,GW',
            'Malabo, Equatorial Guinea': 'Malabo,GQ',
            'Athens, Greece': 'Athens,GR',
            "Saint George's, Grenada": "Saint George's,GD",
            'Nuuk, Greenland': 'Nuuk,GL',
            'Guatemala City, Guatemala': 'Guatemala City,GT',
            'Agana, Guam': 'Agana,GU',
            'Georgetown, Guyana': 'Georgetown,GY',
            'Tegucigalpa, Honduras': 'Tegucigalpa,HN',
            'Zagreb, Croatia': 'Zagreb,HR',
            'Port-au-Prince, Haiti': 'Port-au-Prince,HT',
            'Budapest, Hungary': 'Budapest,HU',
            'Jakarta, Indonesia': 'Jakarta,ID',
            'Douglas, Isle of Man': 'Douglas,IM',
            'New Delhi, India': 'New Delhi,IN',
            'Dublin, Ireland': 'Dublin,IE',
            'Tehran, Iran, Islamic Rep.': 'Tehran,IR',
            'Baghdad, Iraq': 'Baghdad,IQ',
            'Reykjavik, Iceland': 'Reykjavik,IS',
            'Rome, Italy': 'Rome,IT',
            'Kingston, Jamaica': 'Kingston,JM',
            'Amman, Jordan': 'Amman,JO',
            'Tokyo, Japan': 'Tokyo,JP',
            'Astana, Kazakhstan': 'Astana,KZ',
            'Nairobi, Kenya': 'Nairobi,KE',
            'Bishkek, Kyrgyz Republic': 'Bishkek,KG',
            'Phnom Penh, Cambodia': 'Phnom Penh,KH',
            'Tarawa, Kiribati': 'Tarawa,KI',
            'Basseterre, St. Kitts and Nevis': 'Basseterre,KN',
            'Seoul, Korea, Rep.': 'Seoul,KR',
            'Kuwait City, Kuwait': 'Kuwait City,KW',
            'Vientiane, Lao PDR': 'Vientiane,LA',
            'Beirut, Lebanon': 'Beirut,LB',
            'Monrovia, Liberia': 'Monrovia,LR',
            'Tripoli, Libya': 'Tripoli,LY',
            'Castries, St. Lucia': 'Castries,LC',
            'Vaduz, Liechtenstein': 'Vaduz,LI',
            'Colombo, Sri Lanka': 'Colombo,LK',
            'Maseru, Lesotho': 'Maseru,LS',
            'Vilnius, Lithuania': 'Vilnius,LT',
            'Luxembourg, Luxembourg': 'Luxembourg,LU',
            'Riga, Latvia': 'Riga,LV',
            'Marigot, St. Martin (French part)': 'Marigot,MF',
            'Rabat, Morocco': 'Rabat,MA',
            'Monaco, Monaco': 'Monaco,MC',
            'Chisinau, Moldova': 'Chisinau,MD',
            'Antananarivo, Madagascar': 'Antananarivo,MG',
            'Male, Maldives': 'Male,MV',
            'Mexico City, Mexico': 'Mexico City,MX',
            'Majuro, Marshall Islands': 'Majuro,MH',
            'Skopje, North Macedonia': 'Skopje,MK',
            'Bamako, Mali': 'Bamako,ML',
            'Valletta, Malta': 'Valletta,MT',
            'Naypyidaw, Myanmar': 'Naypyidaw,MM',
            'Podgorica, Montenegro': 'Podgorica,ME',
            'Ulaanbaatar, Mongolia': 'Ulaanbaatar,MN',
            'Saipan, Northern Mariana Islands': 'Saipan,MP',
            'Maputo, Mozambique': 'Maputo,MZ',
            'Nouakchott, Mauritania': 'Nouakchott,MR',
            'Port Louis, Mauritius': 'Port Louis,MU',
            'Lilongwe, Malawi': 'Lilongwe,MW',
            'Kuala Lumpur, Malaysia': 'Kuala Lumpur,MY',
            "Noum'ea, New Caledonia": "Noum'ea,NC",
            'Niamey, Niger': 'Niamey,NE',
            'Abuja, Nigeria': 'Abuja,NG',
            'Managua, Nicaragua': 'Managua,NI',
            'Amsterdam, Netherlands': 'Amsterdam,NL',
            'Oslo, Norway': 'Oslo,NO',
            'Kathmandu, Nepal': 'Kathmandu,NP',
            'Yaren District, Nauru': 'Yaren District,NR',
            'Wellington, New Zealand': 'Wellington,NZ',
            'Muscat, Oman': 'Muscat,OM',
            'Islamabad, Pakistan': 'Islamabad,PK',
            'Panama City, Panama': 'Panama City,PA',
            'Lima, Peru': 'Lima,PE',
            'Manila, Philippines': 'Manila,PH',
            'Koror, Palau': 'Koror,PW',
            'Port Moresby, Papua New Guinea': 'Port Moresby,PG',
            'Warsaw, Poland': 'Warsaw,PL',
            'San Juan, Puerto Rico': 'San Juan,PR',
            'Pyongyang, Korea, Dem. People’s Rep.': 'Pyongyang,KP',
            'Lisbon, Portugal': 'Lisbon,PT',
            'Asuncion, Paraguay': 'Asuncion,PY',
            'Papeete, French Polynesia': 'Papeete,PF',
            'Doha, Qatar': 'Doha,QA',
            'Bucharest, Romania': 'Bucharest,RO',
            'Moscow, Russian Federation': 'Moscow,RU',
            'Kigali, Rwanda': 'Kigali,RW',
            'Riyadh, Saudi Arabia': 'Riyadh,SA',
            'Khartoum, Sudan': 'Khartoum,SD',
            'Dakar, Senegal': 'Dakar,SN',
            'Singapore, Singapore': 'Singapore,SG',
            'Honiara, Solomon Islands': 'Honiara,SB',
            'Freetown, Sierra Leone': 'Freetown,SL',
            'San Salvador, El Salvador': 'San Salvador,SV',
            'San Marino, San Marino': 'San Marino,SM',
            'Mogadishu, Somalia': 'Mogadishu,SO',
            'Belgrade, Serbia': 'Belgrade,RS',
            'Juba, South Sudan': 'Juba,SS',
            'Sao Tome, Sao Tome and Principe': 'Sao Tome,ST',
            'Paramaribo, Suriname': 'Paramaribo,SR',
            'Bratislava, Slovak Republic': 'Bratislava,SK',
            'Ljubljana, Slovenia': 'Ljubljana,SI',
            'Stockholm, Sweden': 'Stockholm,SE',
            'Mbabane, Eswatini': 'Mbabane,SZ',
            'Philipsburg, Sint Maarten (Dutch part)': 'Philipsburg,SX',
            'Victoria, Seychelles': 'Victoria,SC',
            'Damascus, Syrian Arab Republic': 'Damascus,SY',
            'Grand Turk, Turks and Caicos Islands': 'Grand Turk,TC',
            "N'Djamena, Chad": "N'Djamena,TD",
            'Lome, Togo': 'Lome,TG',
            'Bangkok, Thailand': 'Bangkok,TH',
            'Dushanbe, Tajikistan': 'Dushanbe,TJ',
            'Ashgabat, Turkmenistan': 'Ashgabat,TM',
            'Dili, Timor-Leste': 'Dili,TL',
            "Nuku'alofa, Tonga": "Nuku'alofa,TO",
            'Port-of-Spain, Trinidad and Tobago': 'Port-of-Spain,TT',
            'Tunis, Tunisia': 'Tunis,TN',
            'Ankara, Turkey': 'Ankara,TR',
            'Funafuti, Tuvalu': 'Funafuti,TV',
            'Dodoma, Tanzania': 'Dodoma,TZ',
            'Kampala, Uganda': 'Kampala,UG',
            'Kiev, Ukraine': 'Kiev,UA',
            'Montevideo, Uruguay': 'Montevideo,UY',
            'Washington D.C., United States': 'Washington D.C.,US',
            'Tashkent, Uzbekistan': 'Tashkent,UZ',
            'Kingstown, St. Vincent and the Grenadines': 'Kingstown,VC',
            'Caracas, Venezuela, RB': 'Caracas,VE',
            'Road Town, British Virgin Islands': 'Road Town,VG',
            'Charlotte Amalie, Virgin Islands (U.S.)': 'Charlotte Amalie,VI',
            'Hanoi, Vietnam': 'Hanoi,VN',
            'Port-Vila, Vanuatu': 'Port-Vila,VU',
            'Apia, Samoa': 'Apia,WS',
            'Pristina, Kosovo': 'Pristina,XK',
            "Sana'a, Yemen, Rep.": "Sana'a,YE",
            'Pretoria, South Africa': 'Pretoria,ZA',
            'Lusaka, Zambia': 'Lusaka,ZM',
            'Harare, Zimbabwe': 'Harare,ZW'}

    return data


def imports_city():

    data = ['Abu Dhabi,AE',
            'Abuja,NG',
            'Accra,GH',
            'Addis Ababa,ET',
            'Agana,GU',
            'Algiers,DZ',
            'Amman,JO',
            'Amsterdam,NL',
            'Andorra la Vella,AD',
            'Ankara,TR',
            'Antananarivo,MG',
            'Apia,WS',
            'Ashgabat,TM',
            'Asmara,ER',
            'Astana,KZ',
            'Asuncion,PY',
            'Athens,GR',
            'Baghdad,IQ',
            'Baku,AZ',
            'Bamako,ML',
            'Bandar Seri Begawan,BN',
            'Bangkok,TH',
            'Bangui,CF',
            'Banjul,GM',
            'Basseterre,KN',
            'Beijing,CN',
            'Beirut,LB',
            'Belgrade,RS',
            'Belmopan,BZ',
            'Berlin,DE',
            'Bern,CH',
            'Bishkek,KG',
            'Bissau,GW',
            'Bogota,CO',
            'Brasilia,BR',
            'Bratislava,SK',
            'Brazzaville,CG',
            'Bridgetown,BB',
            'Brussels,BE',
            'Bucharest,RO',
            'Budapest,HU',
            'Buenos Aires,AR',
            'Bujumbura,BI',
            'Cairo,EG',
            'Canberra,AU',
            'Caracas,VE',
            'Castries,LC',
            'Charlotte Amalie,VI',
            'Chisinau,MD',
            'Colombo,LK',
            'Conakry,GN',
            'Copenhagen,DK',
            'Dakar,SN',
            'Damascus,SY',
            'Dhaka,BD',
            'Dili,TL',
            'Djibouti,DJ',
            'Dodoma,TZ',
            'Doha,QA',
            'Douglas,IM',
            'Dublin,IE',
            'Dushanbe,TJ',
            'Freetown,SL',
            'Funafuti,TV',
            'Gaborone,BW',
            'George Town,KY',
            'Georgetown,GY',
            'Grand Turk,TC',
            'Guatemala City,GT',
            'Hamilton,BM',
            'Hanoi,VN',
            'Harare,ZW',
            'Havana,CU',
            'Helsinki,FI',
            'Honiara,SB',
            'Islamabad,PK',
            'Jakarta,ID',
            'Juba,SS',
            'Kabul,AF',
            'Kampala,UG',
            'Kathmandu,NP',
            'Khartoum,SD',
            'Kiev,UA',
            'Kigali,RW',
            'Kingston,JM',
            'Kingstown,VC',
            'Kinshasa,CD',
            'Koror,PW',
            'Kuala Lumpur,MY',
            'Kuwait City,KW',
            'La Paz,BO',
            'Libreville,GA',
            'Lilongwe,MW',
            'Lima,PE',
            'Lisbon,PT',
            'Ljubljana,SI',
            'Lome,TG',
            'London,GB',
            'Luanda,AO',
            'Lusaka,ZM',
            'Luxembourg,LU',
            'Madrid,ES',
            'Majuro,MH',
            'Malabo,GQ',
            'Male,MV',
            'Managua,NI',
            'Manama,BH',
            'Manila,PH',
            'Maputo,MZ',
            'Marigot,MF',
            'Maseru,LS',
            'Mbabane,SZ',
            'Mexico City,MX',
            'Minsk,BY',
            'Mogadishu,SO',
            'Monaco,MC',
            'Monrovia,LR',
            'Montevideo,UY',
            'Moroni,KM',
            'Moscow,RU',
            'Muscat,OM',
            "N'Djamena,TD",
            'Nairobi,KE',
            'Nassau,BS',
            'Naypyidaw,MM',
            'New Delhi,IN',
            'Niamey,NE',
            'Nicosia,CY',
            'Nouakchott,MR',
            "Noum'ea,NC",
            "Nuku'alofa,TO",
            'Nuuk,GL',
            'Oranjestad,AW',
            'Oslo,NO',
            'Ottawa,CA',
            'Ouagadougou,BF',
            'Pago Pago,AS',
            'Palikir,FM',
            'Panama City,PA',
            'Papeete,PF',
            'Paramaribo,SR',
            'Paris,FR',
            'Philipsburg,SX',
            'Phnom Penh,KH',
            'Podgorica,ME',
            'Port Louis,MU',
            'Port Moresby,PG',
            'Port-Vila,VU',
            'Port-au-Prince,HT',
            'Port-of-Spain,TT',
            'Porto-Novo,BJ',
            'Prague,CZ',
            'Praia,CV',
            'Pretoria,ZA',
            'Pristina,XK',
            'Pyongyang,KP',
            'Quito,EC',
            'Rabat,MA',
            'Reykjavik,IS',
            'Riga,LV',
            'Riyadh,SA',
            'Road Town,VG',
            'Rome,IT',
            'Roseau,DM',
            "Saint George's,GD",
            "Saint John's,AG",
            'Saipan,MP',
            'San Jose,CR',
            'San Juan,PR',
            'San Marino,SM',
            'San Salvador,SV',
            "Sana'a,YE",
            'Santiago,CL',
            'Santo Domingo,DO',
            'Sao Tome,ST',
            'Sarajevo,BA',
            'Seoul,KR',
            'Singapore,SG',
            'Skopje,MK',
            'Sofia,BG',
            'Stockholm,SE',
            'Suva,FJ',
            'Tallinn,EE',
            'Tarawa,KI',
            'Tashkent,UZ',
            'Tbilisi,GE',
            'Tegucigalpa,HN',
            'Tehran,IR',
            'Thimphu,BT',
            'Tirane,AL',
            'Tokyo,JP',
            'Torshavn,FO',
            'Tripoli,LY',
            'Tunis,TN',
            'Ulaanbaatar,MN',
            'Vaduz,LI',
            'Valletta,MT',
            'Victoria,SC',
            'Vienna,AT',
            'Vientiane,LA',
            'Vilnius,LT',
            'Warsaw,PL',
            'Washington D.C.,US',
            'Wellington,NZ',
            'Willemstad,CW',
            'Yamoussoukro,CI',
            'Yaounde,CM',
            'Yaren District,NR',
            'Yerevan,AM',
            'Zagreb,HR']

    return data
