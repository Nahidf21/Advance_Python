
## Collect your Feedback
feedback = ["This product is bad", "This product is good", "This prodict has some problem", "We love this product"]
x=input("Give me your Feedback : ")
feedback.append(x)

##TODO
##Counting the positive words like good , like

count_positive = sum( 1 for comment in feedback if "good" in comment.lower() or "like" in comment.lower() or "love" in comment.lower())
print(f" Total number of comments : {len(feedback)} and number of positive commands {count_positive}")

