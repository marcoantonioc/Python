import urllib
import urllib.request

try:
    site= urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print('O site está fora do ar !')
else:
    print(f"O site esta disponivel !")