import subprocess
import os

def run_command(command):
    print(f"Running: {' '.join(command)}")
    subprocess.run(command, check=True)

# Common settings
ALL_PROJECTS = ["ere", "suggestion-engine", "arborismo", "notes-app"]

ABOUT_EN = "I specialize in building intelligent applications that integrate modern AI capabilities with scalable enterprise development"
ABOUT_ES = "Me especializo en la creación de aplicaciones inteligentes que integran capacidades de IA modernas con desarrollo empresarial escalable"
EXP_EN = "Experienced in building intelligent full-stack applications by integrating .NET and Angular with advanced AI technologies. I have successfully implemented RAG systems and semantic search engines. Proven track record in architecting scalable microservices and containerized environments."
EXP_ES = "He implementado exitosamente sistemas RAG y motores de búsqueda semántica. Trayectoria comprobada arquitectando microservicios escalables y entornos contenerizados."

variants = [
    {
        "id": "ai", #make sure it is oriented to sell as AI engineer
        "greeting_en": "Hello, I'm Nazareno",
        "greeting_es": "Hola, soy Nazareno",
        "role_en": "AI Solutions Engineer",
        "role_es": "IA Solutions Engineer",
        "heading_pre_en": "I build ",
        "heading_pre_es": "Construyo sistemas ",
        "highlight_en": "intelligent",
        "highlight_es": "inteligentes",
        "heading_post_en": " systems and scalable software.",
        "heading_post_es": " y escalables.",
        "subheading_en": "I'm a passionate developer specializing in implementing Generative AI, scalable software and designing cutting-edge models for real-world applications.",
        "subheading_es": "Estoy especializado en implementación de IA generativa y diseño de modelos de vanguardia para aplicaciones del mundo real.",
        "about_en": ABOUT_EN,
        "about_es": ABOUT_ES,
        "exp_en": EXP_EN,
        "exp_es": EXP_ES,
        "color": "198 99.4% 57.2%"
    },
    {
        "id": "backend", #make sure it is oriented to sell as backend
        "greeting_en": "Hello, I'm Nazareno",
        "greeting_es": "Hola, soy Nazareno",
        "role_en": ".NET Backend Developer",
        "role_es": "Desarrollador Backend .NET",
        "heading_pre_en": "I architect ",
        "heading_pre_es": "Arquitecturo sistemas ",
        "highlight_en": "scalable",
        "highlight_es": "escalables",
        "heading_post_en": " backends and robust APIs.",
        "heading_post_es": " y APIs robustas.",
        "subheading_en": "I'm a passionate developer specializing in implementing Generative AI, scalable software and designing cutting-edge models for real-world applications.",
        "subheading_es": "Estoy especializado en implementación de IA generativa y diseño de modelos de vanguardia para aplicaciones del mundo real.",
        "about_en": ABOUT_EN,
        "about_es": ABOUT_ES,
        "exp_en": EXP_EN,
        "exp_es": EXP_ES,
        "color": "271 80.7% 30.2%"
    },
    {
        "id": "frontend", #make sure it is oriented to sell as frontend
        "greeting_en": "Hello, I'm Nazareno",
        "greeting_es": "Hola, soy Nazareno",
        "role_en": "Frontend Angular Developer",
        "role_es": "Desarrollador Frontend Angular",
        "heading_pre_en": "I craft ",
        "heading_pre_es": "Diseño interfaces ",
        "highlight_en": "robust",
        "highlight_es": "robustas",
        "heading_post_en": " and scalable software.",
        "heading_post_es": " y software escalable.",
        "subheading_en": "Focused on Angular 19+, custom scalable systems, and seamless .NET API integration.",
        "subheading_es": "Enfocado en Angular 19+, sistemas escalables personalizados e integración fluida con APIs en .NET.",
        "about_en": ABOUT_EN,
        "about_es": ABOUT_ES,
        "exp_en": EXP_EN,
        "exp_es": EXP_ES,
        "color": "0 80.7% 54.3%"
    },
    {
        "id": "fullstack", #make sure it is oriented to sell as fullstack
        "greeting_en": "Hello, I'm Nazareno",
        "greeting_es": "Hola, soy Nazareno",
        "role_en": "Fullstack Software Engineer",
        "role_es": "Desarrollador de Software Fullstack",
        "heading_pre_en": "I build ",
        "heading_pre_es": "Construyo soluciones ",
        "highlight_en": "end-to-end",
        "highlight_es": "integrales",
        "heading_post_en": " software and AI systems.",
        "heading_post_es": " y sistemas de IA.",
        "subheading_en": "Versatile engineer specialized in the Angular, ASP.NET Core, and SQL Server ecosystem.",
        "subheading_es": "Desarrollador versátil especializado en el ecosistema Angular, ASP.NET Core y SQL Server.",
        "about_en": ABOUT_EN,
        "about_es": ABOUT_ES,
        "exp_en": EXP_EN,
        "exp_es": EXP_ES,
        "color": "225 100% 44%"
    },
    {
        "id": "neutral", #make sure it is oriented to sell to everyone
        "greeting_en": "Hello, I'm Nazareno",
        "greeting_es": "Hola, soy Nazareno",
        "role_en": "Software Engineer",
        "role_es": "Desarrollador de Software",
        "heading_pre_en": "I solve ",
        "heading_pre_es": "Resuelvo problemas ",
        "highlight_en": "complex",
        "highlight_es": "complejos",
        "heading_post_en": " problems with software.",
        "heading_post_es": " mediante software.",
        "subheading_en": "Proactive professional with a solid technical foundation in the Angular, .NET, and SQL Server stack.",
        "subheading_es": "Profesional proactivo con sólida formación técnica en el stack Angular, .NET y SQL Server.",
        "about_en": ABOUT_EN,
        "about_es": ABOUT_ES,
        "exp_en": EXP_EN,
        "exp_es": EXP_ES,
        "color": "225 0% 46.2%"
    }
]

def main():
    python_exe = os.path.join("..", "venv", "Scripts", "python.exe")
    script_path = "generate_variant.py"
    
    # Map focus type to the old variant IDs
    variant_ids = {
        "ai": "64e9200f",
        "backend": "c4ef1978",
        "frontend": "934aef0f",
        "fullstack": "efc162cc",
        "neutral": "5f78cedb"
    }
    
    # Generate one localized JSON file per variant type using the fixed IDs
    for v in variants:
        vid = variant_ids[v["id"]]
        cmd = [
            python_exe, script_path,
            "--id", vid,
            "--greeting-en", v["greeting_en"],
            "--greeting-es", v["greeting_es"],
            "--role-en", v["role_en"],
            "--role-es", v["role_es"],
            "--heading-pre-en", v["heading_pre_en"],
            "--heading-pre-es", v["heading_pre_es"],
            "--highlight-en", v["highlight_en"],
            "--highlight-es", v["highlight_es"],
            "--heading-post-en", v["heading_post_en"],
            "--heading-post-es", v["heading_post_es"],
            "--subheading-en", v["subheading_en"],
            "--subheading-es", v["subheading_es"],
            "--about-en", v["about_en"],
            "--about-es", v["about_es"],
            "--exp-en", v["exp_en"],
            "--exp-es", v["exp_es"],
            "--cv-link-en", f"https://wkwqixrhkcnstazptsdm.supabase.co/storage/v1/object/public/cvs/Nazareno_Tognoli_{v['id']}_en.pdf",
            "--cv-link-es", f"https://wkwqixrhkcnstazptsdm.supabase.co/storage/v1/object/public/cvs/Nazareno_Tognoli_{v['id']}_es.pdf",
            "--projects"
        ] + ALL_PROJECTS + [
            "--color", v["color"],
            "--output-dir", "rawconfiglist"
        ]
        
        run_command(cmd)

if __name__ == "__main__":
    main()
