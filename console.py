from os import *

def clear_screen():
    """Clear the console screen based on the operating system"""
    if name == 'nt':  # Windows
        system('cls')
    else:  # Unix/Linux/MacOS
        system('clear')

class CBrowse:
    def file_browser():
        current_dir = path.abspath('.')
        while True:
            clear_screen()
            print(f"\nCurrent Directory: {current_dir}")
            items = listdir(current_dir)
            
            # Display directories and files
            print("\n[Directories]")
            dirs = [d for d in items if path.isdir(path.join(current_dir, d))]
            for i, d in enumerate(dirs):
                print(f"{i+1}. {d}/")
            
            print("\n[Files]")
            files = [f for f in items if path.isfile(path.join(current_dir, f))]
            for i, f in enumerate(files):
                print(f"{chr(97+i)}. {f}")
            
            print("\nOptions:")
            print(" - Enter directory number to navigate")
            print(" - Enter file letter to open/run")
            print(" - 'del' + file letter to delete file")
            print(" - 'back' to go back to parent directory")
            print(" - 'quit' to quit")
            
            choice = input("\nYour choice: ").strip().lower()
            
            if choice == 'quit':
                break
            elif choice == 'back':
                current_dir = path.dirname(current_dir)
                clear_screen()
            elif choice == 'del' and len(choice) > 1:
                # Delete file
                file_char = choice[1:]
                try:
                    file_index = ord(file_char) - ord('a')
                    if 0 <= file_index < len(files):
                        file_to_delete = path.join(current_dir, files[file_index])
                        remove(file_to_delete)
                        print(f"Deleted: {files[file_index]}")
                        input("\nPress Enter to continue...")
                        clear_screen()
                    else:
                        print("Invalid file selection")
                        input("\nPress Enter to continue...")
                        clear_screen()
                except:
                    print("Error deleting file")
                    input("\nPress Enter to continue...")
                    clear_screen()
            elif choice.isdigit():
                # Navigate to directory
                dir_index = int(choice) - 1
                if 0 <= dir_index < len(dirs):
                    current_dir = path.join(current_dir, dirs[dir_index])
                    clear_screen()
                else:
                    print("Invalid directory selection")
                    input("\nPress Enter to continue...")
                    clear_screen()
            elif choice.isalpha() and len(choice) == 1:
                # Open/run file
                file_index = ord(choice) - ord('a')
                if 0 <= file_index < len(files):
                    file_to_open = path.join(current_dir, files[file_index])
                    try:
                        if name == 'nt':  # Windows
                            startfile(file_to_open)
                        else:  # macOS/Linux
                            system(f'xdg-open "{file_to_open}"')
                        print(f"Opened: {files[file_index]}")
                        input("\nPress Enter to continue...")
                        clear_screen()
                    except:
                        print(f"Could not open {files[file_index]}")
                        input("\nPress Enter to continue...")
                        clear_screen()
                else:
                    print("Invalid file selection")
                    input("\nPress Enter to continue...")
                    clear_screen()
            else:
                print("Invalid choice")
                input("\nPress Enter to continue...")
                clear_screen()