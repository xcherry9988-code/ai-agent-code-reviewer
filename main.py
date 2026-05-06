import os
import argparse


def scan_repository(path):
    print(f"Scanning repository: {path}")

    issues = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()

                        if "TODO" in content:
                            issues.append(f"TODO found in {full_path}")

                        if len(content.splitlines()) > 200:
                            issues.append(f"Large file detected: {full_path}")

                        if "except:" in content:
                            issues.append(
                                f"Risky bare except found in {full_path}"
                            )

                except Exception as e:
                    issues.append(
                        f"Failed to read {full_path}: {e}"
                    )

    return issues


def generate_report(issues):
    os.makedirs("reports", exist_ok=True)

    report_path = "reports/code_review_report.md"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Code Review Report\n\n")

        if not issues:
            f.write("No major issues found.\n")

        else:
            for issue in issues:
                f.write(f"- {issue}\n")

    print(f"Report generated: {report_path}")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--path",
        type=str,
        default="."
    )

    args = parser.parse_args()

    issues = scan_repository(args.path)

    generate_report(issues)


if __name__ == "__main__":
    main()
