{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e67dbe6-0621-49d8-bc4a-bc1b6890af78",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import APIRouter, Depends, status\n",
    "from sqlalchemy.orm import Session\n",
    "\n",
    "from db import get_db\n",
    "from schemas.user import UserOut, UserUpdate, UserPasswordChange, UserInDB\n",
    "from services.auth import update_profile, delete_user, change_password\n",
    "from routers.auth import read_current_user, get_current_user_model\n",
    "\n",
    "router = APIRouter(prefix=\"/mypage\", tags=[\"mypage\"])\n",
    "\n",
    "@router.patch(\"/profile\", response_model=UserOut)\n",
    "def change_profile(\n",
    "    data: UserUpdate,\n",
    "    db: Session = Depends(get_db),\n",
    "    current: UserInDB = Depends(read_current_user),\n",
    ") -> UserOut:\n",
    "    user = update_profile(db, current, data)\n",
    "    return user\n",
    "\n",
    "@router.patch(\"/password\", response_model=UserOut)\n",
    "def change_pw(\n",
    "    passwords: UserPasswordChange,\n",
    "    db: Session = Depends(get_db),\n",
    "    current: UserInDB = Depends(get_current_user_model),  # 여기!\n",
    ") -> UserOut:\n",
    "    user = change_password(db, current, passwords)\n",
    "    return user\n",
    "\n",
    "@router.delete(\"/\", status_code=status.HTTP_204_NO_CONTENT)\n",
    "def withdraw(\n",
    "    hard: bool = False,\n",
    "    db: Session = Depends(get_db),\n",
    "    current: UserInDB = Depends(read_current_user)\n",
    "):\n",
    "    delete_user(db, current, hard)\n",
    "    return"
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
