{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c95e29c1-9dfb-4338-84fe-49be942398f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"${message}\n",
    "\n",
    "Revision ID: ${up_revision}\n",
    "Revises: ${down_revision | comma,n}\n",
    "Create Date: ${create_date}\n",
    "\n",
    "\"\"\"\n",
    "from typing import Sequence, Union\n",
    "\n",
    "from alembic import op\n",
    "import sqlalchemy as sa\n",
    "${imports if imports else \"\"}\n",
    "\n",
    "# revision identifiers, used by Alembic.\n",
    "revision: str = ${repr(up_revision)}\n",
    "down_revision: Union[str, None] = ${repr(down_revision)}\n",
    "branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}\n",
    "depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}\n",
    "\n",
    "\n",
    "def upgrade() -> None:\n",
    "    \"\"\"Upgrade schema.\"\"\"\n",
    "    ${upgrades if upgrades else \"pass\"}\n",
    "\n",
    "\n",
    "def downgrade() -> None:\n",
    "    \"\"\"Downgrade schema.\"\"\"\n",
    "    ${downgrades if downgrades else \"pass\"}"
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
