{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97d023d5-87e3-4bae-b160-c7e2609cddc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# schemas/recommend.py\n",
    "from pydantic import BaseModel\n",
    "from typing import List\n",
    "\n",
    "class Author(BaseModel):\n",
    "    name: str\n",
    "\n",
    "class Publication(BaseModel):\n",
    "    name: str\n",
    "    url: str\n",
    "\n",
    "class Recommendation(BaseModel):\n",
    "    id: int              # ← 반드시 추가!\n",
    "    title: str\n",
    "    authors: List[Author]\n",
    "    publication: Publication\n",
    "    link_url: str\n",
    "\n",
    "class RecommendResponse(BaseModel):\n",
    "    pyymm: str\n",
    "    recommendations: List[Recommendation]\n",
    "    totalcount: int"
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
