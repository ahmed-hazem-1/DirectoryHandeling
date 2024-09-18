# Directory Organizer

This Python script automates the process of organizing files in a directory by categorizing them into specific folders based on file type. It can handle images, documents, videos, audio files, compressed files, applications, and scripts, moving them into appropriate folders for easier management.

## Features

- Automatically categorizes and moves files into the following folders:
  - **Images**: `png`, `jpeg`, `jpg`, `gif`
  - **Documentations**: `pdf`, `docx`, `doc`, `ppt`, `pptx`, `xlsx`, `xls`, `txt`
  - **Videos**: `mp4`, `mkv`, `avi`, `flv`, `mov`
  - **Audios**: `mp3`, `wav`, `ogg`, `flac`
  - **Compressed**: `zip`, `rar`, `7z`, `tar`
  - **Applications**: `exe`, `msi`
  - **Scripts**: `py`, `sh`, `bat`
  
- Automatically creates folders if they do not already exist.
- Skips the organizing script itself (`HandelDirectory.py`) to prevent moving it.
  
## Requirements

- Python 3.x
- No external dependencies required (uses built-in Python modules: `os`, `shutil`)

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/directory-organizer.git
   cd directory-organizer
   ```

2. **Place the script (`HandelDirectory.py`) in the directory you want to organize**.

3. **Run the script**:
   ```bash
   python HandelDirectory.py
   ```

4. The script will move files into respective folders based on their file type. If no matching files are found for a particular category, the folder for that type will not be created.

## Example

Before running the script:

```
/myfolder
│
├── image1.jpg
├── document.pdf
├── video.mp4
├── song.mp3
└── HandelDirectory.py
```

After running the script:

```
/myfolder
│
├── Images/
│   └── image1.jpg
├── Documentations/
│   └── document.pdf
├── Videos/
│   └── video.mp4
├── Audios/
│   └── song.mp3
└── HandelDirectory.py
```

## Contributing

Feel free to submit issues or pull requests if you'd like to improve or expand the functionality of the script.
