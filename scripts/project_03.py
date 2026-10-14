# Spam detection
# Sixteen synthetic messages with spam/legitimate labels. Use only as a teaching demonstration, not a deployment-ready filter.
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
spam=['claim your free prize','exclusive cash award','win money now','free prize click',
      'urgent lottery payment','claim award now','free lottery ticket','big cash jackpot']
legit=['project meeting agenda','invoice attached today','research group discussion',
       'meeting notes attached','your project update','team lunch schedule',
       'lecture slides tomorrow','please review report']
texts=spam+legit;y=[1]*8+[0]*8
a,b,c,d=train_test_split(texts,y,test_size=.25,stratify=y,random_state=7)
clf=make_pipeline(CountVectorizer(),MultinomialNB()).fit(a,c)
base=DummyClassifier(strategy='most_frequent').fit([[0]]*len(c),c)
print('Baseline F1:',round(f1_score(d,base.predict([[0]]*len(d)),zero_division=0),3))
print('Model F1:',round(f1_score(d,clf.predict(b),zero_division=0),3))
print('Test messages:',len(d))
