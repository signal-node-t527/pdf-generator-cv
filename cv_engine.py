import pymupdf
import os
from cv_content import CONTENT

def generate_cv(focus, lang, output_path):
    """
    Generates a PDF CV based on focus and language.
    Focus options: 'frontend', 'backend', 'fullstack', 'ai', 'neutral'
    Lang options: 'en', 'es'
    """
    
    # Translations for section headers
    headers = {
        "en": {
            "summary": "PROFESSIONAL SUMMARY",
            "experience": "EXPERIENCE",
            "skills": "SKILLS",
            "education": "EDUCATION",
            "languages": "LANGUAGES",
            "tech": "Technologies"
        },
        "es": {
            "summary": "RESUMEN PROFESIONAL",
            "experience": "EXPERIENCIA",
            "skills": "HABILIDADES",
            "education": "EDUCACIÓN",
            "languages": "IDIOMAS",
            "tech": "Tecnologías"
        }
    }
    
    h = headers[lang]
    
    # Select summary and website
    summary = CONTENT["summaries"][lang].get(focus, CONTENT["summaries"][lang].get("fullstack"))
    website = CONTENT["contact"]["website"].get(focus, CONTENT["contact"]["website"].get("fullstack"))
    
    # Helper to clean and truncate URLs for display
    def format_link_display(url, max_len=30):
        display = url
        for prefix in ["https://", "http://", "mailto:"]:
            if display.startswith(prefix):
                display = display[len(prefix):]
        if len(display) > max_len:
            display = display[:max_len - 3] + "..."
        return display

    website_url = website if website.startswith(("http://", "https://")) else f"https://{website}"
    website_display = format_link_display(website, 30)
    github_url = CONTENT['contact']['github'] if CONTENT['contact']['github'].startswith(("http://", "https://")) else f"https://{CONTENT['contact']['github']}"
    github_display = format_link_display(CONTENT['contact']['github'], 30)
    linkedin_url = CONTENT['contact']['linkedin'] if CONTENT['contact']['linkedin'].startswith(("http://", "https://")) else f"https://{CONTENT['contact']['linkedin']}"
    linkedin_display = format_link_display(CONTENT['contact']['linkedin'], 30)
    email_url = f"mailto:{CONTENT['contact']['email']}"
    email_display = format_link_display(CONTENT['contact']['email'], 30)

    # Build HTML
    html = f"""
    <style>
        body {{ font-family: Helvetica, Arial, sans-serif; font-size: 9.5pt; line-height: 1.25; color: #000; }}
        h1 {{ font-size: 16pt; text-align: center; margin-bottom: 2pt; text-transform: uppercase; font-weight: bold; }}
        .contact {{ text-align: center; font-size: 8.5pt; margin-bottom: 8pt; line-height: 1.4; }}
        .contact a {{ color: #000; text-decoration: none; }}
        h2 {{ font-size: 10.5pt; font-weight: bold; border-bottom: 0.5pt solid #000; margin-top: 10pt; margin-bottom: 5pt; text-transform: uppercase; }}
        .item {{ margin-bottom: 3pt; text-align: left; }}
        .tech {{ font-size: 8.5pt; font-style: italic; color: #333; margin-bottom: 8pt; }}
        strong {{ font-weight: bold; }}
    </style>
    <body>
        <h1>{CONTENT['name']}</h1>
        <div class="contact">
            Website: <a href="{website_url}">{website_display}</a> &nbsp;|&nbsp; 
            GitHub: <a href="{github_url}">{github_display}</a> &nbsp;|&nbsp; 
            Linkedin: <a href="{linkedin_url}">{linkedin_display}</a><br>
            Email: <a href="{email_url}">{email_display}</a> &nbsp;|&nbsp; Phone: {CONTENT['contact']['phone']}
        </div>
        
        <h2>{h['summary']}</h2>
        <div class="item">{summary}</div>
        
        <h2>{h['experience']}</h2>
    """
    
    for exp in CONTENT["experience"]:
        data = exp[lang]
        html += f"""
        <div class="item"><strong>{data['title']}</strong></div>
        <div class="item">{data['desc']}</div>
        <div class="tech"><strong>{h['tech']}:</strong> {data['tech']}</div>
        """
        
    html += f"<h2>{h['skills']}</h2>"
    for skill in CONTENT["skills"][lang]:
        html += f'<div class="item">&bull; {skill}</div>'
        
    html += f"<h2>{h['education']}</h2>"
    for edu in CONTENT["education"][lang]:
        html += f'<div class="item">&bull; {edu}</div>'
        
    html += f"<h2>{h['languages']}</h2>"
    for l in CONTENT["languages"][lang]:
        html += f'<div class="item">&bull; {l}</div>'
        
    html += "</body>"

    # PDF Creation
    doc = pymupdf.open()
    page = doc.new_page()
    rect = page.rect + (40, 30, -40, -30)
    page.insert_htmlbox(rect, html)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    doc.save(output_path)
    doc.close()
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    # Test generation
    generate_cv("fullstack", "en", "output/cv_fullstack_en.pdf")
