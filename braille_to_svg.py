import svgwrite

def create_a4_text_svg(output_file, text, font_size=16, font_family="Arial"):
    # Define A4 dimensions in mm
    a4_width_mm = 210
    a4_height_mm = 297

    # Create an SVG canvas with A4 dimensions
    dwg = svgwrite.Drawing(output_file, size=(f"{a4_width_mm}mm", f"{a4_height_mm}mm"))

    # Add some text to the SVG
    dwg.add(
        dwg.text(
            text,
            insert=("10mm", "20mm"),  # Start 10mm from the left and 20mm from the top
            font_size=f"{font_size}pt",
            font_family=font_family,
            fill="black"  # Text color
        )
    )

    # Save the SVG file
    dwg.save()
    print(f"SVG saved as: {output_file}")

# Usage
output_file = "text_a4.svg"
text_content = """⠠⠎⠉⠑⠏⠞⠊⠉⠊⠎⠍⠀⠊⠎⠀⠵⠀⠍⠡⠀⠮⠀⠗⠑⠎⠥⠇⠞⠀⠷⠀⠅⠂⠀⠵⠀⠅⠀⠊⠎⠀⠷⠀
⠎⠉⠑⠏⠞⠊⠉⠊⠎⠍⠲⠀⠠⠖⠃⠑⠀⠒⠞⠢⠞⠀⠾⠀⠱⠁⠞⠀⠺⠑⠀⠁⠞⠀⠏⠗⠑⠎⠢⠞⠀⠐⠅⠂⠀⠊⠎⠂⠀⠿⠮⠀
⠍⠕⠌⠀⠐⠏⠂⠀⠖⠩⠥⠞⠀⠳⠗⠀⠑⠜⠎⠀⠁⠛⠌⠀⠒⠧⠊⠉⠰⠝⠆⠀⠎⠔⠉⠑⠂⠀⠋⠀⠮⠀⠧⠀
⠛⠗⠁⠙⠥⠁⠇⠀⠐⠡⠀⠷⠀⠳⠗⠀⠫⠥⠉⠠⠝⠂⠀⠺⠑⠀⠍⠌⠀⠒⠞⠔⠥⠠⠽⠀⠿⠛⠑⠞⠂⠀⠯⠀
⠑⠍⠁⠝⠉⠊⠏⠁⠞⠑⠀⠳⠗⠧⠎⠀⠋⠂⠀⠅⠀⠏⠗⠑⠧⠊⠳⠎⠇⠽⠀⠁⠉⠟⠥⠊⠗⠫⠆⠀⠺⠑⠀⠍⠌⠀⠎⠑⠞⠀
⠁⠎⠊⠙⠑⠀⠕⠇⠙⠀⠝⠕⠰⠝⠎⠀⠯⠀⠑⠍⠃⠗⠁⠉⠑⠀⠋⠗⠑⠩⠀⠐⠕⠎⠆⠀⠯⠂⠀⠵⠀⠺⠑⠀⠇⠑⠜⠝⠂⠀⠺⠑⠀⠍⠌⠀⠆⠀
⠙⠁⠊⠇⠽⠀⠥⠝⠇⠑⠜⠝⠬⠀⠐⠎⠹⠬⠀⠱⠀⠭⠀⠓⠁⠎⠀⠉⠕⠌⠀⠥⠀⠝⠕⠀⠎⠍⠁⠇⠇⠀⠇⠁⠃⠳⠗⠀⠯⠀
⠁⠝⠭⠊⠑⠞⠽⠀⠖⠁⠉⠟⠥⠊⠗⠑⠲⠀"""
create_a4_text_svg(output_file, text_content, font_size=20)
