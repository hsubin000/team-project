{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f036ab0-3caf-49b3-b056-0f313e15aee9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import Column, Integer, String, Date\n",
    "from sqlalchemy.ext.declarative import declarative_base\n",
    "\n",
    "Base = declarative_base()\n",
    "\n",
    "class Paper(Base):\n",
    "    __tablename__ = \"papers\"\n",
    "\n",
    "    id = Column(Integer, primary_key=True, index=True)\n",
    "    title = Column(String, nullable=False)\n",
    "    authors = Column(String)  # \"A, B, C\" 형태\n",
    "    journal = Column(String)\n",
    "    pub_date = Column(Date)\n",
    "    link_url = Column(String, unique=True)\n"
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
