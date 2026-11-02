
"""
Resident Support Eligibility Checker
====================================
A Python prototype for checking whether residents
qualify for local authority Resident Support.
"""

from dataclasses import dataclass
import math


# --- Configuration ------------------------------------------------

MIN_AGE = 18
MAX_AGE = 120
INCOME_THRESHOLD = 30000  # GBP; income must be strictly below this


# --- Errors --------------------------------------------------------

class EligibilityError(ValueError):
    """Raised when inputs to an eligibility check are invalid."""


# --- Result type --------------------------------------------------

@dataclass
class EligibilityResult:
    """Stores the outcome of an eligibility decision."""

    eligible: bool
    reason: str

    def __str__(self) -> str:
        status = "ELIGIBLE" if self.eligible else "NOT ELIGIBLE"
        return f"{status}: {self.reason}"


# --- Input validation ---------------------------------------------

def _validate(age, household_income, is_resident) -> None:
    """Validate applicant information."""

    if age is None or household_income is None or is_resident is None:
        raise EligibilityError(
            "All fields are required: age, household income and residency."
        )

    # Validate age
    if isinstance(age, bool) or not isinstance(age, int):
        raise EligibilityError("Age must be a whole number.")

    if age < 0:
        raise EligibilityError("Age cannot be negative.")

    if age > MAX_AGE:
        raise EligibilityError(f"Age cannot be greater than {MAX_AGE}.")

    # Validate household income
    if isinstance(household_income, bool) or not isinstance(
        household_income, (int, float)
    ):
        raise EligibilityError("Household income must be a number.")

    # Reject NaN and positive or negative infinity
    if isinstance(household_income, float) and not math.isfinite(
        household_income
    ):
        raise EligibilityError(
            "Household income must be a finite number."
        )

    if household_income < 0:
        raise EligibilityError("Household income cannot be negative.")

    # Validate residency
    if not isinstance(is_resident, bool):
        raise EligibilityError(
            "Residency must be either true or false."
        )


# --- Core eligibility decision ------------------------------------

def check_eligibility(
    age, household_income, is_resident
) -> EligibilityResult:
    """
    Decide whether an applicant qualifies for Resident Support.

    Args:
        age: Applicant's age in whole years.
        household_income: Total household income in GBP.
        is_resident: True if the applicant lives in the local authority area.

    Returns:
        EligibilityResult containing the decision and explanation.

    Raises:
        EligibilityError: If any input is invalid.
    """

    _validate(age, household_income, is_resident)

    failures = []

    if age < MIN_AGE:
        failures.append(
            f"applicant must be at least {MIN_AGE}"
        )

    if not is_resident:
        failures.append(
            "applicant must be a resident of the local authority area"
        )

    if household_income >= INCOME_THRESHOLD:
        failures.append(
            f"household income must be below GBP {INCOME_THRESHOLD:,}"
        )

    if failures:
        return EligibilityResult(
            eligible=False,
            reason="Not eligible because " + "; ".join(failures) + "."
        )

    return EligibilityResult(
        eligible=True,
        reason="All criteria met: applicant qualifies for Resident Support."
    )


# --- Command-line interface ---------------------------------------

def main():
    """Run the eligibility checker interactively."""

    print("Resident Support Eligibility Checker")
    print("-----------------------------------")

    try:
        age = int(input("Applicant age (whole years): "))

        household_income = float(
            input("Household income (GBP): ")
        )

        residency = input(
            "Resident of the area? (y/n): "
        ).strip().lower()

        if residency not in ("y", "n"):
            raise EligibilityError(
                "Residency must be either y or n."
            )

        is_resident = residency == "y"

        result = check_eligibility(
            age,
            household_income,
            is_resident
        )

        print()
        print(result)

    except EligibilityError as error:
        print(f"\nInput error: {error}")

    except ValueError:
        print(
            "\nInput error: Please enter valid numeric values."
        )


# --- Run application ----------------------------------------------

if __name__ == "__main__":
    main()
