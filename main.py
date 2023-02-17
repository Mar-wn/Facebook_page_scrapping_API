from fastapi import FastAPI
from facebook_page_scraper import Facebook_scraper
import json
import models
from database import engine, SessionLocal


app = FastAPI()

models.Base.metadata.create_all(bind= engine)

db = SessionLocal()


@app.get('/')
def root():
    return {'hello':'this is a fb page scrapper API'}


@app.get('/all_posts')
def get_all_posts():
    return db.query(models.Posts).all()


@app.post('/scrape_page')
def scrape_and_register_posts(page_name: str, posts_count: int, timeout: int):
    #scrapping

    scraper = Facebook_scraper(page_name, posts_count, timeout= timeout, browser= 'firefox')
    json_data = json.loads(scraper.scrap_to_json())
    Facebook_scraper._Facebook_scraper__data_dict = {}

    #saving
    posts = [models.Posts(
    id = post_id,
    page_name = json_data[post_id]['name'],
    shares_count = json_data[post_id]['shares'],
    reactions_count = json_data[post_id]['reaction_count'],
    comments_count = json_data[post_id]['comments'],
    content = json_data[post_id]['content'],
    posted_on = json_data[post_id]['posted_on'],
    video = str(json_data[post_id]['video']),
    image = str(json_data[post_id]['image']),
    post_url = json_data[post_id]['post_url'],
    likes = json_data[post_id]['reactions']['likes'],
    loves = json_data[post_id]['reactions']['loves'],
    wow = json_data[post_id]['reactions']['wow'],
    cares = json_data[post_id]['reactions']['cares'],
    sad = json_data[post_id]['reactions']['sad'],
    angry = json_data[post_id]['reactions']['angry'],
    haha = json_data[post_id]['reactions']['haha']) for post_id in json_data]

    db.add_all(posts)
    db.commit()
    #db.execute(insert(posts), posts,)
    #db.executemany(models.Posts.__table__.insert().values(posts).prefix_with('OR IGNORE'))

    return('posts scraped and saved!', json_data)
    


