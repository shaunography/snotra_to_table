import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(description="Snotra to CSV Table")
    parser.add_argument(
        "--output-dir",
        help="output dir",
        dest="o",
        required=True,
        metavar="output_dir"
    ),
    parser.add_argument(
        "--results-file",
        help="Snotra results JSON file",
        dest="i",
        required=True,
        metavar="results_file"
    ),
    args = parser.parse_args()

    results_file = args.i
    
    with open(results_file,'r') as f:
        results = json.load(f)

    try:
        filename = os.path.split(results_file)[1].split(".")[0]
    except IndexError:
        filename = "results"
    
    ### CIS
    file_path = os.path.join(args.o, "{}_CIS.csv".format(filename))
    with open(file_path, 'w') as f:
        f.write("Check,Level,Benchmark,Result,Pass/Fail\n")
        for finding in results["findings"]:
            if finding["compliance"] == "cis":
                f.write("{},{},{},{},{}\n".format(finding["ref"],finding["level"],finding["name"],finding["analysis"],finding["pass_fail"]))
    ### All
    file_path = os.path.join(args.o, "{}.csv".format(filename))
    with open(file_path, 'w') as f:
        f.write("Check,Level,Benchmark,Result,Pass/Fail\n")
        for finding in results["findings"]:
            f.write("{},{},{},{},{}\n".format(finding["ref"],finding["level"],finding["name"],finding["analysis"],finding["pass_fail"]))


if __name__ == '__main__':
    main()
