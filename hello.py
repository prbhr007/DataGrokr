import boto3
print("Hello User,")
print("Downloading file from S3 Bucket, Please wait")
s3 = boto3.client('s3')
s3.download_file('datagrokr-assessment','task.txt','mytask.txt')
print("Processing the file for top 5 occurance of word")
import collections
filename='mytask.txt'
wordCounter={}
with open(filename, 'r') as fh:
  for line in fh:
    word_list=line.replace('.',' ').replace(',',' ').lower().split()
    for word in word_list:
      if word not in wordCounter:
        wordCounter[word]=1
      else:
        wordCounter[word]=wordCounter[word]+1

word_counter = collections.Counter(wordCounter)
print("The Top 5 frequently occuring words are") 
for word,count in word_counter.most_common(5):
 	print(word,count)
