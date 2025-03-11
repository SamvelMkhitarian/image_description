from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CaptionHistory(Base):
    __tablename__ = "caption_history"
    id = Column(Integer, primary_key=True, index=True)
    caption = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now())
