from github import Github
#from pydriller import RepositoryMining
import requests
import json 
import csv
# First create a Github instance:

# using an access token
g = Github("\\access_token")
# Opening JSON file 
f = open('sstubs.json') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f)
x = []
z = [] 
for i in range(1500, 2000):
    sha = data[i]['fixCommitSHA1']
    shaparent = data[i]['fixCommitParentSHA1']
    projex = data[i]['projectName']
    projex = projex.replace(".", "/")
    print(projex)
    if projex == "Alluxio/alluxio":
        repo = g.get_repo(projex)
        commit = repo.get_commit(sha= sha)
        commit1 = repo.get_commit(sha= shaparent)
        datediff = commit.commit.committer.date - commit1.commit.committer.date
        try:
            temp = commit.committer.followers
            if not (temp == None):
                x.append(temp)
            else:
                x.append(0)
        except:
            x.append(0)
        z.append((datediff.days * 60 * 24) + datediff.seconds//60)
        print(i)

t = zip(x, z)
with open('collaboratorsAllux.csv', 'a') as f:
    writer = csv.writer(f, delimiter='\t')
    #writer.writerows(zip(["Followers"], ["TimeDiffInMins"]))
    writer.writerows(t)

# 0-200
# 1000 - 1400
# 200 - 600
