{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Iris Dataset Description\n",
    "\n",
    "#### Dataset includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.\n",
    "\n",
    "#### The columns in this dataset are:\n",
    "\n",
    "- Id\n",
    "- SepalLengthCm\n",
    "- SepalWidthCm\n",
    "- PetalLengthCm\n",
    "- PetalWidthCm\n",
    "- Species"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Import the Libraries"
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
    "import seaborn as sns\n",
    "from matplotlib import pyplot as plt\n",
    "from matplotlib import style\n",
    "from sklearn.preprocessing import LabelEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading the modified data \n",
    "df = pd.read_csv(r'/mnt/df.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Manipulating the data\n",
    "\n"
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
       "      <th>Id</th>\n",
       "      <th>SepalLengthCm</th>\n",
       "      <th>SepalWidthCm</th>\n",
       "      <th>PetalLengthCm</th>\n",
       "      <th>PetalWidthCm</th>\n",
       "      <th>Species</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species\n",
       "0   1            5.1           3.5            1.4           0.2  Iris-setosa\n",
       "1   2            4.9           3.0            1.4           0.2  Iris-setosa\n",
       "2   3            4.7           3.2            1.3           0.2  Iris-setosa\n",
       "3   4            4.6           3.1            1.5           0.2  Iris-setosa\n",
       "4   5            5.0           3.6            1.4           0.2  Iris-setosa"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm',\n",
       "       'Species'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.keys()"
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
      "(150, 6)\n"
     ]
    }
   ],
   "source": [
    "print(df.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "#####  Describe the statistics about the data"
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
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm\n",
      "count  150.000000     150.000000    150.000000     150.000000    150.000000\n",
      "mean    75.500000       5.843333      3.054000       3.758667      1.198667\n",
      "std     43.445368       0.828066      0.433594       1.764420      0.763161\n",
      "min      1.000000       4.300000      2.000000       1.000000      0.100000\n",
      "25%     38.250000       5.100000      2.800000       1.600000      0.300000\n",
      "50%     75.500000       5.800000      3.000000       4.350000      1.300000\n",
      "75%    112.750000       6.400000      3.300000       5.100000      1.800000\n",
      "max    150.000000       7.900000      4.400000       6.900000      2.500000\n"
     ]
    }
   ],
   "source": [
    "print(df.describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Preprocessing the dataset\n",
    "\n",
    "##### Remove the ID column from the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "tags": [
     "block:data_preprocessing",
     "prev:loaddata"
    ]
   },
   "outputs": [],
   "source": [
    "df = df.drop(columns = ['Id'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
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
       "      <th>SepalLengthCm</th>\n",
       "      <th>SepalWidthCm</th>\n",
       "      <th>PetalLengthCm</th>\n",
       "      <th>PetalWidthCm</th>\n",
       "      <th>Species</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species\n",
       "0            5.1           3.5            1.4           0.2  Iris-setosa\n",
       "1            4.9           3.0            1.4           0.2  Iris-setosa\n",
       "2            4.7           3.2            1.3           0.2  Iris-setosa\n",
       "3            4.6           3.1            1.5           0.2  Iris-setosa\n",
       "4            5.0           3.6            1.4           0.2  Iris-setosa"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Describe the statistics about the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
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
      "       SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm\n",
      "count     150.000000    150.000000     150.000000    150.000000\n",
      "mean        5.843333      3.054000       3.758667      1.198667\n",
      "std         0.828066      0.433594       1.764420      0.763161\n",
      "min         4.300000      2.000000       1.000000      0.100000\n",
      "25%         5.100000      2.800000       1.600000      0.300000\n",
      "50%         5.800000      3.000000       4.350000      1.300000\n",
      "75%         6.400000      3.300000       5.100000      1.800000\n",
      "max         7.900000      4.400000       6.900000      2.500000\n"
     ]
    }
   ],
   "source": [
    "print(df.describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Information about the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
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
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 150 entries, 0 to 149\n",
      "Data columns (total 5 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   SepalLengthCm  150 non-null    float64\n",
      " 1   SepalWidthCm   150 non-null    float64\n",
      " 2   PetalLengthCm  150 non-null    float64\n",
      " 3   PetalWidthCm   150 non-null    float64\n",
      " 4   Species        150 non-null    object \n",
      "dtypes: float64(4), object(1)\n",
      "memory usage: 6.0+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Display no. of samples on each class"
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
       "Iris-virginica     50\n",
       "Iris-versicolor    50\n",
       "Iris-setosa        50\n",
       "Name: Species, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Species'].value_counts()"
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
   "execution_count": 12,
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
       "      <th>Total</th>\n",
       "      <th>%</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Species</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PetalWidthCm</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PetalLengthCm</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SepalWidthCm</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SepalLengthCm</th>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Total    %\n",
       "Species            0  0.0\n",
       "PetalWidthCm       0  0.0\n",
       "PetalLengthCm      0  0.0\n",
       "SepalWidthCm       0  0.0\n",
       "SepalLengthCm      0  0.0"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total = df.isnull().sum().sort_values(ascending=False)\n",
    "percent_1 = df.isnull().sum()/df.isnull().count()*100\n",
    "percent_2 = (round(percent_1, 1)).sort_values(ascending=False)\n",
    "missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])\n",
    "missing_data.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Exploratory data analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Histogram"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['SepalLengthCm'].hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['SepalWidthCm'].hist()"
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
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['PetalLengthCm'].hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['PetalWidthCm'].hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "##### Scatterplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [],
   "source": [
    "colors = ['red', 'orange', 'blue']\n",
    "species = ['Iris-virginica', 'Iris-setosa', 'Iris-versicolor']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7fab9a563c90>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "for i in range(3):\n",
    "    x = df[df['Species'] == species[i]]\n",
    "    plt.scatter(x['SepalLengthCm'], x['SepalWidthCm'], c = colors[i], label = species[i])\n",
    "plt.xlabel(\"Sepel Length\")\n",
    "plt.ylabel(\"Sepal Width\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7fab9a46cd90>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "for i in range(3):\n",
    "    x = df[df['Species'] == species[i]]\n",
    "    plt.scatter(x['SepalLengthCm'], x['PetalWidthCm'], c = colors[i], label = species[i])\n",
    "plt.xlabel(\"Sepel Length\")\n",
    "plt.ylabel(\"Petal Width\")\n",
    "plt.legend()"
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
       "<matplotlib.legend.Legend at 0x7fab9a3fd290>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "for i in range(3):\n",
    "    x = df[df['Species'] == species[i]]\n",
    "    plt.scatter(x['SepalLengthCm'], x['PetalLengthCm'], c = colors[i], label = species[i])\n",
    "plt.xlabel(\"Sepel Length\")\n",
    "plt.ylabel(\"Petal Length\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7fab9a37a8d0>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "for i in range(3):\n",
    "    x = df[df['Species'] == species[i]]\n",
    "    plt.scatter(x['SepalWidthCm'], x['PetalLengthCm'], c = colors[i], label = species[i])\n",
    "plt.xlabel(\"Sepel Width\")\n",
    "plt.ylabel(\"Petal Length\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7fab9a309350>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXgAAAEGCAYAAABvtY4XAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAnoElEQVR4nO3de5RU5Znv8e9D0wk3o4vLeEO60agJNHQjF0cdjcgYbwRj1EUMOpCMorCMxImJnpjlOEY9ziTLeOIJjp043miVyIwOcRw9ouINTWwI3kAT5WJaPRHhiCAXm+7n/LGrobupqq7aXXtX1a7fZ61aVfXWrnrf3QVP737em7k7IiKSPH2K3QAREYmGAryISEIpwIuIJJQCvIhIQinAi4gkVN9iN6CzoUOHem1tbbGbISJSNpYvX/6Ruw9L91pJBfja2lqam5uL3QwRkbJhZuszvaYUjYhIQinAi4gkVGQB3syONLOVnW6fmNn3oqpPRES6iiwH7+5vAQ0AZlYFvAc8lO/ntLa20tLSwo4dOwrbQOmVfv36MXz4cKqrq4vdFBHJIK5O1inAO+6esTMgk5aWFvbZZx9qa2sxswiaJvlydzZu3EhLSwsjR44sdnNEJIO4cvDfBO5P94KZzTazZjNr3rBhw16v79ixgyFDhii4lxAzY8iQIfqrSpKtqQlqa6FPn+C+qanYLcpb5AHezD4HTAMeTPe6uze6+wR3nzBsWNqhnAruJUjfiSRaUxPMng3r14N7cD97dtkF+Tiu4E8DVrj7X2KoS0Sk966+GrZt61q2bVtQXkbiCPDnkSE9Uy4GDRqU8bVjjz22159/zTXXsGTJkrzes3jxYm666aasx7z//vucc845vWmaSGV69938ykuURbnhh5kNBN4FDnX3zT0dP2HCBO8+k3X16tV8+ctfjqiFuRk0aBBbt27tUrZr1y769o22j7qtrY2qqqpI6+iNUvhuRCJRWxukZbqrqYF16+JuTVZmttzdJ6R7LdIreHf/1N2H5BLcCybCjpGlS5dy/PHHM23aNEaNGgXsubr/4IMPOOGEE2hoaKCuro7nnnuuy3s3b95MTU0N7e3tAHz66acccsghtLa2MmvWLBYtWgQEyzVceeWVHHXUUTz44IM8+uijfOlLX2L8+PFcdtllTJ06FYC77rqLSy+9FIBZs2Zx2WWXceyxx3LooYfu/qx169ZRV1cHBL8srrjiCurq6hg7diy33norANdddx0TJ06krq6O2bNnox2+RIAbboABA7qWDRgQlJeRklqLptc6OkY6cmcdHSMAM2YUpIoVK1bw+uuv7zU88L777uOUU07h6quvpq2tjW3d8nf77rsvDQ0NPPPMM0yePJlHHnmEU045Je048iFDhrBixQp27NjB4YcfzrPPPsvIkSM577zzMrbrgw8+4Pnnn+fNN99k2rRpe6VmGhsbWbduHStXrqRv375s2rQJgEsvvZRrrrkGgAsuuIBHHnmEr33ta6F+NiKJ0REvrr46SMuMGBEE9wLFkbgka6mCGDpGJk2alHbs98SJE7nzzju59tpree2119hnn332Omb69OksXLgQgAceeIDp06enraOj/M033+TQQw/dXV+2AP/1r3+dPn36MGrUKP7yl737s5csWcLFF1+8O600ePBgAJ5++mmOPvpoxowZw1NPPcUbb7yR7fRFCi+O4Yhh6pgxI0jHtLcH92UW3CFpAT6GjpGBAwemLT/hhBN49tlnOfjgg5k1axb33HMPDz30EA0NDTQ0NNDc3My0adN47LHH2LRpE8uXL+ekk07Kq45sPv/5z+9+nGuaZceOHcydO5dFixbx2muvcdFFF2lsu8QrjuGICRnyGEayAvyIEfmVF9D69evZf//9ueiii7jwwgtZsWIFZ511FitXrmTlypVMmDCBQYMGMXHiRObNm8fUqVN77EA98sgjWbNmDetSnTodV/9hnHzyydx+++3s2rULgE2bNu0O5kOHDmXr1q27c/cisYljOGJChjyGkawAX8SOkaVLl1JfX8+4ceNYuHAh8+bNS3vc9OnTWbBgQcb0TGf9+/dn/vz5nHrqqYwfP5599tmHfffdN1T7LrzwQkaMGMHYsWOpr6/nvvvuY7/99uOiiy6irq6OU045hYkTJ4b6bJHQwvzVnW+6JSFDHkNx95K5jR8/3rtbtWrVXmVZLVjgXlPjbhbcL1iQ3/tLzJYtW9zdvb293efMmeM333xzkVu0R97fjUh3NTXuQeKk662mJv3xCxa4DxjQ9dgBA7L/P8+3jjIDNHuGmJqsK3hIRMdIZ7/61a9oaGhg9OjRbN68mYsvvrjYTRIpnHz/6g6TbknIkMcwkjVMMoEuv/xyLr/88mI3QyQa+Q5HDJNuSciQxzAU4EWkuGbM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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "for i in range(3):\n",
    "    x = df[df['Species'] == species[i]]\n",
    "    plt.scatter(x['PetalWidthCm'], x['PetalLengthCm'], c = colors[i], label = species[i])\n",
    "plt.xlabel(\"Petal Width\")\n",
    "plt.ylabel(\"Petal Length\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Correlation Matrix\n",
    "##### A correlation matrix is a table showing correlation coefficients between variables. Each cell in the table showns the correlation between two variables. The values in the range of -1 to 1. If two variables have high correlations, we can neglect one variable from those two."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
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
       "      <th>SepalLengthCm</th>\n",
       "      <th>SepalWidthCm</th>\n",
       "      <th>PetalLengthCm</th>\n",
       "      <th>PetalWidthCm</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>SepalLengthCm</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.109369</td>\n",
       "      <td>0.871754</td>\n",
       "      <td>0.817954</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SepalWidthCm</th>\n",
       "      <td>-0.109369</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.420516</td>\n",
       "      <td>-0.356544</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PetalLengthCm</th>\n",
       "      <td>0.871754</td>\n",
       "      <td>-0.420516</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.962757</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PetalWidthCm</th>\n",
       "      <td>0.817954</td>\n",
       "      <td>-0.356544</td>\n",
       "      <td>0.962757</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm\n",
       "SepalLengthCm       1.000000     -0.109369       0.871754      0.817954\n",
       "SepalWidthCm       -0.109369      1.000000      -0.420516     -0.356544\n",
       "PetalLengthCm       0.871754     -0.420516       1.000000      0.962757\n",
       "PetalWidthCm        0.817954     -0.356544       0.962757      1.000000"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [],
   "source": [
    "# corr = df.corr()\n",
    "# fig, ax = plt.subplots(figsize = (5,5))\n",
    "# sns.heatmap(corr, annot = True, ax = ax)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Label Encoder\n",
    "##### In machine learning, we usually deal with datasets which contains multiple labels in one or more than one columns. These labels can be in the form of words or numbers. Label Encoding refers to converting the labels info the labels into numeric form so as to convert it into the machine-readable form."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "le = LabelEncoder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
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
       "      <th>SepalLengthCm</th>\n",
       "      <th>SepalWidthCm</th>\n",
       "      <th>PetalLengthCm</th>\n",
       "      <th>PetalWidthCm</th>\n",
       "      <th>Species</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm  Species\n",
       "0            5.1           3.5            1.4           0.2        0\n",
       "1            4.9           3.0            1.4           0.2        0\n",
       "2            4.7           3.2            1.3           0.2        0\n",
       "3            4.6           3.1            1.5           0.2        0\n",
       "4            5.0           3.6            1.4           0.2        0"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Species'] = le.fit_transform(df['Species'])\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      0\n",
       "1      0\n",
       "2      0\n",
       "3      0\n",
       "4      0\n",
       "      ..\n",
       "145    2\n",
       "146    2\n",
       "147    2\n",
       "148    2\n",
       "149    2\n",
       "Name: Species, Length: 150, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Species']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    50\n",
       "1    50\n",
       "0    50\n",
       "Name: Species, dtype: int64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Species'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "tags": [
     "skip"
    ]
   },
   "outputs": [],
   "source": [
    "#Writing the modified train and test data and saving thems\n",
    "df.to_csv(r'/mnt/df.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
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
   "docker_image": "",
   "experiment": {
    "id": "",
    "name": ""
   },
   "experiment_name": "",
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
   "pipeline_description": "",
   "pipeline_name": "",
   "snapshot_volumes": false,
   "steps_defaults": [],
   "volume_access_mode": "rwm",
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
