{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "966ac2d6-670a-4cbb-a7f3-bfa4d346afcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "#schemas/bookmark.py\n",
    "from pydantic import BaseModel\n",
    "from datetime import datetime\n",
    "\n",
    "class BookmarkCreate(BaseModel):\n",
    "    paper_id: int\n",
    "    paper_title: str\n",
    "    paper_link:  str  \n",
    "\n",
    "class BookmarkOut(BaseModel):\n",
    "    id: int\n",
    "    paper_id: int\n",
    "    paper_title: str\n",
    "    paper_link:  str  \n",
    "    created_at: datetime\n",
    "\n",
    "    class Config:\n",
    "        orm_mode = True"
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
