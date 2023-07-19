import datetime

user_join_date = f"""{datetime.datetime.now().strftime("%b").title()} {datetime.datetime.now().strftime("%Y")}"""

LANGUAGE_LEVELS = (
    ("Basic", "Basic"),
    ("Conversational", "Conversational"),
    ("Fluent", "Fluent"),
    ("Native", "Native"),
)

EXPERIENCE_LEVELS = (
    ("Basic", "Basic"),
    ("Intermediate", "Intermediate"),
    ("Advance", "Advance"),
)

EDUCATION_TITLE = (
    ("Associate", "Associate"),
    ("Certificate", "Certificate"),
    ("B.A", "B.A"),
    ("BSC", "BSC"),
    ("M.A", "M.A"),
    ("MSC", "MSC"),
    ("PHD", "PHD"),
    ("LLB", "LLB"),
    ("other", "other"),
)
