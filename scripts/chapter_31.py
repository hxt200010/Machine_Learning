from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
texts=['excellent experience','very good','terrible service','very bad','good quality','poor quality']
y=[1,1,0,0,1,0]
model=make_pipeline(TfidfVectorizer(),LogisticRegression()).fit(texts,y)
print('Positive probability:',round(model.predict_proba(['good service'])[0,1],3))
print('Predictions:',model.predict(['excellent','terrible']).tolist())
