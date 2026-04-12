import re

with open('asociados.html', 'r') as f:
    content = f.read()

features_section_search = r'<section class="features-section">[\s\S]*?<div class="cards-grid">[\s\S]*?<div class="card anim-hidden" style="transition-delay: 0.1s;">[\s\S]*?<div class="card-icon"><i class="ph ph-mountains"></i></div>[\s\S]*?<h3>Cultivo de Altura</h3>[\s\S]*?<p>Producido en fincas caucano-andinas a más de 1.700 m.s.n.m, lo que otorga una acidez brillante y un cuerpo inigualable.</p>[\s\S]*?</div>[\s\S]*?<div class="card anim-hidden" style="transition-delay: 0.2s;">[\s\S]*?<div class="card-icon"><i class="ph ph-coffee"></i></div>[\s\S]*?<h3>Perfil Sensorial</h3>[\s\S]*?<p>Deleita tus sentidos con notas profundas a chocolate oscuro, panela caramelizada y un sutil toque cítrico.</p>[\s\S]*?</div>[\s\S]*?<div class="card anim-hidden" style="transition-delay: 0.3s;">[\s\S]*?<div class="card-icon"><i class="ph ph-plant"></i></div>[\s\S]*?<h3>Comercio Justo</h3>[\s\S]*?<p>Trabajamos directamente con los caficultores. Cada compra impulsa el desarrollo social de las comunidades del Cauca.</p>[\s\S]*?</div>[\s\S]*?</div>[\s\S]*?</section>'

features_section_replace = '''<section class="features-section">
        <div class="cards-grid">
            <div class="card anim-hidden" style="transition-delay: 0.1s;">
                <div class="card-icon"><i class="ph ph-ticket"></i></div>
                <h3>Bono de Bienvenida</h3>
                <p>Al registrarse con su Cédula Cafetera, los asociados reciben instantáneamente un bono de descuento del 10% para su primera compra.</p>
            </div>
            <div class="card anim-hidden" style="transition-delay: 0.2s;">
                <div class="card-icon"><i class="ph ph-money"></i></div>
                <h3>Redención de Bonos</h3>
                <p>Opciones para redimir bonos de dinero en efectivo directamente en compras de insumos, herramientas y productos en la tienda.</p>
            </div>
            <div class="card anim-hidden" style="transition-delay: 0.3s;">
                <div class="card-icon"><i class="ph ph-star"></i></div>
                <h3>Puntos por Compras</h3>
                <p>Un sistema de fidelización donde cada compra acumula puntos que se traducen en descuentos y beneficios futuros para la familia cafetera.</p>
            </div>
        </div>
    </section>'''

content = re.sub(features_section_search, features_section_replace, content)

with open('asociados.html', 'w') as f:
    f.write(content)
