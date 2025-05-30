{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3661cc86-d799-4a9f-9354-40de29b2eebf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# services/bookmark.py\n",
    "\n",
    "from sqlalchemy.orm import Session\n",
    "from models.user import User as UserModel\n",
    "from models.bookmark import Bookmark\n",
    "\n",
    "def add_bookmark(\n",
    "    db: Session,\n",
    "    user: UserModel,\n",
    "    paper_id: int,\n",
    "    paper_title: str,\n",
    "    paper_link:  str  \n",
    ") -> Bookmark:\n",
    "    \"\"\"\n",
    "    paper_id, paper_title 을 함께 받아\n",
    "    북마크 레코드를 생성 후 반환합니다.\n",
    "    \"\"\"\n",
    "    bm = Bookmark(\n",
    "        user_id=user.id,\n",
    "        paper_id=paper_id,\n",
    "        paper_title=paper_title,\n",
    "        paper_link= paper_link\n",
    "    )\n",
    "    db.add(bm)\n",
    "    db.commit()\n",
    "    db.refresh(bm)\n",
    "    return bm\n",
    "\n",
    "def list_bookmarks(db: Session, user: UserModel) -> list[Bookmark]:\n",
    "    \"\"\"\n",
    "    DB에서 현재 유저의 Bookmark ORM 객체 리스트를 그대로 반환합니다.\n",
    "    Pydantic BookmarkOut(orm_mode=True) 이 paper_title 등도 직렬화해 줍니다.\n",
    "    \"\"\"\n",
    "    return db.query(Bookmark).filter_by(user_id=user.id).all()\n",
    "\n",
    "def remove_bookmark(\n",
    "    db: Session,\n",
    "    user: UserModel,\n",
    "    bm_id: int\n",
    ") -> None:\n",
    "    \"\"\"\n",
    "    bookmark_id 가 user 의 것인지 확인 후 삭제합니다.\n",
    "    \"\"\"\n",
    "    bm = db.query(Bookmark).filter_by(id=bm_id, user_id=user.id).first()\n",
    "    if bm:\n",
    "        db.delete(bm)\n",
    "        db.commit()"
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
