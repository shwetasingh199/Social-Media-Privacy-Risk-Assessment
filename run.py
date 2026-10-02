import os
import subprocess
import sys


PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)


def run_command(command):

    print(
        "\nRunning:",
        " ".join(command)
    )

    subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        check=True
    )


def main():

    print("=" * 60)
    print("SOCIAL MEDIA PRIVACY RISK ASSESSMENT")
    print("=" * 60)

    print("\nStep 1: Generating dataset...")

    run_command([
        sys.executable,
        "-m",
        "data.generate_dataset"
    ])

    print("\nStep 2: Training ML model...")

    run_command([
        sys.executable,
        "-m",
        "models.train_model"
    ])

    print("\nStep 3: Starting Streamlit dashboard...")

    run_command([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app/streamlit_app.py"
    ])


if __name__ == "__main__":
    main()