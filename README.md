# dslr


Run these commands to get started :

    python -m venv dslr_env
    source dslr_env/bin/activate
    pip install -r requirements.txt
    cd src && tensorboard --logdir=output/log

Then, to launch the data visualisations :

    cd src
    python describe.py --path_csv_to_read ../data/dataset_train.csv
    python histogram.py --path_csv_to_read ../data/dataset_train.csv
    python pair_plot.py --path_csv_to_read ../data/dataset_train.csv
    python scatter_plot.py --path_csv_to_read ../data/dataset_train.csv

Finally, to launch the classifier :

    python logreg_train.py
    python logreg_predict.py --path_truth_csv ../data/dataset_truth.csv
