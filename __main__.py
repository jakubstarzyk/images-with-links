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
            v = re.split("\t|\n", line)
            v[3] = os.path.realpath(v[3])
            weasyprint.HTML(string=h.substitute(width=v[0], height=v[1], link=v[2], image=v[3])).write_pdf(v[3] + ".pdf")
