import os
import pandas as pd
import time
import sys
import re
import json
import requests
import random
from multiprocessing import Process
url = 'https://www.virustotal.com/vtapi/v2/file/report'
keys_list = [
            '15b87efcbe3b10c9674ad9e312e2b3c9820316a4532c5afb561f6f7922f4331a',
            'dcdf3b65b390c37475947a271c4ae35779f3b6a97ae55b3f8256e6554f138e8f',
            'e5b1dbdbe0c5985bce0791e91592423a357e2812c1e83fd152ba423f9864b9e5',
            'fbcaaa242697f15428e2bc741feab44d94c45f36950e8d91ea06bfac6206d85c',
            'f5c413e37119e5690a7c5ca53d6c0ee94a6fbef3cc969a8433469b7305b14089',
            '8bd8f0bc8365d3098aac58e6160d0006614d1aae920d0307f94874d11b0e24b1',
            '42e0c4230f017339bacf1fbdd39e63654485920d1492d2f315fc6581ffba8b4f',
            '1cf874b4b0cde8358afa560258a768eef6a98f1183517d8bcbfc86c492a0c555',
            '81a1b937fb4deef6b95fb5fb5e175588ab74d0ae7b4f95282000404118abc932',
            '32f5638a015dee9568b9bfe932a3244fc6ba3738483e99f0c1f77fdaad866256',
            'd4e3ac5673d26f095990648ce6c6217ba26d86168f6d7c7d1a3e5ac703e586a6',
            'a910ba95eab0f7e8987ab70549db86a02f2ad2b3273c54394230969ff0f53f9d',
            '1f1276c574c753cd577462991769060ef4baa0ef6a5bb2e7275868755d23fe5a',
            '11b6dba579d075f773ded52d89872974fc7d0d30d16f880e0d72965394bf1491',
            '5f346078e1c6ee6b7e89cf05e5d6e97f3b962fbfa795f3548667da95b1c28d07',
            '40b5b437f3feedda33a06939ef35407a6a5a721ca8b87c416cca9a758c8baadf',
            'e6776a46f9c43e0b1366793d4773a12de94e8b03c7598fe41fb2bb5fa81b7781',
            '4fc8d6f19303bb4f515702e4efd4e4bb20963793e9c4133b2afcbbbf64e2f35c',
            '0d23b6aaf870952fa6cb71401ec7b00c6b37446c4b20978360ff05b9fccdf665',
            '3d2de92fa10a60707f2a4920907fd07753989b5d242da0574db4230286e470fa',
            'bd3989515b7d79fc071803596bf4d249584abc4047be9643779ba7a463786fbd',
            'a764411e170585ab61004b5e3a6403b1c7e24de93edf06ad86ffc6b5e67d64b3',
            '8ff74d10d370d10470c1c8a97949bba6e3597c3591cafee653150360b38818e7',
            'e83b7ea1290a54083b17b1a06fc58fcb90d343fe4f3033547f60a68833a6bcb8',
            '4d7c12b5783b07ae6c2a8c8046d64d27fe8f9cacda242add3dbdd6b1097512a8',
            'a43ecf0cf21a6151b54d7c61f704d8f2a7c3c74ca22cc9fc0fb1cb7802cf746c',
            '9c8458357cc549f54b10232a57c4fd60262fdc8309ae5b1aa29e9019b379dc0e',
            '032192107f72ca0cdec907c15324b2c9654392368e6d091f3366f59d8f862431',
            'e2c5167c0e48cd6a94cad4e2cfbd8fd4c0893f463bd9e8e2a6629cb25eda3579',
            'c8f3818f735f6b08425f63ab79098b1fb30406609e748af46633869bf6a2b790',
            '58a7cc20d6e2ffaf4fcde73403af6d4d8c864680159211f5290886abcb97ac6b',
            '18d171805eca09714da66523a286fccb27442ef9f7843af2a850f98acf980d39',
            'aff824f8c76fed6fe7469e7bb9b2ee5bb782e0895adeb11e2cb01a10f4ebaf82',
            'd60e729f8a9abc4d18a475ea16ed192292c668a2d164a9ad1304d6007f9b0659',
            '0fd6cf8a13cf36157f4a0a6c78c1d5f6966981c5c417b9a3d4ca482dfd67f3ae',
            '114c79147867324ceef9b4444c61b58acee26e6a9ce6d44079e5be2de2018375',
            '730d680ea8e1353e67331e8882f5354a720a1e9be8446aec21814e9f138f2043',
            '918fe1b34fd612acb742a3c9ba795afd2569878f2d1f9b5394ccb1f04d93ac80',
            '07583c448c4b4b1d996659d194ce1f0d86c23764a06fd287f6c03f6b6a089400',
            '73a5ecd9de0bea2e10b5ab12934ee08cd381b4df285836504265086a3ae7b168',
            'a099a6f028c356abb036688b5e85df90e25bd551d4af01ea6a7fe6399b2127e3',
            '857e19f62a993bc1d0621a47655094ee49288648b1fa96da6feebfd68c5e457a',
            '2200a8df3ac5f2285c346c722d34f7dae1c1889a21458b4345be44815bad7b85',
            'e858a466dc37179d4f8ea470a7256fa0c0408c02e0f0eae1e7756251a8a2620b',
            '1a1ec968be4824490a378a5f5a69a8a67f3b9d6337128a1fd51f8cfc754a8145',
            '3c8200425d21603b8ac0d4e53cdabb6c654f4ce0374b536ed5480be5d2e3f1e0',
            '87bf74169010d81029c47543a2209c8258617e18cdec63c93dfd0d1f267151e6',
            'd325811c432c6346516c7e4be5dcb8d43cc527e0a510f7621be45ef2bcf4b38b',
            '33a7d44f32fa96d9f3af2c60e2e4ecbbc00de29ec500c76b0faf6eb31a47351a',
            '8195fbfde4f6f37c6687a9449d339129d9e945217c91ec1981f1cce39bf20483',
            '7fa2fbc4456623faa0f4410dc252c4717479ea02b90c27e2dbdc9b8cb28849e1',
            '9024770a9c6ed0d2cd791868527e5822ad84d0f54a3ca52be2424ffb29b09de0',
            'baf922466b93b5761326a7d5841c7ab604c75cbc7bfe8337dc9a5d6ac7e3c8c9',
            '7cda80ddca359a97d4488aad577747b878d89a91cf9762a2933e599e5e6ebee1',
            '53106774943786655ba840b3034c6b03d6fb19121486af774ace8da3c63fb3db',
            '395736f4344fe7879b55e39b81676759b5a37e73c687993ee35cd62572a0e26e',
            'b971eb765317e2188c09252f9cb75cefbea8cc5bb629c160119d958bc2a2c4b4',
            'd96b13916aab4931a6fb36ac2b934c552b03a1f25b045a798cf446e4175da04d']

def multiprocess_get_label(i,split_length,length,sha256_list):
    a=i*split_length
    if i==7:
        b=length
    else:
        b=(i+1)*split_length
    for each_sha256 in sha256_list[a:b]:
        key_selected=random.sample(keys_list,1)[0] 
        params={'apikey': key_selected, 'resource': each_sha256}
        response = requests.get(url, params=params)
        print(1212121212)
        if response.status_code == 200:
            try:
                print(response.json())
                positives= response.json()['positives']
                ret=open('sha256-label.csv','a+')
                ret.write(each_sha256+','+str(positives)+'\n')
                ret.close()
            except Exception:
                ret=open('sha256-label.csv','a+')
                ret.write(each_sha256+','+'none'+'\n')
                ret.close()
                print ('no record.')
        else:
            print ('failed.')
            ret=open('sha256-label.csv','a+')
            ret.write(each_sha256+','+'failed'+'\n')
            ret.close()
  
def get_label():
    ret=open('sha256-label.csv','w')
    ret.write('sha256,label\n')
    ret.close()
    print(23232323)
    sha256_list = list(pd.read_csv('sample_table.csv').sha256)
    length = len(sha256_list)
    split_length = length/8
    processes = []
    for i in range(8):
        p = Process(target=multiprocess_get_label, args=(i,split_length,length,sha256_list,))
        print('Process will start')
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print('Process end')     
 
if __name__ == '__main__':
    get_label()
 
