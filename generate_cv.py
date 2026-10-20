import pymupdf
import os

def create_ats_pdf(source_md_path, output_pdf_path):
    """
    Creates an ATS-friendly PDF using HTML rendering for precise layout.
    """
    if not os.path.exists(source_md_path):
        print(f"Error: {source_md_path} not found.")
        return

    with open(source_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    name = "NAZARENO TOGNOLI"
    summary = (
        "Accomplished Fullstack Developer specializing in Angular and .NET Core, with extensive experience "
        "developing Augmented Intelligence systems and integrating Generative AI solutions. Proficient in "
        "architecting scalable frontend and backend infrastructures, optimizing Developer Experience (DX), "
        "and implementing advanced data-driven applications. Currently pursuing a degree in Data Science "
        "at the University of Buenos Aires, combining technical expertise with a strong analytical foundation."
    )
    
    # Enhanced and Cleaned Content
    sections = [
        {
            "title": "PROFESSIONAL SUMMARY",
            "content": [summary]
        },
        {
            "title": "EXPERIENCE",
            "content": [
                "Augmented Intelligence System for General Problem Resolution",
                "Developed a sophisticated system to assist agents in complex problem-solving scenarios through AI-driven insights and workflow optimization.",
                "tecnologias usadas: HTML, CSS, TypeScript, Angular, Sass, ngx-graph, C#, ASP.NET Core, Entity Framework Core, SQL, SQL Server, Git, Docker",
                
                "AI-Driven Recommendation Algorithm for Generative Chat Responses",
                "Engineered a configurable recommendation engine leveraging Generative AI to provide context-aware chat responses and enhanced user interaction.",
                "tecnologias usadas: HTML, CSS, TypeScript, Angular, Sass, Python, FastAPI, Pydantic, Psycopg, Uvicorn, Google GenAI, PostgreSQL, pgvector, C#, ASP.NET Core, Entity Framework Core, Grafana K6, Google Cloud Platform (GCP), Git, Docker",
                
                "Commercial SEO-Optimized Web Platform",
                "Designed and deployed a high-performance commercial website for a local business, focusing on local SEO optimization and modern web standards.",
                "tecnologias usadas: HTML, CSS, JavaScript, TypeScript, Astro, Tailwind"
            ]
        },
        {
            "title": "SKILLS",
            "content": [
                "Programming & Frameworks: HTML, CSS, JavaScript, TypeScript, Angular, C#, ASP.NET Core",
                "Database & ORM: SQL, SQL Server, Entity Framework Core, PostgreSQL, pgvector",
                "Tools & DevOps: Git, GitHub, Docker, Google Cloud Platform (GCP), Grafana K6",
                "Specialized: Dependency Management, AI Integration, Prompt Engineering"
            ]
        },
        {
            "title": "EDUCATION",
            "content": [
                "University of Buenos Aires (UBA) - B.S. in Data Science, 2025 - 2032",
                "Focus: Mathematics and Computer Science",
                "IBM - AI Fundamentals Certification, 2026",
                "Fray Luis Beltrán Secondary School, 2017 - 2024"
            ]
        },
        {
            "title": "LANGUAGES",
            "content": [
                "English: Advanced (Professional Working Proficiency in Spoken and Written)"
            ]
        }
    ]

    # Construct HTML with CSS for precise control
    html = f"""
    <style>
        body {{ font-family: Helvetica, Arial, sans-serif; font-size: 9.5pt; line-height: 1.25; color: #000; }}
        h1 {{ font-size: 16pt; text-align: center; margin-bottom: 2pt; text-transform: uppercase; font-weight: bold; }}
        .contact {{ text-align: center; font-size: 8.5pt; margin-bottom: 8pt; line-height: 1.4; }}
        h2 {{ font-size: 10.5pt; font-weight: bold; border-bottom: 0.5pt solid #000; margin-top: 10pt; margin-bottom: 5pt; text-transform: uppercase; }}
        .item {{ margin-bottom: 3pt; text-align: left; }}
        .tech {{ font-size: 8.5pt; font-style: italic; color: #333; margin-bottom: 8pt; }}
        strong {{ font-weight: bold; }}
    </style>
    <body>
        <h1>{name}</h1>
        <div class="contact">
            Website: newportfolio.com &nbsp;|&nbsp; GitHub: github.com/signal-node-t527 &nbsp;|&nbsp; 
            Linkedin: linkedin.com/in/emiliano-t-024556279/<br>
            Email: localframe.dev@proton.me &nbsp;|&nbsp; Phone: +54 11 2651 5713
        </div>
    """
    
    for sec in sections:
        html += f"<h2>{sec['title']}</h2>"
        for i, line in enumerate(sec['content']):
            if "tecnologias usadas:" in line.lower():
                techs = line.lower().replace("tecnologias usadas:", "").strip()
                html += f'<div class="tech"><strong>Technologies:</strong> {techs}</div>'
            elif line.startswith("•") or line.startswith("-"):
                line_content = line.lstrip("•- ").strip()
                html += f'<div class="item">&bull; {line_content}</div>'
            else:
                # First line of experience/education items usually bold
                if i == 0 or (len(line) < 100 and not line.endswith('.')):
                    html += f'<div class="item"><strong>{line}</strong></div>'
                else:
                    html += f'<div class="item">{line}</div>'
        
    html += "</body>"

    # Create the PDF document
    doc = pymupdf.open()
    page = doc.new_page()
    
    # Define a larger rectangle to fit all content (smaller margins)
    rect = page.rect + (40, 30, -40, -30)
    
    # Use insert_htmlbox for precise single-page rendering
    page.insert_htmlbox(rect, html)
    
    doc.save(output_pdf_path)
    doc.close()
    print(f"ATS-friendly PDF created at: {output_pdf_path}")

if __name__ == "__main__":
    create_ats_pdf("reference.md", "Nazareno_Tognoli_CV.pdf")
