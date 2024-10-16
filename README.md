<p align="center">
  <img src="https://raw.githubusercontent.com/sayh3x/H3X-Pull/main/main.jpg" style="max-width: 100%; height: auto;" alt="Git Pull logo">
</p>

# H3X-Pull-V2-added

## Project Description
This project provides a Python script that automatically performs a `git pull` whenever a new commit is detected in a specified Git repository. It is useful for developers who need to keep their repository updated without manually performing `git pull` operations.

## How It Works
1. **Monitoring the Git Repository**:
   - The script monitors the local Git repository for any changes. Upon detecting a new change, it checks the remote repository for updates.
2. **Automatic Update**:
   - If there are new commits in the remote repository, the script automatically performs a `git pull` to update the local repository.

## Packages Used
- `GitPython`: A Python library used to interact with Git repositories.
- `watchdog`: A Python library used to monitor file system events.

## Installation of Packages
To install the required packages, run the following commands:
```bash
pip install -r requirements.txt
```
## Script Configuration

Edit the script to specify the path to your Git repository. Change the repo_path variable to the path of your local Git repository:

```python

if __name__ == "__main__":
    repo_path = "/path/to/your/repo"  # Change to your repository path
    event_handler = GitPullHandler(repo_path)
    observer = Observer()
    observer.schedule(event_handler, path=repo_path, recursive=False)
    observer.start()
```
## Running the Script in the Background
To run the script in the background on Unix-like systems (Linux/Mac), use the nohup command:

```bash 
nohup python H3Xpull.py > auto_pull.log 2>&1 &
```
- `nohup`: Runs the script independently of the terminal.
- `> H3Xpull.log`: Redirects the standard output to the `H3Xpull.log` file.
- `2>&1`: Redirects standard errors to the same log file.
- `&`: Runs the script in the background.

## Checking the Running Process
To check if the script is running, use the following command:

```bash
ps aux | grep H3Xpull.py
```
Then, kill the process using its PID:

Enter`kill -9 <PID>`

## Support This Script
If you find this Script useful or interesting, please consider giving it a ⭐ star on GitHub! Your support is greatly appreciated and helps motivate us to keep improving and adding new features. Thank you!
