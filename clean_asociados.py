import re

with open('asociados.html', 'r') as f:
    content = f.read()

# remove other sections from index that are not relevant

# 1. Parallax Tradition & Roast
parallax_2_search = r'<div class="parallax-container">[\s\S]*?<section class="panel bg-3">[\s\S]*?<div class="panel-content anim-hidden">[\s\S]*?<h2 class="panel-title">Tradición Caucana</h2>[\s\S]*?<p class="panel-text">Un proceso artesanal. Lavado, secado al sol y tratado con el mayor de los cuidados.</p>[\s\S]*?</div>[\s\S]*?</section>[\s\S]*?<section class="panel bg-4">[\s\S]*?<div class="panel-content anim-hidden">[\s\S]*?<h2 class="panel-title">Tueste Magistral</h2>[\s\S]*?<p class="panel-text">Nuestros maestros tostadores extraen los aceites esenciales exactos, creando el equilibrio perfecto entre aroma y sabor.</p>[\s\S]*?</div>[\s\S]*?</section>[\s\S]*?</div>'
content = re.sub(parallax_2_search, '', content)

# 2. Caficultores section (as this is the associated pitch, we can replace this entirely, or keep a modified version. Let's remove it for focus since we've added specific benefits).
caficultores_search = r'<section class="caficultores-section" id="caficultores">[\s\S]*?</section>'
content = re.sub(caficultores_search, '', content)

# 3. Product presentations
products_search = r'<section class="app-products-section" id="comprar">[\s\S]*?</section>'
content = re.sub(products_search, '', content)

with open('asociados.html', 'w') as f:
    f.write(content)
