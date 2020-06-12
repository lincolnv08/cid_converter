import csv
import sys

def process_output(keys_file, inputs):
    outputs = {}
    with open(keys_file, newline='') as keys_csv:
        csv_reader = csv.reader(keys_csv)
        for row in csv_reader:
            key = row[0]
            outputs[key] = [inputs[key], inputs[key].replace('-', '')]
    with open('output.csv', 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        for key, value in outputs.items():
            csv_writer.writerow(value)

def parse_input(input_file):
    inputs = {}
    with open(input_file, newline='') as input_csv:
        csv_reader = csv.reader(input_csv)
        for row in csv_reader:
            inputs[row[0]] = row[1]
    return inputs

def convert_cids():
    input_file = sys.argv[1]
    keys_file = sys.argv[2]
    inputs = parse_input(input_file)
    outputs = process_output(keys_file, inputs)

if __name__ == '__main__':
    convert_cids()
