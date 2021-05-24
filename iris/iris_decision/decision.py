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
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "import warnings \n",
    "warnings.filterwarnings(action='ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "tags": [
     "block:loaddata"
    ]
   },
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
    "## Model Training"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "- train = 70\n",
    "- test = 30\n",
    "\n",
    "##### Decision Tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "tags": [
     "block:logisticregression"
    ]
   },
   "outputs": [],
   "source": [
    "X = df.drop(columns = ['Species'])\n",
    "Y = df['Species']\n",
    "X_train_dt, X_test_dt, y_train_dt, y_test_dt = train_test_split(X, Y, test_size=0.30)"
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
       "100.0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "decision_tree = DecisionTreeClassifier()\n",
    "dt = decision_tree.fit(X_train_dt, y_train_dt)\n",
    "acc_decision_tree = round(decision_tree.score(X_train_dt, y_train_dt) * 100, 2)\n",
    "acc_decision_tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.float64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(acc_decision_tree)"
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
