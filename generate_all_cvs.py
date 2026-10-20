from cv_engine import generate_cv
import os

def generate_all():
    """Generates all 10 CV versions as specified in workflow.md"""
    
    # Define tech versions
    tech_focuses = ["frontend", "backend", "fullstack", "ai"]
    languages = ["en", "es"]
    
    # Create output directory
    output_dir = "cv_versions"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"Starting generation of all CV versions in '{output_dir}/'...")

    # 1-8: Tech versions (4 focuses * 2 languages)
    for focus in tech_focuses:
        for lang in languages:
            filename = f"Nazareno_Tognoli_{focus}_{lang}.pdf"
            generate_cv(focus, lang, os.path.join(output_dir, filename))
            
    # 9-10: Neutral versions (English & Spanish)
    for lang in languages:
        filename_neutral = f"Nazareno_Tognoli_neutral_{lang}.pdf"
        generate_cv("neutral", lang, os.path.join(output_dir, filename_neutral))
    
    print("\nAll 10 CV versions have been successfully generated.")

if __name__ == "__main__":
    generate_all()
