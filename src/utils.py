class APIException(Exception):
    def __init__(self, message, status_code=400):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {"error": self.message}


def generate_sitemap(app):
    import urllib
    links = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            url = urllib.parse.unquote(str(rule))
            links.append({"endpoint": rule.endpoint, "url": url})
    return links
