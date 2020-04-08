from textblob import TextBlob
import matplotlib.pyplot as plt

def PlotPieChart(values,Title):
    labels=['Weakly Positive','Positive','Strongly Positive','Neutral','Weakly Negative','Negative','Strongly Negative']
    color=['tab:blue','tab:orange','tab:purple','tab:cyan','tab:pink','aquamarine','rosybrown']
    plt.pie(values,labels=labels,colors=color,autopct='%1.2f%%')
    plt.axis('equal')
    plt.title(Title)
    plt.legend()
    plt.show()

def ReadFile(FileName):
    list_comments=[]
    with open(FileName,'r') as f:
        for line in f.read().split('\n'):
            list_comments.append(line)
        f.close()
    return list_comments

def SentimentAnalysis(Data):
    positive = 0
    wpositive = 0
    spositive = 0
    negative = 0
    wnegative = 0
    snegative = 0
    neutral = 0
    for i in range(0,50):
        analysis = TextBlob(Data[i])
        if (analysis.sentiment.polarity == 0):
            neutral += 1
        elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
            wpositive += 1
        elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
            positive += 1
        elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
            spositive += 1
        elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
            wnegative += 1
        elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
            negative += 1
        elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
            snegative += 1
    return wpositive,positive,spositive,neutral,wnegative,negative,snegative

BiggBoss13=[]
BiggBoss13=ReadFile('BiggBoss13.txt')
print(BiggBoss13)

BiggBoss13_wpositive,BiggBoss13_positive,BiggBoss13_spositive,BiggBoss13_neutral,BiggBoss13_wnegative,BiggBoss13_negative,BiggBoss13_snegative = SentimentAnalysis(BiggBoss13)

BiggBoss13_value=[BiggBoss13_wpositive*2,BiggBoss13_positive*2,BiggBoss13_spositive*2,BiggBoss13_neutral*2,BiggBoss13_wnegative*2,BiggBoss13_negative*2,BiggBoss13_snegative*2]

PlotPieChart(BiggBoss13_value,'Bigg Boss 13')