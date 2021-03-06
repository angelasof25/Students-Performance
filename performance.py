{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Students Performance\n",
    "\n",
    "Kaggle Dataset to better understand the influence of the parents background, ethnicity, test preparation and others on students performance and grades accomplishments. Marks secured by the students in high school\n",
    "Students from the United States. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd \n",
    "import seaborn as sns\n",
    "from matplotlib import pyplot as plt\n",
    "from matplotlib import style\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"StudentsPerformance.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000 entries, 0 to 999\n",
      "Data columns (total 9 columns):\n",
      "ID                             1000 non-null int64\n",
      "gender                         1000 non-null object\n",
      "ethnicity                      1000 non-null object\n",
      "parental level of education    1000 non-null object\n",
      "lunch                          1000 non-null object\n",
      "test preparation course        1000 non-null object\n",
      "math score                     1000 non-null int64\n",
      "reading score                  1000 non-null int64\n",
      "writing score                  1000 non-null int64\n",
      "dtypes: int64(4), object(5)\n",
      "memory usage: 70.4+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>gender</th>\n",
       "      <th>ethnicity</th>\n",
       "      <th>parental level of education</th>\n",
       "      <th>lunch</th>\n",
       "      <th>test preparation course</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>bachelor's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>72</td>\n",
       "      <td>72</td>\n",
       "      <td>74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>69</td>\n",
       "      <td>90</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>master's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>90</td>\n",
       "      <td>95</td>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>group A</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>47</td>\n",
       "      <td>57</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>male</td>\n",
       "      <td>group C</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>76</td>\n",
       "      <td>78</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5</td>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>associate's degree</td>\n",
       "      <td>standard</td>\n",
       "      <td>none</td>\n",
       "      <td>71</td>\n",
       "      <td>83</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>6</td>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>some college</td>\n",
       "      <td>standard</td>\n",
       "      <td>completed</td>\n",
       "      <td>88</td>\n",
       "      <td>95</td>\n",
       "      <td>92</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>7</td>\n",
       "      <td>male</td>\n",
       "      <td>group B</td>\n",
       "      <td>some college</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>40</td>\n",
       "      <td>43</td>\n",
       "      <td>39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8</td>\n",
       "      <td>male</td>\n",
       "      <td>group D</td>\n",
       "      <td>high school</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>completed</td>\n",
       "      <td>64</td>\n",
       "      <td>64</td>\n",
       "      <td>67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>9</td>\n",
       "      <td>female</td>\n",
       "      <td>group B</td>\n",
       "      <td>high school</td>\n",
       "      <td>free/reduced</td>\n",
       "      <td>none</td>\n",
       "      <td>38</td>\n",
       "      <td>60</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ID  gender ethnicity parental level of education         lunch  \\\n",
       "0   0  female   group B           bachelor's degree      standard   \n",
       "1   1  female   group C                some college      standard   \n",
       "2   2  female   group B             master's degree      standard   \n",
       "3   3    male   group A          associate's degree  free/reduced   \n",
       "4   4    male   group C                some college      standard   \n",
       "5   5  female   group B          associate's degree      standard   \n",
       "6   6  female   group B                some college      standard   \n",
       "7   7    male   group B                some college  free/reduced   \n",
       "8   8    male   group D                 high school  free/reduced   \n",
       "9   9  female   group B                 high school  free/reduced   \n",
       "\n",
       "  test preparation course  math score  reading score  writing score  \n",
       "0                    none          72             72             74  \n",
       "1               completed          69             90             88  \n",
       "2                    none          90             95             93  \n",
       "3                    none          47             57             44  \n",
       "4                    none          76             78             75  \n",
       "5                    none          71             83             78  \n",
       "6               completed          88             95             92  \n",
       "7                    none          40             43             39  \n",
       "8               completed          64             64             67  \n",
       "9                    none          38             60             50  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>math score</th>\n",
       "      <th>reading score</th>\n",
       "      <th>writing score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1000.000000</td>\n",
       "      <td>1000.00000</td>\n",
       "      <td>1000.000000</td>\n",
       "      <td>1000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>499.500000</td>\n",
       "      <td>66.08900</td>\n",
       "      <td>69.169000</td>\n",
       "      <td>68.054000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>288.819436</td>\n",
       "      <td>15.16308</td>\n",
       "      <td>14.600192</td>\n",
       "      <td>15.195657</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>10.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>249.750000</td>\n",
       "      <td>57.00000</td>\n",
       "      <td>59.000000</td>\n",
       "      <td>57.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>499.500000</td>\n",
       "      <td>66.00000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>69.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>749.250000</td>\n",
       "      <td>77.00000</td>\n",
       "      <td>79.000000</td>\n",
       "      <td>79.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>999.000000</td>\n",
       "      <td>100.00000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                ID  math score  reading score  writing score\n",
       "count  1000.000000  1000.00000    1000.000000    1000.000000\n",
       "mean    499.500000    66.08900      69.169000      68.054000\n",
       "std     288.819436    15.16308      14.600192      15.195657\n",
       "min       0.000000     0.00000      17.000000      10.000000\n",
       "25%     249.750000    57.00000      59.000000      57.750000\n",
       "50%     499.500000    66.00000      70.000000      69.000000\n",
       "75%     749.250000    77.00000      79.000000      79.000000\n",
       "max     999.000000   100.00000     100.000000     100.000000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Task Details that I'm proposing: \n",
    "\n",
    "Figure out if a correlation exists between the different attributes that are in the dataset.\n",
    "\n",
    "- Gender and reading/writing/math score and overall score. \n",
    "- Test Preparation and reading/writing/math score and overall score.\n",
    "- Ethnicity and reading/writing/math score and overall score.\n",
    "- Test Preparation and Gender.\n",
    "- Test Preparation and Parental level of education.\n",
    "- Ethnicity and Parental level of education.\n",
    "\n",
    "### Data Visualization:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAFgCAYAAACFYaNMAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAU3ElEQVR4nO3de7SddX3n8feHBAYnoICehozogkoGFjpcyoGWyrhU0IXTllC11EtrtKxmXB0vHUsZrFPHqXWqWFud2lumoqHLUkSkgKvFoRFrtQwSLookMCBKS8whB+QScQkT+M4f+0k9pifJTsKzf+ec/X6ttdd+fr/nsr97Za9PnvPbz/PbqSokSaO3T+sCJGlcGcCS1IgBLEmNGMCS1IgBLEmNLG5dwDDOOOOMuvrqq1uXIUl7KrN1zosz4Pvvv791CZL0lJsXASxJC5EBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNzIvZ0DS88847j6mpKQ499FAuuOCC1uVI2gkDeIGZmppi48aNrcuQNASHICSpEQNYkhoxgCWpEQNYkhpZ8F/CnfjrF7UuYaQOvH8Li4B/vH/LWL33Gz/4htYlSLvNM2BJasQAlqRGDGBJasQAlqRGDGBJamTBXwUxbp7cb8kPPUuau3oL4CRHAZfM6PpR4N3ARV3/4cC3gLOr6sG+6hg3jy5/eesSJA2ptyGIqrqjqo6vquOBE4HvAZcD5wNrq2o5sLZrS9LYGdUY8GnAN6rqHmAFsKbrXwOcNaIaJGlOGVUAvwa4uFteWlWbuuUpYOlsOyRZlWRdknXT09OjqFGSRqr3AE6yH3AmcOn266qqgJptv6paXVWTVTU5MTHRc5WSNHqjOAN+BXBTVd3Xte9Lsgyge948ghokac4ZRQC/lh8MPwBcCazsllcCV4ygBkmac3oN4CRLgJcBn5nR/X7gZUnuBE7v2pI0dnq9EaOqHgWeuV3fAwyuipCkseatyJLUiAEsSY0YwJLUiAEsSY0YwJLUiAEsSY0YwJLUiAEsSY0YwJLUiAEsSY0YwJLUiAEsSY0YwJLUiAEsSY30Oh2lpIXlvPPOY2pqikMPPZQLLrigdTnzngEsaWhTU1Ns3LixdRkLhkMQktSIASxJjRjAktSIASxJjfglnLQX/vG3/l3rEkZq63cOARaz9Tv3jNV7f+67b+3luJ4BS1IjBrAkNWIAS1IjBrAkNWIAS1IjXgUhaWjP2v9JYGv3rL1lAEsa2rnHPtS6hAXFIQhJasQAlqRGeg3gJAcl+XSS25NsSHJKkkOSXJPkzu754D5rkKS5qu8z4I8AV1fV0cBxwAbgfGBtVS0H1nZtSRo7vQVwkmcALwI+BlBVj1fVQ8AKYE232RrgrL5qkKS5rM8z4COAaeDjSW5O8mdJlgBLq2pTt80UsLTHGiRpzuozgBcDPwb8cVWdADzKdsMNVVVAzbZzklVJ1iVZNz093WOZktRGnwF8L3BvVV3ftT/NIJDvS7IMoHvePNvOVbW6qiaranJiYqLHMiWpjd4CuKqmgH9KclTXdRqwHrgSWNn1rQSu6KsGSZrL+r4T7q3AJ5PsB9wNvIlB6H8qyTnAPcDZPdcgSXNSrwFcVbcAk7OsOq3P15Wk+cA74SSpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpEQNYkhoxgCWpkcV9HjzJt4AtwBPA1qqaTHIIcAlwOPAt4OyqerDPOiRpLhrFGfBLqur4qprs2ucDa6tqObC2a0vS2GkxBLECWNMtrwHOalCDJDXXdwAX8L+T3JhkVde3tKo2dctTwNLZdkyyKsm6JOump6d7LlOSRq/XMWDg1KramORHgGuS3D5zZVVVkpptx6paDawGmJycnHUbSZrPej0DrqqN3fNm4HLgZOC+JMsAuufNfdYgSXNVbwGcZEmSA7ctAy8Hvg5cCazsNlsJXNFXDZI0l/U5BLEUuDzJttf5i6q6OskNwKeSnAPcA5zdYw2SNGf1FsBVdTdw3Cz9DwCn9fW6kjRfeCecJDViAEtSIwawJDViAEtSIwawJDViAEtSIwawJDViAEtSI0MFcJKnJTmq72IkaZzsMoCT/AxwC3B11z4+yZV9FyZJC90wZ8DvYTCL2UMAVXULcESPNUnSWBgmgP9fVT28XZ/z80rSXhpmMp7bkrwOWJRkOfA24B/6LUuSFr5hzoDfCjwfeAz4C+Bh4Ff7LEqSxsFOz4CTLAJ+q6rOBd41mpIkaTzs9Ay4qp4ATh1RLZI0VoYZA765u+zsUuDRbZ1V9ZneqpKkMTBMAO8PPAC8dEZfAQawJO2FXQZwVb1pFIVI0rgZ5k64w5JcnmRz97gsyWGjKE6SFrJhLkP7OIOfkv833eOqrk+StBeGCeCJqvp4VW3tHp8AJnquS5IWvGEC+IEkv5BkUff4BQZfykmS9sIwAfxLwNnAFLAJeDXgF3OStJeGuQriHuDMEdQiSWNlmKsg1iQ5aEb74CQX9luWJC18wwxBHFtVD21rVNWDwAn9lSRJ42GYAN4nycHbGkkOYbg76CRJOzFMkH4IuC7JpUAYfAn3vl6rkqQxMMyXcBclWccP5oJ4ZVWt77csSVr4dhnASZ4HfKOq1id5MXB6km/PHBeWJO2+YcaALwOeSHIk8KfAcxj8MsZQups3bk7y2a59RJLrk9yV5JIk++1R5ZI0zw0TwE9W1VbglcBHq+rXgWW78RpvBzbMaH8A+P2qOhJ4EDhnN44lSQvGUL+KnOS1wBuAz3Z9+w5z8G7WtJ8C/qxrh8FY8qe7TdYAZ+1OwZK0UAwTwG8CTgHeV1XfTHIE8OdDHv/DwHnAk137mcBD3Rk1wL3As2fbMcmqJOuSrJuenh7y5SRp/thlAFfV+qp6W1Vd3LW/WVUf2NV+SX4a2FxVN+5JYVW1uqomq2pyYsLJ1yQtPH3eUPFC4Mwk/4HBzxo9HfgIcFCSxd1Z8GHAxh5rkKQ5a5ghiD1SVe+sqsOq6nDgNcDnq+r1wLUMbuYAWAlc0VcNkjSX9RbAO/FfgHckuYvBmPDHGtQgSc0NcyPGVQx+BXmmh4F1wJ9W1fd3dYyq+gLwhW75buDk3S1UkhaaYc6A7wa+C/yv7vEIsAX4t11bkrQHhvkS7ier6qQZ7auS3FBVJyW5ra/CJGmhG+YM+IAkz93W6JYP6JqP91KVJI2BYc6Afw34UpJvMJiO8gjgV5IsYXAnmyRpDwwzHeVfJ1kOHN113THji7cP91aZJC1ww96IcSJweLf9cUmoqot6q0qSxsAwl6H9OfA84Bbgia67AANYkvbCMGfAk8AxVbX9tcCSpL0wzFUQXwcO7bsQSRo3w5wBPwtYn+QrwGPbOqvqzN6qkqQxMEwAv6fvIiRpHA1zGdrfjaIQSRo3OwzgJF+qqlOTbOGHJ+MJUFX19N6rk6QFbIcBXFWnds8Hjq4cSRofu7wKorsOeJd9kqTdM8xlaM+f2UiymMGdcZKkvbDDAE7yzm7899gkj3SPLcB9+DNCkrTXdhjAVfU73fjvB6vq6d3jwKp6ZlW9c4Q1StKCtLOrII6uqtuBS5P82Pbrq+qmXiuTpAVuZ9cBvwNYBXxolnUFvLSXiiRpTOzsMrRVSfYB/mtVfXmENUnSWNjpVRBV9STw0RHVIkljZZjL0NYmeVWS9F6NJI2RYQL4PwKXAo9tuxQtySM91yVJC94wk/F4K7Ik9WCoW5GT/HKSo3e1rSRpeMMMQVwILAP+IMndSS5L8vae65KkBW+YIYhrk3wROAl4CfBmBvNDfKTn2iRpQRvmV5HXAkuA64C/B06qqs19FyZJC90wQxBfAx4HXgAcC7wgydN6rUqSxsAuA7iq/nNVvQh4JfAA8HHgoV3tl2T/JF9J8tUktyX5713/EUmuT3JXkkuS7Le3b0KS5qNhroJ4S5JLgJuBFQy+lHvFEMd+DHhpVR0HHA+ckeQngA8Av19VRwIPAufsafGSNJ8N86vI+wO/B9xYVVuHPXBVFfDdrrlv99g2ic/ruv41DH51+Y+HPa4kLRTDXAXxu3t68CSLgBuBI4E/BL4BPDQjyO8Fnr2nx5ek+WyYL+H2WFU9UVXHA4cBJwND38yRZFWSdUnWTU9P91ajJLXSawBvU1UPAdcCpwAHdb8rB4Ng3riDfVZX1WRVTU5MTIyiTEkaqd4COMlEkoO65acBLwM2MAjiV3ebrcTfl5M0pob5Em5PLQPWdOPA+wCfqqrPJlkP/GWS32ZwZcXHeqxBkuas3gK4qr4GnDBL/90MxoMlaayNZAxYkvQvGcCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmNGMCS1IgBLEmN9BbASZ6T5Nok65PcluTtXf8hSa5Jcmf3fHBfNUjSXNbnGfBW4Neq6hjgJ4D/lOQY4HxgbVUtB9Z2bUkaO70FcFVtqqqbuuUtwAbg2cAKYE232RrgrL5qkKS5bCRjwEkOB04ArgeWVtWmbtUUsHQH+6xKsi7Juunp6VGUKUkj1XsAJzkAuAz41ap6ZOa6qiqgZtuvqlZX1WRVTU5MTPRdpiSNXK8BnGRfBuH7yar6TNd9X5Jl3fplwOY+a5CkuarPqyACfAzYUFW/N2PVlcDKbnklcEVfNUjSXLa4x2O/EPhF4NYkt3R9vwG8H/hUknOAe4Cze6xBkuas3gK4qr4EZAerT+vrdSVpvvBOOElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqxACWpEYMYElqpLcATnJhks1Jvj6j75Ak1yS5s3s+uK/Xl6S5rs8z4E8AZ2zXdz6wtqqWA2u7tiSNpd4CuKq+CHxnu+4VwJpueQ1wVl+vL0lz3ajHgJdW1aZueQpYuqMNk6xKsi7Juunp6dFUJ0kj1OxLuKoqoHayfnVVTVbV5MTExAgrk6TRGHUA35dkGUD3vHnEry9Jc8aoA/hKYGW3vBK4YsSvL0lzRp+XoV0MXAccleTeJOcA7wdeluRO4PSuLUljaXFfB66q1+5g1Wl9vaYkzSfeCSdJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjRjAktSIASxJjTQJ4CRnJLkjyV1Jzm9RgyS1NvIATrII+EPgFcAxwGuTHDPqOiSptRZnwCcDd1XV3VX1OPCXwIoGdUhSU4sbvOazgX+a0b4X+PHtN0qyCljVNb+b5I4R1LZQPAu4v3URo5TfXdm6hHEydp8v/lv29ghXV9UZ23e2COChVNVqYHXrOuajJOuqarJ1HVqY/Hw9dVoMQWwEnjOjfVjXJ0ljpUUA3wAsT3JEkv2A1wBXNqhDkpoa+RBEVW1N8hbgc8Ai4MKqum3UdSxwDt2oT36+niKpqtY1SNJY8k44SWrEAJakRgzgOSjJ25JsSPLJno7/niTn9nFsjZ8kL07y2dZ1zEdz9jrgMfcrwOlVdW/rQiT1xzPgOSbJnwA/CvxNkncluTDJV5LcnGRFt80bk/xVkmuSfCvJW5K8o9vm/yQ5pNvul5PckOSrSS5L8q9neb3nJbk6yY1J/j7J0aN9x5oLkhye5PYkn0jyf5N8MsnpSb6c5M4kJ3eP67rP2T8kOWqW4yyZ7TOr2RnAc0xVvRn4NvASYAnw+ao6uWt/MMmSbtMXAK8ETgLeB3yvqk4ArgPe0G3zmao6qaqOAzYA58zykquBt1bVicC5wB/18840DxwJfAg4unu8DjiVwefiN4DbgX/ffc7eDfyPWY7xLnb8mdV2HIKY214OnDljvHZ/4Lnd8rVVtQXYkuRh4Kqu/1bg2G75BUl+GzgIOIDBtdf/LMkBwE8Clyb/fK/7v+rjjWhe+GZV3QqQ5DZgbVVVkluBw4FnAGuSLAcK2HeWY+zoM7uh7+LnIwN4bgvwqqr6oYmIkvw48NiMridntJ/kB/+unwDOqqqvJnkj8OLtjr8P8FBVHf/Ulq15alefqfcy+I//Z5McDnxhlmPM+pnV7ByCmNs+B7w13elpkhN2c/8DgU1J9gVev/3KqnoE+GaSn+uOnyTH7WXNWriewQ/mbXnjDrbZ28/sWDGA57b3Mvgz72vdn4Tv3c39fxO4Hvgyg/G72bweOCfJV4HbcG5m7dgFwO8kuZkd//W8t5/ZseKtyJLUiGfAktSIASxJjRjAktSIASxJjRjAktSIASzNopsT4dWt69DCZgBLT4Ek3lWq3WYAa95L8ptJ7kjypSQXJzl3R7O8dWe2/7ObzevubWe53V2AH+2O87fAj8w4/olJ/q471ueSLOv6v5Dkw0nWAW9v8d41v/m/tua1JCcBrwKOY3AH1k3AjQxmeXtzVd3ZzZ3xR8BLu92WMZjl62gGv8j9aeBngaOAY4ClwHrgwu427j8AVlTVdJKfZzD73C91x9qvqiZ7f6NakAxgzXcvBK6oqu8D309yFYMZuHY2y9tfVdWTwPokS7u+FwEXV9UTwLeTfL7rP4rB1J/XdMdaBGyacaxLenhPGhMGsBaiXc3yNnPWr+xgm5nrb6uqU3aw/tHdLU7axjFgzXdfBn4myf7d/MY/DXyP3Z/l7YvAzydZ1I3xvqTrvwOYSHJKd6x9kzy/l3eisWMAa16rqhsYjON+DfgbBhPSP8zuz/J2OXAng7Hfixj8sghV9TjwauAD3bFuYTC8Ie01Z0PTvJfkgKr6bvebd18EVlXVTa3rknbFMWAtBKuTHMPgy7c1hq/mC8+AJakRx4AlqREDWJIaMYAlqREDWJIaMYAlqZH/D2eD/xRqkbOXAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "grid = sns.catplot(x=\"gender\", y = \"math score\", kind=\"bar\", data=data);\n",
    "grid = sns.catplot(x=\"gender\", y = \"reading score\", kind=\"bar\", data=data);\n",
    "grid = sns.catplot(x=\"gender\", y = \"writing score\", kind=\"bar\", data=data);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "none         642\n",
       "completed    358\n",
       "Name: test preparation course, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "labels = 'Without test Preprataion', 'With Test Preparation'\n",
    "data['test preparation course'].value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "s1 = 642/1000*100 \n",
    "s2 = 358/1000*100\n",
    "sizes = [s1, s2]\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=True, startangle=90)\n",
    "ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "math_score_mean = data.groupby('test preparation course')['math score'].mean()\n",
    "reading_score_mean = data.groupby('test preparation course')['reading score'].mean()\n",
    "writing_score_mean = data.groupby('test preparation course')['writing score'].mean()\n",
    "\n",
    "labels = 'With test Preprataion', 'Without Test Preparation'\n",
    "sizes = [math_score_mean]\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=True, startangle=90)\n",
    "ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.\n",
    "\n",
    "plt.show()\n",
    "labels = 'With test Preprataion', 'Without Test Preparation'\n",
    "sizes = [writing_score_mean]\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=True, startangle=90)\n",
    "ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.\n",
    "\n",
    "plt.show()\n",
    "labels = 'With test Preprataion', 'Without Test Preparation'\n",
    "sizes = [reading_score_mean]\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=True, startangle=90)\n",
    "ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "group C    319\n",
       "group D    262\n",
       "group B    190\n",
       "group E    140\n",
       "group A     89\n",
       "Name: ethnicity, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['ethnicity'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Writing Mean Score')"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x360 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "math_score_mean = data.groupby('ethnicity')['math score'].mean()\n",
    "reading_score_mean = data.groupby('ethnicity')['reading score'].mean()\n",
    "writing_score_mean = data.groupby('ethnicity')['writing score'].mean()\n",
    "\n",
    "plt.figure(figsize=(16,5))\n",
    "plt.subplot(131)\n",
    "grid = sns.barplot(x= math_score_mean.index , y = math_score_mean.values)\n",
    "plt.ylabel('Math Mean Score')\n",
    "\n",
    "plt.subplot(132)\n",
    "grid = sns.barplot(x= reading_score_mean.index , y = reading_score_mean.values)\n",
    "plt.ylabel('Reading Mean Score')\n",
    "\n",
    "plt.subplot(133)\n",
    "grid = sns.barplot(x= writing_score_mean.index , y = writing_score_mean.values)\n",
    "plt.ylabel('Writing Mean Score')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Neither the `x` nor `y` variable appears to be numeric.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-21-7d8dd3514ff9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0msns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcatplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"gender\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0;34m'test preparation course'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0msns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcatplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"gender\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'test preparation course'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0msns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcatplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"gender\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'test preparation course'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.virtualenvs/tensorflow/lib/python3.7/site-packages/seaborn/categorical.py\u001b[0m in \u001b[0;36mcatplot\u001b[0;34m(x, y, hue, data, row, col, col_wrap, estimator, ci, n_boot, units, order, hue_order, row_order, col_order, kind, height, aspect, orient, color, palette, legend, legend_out, sharex, sharey, margin_titles, facet_kws, **kwargs)\u001b[0m\n\u001b[1;32m   3714\u001b[0m     \u001b[0;31m# facets to ensure representation of all data in the final plot\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3715\u001b[0m     \u001b[0mp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_CategoricalPlotter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3716\u001b[0;31m     \u001b[0mp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mestablish_variables\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx_\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my_\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0morient\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0morder\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhue_order\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3717\u001b[0m     \u001b[0morder\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgroup_names\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3718\u001b[0m     \u001b[0mhue_order\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhue_names\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.virtualenvs/tensorflow/lib/python3.7/site-packages/seaborn/categorical.py\u001b[0m in \u001b[0;36mestablish_variables\u001b[0;34m(self, x, y, hue, data, orient, order, hue_order, units)\u001b[0m\n\u001b[1;32m    156\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    157\u001b[0m             \u001b[0;31m# Figure out the plotting orientation\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 158\u001b[0;31m             \u001b[0morient\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minfer_orient\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0morient\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    159\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    160\u001b[0m             \u001b[0;31m# Option 2a:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.virtualenvs/tensorflow/lib/python3.7/site-packages/seaborn/categorical.py\u001b[0m in \u001b[0;36minfer_orient\u001b[0;34m(self, x, y, orient)\u001b[0m\n\u001b[1;32m    359\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mis_not_numeric\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    360\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mis_not_numeric\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 361\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mno_numeric\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    362\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    363\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0;34m\"h\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: Neither the `x` nor `y` variable appears to be numeric."
     ]
    }
   ],
   "source": [
    "\n",
    "sns.catplot(x=\"gender\",y= 'test preparation course', data=data);\n",
    "sns.catplot(x=\"gender\", y='test preparation course', data=data);\n",
    "sns.catplot(x=\"gender\", y='test preparation course', data=data);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    \n",
    "Without = 'none'\n",
    "With = 'completed'\n",
    "\n",
    "fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 4))\n",
    "women = data[data['gender']=='female']\n",
    "men = data[data['gender']=='male']\n",
    "ax = sns.distplot(women[women['test preparation course']=='none'], bins=18, label = Without, ax = axes[0], kde =False)\n",
    "ax = sns.distplot(women[women['test preparation course']=='completed'], bins=40, label = With, ax = axes[0], kde =False)\n",
    "ax.legend()\n",
    "ax.set_title('Female')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " - Is possible o see some patterns  and observations from the data visualization.\n",
    "         - Females achieve better results in Reading/Writing , and males achieve the best results in math. \n",
    "         - in mean scores, the mean score gradually increases for ethnicity from pattern A to E. "
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
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
