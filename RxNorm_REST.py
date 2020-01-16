#RxNav/RxNorm RESTful resources: https://rxnav.nlm.nih.gov/RxNormAPIREST.html
#initial source code taken from: https://realpython.com/blog/python/api-integration-in-python/#appendix-rest-in-a-nutshell
#documentation: http://docs.python-requests.org/en/master/
#download: https://github.com/kennethreitz/requests
#installed on Windows via command prompt: C:\Users\[username]\Downloads\requests-master\requests-master> C:\Users\[username]\AppData\Local\Programs\Python\Python36-32\python.exe setup.py install

#Need this for RESTful request functionality:
import requests

wf = open('.\\rxNavREST_results.xml', 'w')

#some different RxNav API calls
#rxnorm = requests.get('https://rxnav.nlm.nih.gov/REST/brands?ingredientids=8896+20610')
#rxnorm = requests.get('https://rxnav.nlm.nih.gov/REST/interaction/interaction.json?rxcui=88014&sources=ONCHigh')

#Benadryl (Diphenhydraminie): RXCUI used for test: 3498
#Tylenol (Acetaminophen): RXCUI used for test: 161

#rxnorm = requests.get('https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis=3498+161')
rxnorm = requests.get('https://rxnav.nlm.nih.gov/REST/interaction/list.xml?rxcuis=3498+161')


if rxnorm.status_code != 200:
    raise ApiError('GET /tasks/ {}'.format(rxnorm.status_code))

#create newlines on close/open arrows: ><
print(str(rxnorm.content).replace('><', '>\n<'))
xmlLine = str(rxnorm.content).replace('><', '>\n<')

wf.write(xmlLine)

wf.close()
## rf.close()




