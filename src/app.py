import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--message", default="Hello MLOps!")
args = parser.parse_args()

student = os.getenv("STUDENT_NAME", "Future MLOps Engineer")

print("==============================")
print("Message:", args.message)
print("Brought to you by:", student)
print("==============================")