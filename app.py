from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


start_date = datetime(2023, 10, 7, 4, 30)  

@app.route('/')
def home():
    now = datetime.now()
    time_together = now - start_date
    
    days_together = time_together.days
    hours_together = time_together.seconds // 3600
    minutes_together = (time_together.seconds % 3600) // 60
    
    messages = [
        "goofmorning baby 💗",
        "everyday i wake up and thank the universe for sending you to me.",
        "im so grateful to have you here, with me.",
        "and im more grateful that i get to be with you, watch you grow and shine ✨",
        "i know i can be a lot at times" , "mostly unreasonable and selfish :((", "but thank you so much for being the absolute best and putting up with my madness",
        "i know love exists because you exist <33",
        "can't wait to look at you and not say a word <3 beacuse i'm all words no game hehe ✨",
        "i hope i light up your day like you do mine <33"
    ]
    

    spotify_links = [
        {"name": "pov: im in love with you", "url": "https://open.spotify.com/playlist/5P3f6LDLtiV1JdHyi5D6qI?si=2efb90e312154955&pt=65792102ea70da88d5103239375651b1"}, 
        {"name": "full circle", "url": "https://open.spotify.com/playlist/1H9pnWTGDAWpUtPr8xvz7p?si=0b914e86a8b54897&pt=bd0e761c5c3ab6f22d0966252787de0f"} 
    ]
    pinterest_link = "https://www.pinterest.com/ttasmiatabassum/a-year-with-you/" 

    return render_template('index.html', days_together=days_together,hours_together=hours_together, minutes_together=minutes_together , messages=messages, spotify_links=spotify_links, pinterest_link=pinterest_link)

if __name__ == '__main__':
    app.run(debug=True)
