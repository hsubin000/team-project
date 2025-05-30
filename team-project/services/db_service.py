{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2957cdb3-cbbc-4a23-9be5-6ae8e772a196",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy.orm import Session\n",
    "from models.db import Paper\n",
    "from schemas.paper import PaperCreate, PaperOut\n",
    "\n",
    "def create_paper(db: Session, paper: PaperCreate) -> PaperOut:\n",
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
    "    return PaperOut.from_orm(db_paper)\n",
    "\n",
    "def list_papers(db: Session, skip: int = 0, limit: int = 10):\n",
    "    return db.query(Paper).offset(skip).limit(limit).all()"
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
