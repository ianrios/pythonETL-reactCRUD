import csv
import logging
import shutil
import sys
from time import perf_counter
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Callable, Optional
from pathlib import Path

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

input_csv = Path("data/crime.csv")
outputs_dir = Path(".outputs")

def parse():
    """YOUR CODE GOES IN THIS FUNCTION.

    Assignment:
        - Unzip the data from crime.csv.gz to "data/crime.csv" (this does not have to be done in Python).
        - Update this parse() function to:
            - Read the data from "data/crime.csv" and parse all the data rows into the CrimeDataRecord class above.
            - Convert each CrimeDataRecord to JSON and output it to a corresponding text file in a directory called ".outputs".
            Each JSON string should be written to a single line in the corresponding file. The model has a ".to_json()" method 
            to simplify conversion for you. Example:
                - outputs/
                    - PUBLIC PEACE VIOLATION.txt
                    - DECEPTIVE PRACTICE.txt
                    - CRIMINAL DAMAGE.txt
                    - NARCOTICS.txt
                    - etc...
            - Return a list of primary_type values, sorted from most frequently occurring to least.

    Success Criteria:
        - Running this python module executes the parsing logic and test logic successfully without any errors.

    Additional Notes:
        - You may use any third party libraries or tools to execute this task but the entrypoint to the ETL process
        must be executed by Python. You should be able to explain and justify your choices during review.
        - First focus on getting the right solution and then focus on optimizations, like reducing the number of times the
        file is read or the number of times the row items are iterated over or the number of records kept in memory.
        Even if you choose not to make those optimizations, it'll still be good to have a discussion about what could have
        been done.
    """

    pass


def check_criteria(test: Callable, name: str):
    """DO NOT CHANGE THIS."""
    
    try:
        test()
        logger.info(f"Test [{name}]: PASSED")
    except:
        logger.error(f"Test [{name}]: FAILED")
        raise


def test_crime_type_ordering(crime_types: list[str]):
    """DO NOT CHANGE THIS."""

    expected_ordered_crime_types = [
        "THEFT",
        "BATTERY",
        "CRIMINAL DAMAGE",
        "ASSAULT",
        "BURGLARY",
        "OTHER OFFENSE",
        "DECEPTIVE PRACTICE",
        "NARCOTICS",
        "MOTOR VEHICLE THEFT",
        "ROBBERY",
        "CRIMINAL TRESPASS",
        "OFFENSE INVOLVING CHILDREN",
        "WEAPONS VIOLATION",
        "PUBLIC PEACE VIOLATION",
        "SEX OFFENSE",
        "CRIM SEXUAL ASSAULT",
        "LIQUOR LAW VIOLATION",
        "ARSON",
        "PROSTITUTION",
        "KIDNAPPING",
        "INTERFERENCE WITH PUBLIC OFFICER",
        "GAMBLING",
        "HOMICIDE",
        "INTIMIDATION",
        "STALKING",
        "CRIMINAL SEXUAL ASSAULT",
        "OBSCENITY",
        "CONCEALED CARRY LICENSE VIOLATION",
        "NON-CRIMINAL",
        "OTHER NARCOTIC VIOLATION",
        "PUBLIC INDECENCY",
        "HUMAN TRAFFICKING",
        "NON - CRIMINAL",
        "RITUALISM",
        "NON-CRIMINAL (SUBJECT SPECIFIED)",
    ]
    assert (
        ordered_crime_types == expected_ordered_crime_types
    ), "The crime parsed types are not ordered in order of most to least frequently occurring."


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
    ordered_crime_types = parse()
    t2 = perf_counter()
    logger.info(f"Completed parsing in {timedelta(seconds=t2-t1)}.")

    check_criteria(
        lambda: test_crime_type_ordering(crime_types=ordered_crime_types),
        "Returned crime types are ordered by frequency",
    )
    check_criteria(
        lambda: test_output_files(output_path=outputs_dir),
        "Output files are grouped by crime type",
    )
