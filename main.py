import praw
import sqlite3
import sentiment
import chart


opinions = []

def redditInit():
    reddit = praw.Reddit(
    client_id = '--sNjrH1D4GDBXhLT9w0QA',
    client_secret = 'IJwmr--APta5T9SADu0QwXBZAwi_DA',
    user_agent = 'my-app by: Valencia Student',
    username = "Independent-Month552",
    password = "Brooklyn1!")

    #Get sub reddit post
    subreddit = reddit.subreddit("politics")

    topPost = subreddit.hot(limit=2500)# make "limit=None"
    
    #create DB if one not created
    connect_db()

    for post in topPost:
        #print("title", type(post.title))
        #print("ID", post.id)
        insert_db(post.id, post.title)
        #print("Author: ", post.author)
        #print("Post Score: ", post.score)
        #print("Post number of comments: ", post.num_comments)
        print("\n")
        
#connect to DB
def connect_db():
    connect = sqlite3.connect("database.db")#'database.db'
    connect.execute('''CREATE TABLE president(id INTEGER primary key autoincrement, postID TEXT, post TEXT)''')
    connect.close()

#insert data in to DB
def insert_db(postID, post):
    connect = sqlite3.connect("database.db")
    connect.execute('''INSERT INTO president(postID,post) VALUES (?, ?)''', [postID, post])
    connect.commit()
    



#see if data was added to DB
def display():
    connect = sqlite3.connect('database.db')
    cur = connect.execute('SELECT post FROM president')
    res = cur.fetchall()

    #loop DB to get str
    for i in res:
        opinions.append(i[0])


def sentimentFunc():
    for opinion in opinions:
        sentiment.scoreText(opinion)
        print('PERSONAL OPINIONS: \n {}'.format(opinion))




def final():
    chart.plot(sentiment.getPos(), sentiment.getNeg(), sentiment.getNeu())


    
        
    
    
        



   
redditInit()
display()
sentimentFunc()
final()

