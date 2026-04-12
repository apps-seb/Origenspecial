import re

with open('asociados.html', 'r') as f:
    content = f.read()

# Modify title
content = content.replace('<title>Origen Special | Premium Colombian Coffee</title>', '<title>Origen Special | Alianzas y Asociados</title>')

# Modify Hero Video and Title
hero_section_search = r'<section class="panel bg-1">[\s\S]*?<div class="panel-content anim-hidden">[\s\S]*?<h1 class="panel-title">El Oro de Colombia</h1>[\s\S]*?<p class="panel-text"[^>]*>Descubre el alma del Cauca en cada taza. Un café de origen, cultivado en tierras ancestrales y acariciado por las nubes.</p>[\s\S]*?</div>[\s\S]*?<a href="#comprar" class="btn-glow hero-buy-btn">[\s\S]*?<span>Comprar Ahora</span>[\s\S]*?<i class="ph ph-coffee"></i>[\s\S]*?</a>[\s\S]*?</section>'

hero_section_replace = '''<section class="panel bg-1">
            <video class="hero-video lazy-video" loop muted playsinline preload="none" poster="https://mercacol.com.co/wp-content/uploads/2026/03/e6fc9fb7-bbce-453b-afe9-acf78283c8db.jpeg">
                <source src="https://mercacol.com.co/wp-content/uploads/2026/03/gemini_generated_video_60C3A431.mov" type="video/mp4">
            </video>

            <div class="panel-content anim-hidden">
                <h1 class="panel-title">Sumando Valor a la <span>Cédula Cafetera</span></h1>
                <p class="panel-text" style="margin-bottom: 30px;">Una alianza estratégica para fidelizar, premiar y mejorar la calidad de vida de las familias productoras del Cauca y Huila.</p>
            </div>
            <a href="#demostracion" class="btn-glow hero-buy-btn">
                <span>Ver Demostración</span>
                <i class="ph ph-play-circle"></i>
            </a>
        </section>'''

content = re.sub(hero_section_search, hero_section_replace, content)

# Modify Section 2 Hero
hero_2_search = r'<section class="panel bg-2">[\s\S]*?<div class="panel-content anim-hidden">[\s\S]*?<h2 class="panel-title">Selección Perfecta</h2>[\s\S]*?<p class="panel-text">Recolectado a mano en su punto óptimo de maduración para garantizar una experiencia sensorial incomparable.</p>[\s\S]*?</div>[\s\S]*?</section>'

hero_2_replace = '''<section class="panel bg-2">
            <video class="hero-video lazy-video" loop muted playsinline preload="none" poster="https://mercacol.com.co/wp-content/uploads/2026/03/0c898dc9-71d6-4c23-bcac-54909a748715.jpeg">
                <source src="https://mercacol.com.co/wp-content/uploads/2026/03/gemini_generated_video_11F92E45-1.mov" type="video/mp4">
            </video>

            <div class="panel-content anim-hidden">
                <h2 class="panel-title">Fidelización Efectiva</h2>
                <p class="panel-text">Conectamos los esfuerzos institucionales con beneficios reales y tangibles para cada asociado, directamente en sus compras cotidianas.</p>
            </div>
        </section>'''

content = re.sub(hero_2_search, hero_2_replace, content)

with open('asociados.html', 'w') as f:
    f.write(content)
