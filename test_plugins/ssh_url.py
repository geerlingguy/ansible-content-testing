from ansible.module_utils.known_hosts import is_ssh_url

def ssh_url_test(url):
    return is_ssh_url(url)

class TestModule(object):
    def tests(self):
        return dict(ssh_url=ssh_url_test)
