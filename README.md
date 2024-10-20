# 🌳 FolderMirror

FolderMirror is a lightweight desktop application that helps you maintain consistent folder structures across different devices and locations. It copies folder hierarchies without transferring the actual files, making it perfect for organizing your workspace, setting up project templates, or maintaining parallel folder structures across multiple devices.

## 🎯 Purpose

Have you ever needed to:

- Set up the same folder structure across multiple computers?
- Create a template of your project organization?
- Document your folder hierarchy?
- Prepare a folder structure before migrating files?

FolderMirror solves these problems by creating exact folder structure copies while generating detailed logs of the process.

## ✨ Features

- 📁 Clone folder structures without copying files
- 🎨 User-friendly graphical interface
- 📝 Generate detailed log files with complete folder trees
- 🚀 Fast and lightweight
- 🔍 Comprehensive error tracking and debugging
- 💻 Cross-platform compatibility

## 🚀 Getting Started

### Method 1: Direct Download (Recommended for most users)

1. Go to the [Releases](https://github.com/YourUsername/FolderMirror/releases) page
2. Download the latest version for your operating system:
   - Windows: `FolderMirror-windows.exe`
   - macOS: `FolderMirror-macos.dmg`
   - Linux: `FolderMirror-linux.AppImage`
3. Run the downloaded file

### Method 2: From Source Code

#### Prerequisites

- Python 3.8 or higher
- tkinter (usually comes with Python)

#### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/FolderMirror.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FolderMirror
   ```
3. Run the application:
   ```bash
   python folder_mirror.py
   ```

## 🛠️ Building from Source

To create an executable:

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Create the executable:
   ```bash
   pyinstaller --onefile --windowed --name FolderMirror folder_mirror.py
   ```

The executable will be created in the `dist` directory.

## 📝 How to Use

1. Launch FolderMirror
2. Click "Select Source" to choose the folder structure you want to copy
3. Click "Select Destination" to choose where you want the new structure created
4. Click "Copy Folder Structure" to begin the process
5. Check the generated log file for details about the operation

## 📄 Log Files

Log files are automatically created in your destination folder with the naming format:
`folder_structure_log_YYYYMMDD_HHMMSS.txt`

These logs contain:

- Complete folder structure tree
- Operation timestamps
- Success/error messages
- Debugging information

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Inspired by the need for consistent folder organization across multiple devices

## 📞 Support

If you encounter any issues or have suggestions:

1. Check the [Issues](https://github.com/YourUsername/FolderMirror/issues) page
2. Create a new issue if your problem isn't already listed
