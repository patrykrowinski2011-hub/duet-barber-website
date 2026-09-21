from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Studio Fryzjerskie Duet & Duet Barber | Fryzjer Piaseczno</title>
    <meta name="description" content="Studio Fryzjerskie Duet & Duet Barber w Piasecznie. Fryzjer damski, męski, barber, strzyżenia, koloryzacja i stylizacja. Umów wizytę online.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg-dark: #0f1115;
            --bg-card: #181b20;
            --bg-card-hover: #22262d;
            --accent-gold: #c5a059;
            --accent-gold-hover: #d4af37;
            --text-light: #f3f4f6;
            --text-muted: #9ca3af;
            --border-color: #2a2f38;
            --font-heading: 'Cinzel', serif;
            --font-body: 'Montserrat', sans-serif;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-light);
            font-family: var(--font-body);
            line-height: 1.6;
            padding-bottom: 70px; /* Miejsce na mobilny pasek CTA */
        }

        @media (min-width: 992px) {
            body { padding-bottom: 0; }
        }

        /* NAGŁÓWEK I NAWIGACJA */
        header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: rgba(15, 17, 21, 0.92);
            backdrop-filter: blur(10px);
            z-index: 1000;
            border-bottom: 1px solid var(--border-color);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-family: var(--font-heading);
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-light);
            text-decoration: none;
            letter-spacing: 1px;
        }

        .logo span { color: var(--accent-gold); }

        .nav-links {
            display: none;
            gap: 25px;
            list-style: none;
        }

        .nav-links a {
            color: var(--text-light);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover { color: var(--accent-gold); }

        @media (min-width: 992px) {
            .nav-links { display: flex; }
        }

        .btn-header {
            background: var(--accent-gold);
            color: #000;
            padding: 10px 20px;
            border-radius: 4px;
            font-weight: 600;
            text-decoration: none;
            font-size: 0.85rem;
            transition: background 0.3s;
        }

        .btn-header:hover { background: var(--accent-gold-hover); }

        /* HERO SEKCJA */
        .hero {
            position: relative;
            min-height: 90vh;
            background: linear-gradient(rgba(15, 17, 21, 0.75), rgba(15, 17, 21, 0.9)), 
                        url('https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 120px 20px 60px 20px;
        }

        .hero-content {
            max-width: 800px;
        }

        .hero h1 {
            font-family: var(--font-heading);
            font-size: 2.2rem;
            color: var(--text-light);
            margin-bottom: 10px;
            letter-spacing: 1px;
        }

        .hero .subtitle {
            font-size: 1.1rem;
            color: var(--accent-gold);
            margin-bottom: 20px;
            font-weight: 500;
        }

        .hero p {
            font-size: 1rem;
            color: var(--text-muted);
            margin-bottom: 30px;
            max-width: 650px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-buttons {
            display: flex;
            flex-direction: column;
            gap: 15px;
            justify-content: center;
            margin-bottom: 25px;
        }

        @media (min-width: 576px) {
            .hero h1 { font-size: 3.2rem; }
            .hero-buttons { flex-direction: row; }
        }

        .btn-primary {
            background: var(--accent-gold);
            color: #000;
            padding: 14px 32px;
            border-radius: 4px;
            font-weight: 700;
            text-decoration: none;
            letter-spacing: 1px;
            transition: all 0.3s;
        }

        .btn-primary:hover {
            background: var(--accent-gold-hover);
            transform: translateY(-2px);
        }

        .btn-secondary {
            border: 1px solid var(--accent-gold);
            color: var(--accent-gold);
            padding: 14px 32px;
            border-radius: 4px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s;
        }

        .btn-secondary:hover {
            background: rgba(197, 160, 89, 0.1);
        }

        .hero-location {
            font-size: 0.9rem;
            color: var(--text-muted);
            letter-spacing: 1px;
        }

        /* BELKA ZAUFANIA */
        .trust-bar {
            background: var(--bg-card);
            border-y: 1px solid var(--border-color);
            padding: 25px 20px;
        }

        .trust-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            text-align: center;
        }

        @media (min-width: 768px) {
            .trust-container { grid-template-columns: repeat(4, 1fr); }
        }

        .trust-item h4 {
            font-family: var(--font-heading);
            color: var(--accent-gold);
            font-size: 1.1rem;
            margin-bottom: 5px;
        }

        .trust-item p {
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        /* SEKCJE METADANE */
        .section {
            padding: 80px 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-title h2 {
            font-family: var(--font-heading);
            font-size: 2rem;
            color: var(--text-light);
            margin-bottom: 10px;
        }

        .section-title p {
            color: var(--accent-gold);
            font-size: 0.95rem;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        /* POZNAJ DUET */
        .about-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 40px;
            align-items: center;
        }

        @media (min-width: 992px) {
            .about-grid { grid-template-columns: 1fr 1fr; }
        }

        .about-img {
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }

        .about-text h3 {
            font-family: var(--font-heading);
            font-size: 1.6rem;
            color: var(--text-light);
            margin-bottom: 20px;
        }

        .about-text p {
            color: var(--text-muted);
            margin-bottom: 15px;
        }

        /* CENNIK I USŁUGI */
        .pricing-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 30px;
        }

        @media (min-width: 768px) {
            .pricing-grid { grid-template-columns: 1fr 1fr; }
        }

        .price-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            padding: 30px;
            border-radius: 8px;
        }

        .price-card h3 {
            font-family: var(--font-heading);
            color: var(--accent-gold);
            font-size: 1.4rem;
            margin-bottom: 20px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
        }

        .price-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px dashed var(--border-color);
        }

        .price-item:last-child { border-bottom: none; }

        .price-name { font-weight: 500; }
        .price-val { color: var(--accent-gold); font-weight: 600; }

        /* DUET BARBER */
        .barber-section {
            background: linear-gradient(rgba(15, 17, 21, 0.85), rgba(15, 17, 21, 0.85)), 
                        url('https://images.unsplash.com/photo-1503951914875-452162b0f3f1?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
            border-y: 1px solid var(--border-color);
            padding: 80px 20px;
            text-align: center;
        }

        .barber-box {
            max-width: 700px;
            margin: 0 auto;
        }

        .barber-box h2 {
            font-family: var(--font-heading);
            font-size: 2.2rem;
            color: var(--text-light);
            margin-bottom: 15px;
        }

        .barber-box p {
            color: var(--text-muted);
            margin-bottom: 30px;
            font-size: 1.1rem;
        }

        /* GALERIA */
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .gallery-item img {
            width: 100%;
            height: 280px;
            object-fit: cover;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            transition: transform 0.3s;
        }

        .gallery-item img:hover {
            transform: scale(1.02);
        }

        /* KONTAKT */
        .contact-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 40px;
        }

        @media (min-width: 992px) {
            .contact-grid { grid-template-columns: 1fr 1fr; }
        }

        .contact-info {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            padding: 40px;
            border-radius: 8px;
        }

        .contact-info h3 {
            font-family: var(--font-heading);
            color: var(--accent-gold);
            font-size: 1.5rem;
            margin-bottom: 20px;
        }

        .contact-item {
            margin-bottom: 20px;
        }

        .contact-item strong { display: block; color: var(--text-light); }
        .contact-item span { color: var(--text-muted); }

        .map-frame {
            width: 100%;
            height: 100%;
            min-height: 350px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }

        /* MOBILNE STICKY CTA */
        .mobile-sticky-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: var(--bg-card);
            border-top: 1px solid var(--border-color);
            display: flex;
            padding: 10px;
            gap: 10px;
            z-index: 1000;
        }

        @media (min-width: 992px) {
            .mobile-sticky-bar { display: none; }
        }

        .mobile-sticky-bar a {
            flex: 1;
            text-align: center;
            padding: 12px;
            border-radius: 4px;
            font-weight: 700;
            text-decoration: none;
            font-size: 0.9rem;
        }

        /* FOOTER */
        footer {
            background: #08090b;
            border-top: 1px solid var(--border-color);
            padding: 40px 20px;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.85rem;
        }

        footer p { margin-bottom: 10px; }
    </style>
</head>
<body>

    <!-- HEADER -->
    <header>
        <div class="nav-container">
            <a href="#" class="logo">DUET <span>& BARBER</span></a>
            <ul class="nav-links">
                <li><a href="#about">Poznaj Duet</a></li>
                <li><a href="#uslugi">Usługi</a></li>
                <li><a href="#cennik">Cennik</a></li>
                <li><a href="#barber">Duet Barber</a></li>
                <li><a href="#galeria">Galeria</a></li>
                <li><a href="#kontakt">Kontakt</a></li>
            </ul>
            <a href="https://booksy.com" target="_blank" class="btn-header">UMÓW WIZYTĘ</a>
        </div>
    </header>

    <!-- HERO -->
    <section class="hero">
        <div class="hero-content">
            <h1>Studio Fryzjerskie Duet & Duet Barber</h1>
            <div class="subtitle">Fryzjer damski, męski i barber w Piasecznie</div>
            <p>Profesjonalne strzyżenia, koloryzacja, stylizacja oraz usługi barberskie. Umów wizytę szybko i wygodnie online.</p>
            <div class="hero-buttons">
                <a href="https://booksy.com" target="_blank" class="btn-primary">UMÓW WIZYTĘ</a>
                <a href="tel:504443333" class="btn-secondary">ZADZWOŃ: 504 443 333</a>
            </div>
            <div class="hero-location">Piaseczno • ul. Jana Pawła II 19</div>
        </div>
    </section>

    <!-- BELKA ZAUFANIA -->
    <div class="trust-bar">
        <div class="trust-container">
            <div class="trust-item">
                <h4>Fryzjer Damski</h4>
                <p>Stylizacja & Koloryzacja</p>
            </div>
            <div class="trust-item">
                <h4>Fryzjer Męski</h4>
                <p>Precyzyjne Strzyżenia</p>
            </div>
            <div class="trust-item">
                <h4>Duet Barber</h4>
                <p>Broda & Stylizacja</p>
            </div>
            <div class="trust-item">
                <h4>Rezerwacja Online</h4>
                <p>Szybko przez Booksy</p>
            </div>
        </div>
    </div>

    <!-- POZNAJ DUET -->
    <section class="section" id="about">
        <div class="about-grid">
            <img src="https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?auto=format&fit=crop&w=800&q=80" alt="Wnętrze salonu Duet w Piasecznie" class="about-img">
            <div class="about-text">
                <div class="section-title" style="text-align: left; margin-bottom: 20px;">
                    <p>O Salonie</p>
                    <h2>Poznaj Duet</h2>
                </div>
                <p>W Studio Fryzjerskim Duet & Duet Barber stawiamy na profesjonalizm, indywidualne podejście oraz wyjątkową atmosferę.</p>
                <p>Nasz zespół dba o to, aby każda wizyta była chwilą relaksu, a efekt końcowy idealnie dopasowany do Twoich potrzeb i urody. Oferujemy pełen zakres usług fryzjerstwa damskiego, męskiego oraz tradycyjnego barberingu.</p>
            </div>
        </div>
    </section>

    <!-- CENNIK -->
    <section class="section" id="cennik">
        <div class="section-title">
            <p>Usługi i Oferta</p>
            <h2>Cennik</h2>
        </div>

        <div class="pricing-grid">
            <!-- MĘŻCZYŹNI -->
            <div class="price-card">
                <h3>Mężczyźni & Barber</h3>
                <div class="price-item">
                    <span class="price-name">Strzyżenie krótkich włosów</span>
                    <span class="price-val">85 – 90 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Strzyżenie średnich/długich włosów</span>
                    <span class="price-val">90 – 100 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Strzyżenie maszynką</span>
                    <span class="price-val">70 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Pielęgnacja & Strzyżenie Brody</span>
                    <span class="price-val">55 – 65 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Kombo: Strzyżenie + Broda</span>
                    <span class="price-val">140 – 165 zł</span>
                </div>
            </div>

            <!-- KOBIETY -->
            <div class="price-card">
                <h3>Kobiety</h3>
                <div class="price-item">
                    <span class="price-name">Strzyżenie średnich/długich włosów</span>
                    <span class="price-val">160 – 180 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Modelowanie krótkich/średnich włosów</span>
                    <span class="price-val">80 – 90 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Koloryzacja + stylizacja/strzyżenie</span>
                    <span class="price-val">320 – 670 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Balayage + stylizacja/strzyżenie</span>
                    <span class="price-val">380 – 780 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Rozjaśnianie balayage</span>
                    <span class="price-val">od ~500 zł</span>
                </div>
                <div class="price-item">
                    <span class="price-name">Hollywood Waves</span>
                    <span class="price-val">200 – 300 zł</span>
                </div>
            </div>
        </div>
        <p style="text-align: center; color: var(--text-muted); font-size: 0.85rem; margin-top: 25px;">
            * Ceny mogą zależeć od długości i kondycji włosów. Aktualne ceny i dostępne terminy znajdziesz podczas rezerwacji.
        </p>
    </section>

    <!-- DUET BARBER SEKCJA -->
    <section class="barber-section" id="barber">
        <div class="barber-box">
            <h2>DUET BARBER</h2>
            <p>Precyzyjne strzyżenie, stylizacja i pielęgnacja brody w nowoczesnym wydaniu.</p>
            <a href="https://booksy.com" target="_blank" class="btn-primary">UMÓW WIZYTĘ BARBER</a>
        </div>
    </section>

    <!-- GALERIA -->
    <section class="section" id="galeria">
        <div class="section-title">
            <p>Inspiracje</p>
            <h2>Galeria Realizacji</h2>
        </div>
        <div class="gallery-grid">
            <div class="gallery-item"><img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?auto=format&fit=crop&w=600&q=80" alt="Stylizacja damska"></div>
            <div class="gallery-item"><img src="https://images.unsplash.com/photo-1622286342621-4bd786c2447c?auto=format&fit=crop&w=600&q=80" alt="Strzyżenie męskie barber"></div>
            <div class="gallery-item"><img src="https://images.unsplash.com/photo-1595476108010-b4d1f102b1b1?auto=format&fit=crop&w=600&q=80" alt="Koloryzacja włosów"></div>
            <div class="gallery-item"><img src="https://images.unsplash.com/photo-1503951914875-452162b0f3f1?auto=format&fit=crop&w=600&q=80" alt="Pielęgnacja brody"></div>
        </div>
    </section>

    <!-- KONTAKT -->
    <section class="section" id="kontakt">
        <div class="section-title">
            <p>Lokalizacja</p>
            <h2>Kontakt</h2>
        </div>
        <div class="contact-grid">
            <div class="contact-info">
                <h3>Studio Fryzjerskie Duet & Duet Barber</h3>
                <div class="contact-item">
                    <strong>Adres:</strong>
                    <span>ul. Jana Pawła II 19, 05-500 Piaseczno</span>
                </div>
                <div class="contact-item">
                    <strong>Telefon:</strong>
                    <span>504 443 333</span>
                </div>
                <div class="contact-item">
                    <strong>Rezerwacja:</strong>
                    <span>Wygodnie online przez aplikację Booksy</span>
                </div>
                <div style="margin-top: 30px;">
                    <a href="https://booksy.com" target="_blank" class="btn-primary" style="display: inline-block; width: 100%; text-align: center; margin-bottom: 10px;">REZERWUJ W BOOKSY</a>
                    <a href="tel:504443333" class="btn-secondary" style="display: inline-block; width: 100%; text-align: center;">ZADZWOŃ TERAZ</a>
                </div>
            </div>
            <div>
                <!-- Mapa Google Piaseczno -->
                <iframe class="map-frame" src="https://maps.google.com/maps?q=Jana%20Paw%C5%82a%20II%2019%20Piaseczno&t=&z=15&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer>
        <p><strong>Studio Fryzjerskie Duet & Duet Barber</strong></p>
        <p>ul. Jana Pawła II 19 • 05-500 Piaseczno • Tel: 504 443 333</p>
        <p>&copy; 2026 Wszystkie prawa zastrzeżone.</p>
    </footer>

    <!-- STICKY BOTTOM BAR MOBILNY -->
    <div class="mobile-sticky-bar">
        <a href="https://booksy.com" target="_blank" class="btn-primary">UMÓW WIZYTĘ</a>
        <a href="tel:504443333" class="btn-secondary">ZADZWOŃ</a>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
