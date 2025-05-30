{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62443ba7-49bb-470f-99c5-f6d483b6846d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# schemas/user.py\n",
    "\n",
    "from pydantic import BaseModel\n",
    "from datetime import datetime\n",
    "from typing import Optional\n",
    "\n",
    "class UserBase(BaseModel):\n",
    "    username: str\n",
    "    nickname: Optional[str] = None\n",
    "\n",
    "class UserCreate(UserBase):\n",
    "    password: str\n",
    "\n",
    "class UserOut(UserBase):\n",
    "    id: int\n",
    "    is_active: bool\n",
    "    created_at: datetime\n",
    "\n",
    "    model_config = {\"from_attributes\": True}\n",
    "\n",
    "class UserInDB(UserBase):\n",
    "    id: int\n",
    "    hashed_password: str\n",
    "    is_active: bool\n",
    "    created_at: datetime\n",
    "\n",
    "    model_config = {\"from_attributes\": True}\n",
    "\n",
    "class Token(BaseModel):\n",
    "    access_token: str\n",
    "    token_type: str\n",
    "\n",
    "class UserPasswordChange(BaseModel):\n",
    "    current_password: str\n",
    "    new_password: str\n",
    "\n",
    "class UserUpdate(BaseModel):\n",
    "    username: Optional[str] = None\n",
    "    nickname: Optional[str] = None\n",
    "\n",
    "# ✅ 주의: 아래처럼 UserOut만 쓰는 것도 가능함. 불필요하게 User라는 이름 중복 X!"
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
