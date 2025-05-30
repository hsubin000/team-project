{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddde7701-a936-40bb-ab7c-9cf2559c7533",
   "metadata": {},
   "outputs": [],
   "source": [
    "#models/bookmark.py\n",
    "from sqlalchemy import Column, Integer, ForeignKey, DateTime\n",
    "from sqlalchemy import String\n",
    "from sqlalchemy.orm import relationship\n",
    "from db import Base\n",
    "from datetime import datetime\n",
    "\n",
    "class Bookmark(Base):\n",
    "    __tablename__ = 'bookmarks'\n",
    "\n",
    "    id         = Column(Integer, primary_key=True, index=True)\n",
    "    user_id    = Column(Integer, ForeignKey('users.id'), nullable=False)\n",
    "    paper_id   = Column(Integer, nullable=False)  # external paper ID\n",
    "    paper_title  = Column(String,  nullable=False)\n",
    "    paper_link   = Column(String,  nullable=False)\n",
    "    created_at = Column(DateTime, default=datetime.utcnow)\n",
    "\n",
    "    user = relationship('User', back_populates='bookmarks')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
