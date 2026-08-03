# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from content import DATA

OUT = "/mnt/user-data/outputs/DS_ML_AI_Master_Roadmap_Explained.pdf"

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name="CoverTitle", fontSize=26, leading=32, alignment=TA_CENTER,
                           textColor=colors.HexColor("#1a2744"), fontName="Helvetica-Bold", spaceAfter=14))
styles.add(ParagraphStyle(name="CoverSubtitle", fontSize=13, leading=18, alignment=TA_CENTER,
                           textColor=colors.HexColor("#4a5568"), fontName="Helvetica"))
styles.add(ParagraphStyle(name="SectionHeader", fontSize=17, leading=20, spaceBefore=6, spaceAfter=10,
                           textColor=colors.white, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="TopicTitle", fontSize=12.5, leading=15, spaceBefore=2, spaceAfter=4,
                           textColor=colors.HexColor("#1a2744"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="TopicNum", fontSize=9, leading=11,
                           textColor=colors.HexColor("#7c8aa5"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="Explain", fontSize=9.6, leading=13.6, spaceAfter=6,
                           textColor=colors.HexColor("#2d3748"), fontName="Helvetica"))
styles.add(ParagraphStyle(name="QLabel", fontSize=9.3, leading=12.5, spaceBefore=2,
                           textColor=colors.HexColor("#0f5c3d"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="ALabel", fontSize=9.3, leading=12.5, spaceAfter=6, leftIndent=10,
                           textColor=colors.HexColor("#333333"), fontName="Helvetica"))
styles.add(ParagraphStyle(name="TOCSection", fontSize=11.5, leading=15, spaceBefore=10, spaceAfter=3,
                           textColor=colors.HexColor("#1a2744"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="TOCItem", fontSize=9, leading=12.5,
                           textColor=colors.HexColor("#4a5568"), fontName="Helvetica"))

SECTION_COLOR = colors.HexColor("#2b3a67")

def section_header_table(title, count):
    t = Table([[Paragraph(f"{title}  <font size=9 color='#c9d3ee'>({count} topics)</font>", styles["SectionHeader"])]],
               colWidths=[7.0*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), SECTION_COLOR),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

def build():
    doc = SimpleDocTemplate(OUT, pagesize=letter,
                             leftMargin=0.65*inch, rightMargin=0.65*inch,
                             topMargin=0.6*inch, bottomMargin=0.6*inch,
                             title="Data Science / ML / AI Master Roadmap — Explained",
                             author="Compiled reference")
    story = []

    # Cover page
    story.append(Spacer(1, 1.6*inch))
    story.append(Paragraph("DATA SCIENCE / ML / AI", styles["CoverTitle"]))
    story.append(Paragraph("MASTER ROADMAP — FULLY EXPLAINED", styles["CoverTitle"]))
    story.append(Spacer(1, 0.3*inch))
    story.append(HRFlowable(width="60%", thickness=1.2, color=colors.HexColor("#2b3a67"), hAlign="CENTER"))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("143 topics across 15 domains, from foundational math to agentic AI and LLM infrastructure.",
                            styles["CoverSubtitle"]))
    story.append(Paragraph("Each topic: a basic-to-advanced explanation, plus 2 interview questions with answers.",
                            styles["CoverSubtitle"]))
    story.append(Spacer(1, 1.8*inch))
    story.append(Paragraph("10+ Years Senior-Level Expertise Track", styles["CoverSubtitle"]))
    story.append(PageBreak())

    # Table of contents
    toc_title_style = ParagraphStyle(name="TOCTitle", fontSize=18, fontName="Helvetica-Bold",
                                      textColor=colors.HexColor("#1a2744"), spaceAfter=10)
    story.append(Paragraph("TABLE OF CONTENTS", toc_title_style))
    for title, topics in DATA:
        nums = f"{topics[0][0]}–{topics[-1][0]}" if len(topics) > 1 else f"{topics[0][0]}"
        story.append(Paragraph(f"{title} <font color='#7c8aa5'>(#{nums})</font>", styles["TOCSection"]))
        names = ", ".join(t[1] for t in topics)
        story.append(Paragraph(names, styles["TOCItem"]))
    story.append(PageBreak())

    # Content
    for title, topics in DATA:
        story.append(section_header_table(title, len(topics)))
        story.append(Spacer(1, 10))
        for num, topic_title, explanation, qas in topics:
            story.append(Paragraph(f"#{num}", styles["TopicNum"]))
            story.append(Paragraph(topic_title, styles["TopicTitle"]))
            story.append(Paragraph(explanation, styles["Explain"]))
            for i, (q, a) in enumerate(qas, 1):
                story.append(Paragraph(f"Interview Q{i}: {q}", styles["QLabel"]))
                story.append(Paragraph(f"A: {a}", styles["ALabel"]))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e2e8f0")))
            story.append(Spacer(1, 6))
        story.append(PageBreak())

    doc.build(story)
    print("done:", OUT)

if __name__ == "__main__":
    build()