# dslr


getting started :

    python -m venv dslr_env
    source dslr_env/bin/activate
    pip install -r requirements.txt

data visualisation :

    python describe.py --path_csv_to_read ../data/dataset_train.csv
    python histogram.py --path_csv_to_read ../data/dataset_train.csv
    python pair_plot.py --path_csv_to_read ../data/dataset_train.csv
    python scatter_plot.py --path_csv_to_read ../data/dataset_train.csv

