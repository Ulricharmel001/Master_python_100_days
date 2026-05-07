import csv

# step 1: processed user data
def process_studdent_data(input_file, output_file):
    student_report = []
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                # Skip rows with missing or empty required fields
                if not row['Name'] or not row['Math'] or not row['English'] or not row['French']:
                    continue
                try:
                    name = row['Name']
                    math = int(row['Math'])
                    eng = int(row['English'])
                    french = int(row['French'])
                except ValueError:
                    # Skip rows with non-integer values
                    continue
                average = (math + eng + french) / 3
                status = 'pass' if average >= 60 else 'fail'
                student_report.append({
                    'Name': name,
                    'Math': math,
                    'English' : eng,
                    'French' : french,
                    'Average': round(average, 2),
                    'Status': status
                })
# step 2 : calculate average and determine pass/fail status

        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Name', 'Math', 'English', 'French', 'Average', 'Status']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_report)
        print(f"Student report generated in {output_file} successfully")

    except FileNotFoundError:
        print("File not found!")
    except KeyError:
        print("Error: invalid column names in the input file")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = 'student.csv'
output_file = 'student_report.csv'
process_studdent_data(input_file, output_file)