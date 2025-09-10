import urllib
import urllib.request

try:
    url_site = urllib.request.urlopen("https://www.pudim.com.br")
except urllib.error.URLError:
    print("O site está \'Fora\' do Ar!")
else:
    print("O site \'Está\' no Ar!")
