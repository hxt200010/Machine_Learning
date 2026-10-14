# Text sentiment classification
# Small labeled illustrative texts, TF-IDF feature learning and logistic classifier with majority baseline.
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
texts=['great design','excellent results','very useful','high quality','good performance','works well',
       'terrible design','poor results','not useful','low quality','bad performance','fails often']
y=[1]*6+[0]*6
a,b,c,d=train_test_split(texts,y,test_size=.33,stratify=y,random_state=7)
model=make_pipeline(TfidfVectorizer(ngram_range=(1,2)),LogisticRegression()).fit(a,c)
base=DummyClassifier(strategy='most_frequent').fit([[0]]*len(c),c)
print('Baseline accuracy:',round(accuracy_score(d,base.predict([[0]]*len(d))),3))
print('Text model accuracy:',round(accuracy_score(d,model.predict(b)),3))
print('Test set count:',len(d))
