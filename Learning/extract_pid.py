import re
def extract_pid(log_line):
    regex = r"pid\=(\d+)"
    result = re.search(regex,log_line)
    if result is None:
        return ""
    return result[0]
log = "type=SERVICE_STOP msg=audit(1581632088.949:1774): pid=1231142313 uid=0 auid=429496729"
print(extract_pid(log))
