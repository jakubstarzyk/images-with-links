import os, sys, string, re, weasyprint

h = string.Template(
"""\
<html>
<head>
<style>
body {
margin: 0;
}
@page {
margin: 0;
size: ${width}px ${height}px;
}
</style>
</head>
<body>
<a href="${link}">
<img src="file://${image}">
</a>
</body>
</html>
"""
)

if __name__ == "__main__":
    with open(sys.argv[1]) as data:
        for line in data:
            v = dict(zip(["image", "width", "height", "link"], re.split("\t|\n", line)))
            v["image"] = os.path.realpath(v["image"])
            weasyprint.HTML(string=h.substitute(v)).write_pdf(v["image"] + ".pdf")
