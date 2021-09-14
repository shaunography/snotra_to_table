import argparse
import json
import csv
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
        writer = csv.writer(f)
        writer.writerow(["Check", "Level", "Benchmark", "Result", "Pass/Fail"])
        for finding in results["findings"]:
            if finding["compliance"] == "cis":
                writer.writerow([finding["ref"],finding["level"],finding["name"],finding["analysis"],finding["pass_fail"]])
    ### All
    file_path = os.path.join(args.o, "{}.csv".format(filename))
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "ref", "compliance", "level", "service", "name", "affected", "analysis", "description", "remediation", "impact", "probability", "cvss_vector", "cvss_score", "pass_fail"])
        for finding in results["findings"]:
            writer.writerow([finding["id"], finding["ref"], finding["compliance"], finding["level"], finding["service"], finding["name"], finding["affected"], finding["analysis"], finding["description"], finding["remediation"], finding["impact"], finding["probability"], finding["cvss_vector"], finding["cvss_score"], finding["pass_fail"]])


if __name__ == '__main__':
    main()
