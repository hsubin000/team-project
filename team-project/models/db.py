{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c9688a9-99e0-45b7-842a-a3dc8e08ff5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import Column, Integer, String, Date\n",
    "from db import Base\n",
    "\n",
    "class Paper(Base):\n",
    "    __tablename__ = \"papers\"\n",
    "\n",
    "    id         = Column(Integer, primary_key=True, index=True)\n",
    "    title      = Column(String, index=True)\n",
    "    authors    = Column(String)     # JSON 문자열로 직렬화하거나, 별도 테이블로 분리\n",
    "    journal    = Column(String, index=True)\n",
    "    pub_date   = Column(Date)\n",
    "    link_url   = Column(String)"
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
