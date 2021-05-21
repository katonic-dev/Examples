{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Automobile Dataset Description\n",
    "\n",
    "#### This dataset consist of data From 1985 Ward's Automotive Yearbook.\n",
    "\n",
    "#### This data set consists of three types of entities: \n",
    " - (a) The specification of an auto in terms of various characteristics\n",
    " - (b) Its assigned insurance risk rating\n",
    " - (c) Its normalized losses in use as compared to other cars. \n",
    "\n",
    "#### The second rating corresponds to the degree to which the auto is more risky than its price indicates. Cars are initially assigned a risk factor symbol associated with its price. Then if it is more risky (or less), this symbol is adjusted by moving it up (or down) the scale. Actuarians call this process \"symboling\". A value of +3 indicates that the auto is risky, -3 that it is probably pretty safe.\n",
    "\n",
    "#### The third factor is the relative averages loss payment per insured vehicle year. This value is normalized for all autos within a particular size classification (two-door small, station wagons, sports/speciality, etc...), and represents the averages loss per car per year.\n",
    "\n",
    "## Importing the Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # !pip install CUDA \n",
    "# !conda install tensorflow-gpu cudatoolkit=10.1\n",
    "# !sudo apt-get install libcudart10.1\n",
    "#!pip install alibi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "tags": [
     "imports"
    ]
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "#import seaborn as sns\n",
    "#from matplotlib import pyplot as plt\n",
    "#from matplotlib import style\n",
    "\n",
    "from sklearn import linear_model\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.linear_model import Perceptron\n",
    "from sklearn.linear_model import SGDClassifier\n",
    "from sklearn.ensemble import GradientBoostingClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.model_selection import train_test_split\n",
    "#from alibi.explainers import AnchorTabular\n",
    "import joblib\n",
    "from pyspark.sql import SparkSession\n",
    "# from retrieve_minio import *\n",
    "import uuid\n",
    "import os\n",
    "import shutil\n",
    "import pickle\n",
    "from datetime import datetime\n",
    "# from numba import jit, cuda\n",
    "\n",
    "# from minio import Minio\n",
    "# from minio.error import ResponseError\n",
    "\n",
    "from subprocess import run, Popen, PIPE\n",
    "#from ctypes import *\n",
    "from pyspark import SparkContext, SparkConf\n",
    "from pyspark.sql import DataFrame, SparkSession, Window\n",
    "from pyspark.sql.functions import col, expr, monotonically_increasing_id, row_number,current_timestamp\n",
    "# from data_io import *\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from typing import  List\n",
    "from datetime import datetime\n",
    "#from minio import Minio\n",
    "#from minio.error import ResponseError\n",
    "import uuid\n",
    "import os\n",
    "import shutil"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading the modified data \n",
    "automobile = pd.read_csv(r'/mnt/automobile.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "symboling              int64\n",
       "normalized-losses     object\n",
       "make                  object\n",
       "fuel-type             object\n",
       "aspiration            object\n",
       "num-of-doors          object\n",
       "body-style            object\n",
       "drive-wheels          object\n",
       "engine-location       object\n",
       "wheel-base           float64\n",
       "length               float64\n",
       "width                float64\n",
       "height               float64\n",
       "curb-weight            int64\n",
       "engine-type           object\n",
       "num-of-cylinders      object\n",
       "engine-size            int64\n",
       "fuel-system           object\n",
       "bore                  object\n",
       "stroke                object\n",
       "compression-ratio    float64\n",
       "horsepower            object\n",
       "peak-rpm              object\n",
       "city-mpg               int64\n",
       "highway-mpg            int64\n",
       "price                 object\n",
       "dtype: object"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',\n",
       "       'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',\n",
       "       'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type',\n",
       "       'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',\n",
       "       'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',\n",
       "       'highway-mpg', 'price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile.keys()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Shape of the data set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(205, 26)\n"
     ]
    }
   ],
   "source": [
    "print(automobile.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Describe the stats about the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
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
       "      <th>symboling</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>length</th>\n",
       "      <th>width</th>\n",
       "      <th>height</th>\n",
       "      <th>curb-weight</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.834146</td>\n",
       "      <td>98.756585</td>\n",
       "      <td>174.049268</td>\n",
       "      <td>65.907805</td>\n",
       "      <td>53.724878</td>\n",
       "      <td>2555.565854</td>\n",
       "      <td>126.907317</td>\n",
       "      <td>10.142537</td>\n",
       "      <td>25.219512</td>\n",
       "      <td>30.751220</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.245307</td>\n",
       "      <td>6.021776</td>\n",
       "      <td>12.337289</td>\n",
       "      <td>2.145204</td>\n",
       "      <td>2.443522</td>\n",
       "      <td>520.680204</td>\n",
       "      <td>41.642693</td>\n",
       "      <td>3.972040</td>\n",
       "      <td>6.542142</td>\n",
       "      <td>6.886443</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-2.000000</td>\n",
       "      <td>86.600000</td>\n",
       "      <td>141.100000</td>\n",
       "      <td>60.300000</td>\n",
       "      <td>47.800000</td>\n",
       "      <td>1488.000000</td>\n",
       "      <td>61.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>16.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>94.500000</td>\n",
       "      <td>166.300000</td>\n",
       "      <td>64.100000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>2145.000000</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>8.600000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>25.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>173.200000</td>\n",
       "      <td>65.500000</td>\n",
       "      <td>54.100000</td>\n",
       "      <td>2414.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>30.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>102.400000</td>\n",
       "      <td>183.100000</td>\n",
       "      <td>66.900000</td>\n",
       "      <td>55.500000</td>\n",
       "      <td>2935.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>9.400000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>34.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>120.900000</td>\n",
       "      <td>208.100000</td>\n",
       "      <td>72.300000</td>\n",
       "      <td>59.800000</td>\n",
       "      <td>4066.000000</td>\n",
       "      <td>326.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>49.000000</td>\n",
       "      <td>54.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        symboling  wheel-base      length       width      height  \\\n",
       "count  205.000000  205.000000  205.000000  205.000000  205.000000   \n",
       "mean     0.834146   98.756585  174.049268   65.907805   53.724878   \n",
       "std      1.245307    6.021776   12.337289    2.145204    2.443522   \n",
       "min     -2.000000   86.600000  141.100000   60.300000   47.800000   \n",
       "25%      0.000000   94.500000  166.300000   64.100000   52.000000   \n",
       "50%      1.000000   97.000000  173.200000   65.500000   54.100000   \n",
       "75%      2.000000  102.400000  183.100000   66.900000   55.500000   \n",
       "max      3.000000  120.900000  208.100000   72.300000   59.800000   \n",
       "\n",
       "       curb-weight  engine-size  compression-ratio    city-mpg  highway-mpg  \n",
       "count   205.000000   205.000000         205.000000  205.000000   205.000000  \n",
       "mean   2555.565854   126.907317          10.142537   25.219512    30.751220  \n",
       "std     520.680204    41.642693           3.972040    6.542142     6.886443  \n",
       "min    1488.000000    61.000000           7.000000   13.000000    16.000000  \n",
       "25%    2145.000000    97.000000           8.600000   19.000000    25.000000  \n",
       "50%    2414.000000   120.000000           9.000000   24.000000    30.000000  \n",
       "75%    2935.000000   141.000000           9.400000   30.000000    34.000000  \n",
       "max    4066.000000   326.000000          23.000000   49.000000    54.000000  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Checking for the null values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "tags": [
     "block:data_preprocessing",
     "prev:load_data"
    ]
   },
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
       "      <th>total</th>\n",
       "      <th>percent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>symboling</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>normalized-losses</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>highway-mpg</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>city-mpg</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>peak-rpm</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>horsepower</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>compression-ratio</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stroke</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>bore</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fuel-system</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   total  percent\n",
       "symboling              0      0.0\n",
       "normalized-losses      0      0.0\n",
       "highway-mpg            0      0.0\n",
       "city-mpg               0      0.0\n",
       "peak-rpm               0      0.0\n",
       "horsepower             0      0.0\n",
       "compression-ratio      0      0.0\n",
       "stroke                 0      0.0\n",
       "bore                   0      0.0\n",
       "fuel-system            0      0.0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Number of missing in each column\n",
    "missing = pd.DataFrame(automobile.isnull().sum()).rename(columns = {0: 'total'})\n",
    "\n",
    "# Create a percentage missing\n",
    "missing['percent'] = missing['total'] / len(automobile)\n",
    "\n",
    "missing.sort_values('percent', ascending = False).head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "symboling            0\n",
       "normalized-losses    0\n",
       "make                 0\n",
       "fuel-type            0\n",
       "aspiration           0\n",
       "num-of-doors         0\n",
       "body-style           0\n",
       "drive-wheels         0\n",
       "engine-location      0\n",
       "wheel-base           0\n",
       "length               0\n",
       "width                0\n",
       "height               0\n",
       "curb-weight          0\n",
       "engine-type          0\n",
       "num-of-cylinders     0\n",
       "engine-size          0\n",
       "fuel-system          0\n",
       "bore                 0\n",
       "stroke               0\n",
       "compression-ratio    0\n",
       "horsepower           0\n",
       "peak-rpm             0\n",
       "city-mpg             0\n",
       "highway-mpg          0\n",
       "price                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Find out number of records having '?' value for normalized losses"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "41"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile['normalized-losses'].loc[automobile['normalized-losses'] == '?'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Setting the missing value to mean of normalized losses and conver the datatype to integer\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    122\n",
       "1    122\n",
       "2    122\n",
       "3    164\n",
       "4    164\n",
       "Name: normalized-losses, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nl = automobile['normalized-losses'].loc[automobile['normalized-losses'] != '?']\n",
    "nlmean = nl.astype(str).astype(int).mean()\n",
    "automobile['normalized-losses'] = automobile['normalized-losses'].replace('?',nlmean).astype(int)\n",
    "automobile['normalized-losses'].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Find out the number of values which are not numeric\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True     201\n",
       "False      4\n",
       "Name: price, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile['price'].str.isnumeric().value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### List out the values which are not numeric\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9      ?\n",
       "44     ?\n",
       "45     ?\n",
       "129    ?\n",
       "Name: price, dtype: object"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile['price'].loc[automobile['price'].str.isnumeric() == False]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Setting the missing value to mean of price and convert the datatype to integer\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    13495\n",
       "1    16500\n",
       "2    16500\n",
       "3    13950\n",
       "4    17450\n",
       "Name: price, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "price = automobile['price'].loc[automobile['price'] != '?']\n",
    "pmean = price.astype(str).astype(int).mean()\n",
    "automobile['price'] = automobile['price'].replace('?',pmean).astype(int)\n",
    "automobile['price'].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Checking the numberic and replacing with mean value and conver the datatype to integer for horsepower\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "automobile['horsepower'].str.isnumeric().value_counts()\n",
    "horsepower = automobile['horsepower'].loc[automobile['horsepower'] != '?']\n",
    "hpmean = horsepower.astype(str).astype(int).mean()\n",
    "automobile['horsepower'] = automobile['horsepower'].replace('?',pmean).astype(int)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Checking the outlier of horsepower\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
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
       "      <th>symboling</th>\n",
       "      <th>normalized-losses</th>\n",
       "      <th>make</th>\n",
       "      <th>fuel-type</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>num-of-doors</th>\n",
       "      <th>body-style</th>\n",
       "      <th>drive-wheels</th>\n",
       "      <th>engine-location</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>...</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>fuel-system</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>130</th>\n",
       "      <td>0</td>\n",
       "      <td>122</td>\n",
       "      <td>renault</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>wagon</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>96.1</td>\n",
       "      <td>...</td>\n",
       "      <td>132</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.46</td>\n",
       "      <td>3.9</td>\n",
       "      <td>8.7</td>\n",
       "      <td>13207</td>\n",
       "      <td>?</td>\n",
       "      <td>23</td>\n",
       "      <td>31</td>\n",
       "      <td>9295</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>131</th>\n",
       "      <td>2</td>\n",
       "      <td>122</td>\n",
       "      <td>renault</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>96.1</td>\n",
       "      <td>...</td>\n",
       "      <td>132</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.46</td>\n",
       "      <td>3.9</td>\n",
       "      <td>8.7</td>\n",
       "      <td>13207</td>\n",
       "      <td>?</td>\n",
       "      <td>23</td>\n",
       "      <td>31</td>\n",
       "      <td>9895</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     symboling  normalized-losses     make fuel-type aspiration num-of-doors  \\\n",
       "130          0                122  renault       gas        std         four   \n",
       "131          2                122  renault       gas        std          two   \n",
       "\n",
       "    body-style drive-wheels engine-location  wheel-base  ...  engine-size  \\\n",
       "130      wagon          fwd           front        96.1  ...          132   \n",
       "131  hatchback          fwd           front        96.1  ...          132   \n",
       "\n",
       "     fuel-system  bore  stroke compression-ratio horsepower  peak-rpm  \\\n",
       "130         mpfi  3.46     3.9               8.7      13207         ?   \n",
       "131         mpfi  3.46     3.9               8.7      13207         ?   \n",
       "\n",
       "    city-mpg highway-mpg price  \n",
       "130       23          31  9295  \n",
       "131       23          31  9895  \n",
       "\n",
       "[2 rows x 26 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile.loc[automobile['horsepower'] > 10000]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Excluding the outlier data for horsepower\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "tags": []
   },
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
       "      <th>symboling</th>\n",
       "      <th>normalized-losses</th>\n",
       "      <th>make</th>\n",
       "      <th>fuel-type</th>\n",
       "      <th>aspiration</th>\n",
       "      <th>num-of-doors</th>\n",
       "      <th>body-style</th>\n",
       "      <th>drive-wheels</th>\n",
       "      <th>engine-location</th>\n",
       "      <th>wheel-base</th>\n",
       "      <th>...</th>\n",
       "      <th>engine-size</th>\n",
       "      <th>fuel-system</th>\n",
       "      <th>bore</th>\n",
       "      <th>stroke</th>\n",
       "      <th>compression-ratio</th>\n",
       "      <th>horsepower</th>\n",
       "      <th>peak-rpm</th>\n",
       "      <th>city-mpg</th>\n",
       "      <th>highway-mpg</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3</td>\n",
       "      <td>122</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>13495</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>122</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>convertible</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>88.6</td>\n",
       "      <td>...</td>\n",
       "      <td>130</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.47</td>\n",
       "      <td>2.68</td>\n",
       "      <td>9.0</td>\n",
       "      <td>111</td>\n",
       "      <td>5000</td>\n",
       "      <td>21</td>\n",
       "      <td>27</td>\n",
       "      <td>16500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>122</td>\n",
       "      <td>alfa-romero</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>two</td>\n",
       "      <td>hatchback</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>94.5</td>\n",
       "      <td>...</td>\n",
       "      <td>152</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>2.68</td>\n",
       "      <td>3.47</td>\n",
       "      <td>9.0</td>\n",
       "      <td>154</td>\n",
       "      <td>5000</td>\n",
       "      <td>19</td>\n",
       "      <td>26</td>\n",
       "      <td>16500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>164</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>fwd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.8</td>\n",
       "      <td>...</td>\n",
       "      <td>109</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>10.0</td>\n",
       "      <td>102</td>\n",
       "      <td>5500</td>\n",
       "      <td>24</td>\n",
       "      <td>30</td>\n",
       "      <td>13950</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>164</td>\n",
       "      <td>audi</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>4wd</td>\n",
       "      <td>front</td>\n",
       "      <td>99.4</td>\n",
       "      <td>...</td>\n",
       "      <td>136</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.19</td>\n",
       "      <td>3.4</td>\n",
       "      <td>8.0</td>\n",
       "      <td>115</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>22</td>\n",
       "      <td>17450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>200</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>9.5</td>\n",
       "      <td>114</td>\n",
       "      <td>5400</td>\n",
       "      <td>23</td>\n",
       "      <td>28</td>\n",
       "      <td>16845</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>201</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>8.7</td>\n",
       "      <td>160</td>\n",
       "      <td>5300</td>\n",
       "      <td>19</td>\n",
       "      <td>25</td>\n",
       "      <td>19045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>202</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>std</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>173</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.58</td>\n",
       "      <td>2.87</td>\n",
       "      <td>8.8</td>\n",
       "      <td>134</td>\n",
       "      <td>5500</td>\n",
       "      <td>18</td>\n",
       "      <td>23</td>\n",
       "      <td>21485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>203</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>diesel</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>145</td>\n",
       "      <td>idi</td>\n",
       "      <td>3.01</td>\n",
       "      <td>3.4</td>\n",
       "      <td>23.0</td>\n",
       "      <td>106</td>\n",
       "      <td>4800</td>\n",
       "      <td>26</td>\n",
       "      <td>27</td>\n",
       "      <td>22470</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>204</th>\n",
       "      <td>-1</td>\n",
       "      <td>95</td>\n",
       "      <td>volvo</td>\n",
       "      <td>gas</td>\n",
       "      <td>turbo</td>\n",
       "      <td>four</td>\n",
       "      <td>sedan</td>\n",
       "      <td>rwd</td>\n",
       "      <td>front</td>\n",
       "      <td>109.1</td>\n",
       "      <td>...</td>\n",
       "      <td>141</td>\n",
       "      <td>mpfi</td>\n",
       "      <td>3.78</td>\n",
       "      <td>3.15</td>\n",
       "      <td>9.5</td>\n",
       "      <td>114</td>\n",
       "      <td>5400</td>\n",
       "      <td>19</td>\n",
       "      <td>25</td>\n",
       "      <td>22625</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>203 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     symboling  normalized-losses         make fuel-type aspiration  \\\n",
       "0            3                122  alfa-romero       gas        std   \n",
       "1            3                122  alfa-romero       gas        std   \n",
       "2            1                122  alfa-romero       gas        std   \n",
       "3            2                164         audi       gas        std   \n",
       "4            2                164         audi       gas        std   \n",
       "..         ...                ...          ...       ...        ...   \n",
       "200         -1                 95        volvo       gas        std   \n",
       "201         -1                 95        volvo       gas      turbo   \n",
       "202         -1                 95        volvo       gas        std   \n",
       "203         -1                 95        volvo    diesel      turbo   \n",
       "204         -1                 95        volvo       gas      turbo   \n",
       "\n",
       "    num-of-doors   body-style drive-wheels engine-location  wheel-base  ...  \\\n",
       "0            two  convertible          rwd           front        88.6  ...   \n",
       "1            two  convertible          rwd           front        88.6  ...   \n",
       "2            two    hatchback          rwd           front        94.5  ...   \n",
       "3           four        sedan          fwd           front        99.8  ...   \n",
       "4           four        sedan          4wd           front        99.4  ...   \n",
       "..           ...          ...          ...             ...         ...  ...   \n",
       "200         four        sedan          rwd           front       109.1  ...   \n",
       "201         four        sedan          rwd           front       109.1  ...   \n",
       "202         four        sedan          rwd           front       109.1  ...   \n",
       "203         four        sedan          rwd           front       109.1  ...   \n",
       "204         four        sedan          rwd           front       109.1  ...   \n",
       "\n",
       "     engine-size  fuel-system  bore  stroke compression-ratio horsepower  \\\n",
       "0            130         mpfi  3.47    2.68               9.0        111   \n",
       "1            130         mpfi  3.47    2.68               9.0        111   \n",
       "2            152         mpfi  2.68    3.47               9.0        154   \n",
       "3            109         mpfi  3.19     3.4              10.0        102   \n",
       "4            136         mpfi  3.19     3.4               8.0        115   \n",
       "..           ...          ...   ...     ...               ...        ...   \n",
       "200          141         mpfi  3.78    3.15               9.5        114   \n",
       "201          141         mpfi  3.78    3.15               8.7        160   \n",
       "202          173         mpfi  3.58    2.87               8.8        134   \n",
       "203          145          idi  3.01     3.4              23.0        106   \n",
       "204          141         mpfi  3.78    3.15               9.5        114   \n",
       "\n",
       "     peak-rpm city-mpg highway-mpg  price  \n",
       "0        5000       21          27  13495  \n",
       "1        5000       21          27  16500  \n",
       "2        5000       19          26  16500  \n",
       "3        5500       24          30  13950  \n",
       "4        5500       18          22  17450  \n",
       "..        ...      ...         ...    ...  \n",
       "200      5400       23          28  16845  \n",
       "201      5300       19          25  19045  \n",
       "202      5500       18          23  21485  \n",
       "203      4800       26          27  22470  \n",
       "204      5400       19          25  22625  \n",
       "\n",
       "[203 rows x 26 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile[np.abs(automobile.horsepower-automobile.horsepower.mean())<=(3*automobile.horsepower.std())]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Find out the number of invalid value\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55    ?\n",
       "56    ?\n",
       "57    ?\n",
       "58    ?\n",
       "Name: bore, dtype: object"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "automobile['bore'].loc[automobile['bore'] == '?']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Writing the modified data and saving thems\n",
    "automobile.to_csv(r'/mnt/automobile.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "kubeflow_notebook": {
   "autosnapshot": false,
   "docker_image": "subhraj07/seldon-test:0.5",
   "experiment": {
    "id": "new",
    "name": "auto-mobile"
   },
   "experiment_name": "auto-mobile",
   "katib_metadata": {
    "algorithm": {
     "algorithmName": "grid"
    },
    "maxFailedTrialCount": 3,
    "maxTrialCount": 12,
    "objective": {
     "objectiveMetricName": "",
     "type": "minimize"
    },
    "parallelTrialCount": 3,
    "parameters": []
   },
   "katib_run": false,
   "pipeline_description": "pipe-auto-preprocess",
   "pipeline_name": "pipe-auto-preprocess",
   "snapshot_volumes": false,
   "steps_defaults": [],
   "volume_access_mode": "rwo",
   "volumes": []
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
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
