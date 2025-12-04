import pandas as pd
import numpy as np
from datetime import timedelta
from scipy import stats


class CreateDataset:
    def __init__(self, base_dir, granularity):
        self.base_dir = base_dir
        self.granularity = granularity

    def add_left_right(self, dataset):
        left, right = [], []
        label = 0
        for i in range(len(dataset)):
            val = dataset.iloc[i]['Elements']
            if isinstance(val, str):
                if val.startswith('/Marker/'):
                    label = int(val[-1])
            if label == 1:
                left.append(1)
                right.append(0)
            elif label == 2:
                left.append(0)
                right.append(1)
            else:
                left.append(0)
                right.append(0)
        dataset['label_left'] = left
        dataset['label_right'] = right
        return dataset

    def create_dataset(self, start_time, end_time, cols):
        timestamps = pd.date_range(start_time, end_time, freq=f'{self.granularity}ms')
        data_table = pd.DataFrame(index=timestamps, columns=cols)
        data_table[:] = np.nan
        return data_table

    def num_sampling(self, dataset, data_table, value_cols):
        for i in range(len(data_table.index)):
            start = data_table.index[i]
            end = start + timedelta(milliseconds=self.granularity)
            relevant = dataset[(dataset['TimeStamp'] >= start) & (dataset['TimeStamp'] < end)]
            for col in value_cols:
                data_table.loc[start, col] = relevant[col].mean() if not relevant.empty else np.nan
        return data_table

    def cat_sampling(self, dataset, data_table, label_cols):
        for i in range(len(data_table.index)):
            start = data_table.index[i]
            end = start + timedelta(milliseconds=self.granularity)
            relevant = dataset[(dataset['TimeStamp'] >= start) & (dataset['TimeStamp'] < end)]
            for col in label_cols:
                if not relevant.empty:
                    mode_val = stats.mode(relevant[col], keepdims=True).mode[0]
                    data_table.loc[start, col] = mode_val
                else:
                    data_table.loc[start, col] = np.nan
        return data_table

    def add_data(self, file, value_cols, label_cols):
        dataset = pd.read_csv(file, skipinitialspace=True)
        dataset['TimeStamp'] = pd.to_datetime(dataset['TimeStamp'])
        dataset = self.add_left_right(dataset)
        dataset.dropna(thresh=dataset.shape[1]-10, inplace=True)
        all_cols = value_cols + label_cols
        data_table = self.create_dataset(dataset['TimeStamp'].min(), dataset['TimeStamp'].max(), all_cols)
        data_table = self.num_sampling(dataset, data_table, value_cols)
        data_table = self.cat_sampling(dataset, data_table, label_cols)
        return data_table
