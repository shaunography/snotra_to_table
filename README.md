# snotra_to_table
Convert Snotra results JSON into CSV tables for importing into reports.

## usage
`$ python3 snotra_to_table.py --results-file <path_to_snotra_results_json> --output-dir <output_dir>`

## output files
Two CSV files are produced in the output directory.
### CIS
A simple CSV file containing only CIS benchmark checks with the fields "ref", "level", "name", "affected", "analysis" and "pass_fail".
### all
A CSV file containing all checks and all fields
