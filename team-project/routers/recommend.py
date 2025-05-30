{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24bf3018-667b-4ca7-9e73-d542db98dc77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# routers/recommend.py\n",
    "from fastapi import APIRouter, Query, HTTPException\n",
    "from services.dbpia import fetch_recommendations\n",
    "from models.paper import RecommendationResponse\n",
    "\n",
    "router = APIRouter(\n",
    "     prefix=\"/recommend\",\n",
    "     tags=[\"recommend\"]\n",
    " )\n",
    " \n",
    "@router.get(\"\", response_model=RecommendationResponse)\n",
    "def get_recommendations(\n",
    "    pyear: int | None = Query(None, ge=1900, le=2100, description=\"원하는 연도(YYYY). 지정하면 pmonth와 함께 입력해야 합니다.\"),\n",
    "    pmonth: int | None = Query(None, ge=1, le=12, description=\"원하는 월(MM). pyear를 지정할 경우 반드시 입력해야 합니다.\"),\n",
    "    category: str | None = Query(None, regex=\"^[1-9]$\", description=\"주제 분류 코드 (1~9)\"),\n",
    "    page: int = Query(1, ge=1, description=\"페이지 번호 (1부터 시작)\"),\n",
    "    per_page: int = Query(20, ge=1, le=100, description=\"페이지당 결과 수\"),\n",
    "):\n",
    "    # pyear과 pmonth는 함께 입력하거나 모두 생략해야 함을 검사\n",
    "    if (pyear is None) ^ (pmonth is None):\n",
    "        raise HTTPException(422, detail=\"pyear과 pmonth는 함께 지정하거나 모두 생략해야 합니다.\")\n",
    "    # str로 변환하여 서비스 호출\n",
    "    py = str(pyear) if pyear is not None else \"\"\n",
    "    pm = str(pmonth) if pmonth is not None else \"\"\n",
    "    return fetch_recommendations(\n",
    "        pyear=py,\n",
    "        pmonth=pm,\n",
    "        category=category or \"\",\n",
    "        page=page,\n",
    "        per_page=per_page,\n",
    "    )"
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
