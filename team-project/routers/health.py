{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5caeaf66-260d-48b3-ac60-dec01f1b965c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import APIRouter\n",
    "\n",
    "router = APIRouter()\n",
    "\n",
    "@router.get(\"\", summary=\"헬스 체크 엔드포인트\")\n",
    "def health_check():\n",
    "    \"\"\"서비스의 정상 가동 여부를 간단히 확인합니다.\"\"\"\n",
    "    return {\"status\": \"ok\"}"
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
