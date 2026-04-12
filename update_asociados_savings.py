import re

with open('asociados.html', 'r') as f:
    content = f.read()

# Replace the "Más allá de la taza" benefits section with Savings Projection
benefits_parallax_search = r'<section class="benefits-parallax">[\s\S]*?<div class="benefits-bg-img-blur"></div>[\s\S]*?<img src="https://mercacol.com.co/wp-content/uploads/2026/03/9c568e9f-acc1-4dd9-8a06-01fc9398f32b.jpeg" alt="Beneficios de Origen Special" class="benefits-bg-img" loading="lazy">[\s\S]*?<div class="benefits-content">[\s\S]*?<div class="benefits-header anim-hidden">[\s\S]*?<h2 class="section-title">Más allá de la taza</h2>[\s\S]*?<p class="story-text" style="color: var\(--text-main\);">Descubre los beneficios únicos que Origen Special aporta a tu vida y a nuestra tierra.</p>[\s\S]*?</div>[\s\S]*?<div class="benefits-grid">[\s\S]*?<div class="benefit-card anim-hidden" style="transition-delay: 0.1s;">[\s\S]*?<i class="ph ph-heart benefit-icon"></i>[\s\S]*?<h3>Salud y Vitalidad</h3>[\s\S]*?<p>Rico en antioxidantes naturales que protegen tus células y te brindan energía sostenida durante todo el día.</p>[\s\S]*?</div>[\s\S]*?<div class="benefit-card anim-hidden" style="transition-delay: 0.2s;">[\s\S]*?<i class="ph ph-handshake benefit-icon"></i>[\s\S]*?<h3>Empoderamiento Social</h3>[\s\S]*?<p>Cada grano apoya directamente a familias caficultoras del Cauca, promoviendo educación y desarrollo en la región.</p>[\s\S]*?</div>[\s\S]*?<div class="benefit-card anim-hidden" style="transition-delay: 0.3s;">[\s\S]*?<i class="ph ph-leaf benefit-icon"></i>[\s\S]*?<h3>Sostenibilidad Ecológica</h3>[\s\S]*?<p>Prácticas agrícolas responsables que protegen la biodiversidad y los nacimientos de agua de nuestras montañas.</p>[\s\S]*?</div>[\s\S]*?<div class="benefit-card anim-hidden" style="transition-delay: 0.4s;">[\s\S]*?<i class="ph ph-magnifying-glass benefit-icon"></i>[\s\S]*?<h3>Trazabilidad Total</h3>[\s\S]*?<p>Conoce el origen exacto de tu café, desde la semilla en la finca hasta el tueste magistral en tu taza.</p>[\s\S]*?</div>[\s\S]*?</div>[\s\S]*?</div>[\s\S]*?</section>'

benefits_parallax_replace = '''<section class="benefits-parallax">
        <div class="benefits-bg-img-blur"></div>
        <img src="https://mercacol.com.co/wp-content/uploads/2026/03/9c568e9f-acc1-4dd9-8a06-01fc9398f32b.jpeg" alt="Beneficios para Caficultores" class="benefits-bg-img" loading="lazy">
        <div class="benefits-content">
            <div class="benefits-header anim-hidden">
                <h2 class="section-title">Impacto Económico Real</h2>
                <p class="story-text" style="color: var(--text-main);">Proyección de ahorro mensual estimado para una familia cafetera promedio utilizando los beneficios de la alianza.</p>
            </div>
            <div class="benefits-grid">
                <div class="benefit-card anim-hidden" style="transition-delay: 0.1s;">
                    <i class="ph ph-shopping-bag benefit-icon"></i>
                    <h3>Compras Mensuales</h3>
                    <p style="font-size: 1.5rem; font-weight: bold; color: var(--gold); margin-bottom: 10px;">$500.000</p>
                    <p>Gasto promedio estimado en insumos básicos y productos de tienda.</p>
                </div>
                <div class="benefit-card anim-hidden" style="transition-delay: 0.2s;">
                    <i class="ph ph-percent benefit-icon"></i>
                    <h3>Descuento Aplicado</h3>
                    <p style="font-size: 1.5rem; font-weight: bold; color: var(--gold); margin-bottom: 10px;">10%</p>
                    <p>Descuento base garantizado por estar registrado con la Cédula Cafetera.</p>
                </div>
                <div class="benefit-card anim-hidden" style="transition-delay: 0.3s;">
                    <i class="ph ph-piggy-bank benefit-icon"></i>
                    <h3>Ahorro Directo</h3>
                    <p style="font-size: 1.5rem; font-weight: bold; color: var(--gold); margin-bottom: 10px;">$50.000</p>
                    <p>Dinero que queda en el bolsillo del productor mes a mes.</p>
                </div>
                <div class="benefit-card anim-hidden" style="transition-delay: 0.4s;">
                    <i class="ph ph-chart-line-up benefit-icon"></i>
                    <h3>Ahorro Anual Proyectado</h3>
                    <p style="font-size: 1.5rem; font-weight: bold; color: var(--gold); margin-bottom: 10px;">$600.000+</p>
                    <p>Sin contar bonos extra, puntos redimibles ni promociones especiales de temporada.</p>
                </div>
            </div>
        </div>
    </section>'''

content = re.sub(benefits_parallax_search, benefits_parallax_replace, content)

with open('asociados.html', 'w') as f:
    f.write(content)
