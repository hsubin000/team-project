{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70fd1d24-3849-443e-a89f-3009fcb190d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import xml.etree.ElementTree as ET\n",
    "\n",
    "\n",
    "def parse_xml(text: str) -> ET.Element:\n",
    "    \"\"\"XML 문자열을 파싱하여 최상위 Element를 반환합니다.\"\"\"\n",
    "    return ET.fromstring(text)"
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
