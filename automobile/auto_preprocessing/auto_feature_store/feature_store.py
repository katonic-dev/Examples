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
   "execution_count": 3,
   "metadata": {
    "tags": [
     "pipeline-parameters"
    ]
   },
   "outputs": [],
   "source": [
    "MINIO_HOST=\"minio-service.kubeflow:9000\"\n",
    "MINIO_ACCESS_KEY=\"minio\"\n",
    "MINIO_SECRET_KEY=\"minio123\"\n",
    "MINIO_MODEL_BUCKET=\"seldon\"\n",
    "\n",
    "DEPLOY_NAMESPACE=\"kubeflow\"\n",
    "\n",
    "EVENT_TIMESTAMP_ALIAS = \"event_timestamp\"\n",
    "CREATED_TIMESTAMP_ALIAS = \"created_timestamp\"\n",
    "\n",
    "STORAGEACCOUNTNAME= \"katonicusecases\"\n",
    "STORAGEACCOUNTKEY= \"kxGVhR3tKmJoNdEFbhauyHOvBaNMEJR8/uIH+4NKX9QLbHEsEhmo5YQmuiUmSaW2g/96Fq3RrV9f3FeMyizzgg==\"    \n",
    "CONTAINERNAME= \"modelbuilding\"\n",
    "BLOBNAME= \"automobile_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "tags": [
     "functions"
    ]
   },
   "outputs": [],
   "source": [
    "def save_to_feature_store(spark,pandas_df,feaurestore_name,STORAGEACCOUNTNAME,CONTAINERNAME):\n",
    "\n",
    "    pandas_df['Unique_id']=np.random.choice(len(pandas_df), size=len(pandas_df), replace=False)\n",
    "    pandas_df['event_timestamp']=pd.to_datetime(datetime.now())\n",
    "    pandas_df['created_timestamp']=pd.to_datetime(datetime.now())\n",
    "    \n",
    "    df_var = spark.createDataFrame(pandas_df)\n",
    "    \n",
    "    op_path = \"stagging\" + \"/\" + feaurestore_name\n",
    "\n",
    "    op_path = \"wasbs://\" + CONTAINERNAME + \"@\" + STORAGEACCOUNTNAME + \".blob.core.windows.net/\"+op_path\n",
    "    \n",
    "    df_var.write.mode(\"overwrite\").parquet(op_path)\n",
    "    \n",
    "\n",
    "\n",
    "def create_entity_df(spark,unique_id,feaurestore_name,STORAGEACCOUNTNAME,CONTAINERNAME):\n",
    "    \n",
    "    \n",
    "    op_path = \"stagging\" + \"/\" + feaurestore_name\n",
    "\n",
    "    op_path = \"wasbs://\" + CONTAINERNAME + \"@\" + STORAGEACCOUNTNAME + \".blob.core.windows.net/\"+op_path\n",
    "    \n",
    "    df_var = spark.read.parquet(op_path)\n",
    "    \n",
    "    \n",
    "    entity_df= df_var.select(unique_id).withColumn('event_timestamp',current_timestamp())\n",
    "    \n",
    "    return entity_df\n",
    "\n",
    "def fetch_df(spark,feaurestore_name,STORAGEACCOUNTNAME,CONTAINERNAME):\n",
    "    \n",
    "    #os.mkdir('fs_logs')\n",
    "\n",
    "    op_path = \"stagging\" + \"/\" + feaurestore_name\n",
    "\n",
    "    op_path = \"wasbs://\" + CONTAINERNAME + \"@\" + STORAGEACCOUNTNAME + \".blob.core.windows.net/\"+op_path\n",
    "    \n",
    "    df_var = spark.read.parquet(op_path)\n",
    "    \n",
    "    #df_var = spark.createDataFrame(data)\n",
    "    \n",
    "    #shutil.rmtree('fs_logs')\n",
    "    return df_var\n",
    "\n",
    "def create_df_feature(spark,path_dict,feature_dict,STORAGEACCOUNTNAME,CONTAINERNAME):\n",
    "    df_list = []\n",
    "    f_list  = []\n",
    "\n",
    "    for fs,obj,features in zip(path_dict.keys(),path_dict.values(),feature_dict.values()):\n",
    "        df = fetch_df(spark,fs,obj,STORAGEACCOUNTNAME,CONTAINERNAME)\n",
    "        df_list.append(df)\n",
    "        f_list.append(features)\n",
    "    return [df_list,f_list]\n",
    "\n",
    "def as_of_join(\n",
    "    entity_df: DataFrame,\n",
    "    feature_table_entity_names : list,\n",
    "    feature_table_df : DataFrame,\n",
    "    feature_list : list,\n",
    "    feature_table_name : str,\n",
    "    max_age = [],\n",
    "    entity_event_timestamp_column = 'event_timestamp'\n",
    "\n",
    "    ) -> DataFrame:\n",
    "    #print (feature_list)\n",
    "    #print(type(feature_list))\n",
    "    feature_table_df = feature_table_df.select(feature_list+[EVENT_TIMESTAMP_ALIAS,CREATED_TIMESTAMP_ALIAS,feature_table_entity_names[0]])\n",
    "    entity_with_id = entity_df.withColumn(\"_row_nr\", monotonically_increasing_id())\n",
    "    feature_event_timestamp_column_with_prefix = (\n",
    "        f\"{feature_table_name}__{EVENT_TIMESTAMP_ALIAS}\"\n",
    "        )\n",
    "    feature_created_timestamp_column_with_prefix = (\n",
    "        f\"{feature_table_name}__{CREATED_TIMESTAMP_ALIAS}\"\n",
    "        )\n",
    "\n",
    "    projection = [\n",
    "        col(col_name).alias(f\"{feature_table_name}__{col_name}\")\n",
    "        for col_name in feature_table_df.columns\n",
    "        ]\n",
    "\n",
    "    aliased_feature_table_df = feature_table_df.select(projection)\n",
    "    \n",
    "    join_cond = (\n",
    "    entity_with_id[entity_event_timestamp_column]\n",
    "        >= aliased_feature_table_df[feature_event_timestamp_column_with_prefix]\n",
    "    )\n",
    "    if max_age:\n",
    "        join_cond = join_cond & (\n",
    "        aliased_feature_table_df[feature_event_timestamp_column_with_prefix]\n",
    "        >= entity_with_id[entity_event_timestamp_column]\n",
    "        - expr(f\"INTERVAL {max_age[0]} seconds\")\n",
    "        )\n",
    "    for key in feature_table_entity_names:\n",
    "        join_cond = join_cond & (\n",
    "        entity_with_id[key]\n",
    "        == aliased_feature_table_df[f\"{feature_table_name}__{key}\"]\n",
    "        )\n",
    "    conditional_join = entity_with_id.join(\n",
    "        aliased_feature_table_df, join_cond, \"leftOuter\"\n",
    "        )\n",
    "    for key in feature_table_entity_names:\n",
    "        conditional_join = conditional_join.drop(\n",
    "        aliased_feature_table_df[f\"{feature_table_name}__{key}\"]\n",
    "        )\n",
    "    window = Window.partitionBy(\"_row_nr\", *feature_table_entity_names).orderBy(\n",
    "        col(feature_event_timestamp_column_with_prefix).desc(),\n",
    "        col(feature_created_timestamp_column_with_prefix).desc(),\n",
    "        )\n",
    "    filter_most_recent_feature_timestamp = conditional_join.withColumn(\n",
    "        \"_rank\", row_number().over(window)\n",
    "        ).filter(col(\"_rank\") == 1)\n",
    "    return filter_most_recent_feature_timestamp.select(\n",
    "        entity_df.columns\n",
    "        + [\n",
    "            f\"{feature_table_name}__{feature}\"\n",
    "            for feature in feature_list\n",
    "        ]\n",
    "    )\n",
    "    \n",
    "\n",
    "def retrieve_feature(\n",
    "    entity_df: DataFrame,\n",
    "    feature_table_dfs:List[DataFrame],\n",
    "    feature_lists :List[list],\n",
    "    feature_table_names:list,\n",
    "    feature_table_entity_names : List[str],\n",
    "    max_age=[],\n",
    "    entity_event_timestamp_column='event_timestamp',\n",
    "    ) -> DataFrame :\n",
    "    \n",
    "    joined_df = entity_df\n",
    "\n",
    "    for (feature_table_df, feature_list,feature_table_name) in zip(feature_table_dfs, feature_lists,feature_table_names ):\n",
    "            joined_df = as_of_join(\n",
    "                joined_df, feature_table_entity_names,feature_table_df, feature_list,feature_table_name,\n",
    "            max_age = max_age,\n",
    "        entity_event_timestamp_column = entity_event_timestamp_column)\n",
    "    \n",
    "    return joined_df\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading the modified data \n",
    "automobile = pd.read_csv(r'/mnt/automobile.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "tags": [
     "block:feature_stores",
     "prev:featureengineering"
    ]
   },
   "outputs": [],
   "source": [
    "os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.hadoop:hadoop-azure:2.7.3,com.microsoft.azure:azure-storage:2.2.0,org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell'\n",
    "spark =  SparkSession.builder.getOrCreate()\n",
    "spark._jsc.hadoopConfiguration().set(\"fs.azure\", \"org.apache.hadoop.fs.azure.NativeAzureFileSystem\")\n",
    "spark.conf.set(\"fs.wasbs.impl\",\"org.apache.hadoop.fs.azure.NativeAzureFileSystem\")\n",
    "spark.conf.set('fs.azure.account.key.' + STORAGEACCOUNTNAME + '.blob.core.windows.net', STORAGEACCOUNTKEY)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "save_to_feature_store(spark,automobile,\"featurestore\", STORAGEACCOUNTNAME,CONTAINERNAME)"
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
