import sys
import os
import io
import pandas as pd

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 change_text_to_numeric.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("datasets", "stage2", "train.csv")
os.makedirs(os.path.join("datasets", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    data = pd.read_csv(fd_in)
    one_hot = pd.get_dummies(data['rating_MPAA'])
    data_prepared = data.drop('rating_MPAA', axis = 1)
    data_prepared = data_prepared.join(one_hot)
    fd_out.write(data_prepared.to_csv(index = False))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)