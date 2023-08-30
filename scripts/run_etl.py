import logging
import sys
from time import perf_counter
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Callable, Optional
from pathlib import Path
import pandas as pd
import os
import os.path

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel("INFO")


class CrimeDataRecord(BaseModel):
    unique_key: str
    case_number: str
    date: datetime
    block: str
    primary_type: str
    description: str
    location_description: str
    arrest: bool
    latitude: Optional[float]
    longitude: Optional[float]

    def to_json(self) -> str:
        return self.json()


class CrimeTypeMetrics(BaseModel):
    primary_type: str
    # The count of all CrimeDataRecords for a primary_type where arrest == True.
    arrest_count: int
    # The count of all CrimeDataRecords for a primary_type where arrest == False.
    non_arrest_count: int


input_csv = Path("data/crime.csv")
outputs_dir = Path(".outputs")


def parse() -> list[CrimeTypeMetrics]:
    """Parse CSV and pull data"""

    # create outputs_dir if it does not exist
    outputs_dir.mkdir(parents=True, exist_ok=True)

    # read data from csv and store as dataframe for future use
    data_frame = pd.read_csv(input_csv,
                             # dtype=dtypes,
                             engine="pyarrow")

    # group data by primary_type
    grouped_data = data_frame.groupby('primary_type')

    # group sizes
    group_sizes = grouped_data.size()

    # sort data by data frame size and primary_type alphabetically
    sorted_groups = group_sizes.reset_index(name='size').sort_values(
        by=['size', 'primary_type'], ascending=[False, True])

    # output list for validating tests
    output_list = []

    # sort grouped data by data frame size and iterate over each group to generate output list
    for primary_type in sorted_groups['primary_type']:
        # grab group
        group = grouped_data.get_group(primary_type)

        # grab results
        arrests = group['arrest'].value_counts()
        arrest_count = arrests.get(True, 0)
        non_arrest_count = arrests.get(False, 0)

        # format output list data for passing test case
        sub_list = CrimeTypeMetrics(primary_type=primary_type,
                                    arrest_count=arrest_count,
                                    non_arrest_count=non_arrest_count)

        # append CrimeTypeMetric object to output_list
        output_list.append(sub_list)

        # save data in json files
        group.to_json(f'{outputs_dir}/{primary_type}.json',
                      orient='records', lines=True)

    return output_list


def check_criteria(test: Callable, name: str):
    """DO NOT CHANGE THIS."""

    try:
        test()
        logger.info(f"Test [{name}]: PASSED")
    except:
        logger.error(f"Test [{name}]: FAILED")
        raise


def test_crime_type_ordering(crime_metrics: list[CrimeTypeMetrics]):
    """DO NOT CHANGE THIS."""

    expected_ordered_crime_metrics = [
        ["THEFT", 9689, 96847],
        ["BATTERY", 19514, 67270],
        ["CRIMINAL DAMAGE", 3586, 55385],
        ["ASSAULT", 7432, 28653],
        ["BURGLARY", 1823, 32026],
        ["OTHER OFFENSE", 4851, 27937],
        ["DECEPTIVE PRACTICE", 4381, 24413],
        ["NARCOTICS", 27876, 284],
        ["MOTOR VEHICLE THEFT", 2123, 25239],
        ["ROBBERY", 1924, 15515],
        ["CRIMINAL TRESPASS", 7687, 4812],
        ["OFFENSE INVOLVING CHILDREN", 1033, 4727],
        ["WEAPONS VIOLATION", 3799, 1812],
        ["PUBLIC PEACE VIOLATION", 2293, 2035],
        ["SEX OFFENSE", 958, 2137],
        ["CRIM SEXUAL ASSAULT", 429, 1860],
        ["LIQUOR LAW VIOLATION", 1583, 11],
        ["ARSON", 211, 1154],
        ["PROSTITUTION", 1323, 6],
        ["KIDNAPPING", 106, 1051],
        ["INTERFERENCE WITH PUBLIC OFFICER", 933, 126],
        ["GAMBLING", 872, 6],
        ["HOMICIDE", 389, 340],
        ["INTIMIDATION", 97, 445],
        ["STALKING", 80, 427],
        ["CRIMINAL SEXUAL ASSAULT", 24, 260],
        ["OBSCENITY", 71, 20],
        ["CONCEALED CARRY LICENSE VIOLATION", 38, 0],
        ["NON-CRIMINAL", 1, 17],
        ["OTHER NARCOTIC VIOLATION", 15, 3],
        ["PUBLIC INDECENCY", 18, 0],
        ["HUMAN TRAFFICKING", 1, 8],
        ["NON - CRIMINAL", 2, 5],
        ["RITUALISM", 0, 5],
        ["NON-CRIMINAL (SUBJECT SPECIFIED)", 1, 1],
    ]
    print(expected_ordered_crime_metrics)
    assert len(crime_metrics) == len(
        expected_ordered_crime_metrics
    ), "The list of metrics do not match the expected count."
    for i in range(0, len(crime_metrics)):
        assert (
            crime_metrics[i].primary_type == expected_ordered_crime_metrics[i][0]
        ), f"The metric at output index {i} did not match the expected value"
        assert (
            crime_metrics[i].arrest_count == expected_ordered_crime_metrics[i][1]
        ), f"The metric at output index {i} did not match the expected value"
        assert (
            crime_metrics[i].non_arrest_count == expected_ordered_crime_metrics[i][2]
        ), f"The metric at output index {i} did not match the expected value"


def test_output_files(output_path: Path):
    """DO NOT CHANGE THIS."""

    assert output_path.exists(), "The .outputs directory is missing."
    assert output_path.is_dir(), "The .outputs directory is missing."

    for file in output_path.glob("*.txt"):
        primary_type = file.name[: len(file.name) - 4]

        with open(file, "r") as file_handle:
            for line in file_handle:
                record = CrimeDataRecord.parse_raw(line)
                assert (
                    record.primary_type == primary_type
                ), f"The record with crime type {record.primary_type} does not belong in this file of {primary_type} records."


if __name__ == "__main__":
    """DO NOT CHANGE THIS."""

    logger.info("Executing parse() method.")
    t1 = perf_counter()
    output = parse()
    t2 = perf_counter()
    logger.info(f"Completed parsing in {timedelta(seconds=t2-t1)}.")

    check_criteria(
        lambda: test_crime_type_ordering(crime_metrics=output),
        "Crime type metrics are aggregated and sorted by frequency",
    )
    check_criteria(
        lambda: test_output_files(output_path=outputs_dir),
        "Output files are grouped by crime type",
    )
