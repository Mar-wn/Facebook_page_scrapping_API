from sqlalchemy import Column, Integer, String
from database import Base

class Posts(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key= True, index= True)
    page_name = Column(String)
    shares_count = Column(Integer)
    reactions_count = Column(Integer)
    comments_count = Column(Integer)
    content = Column(String)
    posted_on = Column(String)
    video = Column(String)
    image = Column(String)
    post_url = Column(String)
    likes = Column(Integer)
    loves = Column(Integer)
    wow = Column(Integer)
    cares = Column(Integer)
    sad = Column(Integer)
    angry = Column(Integer)
    haha = Column(Integer)