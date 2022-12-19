from googleapiclient.discovery import build

class Youtube:
    def __init__(self):
        pass
    
    def get_comments(api_key, video_id):
        key = api_key
        id = video_id
        comments = list()
        api_obj = build('youtube', 'v3', developerKey=key)
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=id, maxResults=100).execute()
        while response:
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append(comment['textDisplay'])
        
                if item['snippet']['totalReplyCount'] > 0:
                    for reply_item in item['replies']['comments']:
                        reply = reply_item['snippet']
                        comments.append(reply['textDisplay'])
        
            if 'nextPageToken' in response:
                response = api_obj.commentThreads().list(part='snippet,replies', videoId=id, pageToken=response['nextPageToken'], maxResults=100).execute()
            else:
                break
        
        return comments

youtube = Youtube()

def get_youtube():
    return youtube