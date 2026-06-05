from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, role, ats, skills):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Career Mentor Report",
            styles['Title']
        )
    )

    content.append(
        Paragraph(
            f"ATS Score: {ats}%",
            styles['BodyText']
        )
    )

    content.append(
        Paragraph(
            f"Recommended Role: {role}",
            styles['BodyText']
        )
    )

    content.append(
        Paragraph(
            "Skills: " + ", ".join(skills),
            styles['BodyText']
        )
    )

    pdf.build(content)