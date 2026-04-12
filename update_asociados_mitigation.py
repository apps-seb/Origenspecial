import re

with open('asociados.html', 'r') as f:
    content = f.read()

story_section_search = r'<section class="story-section">[\s\S]*?<div class="story-content anim-hidden">[\s\S]*?<h2 class="section-title">Nuestra Historia</h2>[\s\S]*?<p class="story-text">[\s\S]*?En el corazón de las montañas del Cauca, donde la tierra es fértil y el clima es un regalo divino, nace <strong>Origen Special</strong>. No somos solo una marca de café; somos el trabajo de manos campesinas, de familias que han dedicado generaciones a perfeccionar el arte del cultivo. Cada grano cuenta una historia de pasión, de madrugadas frías y de un respeto absoluto por la naturaleza. Nuestro café es 100% colombiano, un tributo líquido a la riqueza de nuestra tierra.[\s\S]*?</p>[\s\S]*?</div>[\s\S]*?</section>'

story_section_replace = '''<section class="story-section">
        <video class="story-bg-img lazy-video" loop muted playsinline preload="none" poster="https://mercacol.com.co/wp-content/uploads/2026/03/IMG_5985.jpeg">
            <source src="https://mercacol.com.co/wp-content/uploads/2026/03/gemini_generated_video_8F7B4BAF.mov" type="video/mp4">
        </video>

        <div class="story-overlay"></div>
        <div class="story-content anim-hidden">
            <h2 class="section-title">Integración Tecnológica Transparente</h2>
            <p class="story-text">
                Sabemos que la innovación no debe ser un obstáculo. Por eso, <strong>nosotros asumimos el 100% de la integración tecnológica</strong>. Su institución no necesitará invertir recursos en desarrollo, modificar sus sistemas internos ni contratar personal adicional. Nuestro equipo se encarga de conectar las bases de datos de forma segura para validar la Cédula Cafetera y activar los beneficios automáticamente en nuestra plataforma. <strong>Cero fricción, máximo impacto.</strong>
            </p>
        </div>
    </section>'''

content = re.sub(story_section_search, story_section_replace, content)

with open('asociados.html', 'w') as f:
    f.write(content)
