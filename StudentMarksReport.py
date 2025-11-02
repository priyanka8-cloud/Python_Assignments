
def read_marks(filename):
    """Reads data from marks.txt and returns a dictionary of student details."""
    data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue

                student_id, name, subject, marks = parts
                try:
                    marks = int(marks)
                except ValueError:
                    print(f"Invalid marks for {name} in {subject}. Skipping...")
                    continue
                if student_id not in data:
                    data[student_id] = {
                        "name": name,
                        "subjects": {},
                    }
                data[student_id]["subjects"][subject] = marks

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}

    return data


def generate_report(data):
    """Generates a summary report with total, average, highest, and lowest marks."""
    report = []
    for student_id, info in data.items():
        subjects = info["subjects"]
        total = sum(subjects.values())
        avg = total / len(subjects)
        highest_subject = max(subjects, key=subjects.get)
        lowest_subject = min(subjects, key=subjects.get)

        report.append({
            "id": student_id,
            "name": info["name"],
            "total": total,
            "average": avg,
            "highest": (highest_subject, subjects[highest_subject]),
            "lowest": (lowest_subject, subjects[lowest_subject])
        })

    report.sort(key=lambda x: x["average"], reverse=True)
    return report


def write_summary(report, output_file):
    """Writes the summary report to report.txt."""
    with open(output_file, "w") as file:
        for r in report:
            file.write(f"Student ID: {r['id']}\n")
            file.write(f"Name: {r['name']}\n")
            file.write(f"Total Marks: {r['total']}\n")
            file.write(f"Average Marks: {r['average']:.2f}\n")
            file.write(f"Highest Scored Subject: {r['highest'][0]} ({r['highest'][1]})\n")
            file.write(f"Lowest Scored Subject: {r['lowest'][0]} ({r['lowest'][1]})\n")
            file.write("-" * 38 + "\n")
    print(f"✅ Report successfully written to '{output_file}'.")

marks_data = read_marks("marks.txt")
if marks_data:
    summary = generate_report(marks_data)
    write_summary(summary, "report.txt")
