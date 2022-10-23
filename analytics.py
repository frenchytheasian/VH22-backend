from sentiments import predict
import sys, os

def blockPrint():
    sys.stdout = open(os.devnull, 'w')
    
def enablePrint():
    sys.stdout = sys.__stdout__


def run_analytics(comments):
    positive = 0
    negative = 0
    total = len(comments)
    
    for comment in comments:
        blockPrint()
        prediction = predict(comment)
        
        if prediction[0]['label'] == 'LABEL_1':
            positive += 1
        else:
            negative += 1
            
    return {'positive': positive, 'negative': negative, 'total': total}
