{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eabed2d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Weighted Accuracy: 0.667\n"
     ]
    }
   ],
   "source": [
    "y_true = [0, 1, 1, 0, 1, 0]\n",
    "y_pred = [0, 1, 0, 0, 1, 1]\n",
    "\n",
    "def weighted_accuracy(y_true, y_pred):\n",
    "    total = 0\n",
    "    correct = 0\n",
    "    for i in range(len(y_true)):\n",
    "        weight = 2 if y_true[i] == 1 else 1\n",
    "        total += weight\n",
    "        if y_true[i] == y_pred[i]:\n",
    "            correct += weight\n",
    "    return correct / total\n",
    "\n",
    "print(\"Weighted Accuracy:\", round(weighted_accuracy(y_true, y_pred), 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44adb995",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
