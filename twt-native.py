import json


str = [

           {
            "author_id": "2798802795",
            "conversation_id": "1582533904191598593",
            "created_at": "2022-10-19T00:47:39.000Z",
            "edit_history_tweet_ids": [
                "1582533904191598593"
            ],
            "id": "1582533904191598593",
            "in_reply_to_user_id": "771436243599040512",
            "lang": "en",
            "public_metrics": {
                "like_count": 0,
                "quote_count": 0,
                "reply_count": 0,
                "retweet_count": 0
            },
            "reply_settings": "everyone",
            "source": "The Tweeted Times",
            "text": "@grownativemo: 'Ditch the rake and help native bees, snails and more when you LEAVE THE LEAVES! If left for nature, the marvel of plant chemistry that happens every fall when leaf abscission occurs and petioles detach f\u2026 https://t.co/Npp1UurS4h, see more https://t.co/S16A3B21Kv"
        },
        {
            "author_id": "1210410098578903043",
            "conversation_id": "1582530814062927872",
            "created_at": "2022-10-19T00:35:22.000Z",
            "edit_history_tweet_ids": [
                "1582530814062927872"
            ],
            "id": "1582530814062927872",
            "lang": "en",
            "public_metrics": {
                "like_count": 0,
                "quote_count": 0,
                "reply_count": 0,
                "retweet_count": 0
            },
            "reply_settings": "everyone",
            "source": "Cheap Bots, Done Quick!",
            "text": "The social burrowing honey bee is native to Australia. It very colorful and eats small fish!"
        }

]

with open('student_list.json', 'w+') as file:
    json.dump(str, file)

with open('student_list.json', 'r') as json_file:
    students = json.load(json_file)

msg = {}
for i in range(0, len(students)):
    print('''<span class="text line">''', students[i]['text'], '''</span>''')


