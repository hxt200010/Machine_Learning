from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
texts = ['free money now','claim free prize','meeting at noon','project meeting today']
y = [1,1,0,0]
vectorizer = CountVectorizer()
model = MultinomialNB().fit(vectorizer.fit_transform(texts), y)
print('Vocabulary size:',len(vectorizer.vocabulary_))
print('Spam predictions:', model.predict(vectorizer.transform(['free prize','team meeting'])).tolist())
