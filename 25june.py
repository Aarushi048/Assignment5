import re


#question1
print("question 1")
emails=["zuck26@facebook.com","page23@google.com","jeff42@amazon.com"]
ls=[]
for i in emails:
    a=re.findall("[\w]+",i)
    a= tuple(a)
    ls.append(a)
print(ls)

#question2
print("question 2")
text="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
x=name=re.findall("[b,B][a-zA-Z]{1,5}",text)
print(x)

#question3
print("question 3")
sentence="A, very very; irregular_sentence"
print("")
print(sentence)
x=re.compile("[,; _]")
for i in sentence:
    y=x.sub(" ",sentence)
print(y)
print("")


# optional question
print("optional question")
print("desired_output=")
tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstat"
reg=re.compile("[!]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[R][T]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[@]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[T][h][e][N][e][x][t][W][e][b][:] ")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile(" [h][t][t][p][:][/][/][t][.][c][o][/][l][b][w][e][j][p][x][O][d]")
for i in sentence:
    tweet=reg.sub("",tweet)
reg=re.compile("[c][c][:][@][g][a][r][y][b][e][r][n][h][a][r][d][t][#][r][s][t][a][t]")
for i in sentence:
    tweet=reg.sub("",tweet)
print(tweet)



