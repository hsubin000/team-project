{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c24d8ee-9ae8-4ceb-8e7e-974e823d05d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import date\n",
    "from pydantic import BaseModel\n",
    "\n",
    "class PaperBase(BaseModel):\n",
    "    title: str\n",
    "    authors: list[str]\n",
    "    journal: str | None = None\n",
    "    pub_date: date | None = None\n",
    "    link_url: str | None = None\n",
    "\n",
    "class PaperCreate(PaperBase):\n",
    "    pass\n",
    "\n",
    "class PaperOut(PaperBase):\n",
    "    id: int\n",
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
