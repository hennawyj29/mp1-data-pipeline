"""
Data Processing Pipeline

DS 3500 - MP1
"""

import argparse
import logging
import sys

from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)


logger = logging.getLogger(__name__)



def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input", "-i",
        required=True
    )

    parser.add_argument(
        "--config",
        required=True
    )

    parser.add_argument(
        "--output", "-o",
        required=True
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true"
    )

    return parser.parse_args()


def main():
    """Main pipeline function."""
    args = parse_arguments()

    setup_logging(args.verbose)

    logger.debug(
        f"Arguments parsed: input={args.input}, "
        f"output={args.output}, config={args.config}"
    )

    if not validate_input(args.input):
        sys.exit(1)

    if not validate_input(args.config):
        sys.exit(1)

    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)
    
    required_columns = config["validation"]["required_columns"]
    numeric_columns = config["validation"]["numeric_columns"]

    rows_before_validation = len(data)

    try:
        data = validate_dataframe(
            data,
            required_columns,
            numeric_columns
        )
    except ValueError:
        sys.exit(1)

    logger.info(
        f"Validation complete: {rows_before_validation} → {len(data)} rows"
    )

    data_before = data.copy()

    try:
        cleaned_data = process_data(data, config)
    except ValueError:
        sys.exit(1)

    report = create_cleaning_report(data_before, cleaned_data)

    logger.info(
        f"Processing complete: {len(data_before)} → {len(cleaned_data)} rows"
    )

    output_path = save_data(cleaned_data, args.output)

    logger.info(f"Saved cleaned data to {output_path}")

    print(report)

if __name__ == "__main__":
    main()
