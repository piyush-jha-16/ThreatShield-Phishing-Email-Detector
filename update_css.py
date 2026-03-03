import re
import os

filepath = r'd:\Projects\ThreatShield-Phishing-Email-Detector\static\css\style.css'
with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Root variables
root_pattern = re.compile(r':root\s*\{.*?(?=\/\* === Reset & Base Styles === \*\/)', re.DOTALL)
new_root = """:root {
    /* Color Palette - Professional Enterprise Dark */
    --color-background: #09090b;
    --color-surface: #121214;
    --color-surface-elevated: #18181b;
    --color-surface-hover: #27272a;
    --color-border: #27272a;
    --color-border-light: #3f3f46;
    
    /* Text Colors */
    --color-text-primary: #fafafa;
    --color-text-secondary: #a1a1aa;
    --color-text-tertiary: #71717a;
    --color-text-inverse: #09090b;
    
    /* Status Colors */
    --color-safe: #10b981;
    --color-safe-bg: rgba(16, 185, 129, 0.15);
    --color-suspicious: #f59e0b;
    --color-suspicious-bg: rgba(245, 158, 11, 0.15);
    --color-danger: #ef4444;
    --color-danger-bg: rgba(239, 68, 68, 0.15);
    
    /* Accent Colors - Electric Indigo */
    --color-accent: #6366f1;
    --color-accent-hover: #4f46e5;
    --color-accent-light: rgba(99, 102, 241, 0.15);
    --color-accent-glow: rgba(99, 102, 241, 0.4);
    
    /* Shadows */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.5);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.6), 0 2px 4px -1px rgba(0, 0, 0, 0.4);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.7), 0 4px 6px -2px rgba(0, 0, 0, 0.4);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.8), 0 10px 10px -5px rgba(0, 0, 0, 0.5);
    
    /* Typography */
    --font-heading: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-size-xs: 0.75rem;
    --font-size-sm: 0.875rem;
    --font-size-base: 1rem;
    --font-size-lg: 1.125rem;
    --font-size-xl: 1.25rem;
    --font-size-2xl: 1.75rem;
    --font-size-3xl: 2.75rem;
    
    /* Spacing */
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;
    
    /* Border Radius */
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 16px;
    --radius-xl: 24px;
    
    /* Transitions */
    --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
"""
css = root_pattern.sub(new_root, css)

# Add heading font styles and typography reset
heading_styles = """
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    letter-spacing: -0.02em;
}

/* === Ambient Background === */
.ambient-glow {
    position: fixed;
    border-radius: 50%;
    filter: blur(120px);
    z-index: -1;
    pointer-events: none;
    opacity: 0.15;
}
.glow-1 {
    top: -10%;
    right: -5%;
    width: 600px;
    height: 600px;
    background: var(--color-accent);
}
.glow-2 {
    bottom: -10%;
    left: -10%;
    width: 600px;
    height: 600px;
    background: #8b5cf6;
}
body.light-mode .ambient-glow {
    opacity: 0.08;
}

"""
css = css.replace('/* === Reset & Base Styles === */\n*', '/* === Reset & Base Styles === */\n' + heading_styles + '\n*')

# 2. Update Light mode variables
light_mode_pattern = re.compile(r'body\.light-mode\s*\{.*?(?=\}\s*body\.light-mode \.theme-toggle)', re.DOTALL)
new_light_mode = """body.light-mode {
    --color-background: #ffffff;
    --color-surface: #f8fafc;
    --color-surface-elevated: #ffffff;
    --color-surface-hover: #f1f5f9;
    --color-border: #e2e8f0;
    --color-border-light: #cbd5e1;
    
    --color-text-primary: #0f172a;
    --color-text-secondary: #475569;
    --color-text-tertiary: #64748b;
    --color-text-inverse: #ffffff;
    
    --color-accent: #4f46e5;
    --color-accent-hover: #4338ca;
    --color-accent-light: rgba(79, 70, 229, 0.1);
    --color-accent-glow: rgba(79, 70, 229, 0.25);
    
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.03);
"""
css = light_mode_pattern.sub(new_light_mode, css)

# 3. Update Buttons
btn_primary_pattern = re.compile(r'\.btn-primary\s*\{[^}]*\}', re.DOTALL)
new_btn_primary = """.btn-primary {
    background: var(--color-accent);
    color: white;
    box-shadow: 0 2px 8px var(--color-accent-glow);
    position: relative;
    overflow: hidden;
    font-weight: 600;
    letter-spacing: 0.01em;
    border: 1px solid rgba(255, 255, 255, 0.1);
}"""
css = btn_primary_pattern.sub(new_btn_primary, css)

btn_primary_hover_pattern = re.compile(r'\.btn-primary:hover:not\(:disabled\)\s*\{[^}]*\}', re.DOTALL)
new_btn_primary_hover = """.btn-primary:hover:not(:disabled) {
    background: var(--color-accent-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px var(--color-accent-glow), 0 2px 6px rgba(0, 0, 0, 0.2);
}"""
css = btn_primary_hover_pattern.sub(new_btn_primary_hover, css)

# 4. App header
header_pattern = re.compile(r'\.app-header\s*\{[^}]*\}', re.DOTALL)
new_header = """.app-header {
    background: rgba(9, 9, 11, 0.7);
    border-bottom: 1px solid var(--color-border);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: var(--shadow-sm);
    backdrop-filter: blur(16px) saturate(1.8);
    -webkit-backdrop-filter: blur(16px) saturate(1.8);
}"""
css = header_pattern.sub(new_header, css)

header_light_pattern = re.compile(r'body\.light-mode \.app-header\s*\{[^}]*\}', re.DOTALL)
new_header_light = """body.light-mode .app-header {
    background: rgba(255, 255, 255, 0.85);
    border-bottom: 1px solid var(--color-border);
    box-shadow: var(--shadow-sm);
}"""
css = header_light_pattern.sub(new_header_light, css)

# 5. Welcome section typographic flair
welcome_pattern = re.compile(r'\.welcome-section h1\s*\{[^}]*\}', re.DOTALL)
new_welcome = """.welcome-section h1 {
    font-size: var(--font-size-3xl);
    font-weight: 800;
    margin-bottom: var(--spacing-sm);
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, var(--color-text-primary) 0%, var(--color-text-tertiary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}"""
css = welcome_pattern.sub(new_welcome, css)

# 6. Card hovers
card_hover_pattern = re.compile(r'\.panel-card:hover\s*\{[^}]*\}', re.DOTALL)
new_card_hover = """.panel-card:hover {
    box-shadow: var(--shadow-xl), 0 0 0 1px var(--color-accent-light);
    border-color: var(--color-border-light);
    transform: translateY(-4px);
}"""
css = card_hover_pattern.sub(new_card_hover, css)

result_card_hover_pattern = re.compile(r'\.result-card:hover\s*\{[^}]*\}', re.DOTALL)
new_result_card_hover = """.result-card:hover {
    box-shadow: var(--shadow-xl), 0 0 0 1px var(--color-accent-light);
    border-color: var(--color-border-light);
    transform: translateY(-4px);
}"""
css = result_card_hover_pattern.sub(new_result_card_hover, css)

# 7. Replace hardcoded old greens with CSS variables where applicable
css = css.replace('#5bc99a', 'var(--color-accent-light)')
css = css.replace('rgba(80, 184, 136, 0.05)', 'var(--color-accent-light)')
css = css.replace('rgba(80, 184, 136, 0.1)', 'var(--color-accent-light)')
css = css.replace('rgba(80, 184, 136, 0.15)', 'var(--color-accent-light)')
css = css.replace('rgba(80, 184, 136, 0.2)', 'var(--color-accent-light)')
css = css.replace('rgba(80, 184, 136, 0.25)', 'var(--color-accent-glow)')
css = css.replace('rgba(80, 184, 136, 0.3)', 'var(--color-accent-glow)')
css = css.replace('rgba(80, 184, 136, 0.35)', 'var(--color-accent-glow)')

# Overhaul Risk Card background
risk_card_pattern = re.compile(r'\.risk-card\s*\{[^}]*\}', re.DOTALL)
new_risk_card = """.risk-card {
    background: linear-gradient(135deg, var(--color-surface) 0%, var(--color-surface-elevated) 100%);
    position: relative;
    overflow: hidden;
    border: 1px solid var(--color-border);
}"""
css = risk_card_pattern.sub(new_risk_card, css)

# Make inputs more premium
input_hover_pattern = re.compile(r'input\[type="text"\]:hover,\s*input\[type="email"\]:hover,\s*input\[type="password"\]:hover,\s*textarea:hover\s*\{[^}]*\}', re.DOTALL)
new_input_hover = """input[type="text"]:hover,
input[type="email"]:hover,
input[type="password"]:hover,
textarea:hover {
    border-color: var(--color-border-light);
    background: var(--color-surface-hover);
}"""
css = input_hover_pattern.sub(new_input_hover, css)

input_focus_pattern = re.compile(r'input\[type="text"\]:focus,\s*input\[type="email"\]:focus,\s*input\[type="password"\]:focus,\s*textarea:focus\s*\{[^}]*\}', re.DOTALL)
new_input_focus = """input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus,
textarea:focus {
    border-color: var(--color-accent);
    background: var(--color-background);
    box-shadow: 0 0 0 3px var(--color-accent-light);
    transform: translateY(-1px);
}"""
css = input_focus_pattern.sub(new_input_focus, css)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css successfully!")
