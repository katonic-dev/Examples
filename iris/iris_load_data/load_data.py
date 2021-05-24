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
    "import pandas as pd\n",
    "import numpy as np\n",
    "import datetime"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Loading the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "tags": [
     "block:loaddata",
     "prev:setup"
    ]
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"/usr/src/workdir/COMP_DEMO/iris/iris_load_data/iris.csv\")"
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
   "outputs": [],
   "source": [
    "#Writing the modified data and saving thems\n",
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
