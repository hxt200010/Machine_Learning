from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
y=[1,0,1,1,0,0,1,0]
pred=[1,0,0,1,1,0,1,0]
print('Confusion matrix:',confusion_matrix(y,pred).tolist())
print('Precision:',round(precision_score(y,pred),3))
print('Recall:',round(recall_score(y,pred),3))
print('F1:',round(f1_score(y,pred),3))
