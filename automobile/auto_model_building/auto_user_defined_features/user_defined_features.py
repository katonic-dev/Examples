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
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# conda install cudatoolkit\n",
    "#!pip install alibi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
    "# from matplotlib import pyplot as plt\n",
    "# from matplotlib import style\n",
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
    "\n",
    "from pyspark.sql import SparkSession\n",
    "\n",
    "\n",
    "#from numba import jit, cuda\n",
    "\n",
    "\n",
    "\n",
    "from subprocess import run, Popen, PIPE\n",
    "\n",
    "from pyspark.sql import DataFrame, SparkSession, Window\n",
    "from pyspark.sql.functions import col, expr, monotonically_increasing_id, row_number,current_timestamp\n",
    "# from data_io import *\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from typing import  List\n",
    "from datetime import datetime\n",
    "from minio import Minio\n",
    "# from minio.error import ResponseError\n",
    "\n",
    "#from azure.storage.blob import BlockBlobService\n",
    "import pandas as pd\n",
    "\n",
    "import uuid\n",
    "import os\n",
    "import shutil\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "#### User define features location, feature list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "tags": [
     "block:user_defined_features"
    ]
   },
   "outputs": [],
   "source": [
    "path_dict = {'featurestore':'automobile'}\n",
    "feature_dict = {'featureSET':['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',\n",
    "       'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',\n",
    "       'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type',\n",
    "       'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',\n",
    "       'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',\n",
    "       'highway-mpg', 'price']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "path_dict = pd.DataFrame(list(path_dict.items()))\n",
    "feature_dict = pd.DataFrame(list(feature_dict.items()))"
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
   "outputs": [],
   "source": [
    "#Writing the modified data and saving thems\n",
    "path_dict.to_csv(r'/mnt/path_dict.csv', index=False)\n",
    "feature_dict.to_csv(r'/mnt/feature_dict.csv', index=False)"
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
    "id": "75b16a8e-0270-4d9f-a685-2a4512632b53",
    "name": "automobile"
   },
   "experiment_name": "automobile",
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
   "pipeline_description": "manual-1",
   "pipeline_name": "manual-1",
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
