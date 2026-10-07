"""
Helper utility to render terminal execution output as a dark-mode screenshot PNG.
"""
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont

def render_terminal_output(command_args, cwd, output_png_path, title="Terminal - PowerShell"):
    # Run command and capture output
    result = subprocess.run(
        command_args,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True
    )
    terminal_text = result.stdout
    
    # Lines
    prompt_str = f"PS {cwd}> python main.py"
    lines = [prompt_str]
    lines.extend(terminal_text.splitlines())
    
    # Font setup
    font_size = 15
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()
        
    line_height = font_size + 7
    padding_x = 24
    header_height = 40
    
    # Calculate dimensions
    max_len = max(len(line) for line in lines) if lines else 70
    char_width = 9.2
    img_width = max(860, int(max_len * char_width) + padding_x * 2 + 10)
    img_height = header_height + (len(lines) * line_height) + 35
    
    # Colors
    bg_color = (30, 30, 30)         # VS Code / Windows Terminal Dark
    header_color = (45, 45, 45)     # Window Header
    border_color = (60, 60, 60)
    text_color = (220, 220, 220)    # White-ish
    prompt_color = (97, 175, 239)   # Blueish PS prompt
    accent_green = (152, 195, 121)
    accent_yellow = (229, 192, 123)
    accent_cyan = (86, 182, 194)
    
    img = Image.new("RGB", (img_width, img_height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw Window Header
    draw.rectangle([(0, 0), (img_width, header_height)], fill=header_color)
    draw.line([(0, header_height), (img_width, header_height)], fill=border_color, width=1)
    
    # macOS / Modern style window control buttons
    button_y = 20
    draw.ellipse([(18, button_y - 6), (30, button_y + 6)], fill=(255, 95, 86))    # Red
    draw.ellipse([(38, button_y - 6), (50, button_y + 6)], fill=(255, 189, 46))   # Yellow
    draw.ellipse([(58, button_y - 6), (70, button_y + 6)], fill=(39, 201, 63))    # Green
    
    # Draw title
    title_font_size = 13
    try:
        title_font = ImageFont.truetype("C:/Windows/Fonts/seguiemj.ttf", title_font_size)
    except:
        title_font = font
    draw.text((85, 12), title, fill=(180, 180, 180), font=font)
    
    # Draw content
    y = header_height + 15
    for i, line in enumerate(lines):
        color = text_color
        if i == 0:
            color = prompt_color
        elif line.startswith("=") or line.startswith("#"):
            color = accent_cyan
        elif "TERBAIK" in line or "BERPRESTASI" in line or "BERHASIL" in line or "Normal" in line:
            color = accent_green
        elif "DITOLAK" in line or "Panas" in line or "ERROR" in line:
            color = (244, 71, 71)
        elif "Dingin" in line:
            color = (97, 175, 239)
        elif "|" in line:
            color = accent_yellow if "No" in line else text_color
            
        draw.text((padding_x, y), line, fill=color, font=font)
        y += line_height
        
    img.save(output_png_path, "PNG")
    print(f"Generated {output_png_path} ({img_width}x{img_height})")

if __name__ == "__main__":
    import os
    target_case = sys.argv[1] if len(sys.argv) > 1 else "case-01-analisis-nilai"
    cwd = os.path.abspath(target_case)
    out_png = os.path.join(cwd, "output.png")
    py_exec = sys.executable
    render_terminal_output([py_exec, "main.py"], cwd, out_png, title=f"Terminal - {target_case}")
