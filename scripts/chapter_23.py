# Manually compute association-rule support, confidence, lift.
transactions=[{'milk','bread'},{'milk','eggs'},{'bread','milk'},{'bread'}]
a=sum('milk' in t for t in transactions)
b=sum('bread' in t for t in transactions)
ab=sum({'milk','bread'}.issubset(t) for t in transactions)
support=ab/len(transactions)
confidence=ab/a
lift=confidence/(b/len(transactions))
print('Support:',support)
print('Confidence milk->bread:',round(confidence,3))
print('Lift:',round(lift,3))
