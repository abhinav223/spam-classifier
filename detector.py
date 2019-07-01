import pickle as c
import os
from collections import Counter
from sklearn import *
def load(clf_file):
    with open(clf_file) as fp:
        clf=c.load(fp)
    return clf
def make_dict():
    direc='emails/'
    files=os.listdir(direc)
    #print(files)
    emails=[direc + email for email in files]
    words=[]
    c=len(emails)
    for email in emails:
        f=open(email,encoding='latin-1')#f=open(filename,errors='ignore')
        blob=f.read()
        words+=blob.split(' ')
        print(c)
        c-=1
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i]=' '
    words = list(filter(lambda x: x!= ' ', words))

    dictionary=Counter(words)
    
    #del.dictionary['']
    return(dictionary.most_common(3000))


with open('model_pickle','rb') as f:
    clf=c.load(f)
d=make_dict()
features=[]


from_user=input('>')
for words in d:
    features.append(from_user.count(words[0]))


res=clf.predict([features])

print(['ham','spam'][res[0]])

