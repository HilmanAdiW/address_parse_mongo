import os

# DB Configuration
db_hosts = [{'host': os.getenv('ES_HOST', '124.41.211.23'), 'port': os.getenv('ES_PORT', '9007')}]
# ElasticSearch authetication details
http_auth = (os.getenv('ES_USER', 'elastic'), os.getenv('ES_PASSWORD', '02MzdT9hHyftrzWCxpOs'))

# threshold value for address verification score
THRESHOLD = 85

# language to parse the address , options : ['id','en']
LANG = 'id'

# corresponding translation of en to id
LANG_MAPPING_ID_EN = {"street": "jalan",
                      "other": "lainnya",
                      "house number": "nomor_rumah",
                      "locality": "lokalitas",
                      "name_company": "nama_perusahaan",
                      "postal_code": "kode_pos",
                      "village": "desa",
                      "district": "distrik",
                      "city": "kota",
                      "regency": "kabupaten",
                      "province": "provinsi"}

# list of address tags in en
ADDRESS_TAGS_EN = list(LANG_MAPPING_ID_EN.keys())

def get_address_tags():
    choice_en = list(LANG_MAPPING_ID_EN.keys())
    choice_id = list(LANG_MAPPING_ID_EN.values())
    return choice_id if LANG == 'id' else choice_en
