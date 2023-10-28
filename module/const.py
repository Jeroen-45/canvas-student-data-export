from pathlib import Path

# Directory in which to download course information to (will be created if not present)
DL_LOCATION = Path("./output").resolve().expanduser().absolute()

# List of Course IDs that should be skipped (need to be integers)
COURSES_TO_SKIP = [288290, 512033]

DATE_TEMPLATE = "%B %d, %Y %I:%M %p"

# Max PATH length is 260 characters on Windows. 70 is just an estimate for a reasonable max folder name to prevent the chance of reaching the limit
# Applies to modules, assignments, announcements, and discussions
# If a folder exceeds this limit, a "-" will be added to the end to indicate it was shortened ("..." not valid)
MAX_FOLDER_NAME_SIZE = 70
