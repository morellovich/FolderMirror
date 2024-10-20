import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import datetime
import os
import traceback
import logging

class FolderStructureCopier:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Structure Copier")
        self.root.geometry("600x400")
        
        # Variables to store selected paths
        self.source_path = tk.StringVar()
        self.dest_path = tk.StringVar()
        
        # Initialize logger
        self.setup_logger()
        
        self.create_gui()
    
    def setup_logger(self):
        """Configure logging with both file and console handlers"""
        self.logger = logging.getLogger('FolderCopier')
        self.logger.setLevel(logging.DEBUG)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
    
    def create_gui(self):
        # Source folder selection
        source_frame = tk.LabelFrame(self.root, text="Source Folder", padx=10, pady=5)
        source_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(source_frame, textvariable=self.source_path, width=50).pack(side="left", padx=5)
        tk.Button(source_frame, text="Select Source", command=self.select_source).pack(side="right", padx=5)
        
        # Destination folder selection
        dest_frame = tk.LabelFrame(self.root, text="Destination Folder", padx=10, pady=5)
        dest_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(dest_frame, textvariable=self.dest_path, width=50).pack(side="left", padx=5)
        tk.Button(dest_frame, text="Select Destination", command=self.select_destination).pack(side="right", padx=5)
        
        # Copy button
        tk.Button(self.root, text="Copy Folder Structure", command=self.copy_structure).pack(pady=20)
        
        # Status text
        self.status_text = tk.Text(self.root, height=15, width=60)
        self.status_text.pack(padx=10, pady=10)
    
    def log_to_gui(self, message, level=logging.INFO):
        """Add message to GUI status text with appropriate color"""
        tag = "normal"
        if level == logging.ERROR:
            tag = "error"
        elif level == logging.WARNING:
            tag = "warning"
        
        self.status_text.tag_config("error", foreground="red")
        self.status_text.tag_config("warning", foreground="orange")
        
        self.status_text.insert(tk.END, f"{message}\n", tag)
        self.status_text.see(tk.END)
    
    def select_source(self):
        try:
            folder = filedialog.askdirectory(title="Select Source Folder")
            if folder:
                self.source_path.set(folder)
                self.logger.info(f"Source folder selected: {folder}")
        except Exception as e:
            self.logger.error(f"Error selecting source folder: {str(e)}")
            self.log_to_gui(f"Error selecting source folder: {str(e)}", logging.ERROR)
    
    def select_destination(self):
        try:
            folder = filedialog.askdirectory(title="Select Destination Folder")
            if folder:
                self.dest_path.set(folder)
                self.logger.info(f"Destination folder selected: {folder}")
        except Exception as e:
            self.logger.error(f"Error selecting destination folder: {str(e)}")
            self.log_to_gui(f"Error selecting destination folder: {str(e)}", logging.ERROR)
    
    def generate_folder_tree(self, path, prefix=""):
        """Generate a text representation of the folder structure"""
        tree = []
        try:
            path_obj = Path(path)
            for item in sorted(path_obj.iterdir()):
                if item.is_dir():
                    tree.append(f"{prefix}├── {item.name}/")
                    tree.extend(self.generate_folder_tree(item, prefix + "│   "))
        except Exception as e:
            self.logger.error(f"Error generating folder tree for {path}: {str(e)}")
            tree.append(f"{prefix}├── ERROR: {str(e)}")
        return tree
    
    def copy_structure(self):
        if not self.source_path.get() or not self.dest_path.get():
            error_msg = "Please select both source and destination folders"
            self.logger.error(error_msg)
            self.log_to_gui(error_msg, logging.ERROR)
            messagebox.showerror("Error", error_msg)
            return
        
        try:
            # Clear status text
            self.status_text.delete(1.0, tk.END)
            
            source = Path(self.source_path.get())
            dest = Path(self.dest_path.get())
            
            # Create log file
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = dest / f"folder_structure_log_{timestamp}.txt"
            
            # Add file handler for this session
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            
            # Log initial information
            self.logger.info("Starting folder structure copy operation")
            self.logger.info(f"Source: {source}")
            self.logger.info(f"Destination: {dest}")
            
            # Generate folder tree
            self.logger.info("Generating folder tree...")
            folder_tree = self.generate_folder_tree(source)
            
            # Copy folder structure
            copied_count = 0
            error_count = 0
            
            for root, dirs, _ in os.walk(source):
                rel_path = os.path.relpath(root, source)
                if rel_path == ".":
                    continue
                    
                try:
                    target_dir = dest / rel_path
                    target_dir.mkdir(parents=True, exist_ok=True)
                    copied_count += 1
                    self.logger.info(f"Created: {target_dir}")
                    self.log_to_gui(f"Created: {target_dir}")
                except Exception as e:
                    error_count += 1
                    error_msg = f"Error creating {rel_path}: {str(e)}"
                    self.logger.error(error_msg)
                    self.log_to_gui(error_msg, logging.ERROR)
            
            # Write folder tree to log file
            self.logger.info("Writing folder tree to log file...")
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write("\nFolder Structure:\n")
                f.write("\n".join(folder_tree))
            
            # Log summary
            summary = f"\nOperation completed:\n- Folders created: {copied_count}\n- Errors encountered: {error_count}"
            self.logger.info(summary)
            self.log_to_gui(summary)
            
            if error_count == 0:
                messagebox.showinfo("Success", "Folder structure copied successfully!")
            else:
                messagebox.showwarning("Completed with Errors", 
                    f"Operation completed with {error_count} errors. Check the log file for details.")
            
            # Remove file handler
            self.logger.removeHandler(file_handler)
            file_handler.close()
            
        except Exception as e:
            error_msg = f"Critical error during operation: {str(e)}\n{traceback.format_exc()}"
            self.logger.error(error_msg)
            self.log_to_gui(error_msg, logging.ERROR)
            messagebox.showerror("Error", f"A critical error occurred. Check the log file for details.")
            
def main():
    root = tk.Tk()
    app = FolderStructureCopier(root)
    root.mainloop()

if __name__ == "__main__":
    main()
