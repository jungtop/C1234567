from automatic_view_updater.update_view import update_view
import sys

def update(issue_cmnt,token):
    update_view(issue_cmnt,token)

if __name__ == "__mian__":
    issue_cmnt = sys.argv[1]
    token = sys.argv[2]
    update(issue_cmnt,token)