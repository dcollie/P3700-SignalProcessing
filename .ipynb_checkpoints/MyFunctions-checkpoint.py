{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myconv(x,h):\n",
    "    '''This function takes a 2 lists of numbers and convolves them.'''\n",
    "    i = 0\n",
    "    lst = []\n",
    "    while (i < (len(x)+len(h))-1):\n",
    "        j=0\n",
    "        value = 0\n",
    "        while (j < len(h)):\n",
    "            if ((i-j)>=0) and ((i-j)<len(x)):\n",
    "                value = value + h[j]*x[i-j]\n",
    "            j+=1\n",
    "        lst.append(value)\n",
    "        i+=1\n",
    "    return lst\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
