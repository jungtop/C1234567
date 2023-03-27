from automatic_view_updater.update_view import update_view
import sys

def update(issue_cmnt):
    update_view(issue_cmnt)

if __name__ == "__mian__":
    issue_cmnt = sys.argv[1]
    update(issue_cmnt)