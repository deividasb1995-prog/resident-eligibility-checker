
# Resident Support Eligibility Checker

## 1. Project Overview

The Resident Support Eligibility Checker is a Python-based prototype designed to help residents and local authority staff determine whether an applicant qualifies for Resident Support.

The application evaluates eligibility using three criteria:

- The applicant must be at least 18 years old.
- The applicant must live within the local authority area.
- The household income must be below £30,000.

## 2. Main Features

- Automated eligibility decisions.
- Age, income and residency checks.
- Input validation to prevent invalid information.
- Clear explanations of eligibility decisions.
- Behaviour-Driven Development (BDD) testing.

## 3. Project Structure

```text
resident-eligibility-checker/
├── features/
│   ├── eligibility.feature
│   └── steps/
│       └── eligibility_steps.py
├── eligibility.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 4. Technologies Used

- Python
- Behave
- Gherkin
- Git
- GitHub

## 5. Installation

Clone the repository:

```bash
git clone https://github.com/deividasb1995-prog/resident-eligibility-checker.git
cd resident-eligibility-checker
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## 6. Running the Application

Run the eligibility checker:

```bash
python eligibility.py
```

Follow the prompts to enter the applicant's age, household income and residency information.

## 7. Running BDD Tests

Run the automated BDD scenarios using:

```bash
python -m behave
```

The scenarios test successful eligibility, boundary conditions and invalid input.

## 8. Eligibility Rules

An applicant is eligible only when all three conditions are satisfied:

1. Age is at least 18.
2. The applicant is a resident of the local authority area.
3. Household income is below £30,000.

Invalid input, such as negative household income, is rejected with an error message.
