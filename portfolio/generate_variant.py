import json
import uuid
import os
import argparse

def generate_variant(args):
    """
    Generates a corresponding JSON configuration file for the portfolio variants
    using provided arguments or defaults.
    """
    variant_id = args.id if args.id else str(uuid.uuid4())[:8]
    
    config = {
        "id": variant_id,
        "heroBadgeGreeting": {
            "en": args.greeting_en or f"Hello, I'm Nazareno - Custom Variant {variant_id}",
            "es": args.greeting_es or f"Hola, soy Nazareno - Variante Personalizada {variant_id}"
        },
        "heroBadgeRole": {
            "en": args.role_en or "Custom AI Engineer",
            "es": args.role_es or "Ingeniero de IA a medida"
        },
        "heroHeadingPre": {
            "en": args.heading_pre_en or "I build ",
            "es": args.heading_pre_es or "Construyo sistemas "
        },
        "heroHeadingHighlight": {
            "en": args.highlight_en or "revolutionary",
            "es": args.highlight_es or "revolucionarios"
        },
        "heroHeadingPost": {
            "en": args.heading_post_en or " systems and scalable software.",
            "es": args.heading_post_es or " y escalables."
        },
        "heroSubheading": {
            "en": args.subheading_en or "This content was loaded in real-time from a remote configuration file.",
            "es": args.subheading_es or "Este contenido fue cargado en tiempo real desde un archivo de configuración."
        },
        "aboutSubtitle": {
            "en": args.about_en or "Engineer focused on bridging AI research and production systems.",
            "es": args.about_es or "Enfocado en conectar la investigación en IA con sistemas de producción."
        },
        "aboutExperience": {
            "en": args.exp_en or "5+ years designing and deploying machine learning models, data pipelines, and AI-driven products.",
            "es": args.exp_es or "Más de 2 años diseñando e implementando modelos de machine learning y productos impulsados por IA."
        },
        "cvLink": {
            "en": args.cv_link_en or args.cv_link or "https://drive.google.com/file/d/YOUR_CV_FILE_ID_EN/view?usp=sharing",
            "es": args.cv_link_es or args.cv_link or "https://drive.google.com/file/d/YOUR_CV_FILE_ID_ES/view?usp=sharing"
        },
        "customProjects": args.projects if args.projects else ["agent-system"],
        "primaryColor": args.color or "280 65% 45%"
    }
    
    # Ensure output directory exists
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        
    file_path = os.path.join(args.output_dir, f"{variant_id}.json")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        
    print(f"Generated variant: {variant_id}")
    print(f"File saved to: {file_path}")
    return variant_id

def main():
    parser = argparse.ArgumentParser(description="Generate a portfolio variant JSON configuration.")
    
    parser.add_argument("--id", type=str, help="Unique identifier for the variant (default: random 8-char UUID)")
    parser.add_argument("--greeting-en", type=str, help="English badge greeting")
    parser.add_argument("--greeting-es", type=str, help="Spanish badge greeting")
    parser.add_argument("--role-en", type=str, help="English role description")
    parser.add_argument("--role-es", type=str, help="Spanish role description")
    parser.add_argument("--heading-pre-en", type=str, help="English heading prefix")
    parser.add_argument("--heading-pre-es", type=str, help="Spanish heading prefix")
    parser.add_argument("--highlight-en", type=str, help="English heading highlight word")
    parser.add_argument("--highlight-es", type=str, help="Spanish heading highlight word")
    parser.add_argument("--heading-post-en", type=str, help="English heading suffix")
    parser.add_argument("--heading-post-es", type=str, help="Spanish heading suffix")
    parser.add_argument("--subheading-en", type=str, help="English subheading text")
    parser.add_argument("--subheading-es", type=str, help="Spanish subheading text")
    parser.add_argument("--about-en", type=str, help="English about description")
    parser.add_argument("--about-es", type=str, help="Spanish about description")
    parser.add_argument("--exp-en", type=str, help="English experience description")
    parser.add_argument("--exp-es", type=str, help="Spanish experience description")
    parser.add_argument("--cv-link", type=str, help="Link to a generic CV file (fallback)")
    parser.add_argument("--cv-link-en", type=str, help="Link to the English CV file")
    parser.add_argument("--cv-link-es", type=str, help="Link to the Spanish CV file")
    parser.add_argument("--projects", nargs="+", help="List of project IDs to display")
    parser.add_argument("--color", type=str, help="Primary color HSL components (e.g., '210 60%% 35%%')")
    parser.add_argument("--output-dir", type=str, default="portfolio/rawconfiglist", help="Directory to save the JSON file (default: portfolio/rawconfiglist)")

    args = parser.parse_args()
    generate_variant(args)

if __name__ == "__main__":
    main()
