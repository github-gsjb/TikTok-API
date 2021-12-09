#Import the TikTokAPI:
from TikTokAPI import TTAPI

#Create API object:
api = TTAPI()

#Now lets get the information from a specific tiktok video post

#TikTok video url's can be in the following formats:
#https://vm.tiktok.com/(stringId)
#https://vt.tiktok.com/(stringId)
#https://m.tiktok.com/v/(intId)
#https://tiktok.com/@(userName)/video/(intId)

#Get the id of the video post using a url:
postId = api.getPostId("https://www.tiktok.com/@elpanaarabe/video/7038818332270808325")
print("The post id is "+postId+"\n")

#Get the video post information using the id:
postInfo = api.getPost(postId)

#Print out the info in the console:
print(postInfo)

#Get author id
authorId = postInfo["aweme_detail"]["author"]["uid"]

#Print user info
print(api.getUser(authorId))

#Print user posts
print(api.listPosts(authorId))

#Print people following user
print(api.listFollowers(authorId))

#Print people user is following
print(api.listFollowing(authorId))
