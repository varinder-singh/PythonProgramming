from reports import Report

r = Report(filename="report.html")
r.jinja['title'] = "My new report title"
r.jinja['p'] = "jdfjfdsjfhdjksfkdsjfkdjfkdjfdkj"

print(r.jinja)
r.create_report(onweb=True)

