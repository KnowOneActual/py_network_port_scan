# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [1.0.0] - 2025-10-03

### Added
- **New Multi-Threaded Scanner**: A new script (`port_scan_v2.py`) was added, featuring concurrent scanning to dramatically improve performance.
- **Command-Line Interface**: Implemented `argparse` to allow users to specify targets, ports, and thread counts via command-line arguments.
- **Service Banner Grabbing**: The new scanner can now attempt to retrieve and display the banner of the service running on an open port.
- **Project Documentation**: Created a detailed `README.md` with a feature list, usage instructions, and examples.
- **Original Script**: The first script was saved as `port_scan_original.py` to show the project's evolution.
- **Repository Files**: Added `LICENSE`, `CONTRIBUTING.md`, and issue templates to the project.

### Changed
- **Initial Project Setup**: The basic file structure from the initial commit is now part of the first official release.