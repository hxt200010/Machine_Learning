from sklearn.tree import DecisionTreeClassifier, export_text
X=[[1],[2],[3],[4],[5],[6]]
y=[0,0,0,1,1,1]
tree=DecisionTreeClassifier(max_depth=2,random_state=0).fit(X,y)
print(export_text(tree,feature_names=['signal']).strip())
print('Prediction at signal=5:',tree.predict([[5]]).tolist())
