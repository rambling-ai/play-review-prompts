from google_play_scraper import Sort, reviews_all
import sqlite3
from datetime import datetime

app_id = 'com.example' # change for your app's id

def get_reviews(app_id):
    result = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang='en',
        country='us',
        sort=Sort.MOST_RELEVANT,
    )
    return result

conn = sqlite3.connect('reviews.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        reviewId TEXT,
        userName TEXT,
        userImage TEXT,
        content TEXT,
        score INTEGER,
        thumbsUpCount INTEGER,
        reviewCreatedVersion TEXT,
        at TEXT,
        replyContent TEXT,
        repliedAt TEXT,
        appVersion TEXT
    )
''')

reviews = get_reviews(app_id)

for review in reviews:
    cursor.execute('''
        INSERT INTO reviews (
            reviewId,
            userName,
            userImage,
            content,
            score,
            thumbsUpCount,
            reviewCreatedVersion,
            at,
            replyContent,
            repliedAt,
            appVersion
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        review.get('reviewId', None),
        review.get('userName', None),
        review.get('userImage', None),
        review.get('content', None),
        review.get('score', None),
        review.get('thumbsUpCount', None),
        review.get('reviewCreatedVersion', None),
        review.get('at', None),
        review.get('replyContent', None),
        review.get('repliedAt', None),
        review.get('appVersion', None)
    ))

conn.commit()
conn.close()
