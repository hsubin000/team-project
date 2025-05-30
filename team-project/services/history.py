{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7fb6d31d-6661-4d66-9963-33d8ba12b863",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy.orm import Session\n",
    "from models.db import Paper\n",
    "from models.user import User as UserModel\n",
    "from models.bookmark import Bookmark\n",
    "\n",
    "def list_saved_papers(db: Session, user: UserModel):\n",
    "    # 북마크된 논문 목록\n",
    "    bookmarks = db.query(Bookmark).filter_by(user_id=user.id).all()\n",
    "    return [bm.paper for bm in bookmarks]\n"
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
