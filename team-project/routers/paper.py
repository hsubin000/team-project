{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd0d0e97-832e-4ca9-85d3-733a1a2bc18f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import APIRouter, Depends\n",
    "from sqlalchemy.orm import Session\n",
    "from schemas.paper import PaperCreate, PaperOut\n",
    "from services.db_service import create_paper, list_papers\n",
    "from db import get_db\n",
    "\n",
    "router = APIRouter()\n",
    "\n",
    "@router.post(\"\", response_model=PaperOut)\n",
    "def api_create_paper(\n",
    "    paper: PaperCreate,\n",
    "    db: Session = Depends(get_db)\n",
    "):\n",
    "    return create_paper(db, paper)\n",
    "\n",
    "@router.get(\"\", response_model=list[PaperOut])\n",
    "def api_list_papers(\n",
    "    skip: int = 0,\n",
    "    limit: int = 10,\n",
    "    db: Session = Depends(get_db)\n",
    "):\n",
    "    return list_papers(db, skip, limit)"
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
