import re

with open('asociados.html', 'r') as f:
    content = f.read()

# Replace the "La Experiencia Origen Special" section with a Live Demo section
product_section_search = r'<section class="product-section">[\s\S]*?<div class="anim-hidden text-center" style="text-align: center;">[\s\S]*?<h2 class="section-title">La Experiencia Origen Special</h2>[\s\S]*?<p style="color: var\(--text-muted\); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">Pasa el cursor o toca la bolsa para descubrir la información técnica de nuestro lote exclusivo.</p>[\s\S]*?</div>[\s\S]*?<div class="flip-container anim-zoom">[\s\S]*?<div class="flipper">[\s\S]*?<div class="front">[\s\S]*?<img src="https://mercacol.com.co/wp-content/uploads/2026/03/91f3b12f-bdc7-4051-83c2-dd349b84b981.jpeg" alt="Origen Special Empaque Frontal" loading="lazy">[\s\S]*?</div>[\s\S]*?<div class="back">[\s\S]*?<img src="https://mercacol.com.co/wp-content/uploads/2026/03/24fbf367-db2b-44cf-97a1-225e2416b49d.jpeg" alt="Origen Special Detalles del Producto" loading="lazy">[\s\S]*?</div>[\s\S]*?</div>[\s\S]*?</div>[\s\S]*?</section>'

product_section_replace = '''<section class="product-section" id="demostracion">
        <div class="anim-hidden text-center" style="text-align: center; margin-bottom: 40px; width: 100%;">
            <h2 class="section-title">Demostración en Vivo</h2>
            <p style="color: var(--text-muted); font-size: 1.1rem; max-width: 700px; margin: 0 auto;">Simule la experiencia de un caficultor en nuestra tienda. Ingrese un número de Cédula Cafetera (ej. 123456) para ver cómo se aplica el descuento en tiempo real.</p>
        </div>

        <div class="demo-container anim-zoom" style="background: linear-gradient(145deg, #1e2028, #252730); border-radius: 24px; padding: 40px; border: 1px solid rgba(229, 141, 87, 0.2); box-shadow: 0 20px 40px rgba(0,0,0,0.4); max-width: 800px; width: 100%; margin: 0 auto; display: flex; flex-direction: column; gap: 30px;">

            <!-- Pos Simulation Header -->
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 20px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <i class="ph ph-storefront" style="font-size: 2rem; color: var(--gold);"></i>
                    <h3 style="font-size: 1.4rem; color: var(--text-main);">Punto de Venta Mercacol</h3>
                </div>
                <div style="background: rgba(20,21,25,0.5); padding: 8px 16px; border-radius: 8px; font-family: monospace; color: var(--text-muted);">Terminal: T-01</div>
            </div>

            <!-- Input and Cart Area -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

                <!-- Validation -->
                <div style="display: flex; flex-direction: column; gap: 15px;">
                    <label style="color: var(--text-muted); font-size: 0.9rem;">Validación de Asociado</label>
                    <div style="display: flex; gap: 10px;">
                        <input type="text" id="demoCedula" placeholder="Ingrese Cédula Cafetera" style="flex: 1; padding: 12px 15px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); background: rgba(20,21,25,0.8); color: var(--text-main); font-family: 'Poppins', sans-serif; font-size: 1rem; outline: none;">
                        <button id="demoValidarBtn" style="background: var(--gold); color: var(--bg-dark); border: none; padding: 0 20px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">Validar</button>
                    </div>

                    <div id="demoStatus" style="padding: 15px; border-radius: 8px; background: rgba(20,21,25,0.5); border: 1px solid rgba(255,255,255,0.05); margin-top: 10px; min-height: 80px; display: flex; align-items: center; gap: 15px;">
                        <i class="ph ph-info" style="font-size: 1.5rem; color: var(--text-muted);"></i>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0;">Esperando validación de documento...</p>
                    </div>
                </div>

                <!-- Cart Summary -->
                <div style="background: rgba(20,21,25,0.8); border-radius: 12px; padding: 25px; border: 1px solid rgba(255,255,255,0.05);">
                    <h4 style="color: var(--text-main); margin-bottom: 20px; font-size: 1.1rem; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 10px;">Resumen de Compra</h4>

                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px; color: var(--text-muted);">
                        <span>Subtotal</span>
                        <span>$120.000</span>
                    </div>

                    <div id="demoDiscountRow" style="display: flex; justify-content: space-between; margin-bottom: 10px; color: #4ade80; font-weight: 500; opacity: 0.3; transition: all 0.3s ease;">
                        <span>Descuento Asociado (10%)</span>
                        <span id="demoDiscountAmount">-$0</span>
                    </div>

                    <div style="display: flex; justify-content: space-between; margin-top: 20px; padding-top: 15px; border-top: 1px dashed rgba(255,255,255,0.1); color: var(--text-main); font-size: 1.3rem; font-weight: 700;">
                        <span>Total</span>
                        <span id="demoTotal">$120.000</span>
                    </div>
                </div>
            </div>

            <button id="demoResetBtn" style="align-self: flex-end; background: transparent; color: var(--text-muted); border: 1px solid rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; transition: all 0.3s ease;">Reiniciar Demo</button>

        </div>
    </section>'''

content = re.sub(product_section_search, product_section_replace, content)

# Inject Javascript for the demo
js_search = r'// Optimización Premium de UX: Lazy Loading Inteligente para Videos'
js_replace = '''
        // Lógica de Demostración en Vivo
        const demoValidarBtn = document.getElementById('demoValidarBtn');
        const demoCedula = document.getElementById('demoCedula');
        const demoStatus = document.getElementById('demoStatus');
        const demoDiscountRow = document.getElementById('demoDiscountRow');
        const demoDiscountAmount = document.getElementById('demoDiscountAmount');
        const demoTotal = document.getElementById('demoTotal');
        const demoResetBtn = document.getElementById('demoResetBtn');

        if(demoValidarBtn) {
            demoValidarBtn.addEventListener('click', () => {
                const cedula = demoCedula.value.trim();

                demoStatus.innerHTML = `<i class="ph ph-spinner ph-spin" style="font-size: 1.5rem; color: var(--gold);"></i><p style="color: var(--text-main); font-size: 0.9rem; margin: 0;">Conectando con base de datos...</p>`;

                setTimeout(() => {
                    if(cedula.length > 3) {
                        // Simular éxito
                        demoStatus.innerHTML = `<i class="ph ph-check-circle" style="font-size: 2rem; color: #4ade80;"></i>
                        <div>
                            <p style="color: #4ade80; font-weight: 600; margin: 0; font-size: 1rem;">Asociado Validado</p>
                            <p style="color: var(--text-muted); font-size: 0.8rem; margin: 0;">Federación de Cafeteros - Activo</p>
                        </div>`;
                        demoStatus.style.borderColor = "rgba(74, 222, 128, 0.3)";
                        demoStatus.style.background = "rgba(74, 222, 128, 0.05)";

                        demoDiscountRow.style.opacity = "1";
                        demoDiscountAmount.textContent = "-$12.000";
                        demoTotal.textContent = "$108.000";
                        demoTotal.style.color = "#4ade80";
                    } else {
                        // Simular error
                        demoStatus.innerHTML = `<i class="ph ph-warning-circle" style="font-size: 2rem; color: #f87171;"></i>
                        <div>
                            <p style="color: #f87171; font-weight: 600; margin: 0; font-size: 1rem;">Cédula no encontrada</p>
                            <p style="color: var(--text-muted); font-size: 0.8rem; margin: 0;">Intente de nuevo (ej. 123456)</p>
                        </div>`;
                        demoStatus.style.borderColor = "rgba(248, 113, 113, 0.3)";
                        demoStatus.style.background = "rgba(248, 113, 113, 0.05)";
                    }
                }, 1200);
            });

            demoResetBtn.addEventListener('click', () => {
                demoCedula.value = "";
                demoStatus.innerHTML = `<i class="ph ph-info" style="font-size: 1.5rem; color: var(--text-muted);"></i><p style="color: var(--text-muted); font-size: 0.9rem; margin: 0;">Esperando validación de documento...</p>`;
                demoStatus.style.borderColor = "rgba(255,255,255,0.05)";
                demoStatus.style.background = "rgba(20,21,25,0.5)";

                demoDiscountRow.style.opacity = "0.3";
                demoDiscountAmount.textContent = "-$0";
                demoTotal.textContent = "$120.000";
                demoTotal.style.color = "var(--text-main)";
            });
        }

        // Optimización Premium de UX: Lazy Loading Inteligente para Videos'''

content = content.replace(js_search, js_replace)


with open('asociados.html', 'w') as f:
    f.write(content)
