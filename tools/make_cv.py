#!/usr/bin/env python3
"""Generate cv.pdf — minimalist one-page resume in the site's terminal style."""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

OUT = "/Users/om/self_site/cv.pdf"
W, H = A4
M = 40

DARK = HexColor("#101B26")
BODY = HexColor("#2A3942")
GRAY = HexColor("#5B6B7A")
GREEN = HexColor("#0E9F6E")
TECH = HexColor("#0B7A55")
LINK = HexColor("#0E7C9E")
HAIR = HexColor("#E2E8ED")

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Oleg Miagkov — Tech Lead Data Engineer")
c.setAuthor("Oleg Miagkov")
c.setSubject("high-load data platforms · fintech")


def text(x, y, s, font, size, color, charspace=0):
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setFillColor(color)
    t.setCharSpace(charspace)
    t.textOut(s)
    t.setCharSpace(0)
    c.drawText(t)


def wrap_lines(s, font, size, width):
    words = s.split()
    lines, cur = [], ""
    for w_ in words:
        cand = (cur + " " + w_).strip()
        if not cur or c.stringWidth(cand, font, size) <= width:
            cur = cand
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def wrap(x, y, s, font, size, color, width, leading):
    c.setFont(font, size)
    c.setFillColor(color)
    for ln in wrap_lines(s, font, size, width):
        c.drawString(x, y, ln)
        y -= leading
    return y


# ---------- header ----------
text(M, 797, "OLEG MIAGKOV", "Helvetica-Bold", 25, DARK, charspace=1.4)
text(M, 778, "$ tech lead data engineer — high-load data platforms · fintech",
     "Courier-Bold", 10, GREEN)

parts = [
    ("mrobenner@gmail.com", "mailto:mrobenner@gmail.com"),
    ("www.oom.fyi", "https://www.oom.fyi"),
    ("linkedin.com/in/omiagkov", "https://www.linkedin.com/in/omiagkov"),
    ("github.com/obenner", "https://github.com/obenner"),
    ("russia · remote-friendly", None),
]
SEP = "  ·  "
c.setFont("Helvetica", 8.5)
x = M
for i, (s, url) in enumerate(parts):
    w = c.stringWidth(s, "Helvetica", 8.5)
    c.setFillColor(LINK if url else GRAY)
    c.drawString(x, 762, s)
    if url:
        c.linkURL(url, (x, 759, x + w, 771), relative=0)
    x += w
    if i < len(parts) - 1:
        c.setFillColor(GRAY)
        c.drawString(x, 762, SEP)
        x += c.stringWidth(SEP, "Helvetica", 8.5)

c.setStrokeColor(GREEN)
c.setLineWidth(2)
c.line(M, 749, W - M, 749)

TOP = 726
LW = 145
RX = 212
RW = W - M - RX

# ---------- left column ----------
ly = TOP
text(M, ly, "$ skills", "Courier-Bold", 9.5, GREEN)
ly -= 16
groups = [
    ("languages", "Java · Scala · Go · Python · SQL"),
    ("streaming", "Kafka · Flink · Spark Streaming"),
    ("batch & orchestration", "Spark · Airflow · Great Expectations"),
    ("storage", "Hadoop · S3 · Delta Lake · Greenplum · PostgreSQL"),
    ("cloud & infra", "Kubernetes · OpenShift · GCP (BigQuery, DataProc) · AWS (EMR, S3)"),
    ("leadership", "team leading · planning · stakeholder communication"),
]
for label, items in groups:
    text(M, ly, label, "Helvetica-Bold", 8.5, DARK)
    ly -= 11
    ly = wrap(M, ly, items, "Helvetica", 8.5, GRAY, LW, 10.5)
    ly -= 5

ly -= 8
text(M, ly, "$ certifications", "Courier-Bold", 9.5, GREEN)
ly -= 16
certs = [
    "Reactive Architecture: CQRS & Event Sourcing",
    "Hadoop: Big Data Processing",
    "GCP Big Data & ML Fundamentals",
    "Functional Programming Principles in Scala",
    "Data Engineering on GCP (specialization)",
]
for ct in certs:
    ly = wrap(M, ly, "— " + ct, "Helvetica", 8.5, GRAY, LW, 10.5)
    ly -= 3

ly -= 10
text(M, ly, "$ education", "Courier-Bold", 9.5, GREEN)
ly -= 16
ly = wrap(M, ly, "Saratov State Agrarian University", "Helvetica-Bold", 8.5, DARK, LW, 10.5)
ly = wrap(M, ly, "2008 — 2014", "Helvetica", 8.5, GRAY, LW, 10.5)

ly -= 12
text(M, ly, "$ languages", "Courier-Bold", 9.5, GREEN)
ly -= 16
ly = wrap(M, ly, "english — limited working", "Helvetica", 8.5, GRAY, LW, 10.5)
ly = wrap(M, ly, "russian — native", "Helvetica", 8.5, GRAY, LW, 10.5)

# ---------- right column ----------
ry = TOP
text(RX, ry, "$ summary", "Courier-Bold", 9.5, GREEN)
ry -= 15
summary = ("Data engineer with 8+ years of building and optimizing high-load systems "
           "in the fintech sector. Leading engineering teams and delivering big data "
           "projects in Java, Scala, Go and Python. Focused on scalable data architectures "
           "and effective solutions for data processing and analytics. Next step — data "
           "leadership: shaping data strategy and turning it into business impact.")
ry = wrap(RX, ry, summary, "Helvetica", 9, BODY, RW, 12.3)

ry -= 10
text(RX, ry, "$ experience", "Courier-Bold", 9.5, GREEN)
ry -= 17

jobs = [
    ("United Credit Bureau", "aug 2023 — now",
     "Senior Data Engineer -> Tech Lead Data Engineer · Moscow",
     "Real-time analytics platform for the credit bureau: streaming pipelines, batch "
     "data marts, business-event monitoring and raw-data aggregation. Service "
     "architecture and business logic for stateful and stateless streaming.",
     "Scala · Python · Spark · Kafka · Hadoop · S3 · Airflow · OpenMetadata"),
    ("Action-MCFR Mediagroup", "jun 2022 — aug 2023",
     "Senior Data Engineer",
     "Company-wide data platform: corporate DWH, statistics collection at 40M+ events "
     "a day, Hadoop and Greenplum infrastructure, ML-ready datasets, Data Catalog, "
     "product integrations.",
     "Python · Go · Spark · Kafka · Airflow · Greenplum · Postgres · Hadoop · K8s · DataHub · Great Expectations"),
    ("EPAM Systems", "sep 2021 — jun 2022",
     "Senior Software Engineer · Development Team Leader",
     "Payments analytics for Europe's largest sportswear manufacturer: team management "
     "and planning, raw-data ingestion, batch and stream processing, data lake and "
     "data marts.",
     "Python · Spark · Kafka · SQL · AWS (EMR, Hive, S3) · Jenkins · K8s · Exasol"),
    ("Neoflex", "apr 2020 — sep 2021",
     "Lead Data Engineer / Senior Software Engineer (Big Data)",
     "Data lake delivery for a top-3 Russian bank: team organization, data-flow design, "
     "replication, SQL optimization. Automotive IoT data lake. Real-time analytics "
     "platform on Lightbend Cloudflow.",
     "Scala · Akka · Kafka · Flink · Spark · Delta Lake · Cloudera · OpenShift"),
    ("Grid Dynamics", "sep 2019 — apr 2020",
     "Data Engineer",
     "Enterprise data warehouse: ETL pipelines and migration of traditional databases "
     "to Google Cloud from MSSQL, Oracle, DB2 and MySQL.",
     "Python · Scala · BigQuery · DataProc · Airflow · Spark"),
    ("Neoflex", "feb 2018 — sep 2019",
     "Software Engineer",
     "Enterprise banking systems: microservice architecture, OpenAPI.",
     "Java 8 · Spring · Kafka Streams · OpenShift · Oracle · MySQL"),
]

for n, (company, dates, role, desc, tech) in enumerate(jobs):
    text(RX, ry, company, "Helvetica-Bold", 10, DARK)
    c.setFont("Courier", 8)
    c.setFillColor(GREEN)
    c.drawRightString(W - M, ry, dates)
    ry -= 12
    text(RX, ry, role, "Helvetica-Oblique", 8.7, GRAY)
    ry -= 11.5
    ry = wrap(RX, ry, desc, "Helvetica", 8.7, BODY, RW, 10.8)
    ry -= 0.5
    ry = wrap(RX, ry, tech, "Courier", 7.8, TECH, RW, 9.5)
    if n < len(jobs) - 1:
        c.setStrokeColor(HAIR)
        c.setLineWidth(0.7)
        c.line(RX, ry + 3, W - M, ry + 3)
        ry -= 11

# ---------- footer ----------
c.setFont("Courier", 7.5)
c.setFillColor(GRAY)
c.drawCentredString(W / 2, 26, "// omiagkov@prod:~$ cv --pdf · 2026")

c.save()
print("written:", OUT, "| right column ends at y =", round(ry, 1))
