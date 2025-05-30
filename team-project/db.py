{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a50a509-f54d-4169-b632-0582622c24c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# db.py\n",
    "from sqlalchemy import create_engine\n",
    "from sqlalchemy.orm import sessionmaker, declarative_base\n",
    "\n",
    "Base = declarative_base()\n",
    "\n",
    "# 모든 모델 import (순서는 중요 X, 단 import는 반드시 필요)\n",
    "import models.user\n",
    "import models.bookmark\n",
    "# import models.paper 등 필요한 것들\n",
    "\n",
    "DATABASE_URL = \"sqlite:///./test.db\"\n",
    "\n",
    "engine = create_engine(\n",
    "    DATABASE_URL,\n",
    "    connect_args={\"check_same_thread\": False} if DATABASE_URL.startswith(\"sqlite\") else {}\n",
    ")\n",
    "\n",
    "# (개발 중이라면) 기존 테이블 삭제\n",
    "Base.metadata.drop_all(bind=engine)\n",
    "# 테이블 생성\n",
    "Base.metadata.create_all(bind=engine)\n",
    "\n",
    "SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\n",
    "\n",
    "def get_db():\n",
    "    db = SessionLocal()\n",
    "    try:\n",
    "        yield db\n",
    "    finally:\n",
    "        db.close()"
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
