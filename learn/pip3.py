import re
text_error = '''
crcelk      1.1      1.2      sdist
httplib2    0.9.2    0.11.3   sdist
mysqlclient 1.3.10   1.3.13   sdist
pycairo     1.16.2   1.17.1   sdist
pycurl      7.43.0.1 7.43.0.2 sdist
pysmbc      1.0.15.6 1.0.15.8 sdist
pyxdg       0.25     0.26     wheel
PyYAML      3.12     3.13     sdist
XlsxWriter  0.9.6    1.0.7    wheel

'''
text ='''
beautifulsoup4      4.6.3      4.7.1      wheel
capstone            3.0.5      4.0.1      wheel
certifi             2018.8.24  2018.11.29 wheel
colorama            0.3.7      0.4.1      wheel
cryptography        2.3        2.5        wheel
decorator           4.3.0      4.3.2      wheel
distro              1.3.0      1.4.0      wheel
future              0.16.0     0.17.1     sdist
graphene            2.0.1      2.1.3      wheel
graphene-sqlalchemy 2.0.0      2.1.0      wheel
h2                  3.0.1      3.1.0      wheel
httplib2            0.11.3     0.12.0     sdist
hyperframe          5.1.0      5.2.0      wheel
idna                2.6        2.8        wheel
ipykernel           4.9.0      5.1.0      wheel
ipython             5.8.0      7.2.0      wheel
ipywidgets          6.0.0      7.4.2      wheel
iso8601             0.1.11     0.1.12     wheel
jupyter-client      5.2.3      5.2.4      wheel
jupyter-console     5.2.0      6.0.0      wheel
ldap3               2.4.1      2.5.2      wheel
msgpack             0.5.6      0.6.1      wheel
notebook            5.4.1      5.7.4      wheel
plotly              3.5.0      3.6.0      sdist
pluginbase          0.7        1.0.0      sdist
promise             2.0.1      2.2.1      sdist
prompt-toolkit      1.0.15     2.0.8      wheel
pyasn1              0.4.2      0.4.5      wheel
pycryptodomex       3.6.1      3.7.3      wheel
pyotp               2.2.6      2.2.7      wheel
pyparsing           2.2.0      2.3.1      wheel
pyperclip           1.6.4      1.7.0      sdist
pysmi               0.3.2      0.3.3      wheel
pysnmp              4.4.6      4.4.8      wheel
python-dateutil     2.6.1      2.8.0      wheel
python-editor       1.0.3      1.0.4      wheel
pyxdg               0.25       0.26       wheel
requests            2.20.0     2.21.0     wheel
ruamel.yaml         0.15.34    0.15.87    wheel
scipy               1.1.0      1.2.0      wheel
SecretStorage       2.3.1      3.1.1      wheel
Send2Trash          1.4.2      1.5.0      wheel
setuptools          40.6.3     40.8.0     wheel
sortedcontainers    2.0.4      2.1.0      wheel
SQLAlchemy          1.2.15     1.2.17     sdist
tabulate            0.8.2      0.8.3      sdist
tld                 0.9.1      0.9.2      wheel
urllib3             1.24       1.24.1     wheel
websocket-client    0.53.0     0.54.0     wheel
wheel               0.30.0     0.32.3     wheel
wsproto             0.11.0     0.13.0     wheel
'''
regex =r"([a-zA-Z\d.-]+)"
pattern = re.compile(regex)
lmatches = pattern.findall(text)
ls = []
for cha in lmatches:
    if cha =='sdist' or cha == 'wheel' or cha[0].isdigit():
        continue
    else:
        ls.append(cha)
str1 =' '.join(ls)
python3 = "pip3 install -U "
print(str1)
# print(lmatche[0])
