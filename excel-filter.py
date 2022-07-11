import sys

if len(sys.argv) != 4:
    raise Exception("argument error. 3 required " + str(len(sys.argv) - 1) + " provided")

input_file_name = sys.argv[1]
if input_file_name.rpartition('.')[-1] != 'xlsx':
    raise Exception("invalid input file format. Required format: \"xlsx\"" + " provided file format: \"" + input_file_name.rpartition('.')[-1] + "\"")
output_file_name = sys.argv[2]

if output_file_name.rpartition('.')[-1] != 'xlsx':
    raise Exception("invalid output file format. Required format: \"xlsx\"" + " provided file format: \"" + output_file_name.rpartition('.')[-1] + "\"")

try:
    interval = int(sys.argv[3])
    if interval < 1:
        raise Exception("inteval should be positive")
except Exception as e:
    raise Exception("Invalid interval. interval should be positive integer")

import pandas as pd
df = pd.read_excel(input_file_name, header=0)
#print(df.head(10))
df = df[df.index % interval == 0]
#print(df.head(10))
df.to_excel(output_file_name, index = False) 