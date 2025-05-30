{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83ea44ab-7fd3-4a1a-afb5-f794e909161c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy.orm import Session\n",
    "from models.db import Paper\n",
    "from schemas.paper import PaperCreate, PaperOut\n",
    "\n",
    "def store_search_result(db: Session, paper: PaperCreate) -> Paper:\n",
    "    # 기존에 저장된 논문이 있다면 재사용\n",
    "    existing = db.query(Paper).filter_by(link_url=paper.link_url).first()\n",
    "    if existing:\n",
    "        return existing\n",
    "\n",
    "    db_paper = Paper(\n",
    "        title=paper.title,\n",
    "        authors=\",\".join(paper.authors),\n",
    "        journal=paper.journal,\n",
    "        pub_date=paper.pub_date,\n",
    "        link_url=paper.link_url\n",
    "    )\n",
    "    db.add(db_paper)\n",
    "    db.commit()\n",
    "    db.refresh(db_paper)\n",
    "    return db_paper\n"
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
