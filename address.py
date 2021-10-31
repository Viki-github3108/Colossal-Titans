print("welcome to aadhar update center")
print("1.verify the captcha")
import requests
from requests.auth import HTTPBasicAuth
#headers = {'content-type':'application/python'}
#headers={'content-type':'application/json', 'Accept':'application/json'}
url = 'https://stage1.uidai.gov.in/unifiedAppAuthService/api/v2/get/captcha'
data={
 "langCode": "en",
 "captchaLength": "3",
 "captchaType": "2"
}
response = requests.post(url, auth=HTTPBasicAuth('colossal titans', '999933587512'),json=data)
print(response.status_code)
print(response.text)
from captcha.image import ImageCaptcha
image=ImageCaptcha()
data=image.generate('13B')
image.write('1a3B','capt.png')
print("2. otp generation")

import requests
from requests.auth import HTTPBasicAuth
response.headers
headers= {'x-request-id':'This value should be generated using UUIDv4 standard'} 
headers= {'appid':'MYAADHAAR'}
headers= {'Accept-Language':'en_in'}
headers= {'Content-Type':'application/json'}
url="https://stage1.uidai.gov.in/unifiedAppAuthService/api/v2/generate/aadhaar/otp" 
data={
 "uidNumber": "999933587512",
 "captchaTxnId": "h4YW9RdkR0JE",
 "captchaValue": "dvw2kz",
 "transactionId": "MYAADHAAR:59142477-3f57-465d-8b9a-75b28fe48725"
}
response=requests.post(url,auth=HTTPBasicAuth('uidNumber','999933587512'),json=data)
response=requests.post(url,auth=HTTPBasicAuth('captchaTxnId','h4YW9RdkR0JE'),json=data)
response=requests.post(url,auth=HTTPBasicAuth('captchaValue','dvw2kz'),json=data)
response=requests.post(url,auth=HTTPBasicAuth('transactionId','MYAADHAAR:59142477-3f57-465d-8b9a-75b28fe48725'),json=data)
print(response.status_code)
print(response.text)
import requests
from requests.auth import HTTPBasicAuth

#headers = {'content-type':'application/python'}
#headers={'content-type':'application/json', 'Accept':'application/json'}
 
data={ 
 "txnNumber": "mAadhaar:0ff94f02-a7f6-4526-9540-c7dcaaea217b",
 "otp":"615915",
 "shareCode": "4567",
 "uid":"999933587512"
}
url = "https://stage1.uidai.gov.in/eAadhaarService/api/downloadOfflineEkyc"
response = requests.post(url, auth=HTTPBasicAuth('colossal titans','999933587512'),json=data)
print(response.status_code)
print(response.text)

from tkinter import*
from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("AADHAR LOGIN")
label_0 = Label(root, text="AADHAR LOGIN",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
entry_2 = Entry(root)
entry_2.place(x=240,y=280)
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)


