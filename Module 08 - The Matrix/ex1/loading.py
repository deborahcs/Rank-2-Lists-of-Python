import sys
import importlib.metadata
from typing import Optional, Dict, List

REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]


def get_package_version(package_name: str) -> Optional[str]:
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None


def check_dependencies(required: List[str]) -> Dict[str, str]:
    installed_versions: Dict[str, str] = {}
    missing_packages: List[str] = []

    for package in required:
        version = get_package_version(package)
        if version:
            installed_versions[package] = version
        else:
            missing_packages.append(package)

    if missing_packages:
        print("You are missing some required dependencies:")
        for package in missing_packages:
            print(f" - {package}")
        print("\nTo install with pip:")
        print("  pip install -r requirements.txt")
        print("\nTo install with Poetry:")
        print("  poetry install")
        sys.exit(1)

    return installed_versions


def display_status(versions: Dict[str, str]) -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    status_notes = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }

    packages_to_check = ["pandas", "numpy", "requests", "matplotlib"]
    for package in packages_to_check:
        if package in versions:
            note = status_notes.get(package, "")
            print(f"[OK] {package} ({versions[package]}) - {note}")


def generate_and_save_plot(num_points: int, output_filename: str) -> None:
    import numpy as np
    import pandas as pd
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print(f"Processing {num_points} data points...")

    x_values = np.random.normal(0, 1, num_points)
    y_values = np.sin(x_values) + np.random.normal(0, 0.2, num_points)
    data_frame = pd.DataFrame({"x": x_values, "y": y_values})

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(data_frame["x"], data_frame["y"], s=6, alpha=0.6)
    ax.set_title("Simulated Matrix Data")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fig.savefig(output_filename, dpi=150)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_filename}")


def main() -> None:
    versions = check_dependencies(REQUIRED_PACKAGES)
    display_status(versions)

    generate_and_save_plot(
        num_points=1000,
        output_filename="matrix_analysis.png"
        )


if __name__ == "__main__":
    main()
