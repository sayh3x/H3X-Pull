import time
from git import Repo
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitPullHandler(FileSystemEventHandler):
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = Repo(repo_path)
    
    def on_any_event(self, event):
        # Check for changes in the remote repository
        origin = self.repo.remotes.origin
        fetch_info = origin.fetch()
        for info in fetch_info:
            if info.commit != self.repo.head.commit:
                print("New commit detected. Pulling changes...")
                origin.pull()
                print("Changes pulled successfully.")

if __name__ == "__main__":
    repo_path = "/path/to/your/repo"  # Change to your repository path
    event_handler = GitPullHandler(repo_path)
    observer = Observer()
    observer.schedule(event_handler, path=repo_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
