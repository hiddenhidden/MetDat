# MetDat (Meta Injector)

A desktop application for MacOS that allows batch processing of metadata injection for images and audio files.

## Features
- Image and audio metadata injection
- iOS and Android device simulation
- Location data injection
- Batch processing
- Custom metadata input
- Randomization options

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hiddenhidden/MetDat.git
cd MetDat
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate metdat
```

3. Install ExifTool:
```bash
brew install exiftool
```

## Project Structure
```
MetDat/
├── src/
│   ├── ui/          # User interface components
│   ├── core/        # Core functionality
│   └── utils/       # Utility functions
├── tests/           # Test files
├── resources/       # Application resources
└── README.md        # This file
```

## Development
- Python 3.11+
- Tkinter for GUI
- ExifTool for metadata manipulation
- Faker for data generation

## License
[MIT License](LICENSE)
