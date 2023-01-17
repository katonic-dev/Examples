# Custom Component

The `custom_component.pipeline` is a sample pipeline that you can use to test and understand the working of custom components.

Here we are using a bank customer segmentation dataset but will use it for regression purpose where `TransactionAmount (INR)` will be the target column from the data. The data will be processes and different feature engineering techniques will be applied to prepare it to feed it to a model.

### Dataset

The example pipeline is running using the below dataset:

```bash
https://www.kaggle.com/datasets/shivamb/bank-customer-segmentation
```

As this data doesn't have any unique `ID` columns that's why we made a unique ID column and concatenated with it after downloading from the link. The name of the id columns doesn't have to be `ID` it can be anything.