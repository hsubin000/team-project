{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9aeceeee-375a-4f9d-b808-f949948fe4e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#models/paper.py\n",
    "from pydantic import BaseModel\n",
    "from typing import List, Optional\n",
    "\n",
    "class Author(BaseModel):\n",
    "    order: Optional[int]\n",
    "    url:   Optional[str]\n",
    "    name:  str\n",
    "\n",
    "class Publication(BaseModel):\n",
    "    url:  Optional[str]\n",
    "    name: Optional[str]\n",
    "\n",
    "class Recommendation(BaseModel):\n",
    "    id: Optional[int]\n",
    "    paper_id: Optional[int]\n",
    "    title:        Optional[str]\n",
    "    authors:      List[Author]\n",
    "    publisher:    Publication\n",
    "    publication:  Publication\n",
    "    issue_yymm:   Optional[str]\n",
    "    pages:        Optional[str]\n",
    "    free_yn:      Optional[str]\n",
    "    price:        Optional[str]\n",
    "    preview_yn:   Optional[str]\n",
    "    preview:      Optional[str]\n",
    "    link_url:     Optional[str]\n",
    "    link_api:     Optional[str]\n",
    "\n",
    "class RecommendationResponse(BaseModel):\n",
    "    totalcount:      int\n",
    "    pyymm:           Optional[str]\n",
    "    recommendations: List[Recommendation]\n",
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
