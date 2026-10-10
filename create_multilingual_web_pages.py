#!/usr/bin/env python3
"""
Generador de páginas web completas de Marketing y Soporte en Inglés, Alemán y Francés
para el repositorio PalletGrid-Web (GitHub Pages).
"""

import os

WEB_DIR = "/Users/joseantoniocorralesortega/Documents/App IOS/PalletGrid-Web"

# -------------------------------------------------------------
# 1. MARKETING ENGLSH (index-en.html / marketing-en.html)
# -------------------------------------------------------------
MARKETING_EN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PalletGrid — 3D Pallet Load Optimizer & Cargo Calculator</title>
  <meta name="description" content="PalletGrid is the professional logistics engineering tool for 3D pallet load optimization, ≥80% pattern calculations, UNE-EN 13698 norms, and official A4 PDF technical sheets.">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/app-icon.png">
</head>
<body>

  <!-- HEADER / NAVBAR -->
  <header class="navbar">
    <div class="container nav-wrap">
      <a href="index-en.html" class="nav-brand">
        <img src="assets/app-icon.png" alt="PalletGrid Icon" class="nav-logo">
        <div>
          <div class="nav-title">PalletGrid</div>
          <div class="nav-subtitle">by Jacoor Logistics</div>
        </div>
      </a>
      <ul class="nav-menu">
        <li><a href="#features" class="nav-link">Features</a></li>
        <li><a href="#standards" class="nav-link">Standards</a></li>
        <li><a href="#gallery" class="nav-link">Screenshots</a></li>
        <li><a href="support-en.html" class="nav-link">Support</a></li>
        <li><a href="privacy.html" class="nav-link">Privacy</a></li>
        <li>
          <span style="color: var(--primary-light); font-weight: 700; font-size: 13px;">🌐 EN</span>
          <a href="index.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">ES</a>
          <a href="index-de.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">DE</a>
          <a href="index-fr.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">FR</a>
        </li>
      </ul>
      <a href="#download" class="nav-btn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        App Store
      </a>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="hero">
    <div class="hero-glow"></div>
    <div class="container hero-grid">
      <div class="hero-content">
        <div class="hero-tag">
          <div class="hero-tag-pulse"></div>
          LOGISTICS INDUSTRIAL ENGINEERING V4
        </div>
        <h1 class="hero-title">
          3D Pallet Load Optimizer & <span>Cargo Planning</span>
        </h1>
        <p class="hero-lead">
          Calculate instant load patterns with ≥ 80% surface efficiency, simulate interlocking Layer B in interactive 3D, and generate official vector DIN A4 technical sheets for warehouse and freight operations.
        </p>
        <div class="hero-actions">
          <a href="#download" class="btn-primary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.84c.62-.75 1.04-1.8 1.01-2.84-.96.04-2.13.64-2.79 1.41-.58.68-1.1 1.77-1.02 2.81 1.08.08 2.18-.63 2.8-1.38z"/></svg>
            Available on App Store
          </a>
          <a href="support-en.html" class="btn-secondary">
            Support Center →
          </a>
        </div>
        <div class="hero-badges">
          <div class="badge-item">
            <span class="badge-val">≥ 80%</span>
            <span class="badge-lbl">Occupancy Filter</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">4 Types</span>
            <span class="badge-lbl">EUR, USA, 1/2 & Custom</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">7 Languages</span>
            <span class="badge-lbl">EN, ES, DE, FR, IT, PT, RU</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">100%</span>
            <span class="badge-lbl">Offline & Secure</span>
          </div>
        </div>
      </div>
      <div class="hero-mockup-wrap">
        <div class="hero-mockup-glow"></div>
        <img src="assets/01_Visor_3D_Explosion.png" alt="PalletGrid 3D Isometric Mockup" class="hero-mockup-img">
      </div>
    </div>
  </section>

  <!-- FEATURES SECTION -->
  <section class="section" id="features">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Technical Capabilities</span>
        <h2 class="section-title">Engineered for Demanding Supply Chains</h2>
        <p class="section-desc">Geometric calculation and physical simulation algorithms ensuring stable, compliant, and cost-effective pallet loads.</p>
      </div>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon-box">⭐</div>
          <h3 class="feature-title">Guided Setup Assistant</h3>
          <p class="feature-desc">Step-by-step workflow to configure products, box dimensions, net weight, and pallet selection with instant mm/in and kg/lb conversion.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📐</div>
          <h3 class="feature-title">Patterns with ≥ 80% Utilization</h3>
          <p class="feature-desc">Rigorous algorithm filtering out inefficient combinations. Generates longitudinal, transverse, 2-block and 3-block mixed layouts.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">🧱</div>
          <h3 class="feature-title">Automatic Layer B Interlocking</h3>
          <p class="feature-desc">Physical brick-bonding across alternate layers to prevent vertical cleavage and load shifting during road transport.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">🛡️</div>
          <h3 class="feature-title">Stability & Physical Audit</h3>
          <p class="feature-desc">Precise Center of Gravity Z (Z_cdg), slenderness ratio (λ ≤ 1.8), and static tipping angle (θ) verified against UNE-EN standards.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📦</div>
          <h3 class="feature-title">Clean 3D Isometric Viewer</h3>
          <p class="feature-desc">Touch 360° rotation with layer explosion slider in height. Focused solely on pallet timber and cargo boxes with zero distracting numbers.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📑</div>
          <h3 class="feature-title">Official A4 PDF Technical Sheet</h3>
          <p class="feature-desc">Generates warehouse dispatch dossiers ready to print via AirPrint, share via AirDrop, or archive with quality compliance stamp.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- STANDARDS SECTION -->
  <section class="section" id="standards" style="background: var(--bg-surface);">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">International Norms</span>
        <h2 class="section-title">Standard & Custom Pallet Support</h2>
        <p class="section-desc">PalletGrid integrates official dimensions, tare weights, and wood deck heights compliant with global logistics norms.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
        <div class="feature-card" style="border-color: rgba(16, 185, 129, 0.4);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🇪🇺</span>
            <span style="background: rgba(16, 185, 129, 0.15); color: var(--primary-light); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">EUROPEAN NORM</span>
          </div>
          <h3 class="feature-title">Euro Pallet UNE-EN 13698-1</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Standard EPAL pallet for European supply chain distribution.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Dimensions:</strong> 1200 × 800 mm</li>
            <li>✓ <strong>Wood height:</strong> 145 mm (3 skids & 9 blocks)</li>
            <li>✓ <strong>Official tare:</strong> 25.0 kg</li>
            <li>✓ <strong>Tolerance:</strong> Up to +20 mm overhang evaluable</li>
          </ul>
        </div>
        <div class="feature-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🇺🇸</span>
            <span style="background: rgba(255, 255, 255, 0.1); color: var(--text-main); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">GLOBAL NORM</span>
          </div>
          <h3 class="feature-title">American Pallet UNE-EN 13698-2</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Universal ISO 6780 industrial pallet for overseas container shipping.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Dimensions:</strong> 1200 × 1000 mm</li>
            <li>✓ <strong>Wood height:</strong> 150 mm</li>
            <li>✓ <strong>Official tare:</strong> 30.0 kg</li>
            <li>✓ <strong>Capacity:</strong> High volumetric density</li>
          </ul>
        </div>
        <div class="feature-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🏬</span>
            <span style="background: rgba(255, 255, 255, 0.1); color: var(--text-main); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">RETAIL / DISPLAY</span>
          </div>
          <h3 class="feature-title">Half Pallet (Display)</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Ideal for supermarket point-of-sale displays and urban micro-distribution.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Dimensions:</strong> 800 × 600 mm</li>
            <li>✓ <strong>Wood height:</strong> 140 mm</li>
            <li>✓ <strong>Official tare:</strong> 15.0 kg</li>
            <li>✓ <strong>Usage:</strong> Direct retail floor replenishment</li>
          </ul>
        </div>
        <div class="feature-card" style="border-color: rgba(16, 185, 129, 0.3);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">⚙️</span>
            <span style="background: rgba(16, 185, 129, 0.15); color: var(--primary-light); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">CUSTOM SPECS</span>
          </div>
          <h3 class="feature-title">Custom Pallet</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Configure any industrial or special size with zero catalog restrictions.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Length & Width:</strong> Freely adjustable in mm</li>
            <li>✓ <strong>Wood height:</strong> Fully customizable</li>
            <li>✓ <strong>Tare weight:</strong> Accurate custom base tare</li>
            <li>✓ <strong>Engine:</strong> Real-time 3D & pattern solver</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- GALLERY -->
  <section class="section" id="gallery">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">App Screenshots</span>
        <h2 class="section-title">PalletGrid V4 Interface</h2>
        <p class="section-desc">Designed specifically for warehouse operations and iOS / iPadOS native fluidity.</p>
      </div>
      <div class="gallery-wrap">
        <div class="gallery-card">
          <img src="assets/01_Visor_3D_Explosion.png" alt="3D Isometric Viewer" class="gallery-thumb">
          <div class="gallery-caption">Interactive 3D Viewer</div>
          <div class="gallery-sub">360° rotation & layer explosion</div>
        </div>
        <div class="gallery-card">
          <img src="assets/02_Dossier_Ficha_Tecnica_PDF.png" alt="A4 Technical PDF" class="gallery-thumb">
          <div class="gallery-caption">Official A4 PDF Sheet</div>
          <div class="gallery-sub">Stacking plans, elevations & seal</div>
        </div>
        <div class="gallery-card">
          <img src="assets/03_Mosaicos_2D_Ocupacion80.png" alt="2D Patterns" class="gallery-thumb">
          <div class="gallery-caption">2D Patterns (≥ 80%)</div>
          <div class="gallery-sub">Overhang solver & mm KPIs</div>
        </div>
        <div class="gallery-card">
          <img src="assets/04_Asistente_Guiado_Nuevo_Pallet.png" alt="Guided Assistant" class="gallery-thumb">
          <div class="gallery-caption">Guided Assistant</div>
          <div class="gallery-sub">mm/in, kg/lb & custom pallets</div>
        </div>
        <div class="gallery-card">
          <img src="assets/05_Gestor_Fichas_Guardadas.png" alt="Saved Pallet Sheets" class="gallery-thumb">
          <div class="gallery-caption">Saved Pallet Sheets</div>
          <div class="gallery-sub">Local archive & 3D reopen</div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section" id="download" style="text-align: center;">
    <div class="container">
      <div class="contact-box" style="margin: 0 auto;">
        <h3>Start optimizing your freight today</h3>
        <p>Available for iPhone and iPad on the Apple App Store. One-time purchase, no mandatory account, no ads, 100% private.</p>
        <a href="https://apps.apple.com" target="_blank" class="contact-mail-btn">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.84c.62-.75 1.04-1.8 1.01-2.84-.96.04-2.13.64-2.79 1.41-.58.68-1.1 1.77-1.02 2.81 1.08.08 2.18-.63 2.8-1.38z"/></svg>
          Download on App Store
        </a>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="nav-brand">
            <img src="assets/app-icon.png" alt="PalletGrid Logo" class="nav-logo">
            <div>
              <div class="nav-title">PalletGrid</div>
              <div class="nav-subtitle">by Jacoor Logistics</div>
            </div>
          </div>
          <p>Professional engineering tool for cargo stacking, volumetric optimization, and pallet standardization in transport & logistics.</p>
        </div>
        <div class="footer-col">
          <h4>Navigation</h4>
          <ul>
            <li><a href="#features">Features</a></li>
            <li><a href="#standards">Standards</a></li>
            <li><a href="#gallery">Screenshots</a></li>
            <li><a href="#download">App Store</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Legal & Support</h4>
          <ul>
            <li><a href="support-en.html">Support Center</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="mailto:ayeneso2023@gmail.com">Contact Email</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 Jacoor Logistics. All rights reserved.</div>
        <div>Compliant with Apple App Store Review Guidelines.</div>
      </div>
    </div>
  </footer>

</body>
</html>
"""

# -------------------------------------------------------------
# 2. SUPPORT ENGLISH (support-en.html)
# -------------------------------------------------------------
SUPPORT_EN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Official Support — PalletGrid</title>
  <meta name="description" content="Official technical support center, assistance and FAQ for PalletGrid on iOS & iPadOS.">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/app-icon.png">
</head>
<body>

  <!-- HEADER -->
  <header class="navbar">
    <div class="container nav-wrap">
      <a href="index-en.html" class="nav-brand">
        <img src="assets/app-icon.png" alt="PalletGrid Icon" class="nav-logo">
        <div>
          <div class="nav-title">PalletGrid</div>
          <div class="nav-subtitle">Support Center</div>
        </div>
      </a>
      <ul class="nav-menu">
        <li><a href="index-en.html" class="nav-link">Home / Marketing</a></li>
        <li><a href="support-en.html" class="nav-link active">Support</a></li>
        <li><a href="privacy.html" class="nav-link">Privacy</a></li>
        <li>
          <span style="color: var(--primary-light); font-weight: 700; font-size: 13px;">🌐 EN</span>
          <a href="soporte.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">ES</a>
          <a href="support-de.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">DE</a>
          <a href="support-fr.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">FR</a>
        </li>
      </ul>
      <a href="index-en.html#download" class="nav-btn">
        App Store
      </a>
    </div>
  </header>

  <!-- SUPPORT CONTENT -->
  <main class="legal-page">
    <div class="container">
      <div class="legal-header">
        <span class="section-tag">Official Help & Contact</span>
        <h1 class="legal-title">How can we assist you with PalletGrid?</h1>
        <p class="legal-meta">Official user help desk and technical incident resolution • Developed by Jacoor Logistics</p>
      </div>

      <!-- DIRECT CONTACT CARD -->
      <div class="contact-box" style="margin: 0 0 60px 0; text-align: left; display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 32px; align-items: center;">
        <div>
          <h2 style="font-size: 26px; font-weight: 900; margin-bottom: 12px; color: #FFFFFF;">Direct Technical Support</h2>
          <p style="color: var(--text-muted); font-size: 15px; margin-bottom: 20px;">
            Whether you have operational questions, need to report an edge case, or require help with pallet sheet compliance, our engineering support team is here to assist you.
          </p>
          <div style="color: var(--text-main); font-size: 14px; line-height: 2;">
            <div>📧 <strong>Support Email:</strong> <a href="mailto:ayeneso2023@gmail.com?subject=PalletGrid%20Support%20iOS" style="color: var(--primary-light); text-decoration: underline;">ayeneso2023@gmail.com</a></div>
            <div>⏱️ <strong>Estimated Response Time:</strong> Under 24 business hours.</div>
            <div>🏢 <strong>Developer / Rights Holder:</strong> Jose Antonio Corrales Ortega (Jacoor Logistics)</div>
          </div>
        </div>
        <div style="text-align: center;">
          <a href="mailto:ayeneso2023@gmail.com?subject=PalletGrid%20Support%20iOS" class="contact-mail-btn" style="width: 100%; justify-content: center;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            Email Support Team
          </a>
        </div>
      </div>

      <!-- FAQ SECTION -->
      <div class="legal-body">
        <h2 style="font-size: 28px; margin-bottom: 24px;">Frequently Asked Questions (FAQ)</h2>
        <div class="faq-list">
          <div class="faq-item">
            <h3 class="faq-q"><span>Q1.</span> What pallet standards and custom sizes are supported?</h3>
            <p class="faq-a">
              PalletGrid natively supports:
              <br>• <strong>Euro Pallet UNE-EN 13698-1</strong> (1200 × 800 mm, wood 145 mm, tare 25.0 kg).
              <br>• <strong>American / ISO Pallet UNE-EN 13698-2</strong> (1200 × 1000 mm, wood 150 mm, tare 30.0 kg).
              <br>• <strong>Half Pallet (Display)</strong> (800 × 600 mm, wood 140 mm, tare 15.0 kg).
              <br>• <strong>Custom Pallets:</strong> Input any length, width, wood deck height, and tare weight.
              <br>Includes instantaneous conversion between millimeters ⇄ inches and kilograms ⇄ pounds.
            </p>
          </div>

          <div class="faq-item">
            <h3 class="faq-q"><span>Q2.</span> Why do some patterns display a ⚠️ badge with overhang mm?</h3>
            <p class="faq-a">
              In real-world logistics, certain box geometries slightly exceed standard pallet edges. When you enable the <em>"Allow overhang up to +20 mm"</em> toggle, our solver evaluates high-efficiency patterns that make use of that margin. The ⚠️ badge specifies exact overhang on length and width so the warehouse supervisor can approve it against trailer or rack clearances.
            </p>
          </div>

          <div class="faq-item">
            <h3 class="faq-q"><span>Q3.</span> What is Layer B and why is interlocking necessary?</h3>
            <p class="faq-a">
              Stacking boxes identically layer over layer creates continuous vertical columns prone to tipping under road vibration or braking. <strong>Interlocked Layer B</strong> rotates or mirrors the layout on even floors, brick-bonding the stack into a cohesive structural unit.
            </p>
          </div>

          <div class="faq-item">
            <h3 class="faq-q"><span>Q4.</span> How do I export or print the official PDF Technical Sheet?</h3>
            <p class="faq-a">
              From the <em>Technical Sheet</em> tab, tap <strong>"Download PDF Sheet"</strong>. The native iOS / iPadOS share sheet will open, allowing you to:
              <br>• Print via <strong>AirPrint</strong> directly to any network printer.
              <br>• Share via <strong>AirDrop</strong> to Mac or nearby devices.
              <br>• Send as an attachment via Mail, WhatsApp, or cloud storage (Files, iCloud Drive).
            </p>
          </div>

          <div class="faq-item">
            <h3 class="faq-q"><span>Q5.</span> Does PalletGrid require an internet connection or user account?</h3>
            <p class="faq-a">
              <strong>No.</strong> PalletGrid is 100% offline and operates entirely on your device. All calculations, 3D simulations, and saved technical sheets remain confidential on your iPhone or iPad. No telemetry, no third-party tracking, and zero advertising.
            </p>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container footer-bottom" style="border: none;">
      <div>© 2026 Jacoor Logistics. All rights reserved.</div>
      <div>Support & Inquiries: ayeneso2023@gmail.com</div>
    </div>
  </footer>

</body>
</html>
"""

# -------------------------------------------------------------
# 3. MARKETING GERMAN (index-de.html / marketing-de.html)
# -------------------------------------------------------------
MARKETING_DE = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PalletGrid — 3D-Palettenrechner & Ladungsoptimierung</title>
  <meta name="description" content="PalletGrid ist das professionelle Logistik-Engineering-Tool für 3D-Palettenoptimierung, Packmuster ≥80%, DIN EN 13698 und offizielle A4 PDF-Palettenscheine.">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/app-icon.png">
</head>
<body>

  <!-- HEADER / NAVBAR -->
  <header class="navbar">
    <div class="container nav-wrap">
      <a href="index-de.html" class="nav-brand">
        <img src="assets/app-icon.png" alt="PalletGrid Icon" class="nav-logo">
        <div>
          <div class="nav-title">PalletGrid</div>
          <div class="nav-subtitle">von Jacoor Logistik</div>
        </div>
      </a>
      <ul class="nav-menu">
        <li><a href="#features" class="nav-link">Funktionen</a></li>
        <li><a href="#standards" class="nav-link">Normen</a></li>
        <li><a href="#gallery" class="nav-link">Screenshots</a></li>
        <li><a href="support-de.html" class="nav-link">Support</a></li>
        <li><a href="privacy.html" class="nav-link">Datenschutz</a></li>
        <li>
          <span style="color: var(--primary-light); font-weight: 700; font-size: 13px;">🌐 DE</span>
          <a href="index.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">ES</a>
          <a href="index-en.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">EN</a>
          <a href="index-fr.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">FR</a>
        </li>
      </ul>
      <a href="#download" class="nav-btn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        App Store
      </a>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="hero">
    <div class="hero-glow"></div>
    <div class="container hero-grid">
      <div class="hero-content">
        <div class="hero-tag">
          <div class="hero-tag-pulse"></div>
          INDUSTRIELLES LOGISTIK-ENGINEERING V4
        </div>
        <h1 class="hero-title">
          3D-Palettenrechner & <span>Ladungsoptimierung</span>
        </h1>
        <p class="hero-lead">
          Berechnen Sie sofort Packmuster mit ≥ 80% Flächenausnutzung, simulieren Sie den Schichtverbund in interaktivem 3D und erstellen Sie offizielle vektorielle DIN A4-Palettenscheine für Lager und Frachtverkehr.
        </p>
        <div class="hero-actions">
          <a href="#download" class="btn-primary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.84c.62-.75 1.04-1.8 1.01-2.84-.96.04-2.13.64-2.79 1.41-.58.68-1.1 1.77-1.02 2.81 1.08.08 2.18-.63 2.8-1.38z"/></svg>
            Im App Store laden
          </a>
          <a href="support-de.html" class="btn-secondary">
            Support-Zentrum →
          </a>
        </div>
        <div class="hero-badges">
          <div class="badge-item">
            <span class="badge-val">≥ 80%</span>
            <span class="badge-lbl">Ausnutzungsfilter</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">4 Typen</span>
            <span class="badge-lbl">EUR, USA, Halb & Maß</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">7 Sprachen</span>
            <span class="badge-lbl">DE, EN, ES, FR, IT, PT, RU</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">100%</span>
            <span class="badge-lbl">Offline & Sicher</span>
          </div>
        </div>
      </div>
      <div class="hero-mockup-wrap">
        <div class="hero-mockup-glow"></div>
        <img src="assets/01_Visor_3D_Explosion.png" alt="PalletGrid 3D Isometrische Ansicht" class="hero-mockup-img">
      </div>
    </div>
  </section>

  <!-- FEATURES SECTION -->
  <section class="section" id="features">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Technische Leistungsmerkmale</span>
        <h2 class="section-title">Entwickelt für anspruchsvolle Lieferketten</h2>
        <p class="section-desc">Geometrische Berechnungs- und Physik-Simulationsalgorithmen für stabile, normgerechte und kosteneffiziente Palettenladungen.</p>
      </div>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon-box">⭐</div>
          <h3 class="feature-title">Geführter Konfigurations-Assistent</h3>
          <p class="feature-desc">Schrittweiser Ablauf zur Eingabe von Kartonmaßen, Eigengewicht und Palettenauswahl mit direkter mm/Zoll- und kg/Pfund-Umrechnung.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📐</div>
          <h3 class="feature-title">Packmuster mit ≥ 80% Ausnutzung</h3>
          <p class="feature-desc">Strenger Filter gegen ineffiziente Muster. Berechnet Längs-, Quer-, 2- und 3-Block- sowie Windmühlenmuster.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">🧱</div>
          <h3 class="feature-title">Automatischer Schichtverbund (Lage B)</h3>
          <p class="feature-desc">Kreuzung der Stoßfugen zwischen ungeraden und geraden Lagen zur Vermeidung von Ladungsverschiebungen während des Transports.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">🛡️</div>
          <h3 class="feature-title">Stabilitätsprüfung & Physikalisches Audit</h3>
          <p class="feature-desc">Exakte Berechnung des Schwerpunkts Z, des Schlankheitsgrades (λ ≤ 1,8) und des statischen Kippwinkels (θ) nach DIN EN-Normen.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📦</div>
          <h3 class="feature-title">3D-Isometrischer Betrachter</h3>
          <p class="feature-desc">360°-Touch-Drehung mit Höhenexplosions-Schieberegler zur schichtweisen visuellen Inspektion ohne störende Ziffern.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📑</div>
          <h3 class="feature-title">Offizieller DIN A4 PDF-Palettenschein</h3>
          <p class="feature-desc">Erstellt versandfertige Vektor-Dossiers für Lager und Spedition, druckbar via AirPrint oder teilbar via AirDrop.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- STANDARDS -->
  <section class="section" id="standards" style="background: var(--bg-surface);">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Internationale Standards</span>
        <h2 class="section-title">Norm- und Maßpaletten-Unterstützung</h2>
        <p class="section-desc">PalletGrid integriert offizielle Maße, Taragewichte und Holzhöhen nach weltweiten Logistikstandards.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
        <div class="feature-card" style="border-color: rgba(16, 185, 129, 0.4);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🇪🇺</span>
            <span style="background: rgba(16, 185, 129, 0.15); color: var(--primary-light); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">EUROPÄISCHE NORM</span>
          </div>
          <h3 class="feature-title">Europalette DIN EN 13698-1</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Homologierte EPAL-Palette für die europäische Logistikkette.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Nennmaße:</strong> 1200 × 800 mm</li>
            <li>✓ <strong>Holzhöhe:</strong> 145 mm (3 Kufen & 9 Klötze)</li>
            <li>✓ <strong>Tara:</strong> 25,0 kg</li>
            <li>✓ <strong>Toleranz:</strong> Bis zu +20 mm Überhang bewertbar</li>
          </ul>
        </div>
        <div class="feature-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🇺🇸</span>
            <span style="background: rgba(255, 255, 255, 0.1); color: var(--text-main); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">GLOBALER STANDARD</span>
          </div>
          <h3 class="feature-title">US-Industriepalette DIN EN 13698-2</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">ISO 6780 Industriepalette für den internationalen Übersee- und Containertransport.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Nennmaße:</strong> 1200 × 1000 mm</li>
            <li>✓ <strong>Holzhöhe:</strong> 150 mm</li>
            <li>✓ <strong>Tara:</strong> 30,0 kg</li>
            <li>✓ <strong>Kapazität:</strong> Hohe volumetrische Dichte</li>
          </ul>
        </div>
        <div class="feature-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🏬</span>
            <span style="background: rgba(255, 255, 255, 0.1); color: var(--text-main); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">RETAIL / DISPLAY</span>
          </div>
          <h3 class="feature-title">Halbpalette (Display)</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Ideal für POS-Aufsteller und urbane Feinverteilung im Lebensmitteleinzelhandel.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Nennmaße:</strong> 800 × 600 mm</li>
            <li>✓ <strong>Holzhöhe:</strong> 140 mm</li>
            <li>✓ <strong>Tara:</strong> 15,0 kg</li>
            <li>✓ <strong>Einsatz:</strong> Direkte Filialplatzierung</li>
          </ul>
        </div>
        <div class="feature-card" style="border-color: rgba(16, 185, 129, 0.3);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">⚙️</span>
            <span style="background: rgba(16, 185, 129, 0.15); color: var(--primary-light); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">MAßANFERTIGUNG</span>
          </div>
          <h3 class="feature-title">Maßpalette</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Konfigurieren Sie Sondermaße ohne jegliche Einschränkungen.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Länge & Breite:</strong> Frei in mm wählbar</li>
            <li>✓ <strong>Holzhöhe:</strong> Frei konfigurierbar</li>
            <li>✓ <strong>Taragewicht:</strong> Exaktes Leergewicht</li>
            <li>✓ <strong>Berechnung:</strong> Echtzeit-3D & Solver</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- GALLERY -->
  <section class="section" id="gallery">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">App-Screenshots</span>
        <h2 class="section-title">PalletGrid V4 Benutzeroberfläche</h2>
        <p class="section-desc">Optimiert für den operativen Lageralltag auf iPhone und iPad.</p>
      </div>
      <div class="gallery-wrap">
        <div class="gallery-card">
          <img src="assets/01_Visor_3D_Explosion.png" alt="3D-Isometrischer Betrachter" class="gallery-thumb">
          <div class="gallery-caption">3D-Betrachter</div>
          <div class="gallery-sub">360°-Drehung & Schichtzerlegung</div>
        </div>
        <div class="gallery-card">
          <img src="assets/02_Dossier_Ficha_Tecnica_PDF.png" alt="A4 PDF-Palettenschein" class="gallery-thumb">
          <div class="gallery-caption">PDF-Palettenschein</div>
          <div class="gallery-sub">Packmuster, Aufrisse & Siegel</div>
        </div>
        <div class="gallery-card">
          <img src="assets/03_Mosaicos_2D_Ocupacion80.png" alt="2D-Packmuster" class="gallery-thumb">
          <div class="gallery-caption">2D-Packmuster (≥ 80%)</div>
          <div class="gallery-sub">Überhangkontrolle & Kennzahlen</div>
        </div>
        <div class="gallery-card">
          <img src="assets/04_Asistente_Guiado_Nuevo_Pallet.png" alt="Geführter Assistent" class="gallery-thumb">
          <div class="gallery-caption">Geführter Assistent</div>
          <div class="gallery-sub">mm/in, kg/lb & Maßpaletten</div>
        </div>
        <div class="gallery-card">
          <img src="assets/05_Gestor_Fichas_Guardadas.png" alt="Gespeicherte Scheine" class="gallery-thumb">
          <div class="gallery-caption">Gespeicherte Scheine</div>
          <div class="gallery-sub">Lokales Archiv & 3D-Ansicht</div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section" id="download" style="text-align: center;">
    <div class="container">
      <div class="contact-box" style="margin: 0 auto;">
        <h3>Optimieren Sie Ihre Frachtkosten ab heute</h3>
        <p>Erhältlich für iPhone und iPad im Apple App Store. Einmalkauf, ohne Registrierung, werbefrei, 100% datensicher.</p>
        <a href="https://apps.apple.com" target="_blank" class="contact-mail-btn">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.84c.62-.75 1.04-1.8 1.01-2.84-.96.04-2.13.64-2.79 1.41-.58.68-1.1 1.77-1.02 2.81 1.08.08 2.18-.63 2.8-1.38z"/></svg>
          Im App Store laden
        </a>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="nav-brand">
            <img src="assets/app-icon.png" alt="PalletGrid Logo" class="nav-logo">
            <div>
              <div class="nav-title">PalletGrid</div>
              <div class="nav-subtitle">von Jacoor Logistik</div>
            </div>
          </div>
          <p>Technisches Engineering-Tool für Ladungsstauung, volumetrische Optimierung und Palettenstandardisierung in Transport & Logistik.</p>
        </div>
        <div class="footer-col">
          <h4>Navigation</h4>
          <ul>
            <li><a href="#features">Funktionen</a></li>
            <li><a href="#standards">Normen</a></li>
            <li><a href="#gallery">Screenshots</a></li>
            <li><a href="#download">App Store</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Rechtliches & Support</h4>
          <ul>
            <li><a href="support-de.html">Support-Zentrum</a></li>
            <li><a href="privacy.html">Datenschutzerklärung</a></li>
            <li><a href="mailto:ayeneso2023@gmail.com">Kontakt per E-Mail</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 Jacoor Logistik. Alle Rechte vorbehalten.</div>
        <div>Erfüllt die Richtlinien des Apple App Store Review.</div>
      </div>
    </div>
  </footer>

</body>
</html>
"""

# -------------------------------------------------------------
# 4. SUPPORT GERMAN (support-de.html)
# -------------------------------------------------------------
SUPPORT_DE = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Offizieller Support — PalletGrid</title>
  <meta name="description" content="Offizielles Support-Zentrum, technischer Kundendienst und FAQ für PalletGrid auf iOS & iPadOS.">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/app-icon.png">
</head>
<body>

  <!-- HEADER -->
  <header class="navbar">
    <div class="container nav-wrap">
      <a href="index-de.html" class="nav-brand">
        <img src="assets/app-icon.png" alt="PalletGrid Icon" class="nav-logo">
        <div>
          <div class="nav-title">PalletGrid</div>
          <div class="nav-subtitle">Support-Zentrum</div>
        </div>
      </a>
      <ul class="nav-menu">
        <li><a href="index-de.html" class="nav-link">Startseite / Marketing</a></li>
        <li><a href="support-de.html" class="nav-link active">Support</a></li>
        <li><a href="privacy.html" class="nav-link">Datenschutz</a></li>
        <li>
          <span style="color: var(--primary-light); font-weight: 700; font-size: 13px;">🌐 DE</span>
          <a href="soporte.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">ES</a>
          <a href="support-en.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">EN</a>
          <a href="support-fr.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">FR</a>
        </li>
      </ul>
      <a href="index-de.html#download" class="nav-btn">
        App Store
      </a>
    </div>
  </header>

  <!-- CONTENT -->
  <main class="legal-page">
    <div class="container">
      <div class="legal-header">
        <span class="section-tag">Offizieller Kundendienst & Kontakt</span>
        <h1 class="legal-title">Wie können wir Ihnen bei PalletGrid helfen?</h1>
        <p class="legal-meta">Offizielle Anlaufstelle für Benutzerhilfe und technische Fragen • Entwickelt von Jacoor Logistik</p>
      </div>

      <!-- DIRECT CONTACT CARD -->
      <div class="contact-box" style="margin: 0 0 60px 0; text-align: left; display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 32px; align-items: center;">
        <div>
          <h2 style="font-size: 26px; font-weight: 900; margin-bottom: 12px; color: #FFFFFF;">Direkter technischer Support</h2>
          <p style="color: var(--text-muted); font-size: 15px; margin-bottom: 20px;">
            Ob Sie betriebliche Fragen haben, ein Problem melden möchten oder Hilfe bei der Normkonformität Ihrer Palettenscheine benötigen – unser technisches Support-Team steht Ihnen gerne zur Seite.
          </p>
          <div style="color: var(--text-main); font-size: 14px; line-height: 2;">
            <div>📧 <strong>Support-E-Mail:</strong> <a href="mailto:ayeneso2023@gmail.com?subject=PalletGrid%20Support%20iOS%20DE" style="color: var(--primary-light); text-decoration: underline;">ayeneso2023@gmail.com</a></div>
            <div>⏱️ <strong>Geschätzte Antwortzeit:</strong> Innerhalb von 24 Arbeitsstunden.</div>
            <div>🏢 <strong>Entwickler / Rechteinhaber:</strong> Jose Antonio Corrales Ortega (Jacoor Logistik)</div>
          </div>
        </div>
        <div style="text-align: center;">
          <a href="mailto:ayeneso2023@gmail.com?subject=PalletGrid%20Support%20iOS%20DE" class="contact-mail-btn" style="width: 100%; justify-content: center;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            Support kontaktieren
          </a>
        </div>
      </div>

      <!-- FAQ -->
      <div class="legal-body">
        <h2 style="font-size: 28px; margin-bottom: 24px;">Häufig gestellte Fragen (FAQ)</h2>
        <div class="faq-list">
          <div class="faq-item">
            <h3 class="faq-q"><span>Q1.</span> Welche Palettennormen und Sondermaße werden unterstützt?</h3>
            <p class="faq-a">
              PalletGrid unterstützt nativ:
              <br>• <strong>Europalette DIN EN 13698-1</strong> (1200 × 800 mm, Holzhöhe 145 mm, Tara 25,0 kg).
              <br>• <strong>US-/Industriepalette DIN EN 13698-2</strong> (1200 × 1000 mm, Holzhöhe 150 mm, Tara 30,0 kg).
              <br>• <strong>Halbpalette (Display)</strong> (800 × 600 mm, Holzhöhe 140 mm, Tara 15,0 kg).
              <br>• <strong>Maßpaletten:</strong> Beliebige Eingabe von Länge, Breite, Holzhöhe und Taragewicht.
              <br>Inklusive direkter Umrechnung zwischen Millimetern ⇄ Zoll und Kilogramm ⇄ Pfund.
            </p>
          </div>
          <div class="faq-item">
            <h3 class="faq-q"><span>Q2.</span> Warum zeigen einige Packmuster ein ⚠️ Symbol mit Überhang in mm?</h3>
            <p class="faq-a">
              In der logistischen Praxis stehen manche Kartons leicht über das Palettenmaß hinaus. Wenn Sie die Option <em>"Überhang bis zu +20 mm zulassen"</em> aktivieren, berechnet das System hocheffiziente Varianten, die diesen Spielraum nutzen. Das ⚠️ Symbol zeigt den genauen Überhang auf Länge und Breite an, damit der Verlademeister entscheiden kann, ob dies für LKW oder Hochregal zulässig ist.
            </p>
          </div>
          <div class="faq-item">
            <h3 class="faq-q"><span>Q3.</span> Was ist Lage B und warum ist der Schichtverbund wichtig?</h3>
            <p class="faq-a">
              Wenn Kartons Lage für Lage im identischen Muster gestapelt werden, entstehen durchgehende vertikale Fugen (Säulenbildung), die bei Bremsmanövern leicht umkippen. <strong>Lage B im Verbund</strong> spiegelt oder dreht das Muster auf geraden Lagen, sodass die Ladung stabil wie ein Mauerwerksverband verklammert wird.
            </p>
          </div>
          <div class="faq-item">
            <h3 class="faq-q"><span>Q4.</span> Wie exportiere oder drucke ich den PDF-Palettenschein?</h3>
            <p class="faq-a">
              Tippen Sie im Reiter <em>Technischer Bericht</em> auf <strong>"PDF-Palettenschein herunterladen"</strong>. Über das iOS / iPadOS Teilen-Menü können Sie:
              <br>• Direkt via <strong>AirPrint</strong> drucken.
              <br>• Per <strong>AirDrop</strong> an Mac oder andere Geräte senden.
              <br>• Als E-Mail-Anhang versenden oder in iCloud Drive speichern.
            </p>
          </div>
          <div class="faq-item">
            <h3 class="faq-q"><span>Q5.</span> Benötigt PalletGrid eine Internetverbindung oder ein Benutzerkonto?</h3>
            <p class="faq-a">
              <strong>Nein.</strong> PalletGrid funktioniert zu 100% offline und arbeitet vollständig lokal auf Ihrem Gerät. Alle Berechnungen, 3D-Simulationen und gespeicherten Palettenscheine verbleiben streng vertraulich auf Ihrem iPhone oder iPad.
            </p>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container footer-bottom" style="border: none;">
      <div>© 2026 Jacoor Logistik. Alle Rechte vorbehalten.</div>
      <div>Support & Anfragen: ayeneso2023@gmail.com</div>
    </div>
  </footer>

</body>
</html>
"""

# -------------------------------------------------------------
# 5. MARKETING FRENCH (index-fr.html / marketing-fr.html)
# -------------------------------------------------------------
MARKETING_FR = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PalletGrid — Optimiseur de Palettisation 3D & Calcul de Charge</title>
  <meta name="description" content="PalletGrid est l'outil professionnel d'ingénierie logistique pour l'optimisation de palettisation 3D, plans de charge ≥80%, normes UNE-EN 13698 et fiches A4 en PDF.">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/app-icon.png">
</head>
<body>

  <!-- HEADER / NAVBAR -->
  <header class="navbar">
    <div class="container nav-wrap">
      <a href="index-fr.html" class="nav-brand">
        <img src="assets/app-icon.png" alt="PalletGrid Icon" class="nav-logo">
        <div>
          <div class="nav-title">PalletGrid</div>
          <div class="nav-subtitle">par Jacoor Logistique</div>
        </div>
      </a>
      <ul class="nav-menu">
        <li><a href="#features" class="nav-link">Fonctionnalités</a></li>
        <li><a href="#standards" class="nav-link">Normes</a></li>
        <li><a href="#gallery" class="nav-link">Captures</a></li>
        <li><a href="support-fr.html" class="nav-link">Support</a></li>
        <li><a href="privacy.html" class="nav-link">Confidentialité</a></li>
        <li>
          <span style="color: var(--primary-light); font-weight: 700; font-size: 13px;">🌐 FR</span>
          <a href="index.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">ES</a>
          <a href="index-en.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">EN</a>
          <a href="index-de.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">DE</a>
        </li>
      </ul>
      <a href="#download" class="nav-btn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        App Store
      </a>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="hero">
    <div class="hero-glow"></div>
    <div class="container hero-grid">
      <div class="hero-content">
        <div class="hero-tag">
          <div class="hero-tag-pulse"></div>
          GÉNIE LOGISTIQUE INDUSTRIEL V4
        </div>
        <h1 class="hero-title">
          Optimiseur de Palettisation 3D & <span>Calcul de Charge</span>
        </h1>
        <p class="hero-lead">
          Calculez instantanément les meilleurs plans de charge avec un taux d'occupation ≥ 80%, simulez le croisement de la Couche B en 3D interactif et éditez des fiches techniques vectorielles officielles A4 pour l'entrepôt et le transport.
        </p>
        <div class="hero-actions">
          <a href="#download" class="btn-primary">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.84c.62-.75 1.04-1.8 1.01-2.84-.96.04-2.13.64-2.79 1.41-.58.68-1.1 1.77-1.02 2.81 1.08.08 2.18-.63 2.8-1.38z"/></svg>
            Disponible sur l'App Store
          </a>
          <a href="support-fr.html" class="btn-secondary">
            Centre d'Assistance →
          </a>
        </div>
        <div class="hero-badges">
          <div class="badge-item">
            <span class="badge-val">≥ 80%</span>
            <span class="badge-lbl">Filtre d'Occupation</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">4 Types</span>
            <span class="badge-lbl">EUR, USA, 1/2 & Sur mesure</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">7 Langues</span>
            <span class="badge-lbl">FR, EN, ES, DE, IT, PT, RU</span>
          </div>
          <div class="badge-item">
            <span class="badge-val">100%</span>
            <span class="badge-lbl">Hors ligne & Sécurisé</span>
          </div>
        </div>
      </div>
      <div class="hero-mockup-wrap">
        <div class="hero-mockup-glow"></div>
        <img src="assets/01_Visor_3D_Explosion.png" alt="PalletGrid 3D Visualiseur" class="hero-mockup-img">
      </div>
    </div>
  </section>

  <!-- FEATURES -->
  <section class="section" id="features">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Capacités Techniques</span>
        <h2 class="section-title">Conçu pour la Chaîne d'Approvisionnement Exigeante</h2>
        <p class="section-desc">Technologies de calcul géométrique et de simulation physique garantissant des palettes stables, homologuées et rentables.</p>
      </div>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon-box">⭐</div>
          <h3 class="feature-title">Assistant de Configuration Guidé</h3>
          <p class="feature-desc">Flux pas à pas pour saisir les cartons, leur poids et le choix de la palette avec conversion directe mm/pouces et kg/livres.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📐</div>
          <h3 class="feature-title">Plans avec Taux d'Occupation ≥ 80%</h3>
          <p class="feature-desc">Filtre rigoureux écartant les combinaisons inefficaces. Plans longitudinaux, transversaux, mixtes à 2 et 3 blocs.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">🧱</div>
          <h3 class="feature-title">Croisement Automatique (Couche B)</h3>
          <p class="feature-desc">Agencement en quinconce entre étages pairs et impairs pour éviter le déversement de la charge sur route.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">🛡️</div>
          <h3 class="feature-title">Contrôle Physique & Stabilité</h3>
          <p class="feature-desc">Calcul exact du centre de gravité Z, du coefficient d'élancement (λ ≤ 1,8) et de l'angle critique de basculement (θ).</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📦</div>
          <h3 class="feature-title">Visualiseur Isométrique 3D Épuré</h3>
          <p class="feature-desc">Rotation tactile à 360° et curseur d'éclatement des couches en hauteur pour inspecter chaque étage sans numéros distrayants.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon-box">📑</div>
          <h3 class="feature-title">Fiche Technique Officielle A4 en PDF</h3>
          <p class="feature-desc">Édite des dossiers d'expédition complets prêts à imprimer via AirPrint, partager par AirDrop ou archiver avec sceau de qualité.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- STANDARDS -->
  <section class="section" id="standards" style="background: var(--bg-surface);">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Normes Internationales</span>
        <h2 class="section-title">Palettes Normalisées et Sur Mesure</h2>
        <p class="section-desc">PalletGrid intègre les cotes officielles, tares et hauteurs de bois réglementaires.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
        <div class="feature-card" style="border-color: rgba(16, 185, 129, 0.4);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🇪🇺</span>
            <span style="background: rgba(16, 185, 129, 0.15); color: var(--primary-light); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">NORME EUROPÉENNE</span>
          </div>
          <h3 class="feature-title">Palette Europe UNE-EN 13698-1</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Palette homologuée EPAL pour la grande distribution européenne.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Dimensions:</strong> 1200 × 800 mm</li>
            <li>✓ <strong>Hauteur de bois:</strong> 145 mm (3 semelles & 9 dés)</li>
            <li>✓ <strong>Tare officielle:</strong> 25,0 kg</li>
            <li>✓ <strong>Tolérance:</strong> Débordement jusqu'à +20 mm</li>
          </ul>
        </div>
        <div class="feature-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🇺🇸</span>
            <span style="background: rgba(255, 255, 255, 0.1); color: var(--text-main); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">NORME UNIVERSELLE</span>
          </div>
          <h3 class="feature-title">Palette Américaine UNE-EN 13698-2</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Palette industrielle ISO 6780 utilisée mondialement pour les conteneurs maritimes.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Dimensions:</strong> 1200 × 1000 mm</li>
            <li>✓ <strong>Hauteur de bois:</strong> 150 mm</li>
            <li>✓ <strong>Tare officielle:</strong> 30,0 kg</li>
            <li>✓ <strong>Capacité:</strong> Haute densité volumétrique</li>
          </ul>
        </div>
        <div class="feature-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">🏬</span>
            <span style="background: rgba(255, 255, 255, 0.1); color: var(--text-main); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">RETAIL / DISPLAY</span>
          </div>
          <h3 class="feature-title">Demi-palette (Display)</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Idéale pour les têtes de gondole, le retail et la livraison urbaine.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Dimensions:</strong> 800 × 600 mm</li>
            <li>✓ <strong>Hauteur de bois:</strong> 140 mm</li>
            <li>✓ <strong>Tare officielle:</strong> 15,0 kg</li>
            <li>✓ <strong>Usage:</strong> Mise en rayon directe</li>
          </ul>
        </div>
        <div class="feature-card" style="border-color: rgba(16, 185, 129, 0.3);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 28px;">⚙️</span>
            <span style="background: rgba(16, 185, 129, 0.15); color: var(--primary-light); font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 12px;">SUR MESURE</span>
          </div>
          <h3 class="feature-title">Palette Personnalisée</h3>
          <p class="feature-desc" style="margin-bottom: 20px;">Configurez n'importe quel gabarit sans contrainte de catalogue.</p>
          <ul style="list-style: none; color: var(--text-muted); font-size: 14px; line-height: 2;">
            <li>✓ <strong>Longueur & Largeur:</strong> Libres en millimètres</li>
            <li>✓ <strong>Hauteur bois:</strong> Totalement personnalisable</li>
            <li>✓ <strong>Tare manuelle:</strong> Poids de base précis</li>
            <li>✓ <strong>Moteur:</strong> 3D et calcul en temps réel</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- GALLERY -->
  <section class="section" id="gallery">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Captures d'Écran</span>
        <h2 class="section-title">Interface PalletGrid V4</h2>
        <p class="section-desc">Conçue pour les opérations d'entrepôt sur iPhone et iPad.</p>
      </div>
      <div class="gallery-wrap">
        <div class="gallery-card">
          <img src="assets/01_Visor_3D_Explosion.png" alt="Visualiseur 3D" class="gallery-thumb">
          <div class="gallery-caption">Visualiseur 3D</div>
          <div class="gallery-sub">Rotation 360° & vue éclatée</div>
        </div>
        <div class="gallery-card">
          <img src="assets/02_Dossier_Ficha_Tecnica_PDF.png" alt="Fiche A4 PDF" class="gallery-thumb">
          <div class="gallery-caption">Fiche Technique PDF</div>
          <div class="gallery-sub">Plans, élévations et sceau</div>
        </div>
        <div class="gallery-card">
          <img src="assets/03_Mosaicos_2D_Ocupacion80.png" alt="Plans 2D" class="gallery-thumb">
          <div class="gallery-caption">Plans 2D (≥ 80%)</div>
          <div class="gallery-sub">Contrôle du débord & KPIs</div>
        </div>
        <div class="gallery-card">
          <img src="assets/04_Asistente_Guiado_Nuevo_Pallet.png" alt="Assistant Guidé" class="gallery-thumb">
          <div class="gallery-caption">Assistant Guidé</div>
          <div class="gallery-sub">mm/po, kg/lb & sur mesure</div>
        </div>
        <div class="gallery-card">
          <img src="assets/05_Gestor_Fichas_Guardadas.png" alt="Fiches Sauvegardées" class="gallery-thumb">
          <div class="gallery-caption">Fiches Sauvegardées</div>
          <div class="gallery-sub">Archives locales & réouverture 3D</div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section" id="download" style="text-align: center;">
    <div class="container">
      <div class="contact-box" style="margin: 0 auto;">
        <h3>Optimisez vos chargements dès aujourd'hui</h3>
        <p>Disponible sur l'App Store pour iPhone et iPad. Achat unique, sans compte obligatoire, sans publicité, 100% privé.</p>
        <a href="https://apps.apple.com" target="_blank" class="contact-mail-btn">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.84c.62-.75 1.04-1.8 1.01-2.84-.96.04-2.13.64-2.79 1.41-.58.68-1.1 1.77-1.02 2.81 1.08.08 2.18-.63 2.8-1.38z"/></svg>
          Télécharger sur l'App Store
        </a>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="nav-brand">
            <img src="assets/app-icon.png" alt="PalletGrid Logo" class="nav-logo">
            <div>
              <div class="nav-title">PalletGrid</div>
              <div class="nav-subtitle">par Jacoor Logistique</div>
            </div>
          </div>
          <p>Outil d'ingénierie pour le gerbage, l'optimisation volumétrique et la standardisation des palettes de transport.</p>
        </div>
        <div class="footer-col">
          <h4>Navigation</h4>
          <ul>
            <li><a href="#features">Fonctionnalités</a></li>
            <li><a href="#standards">Normes</a></li>
            <li><a href="#gallery">Captures</a></li>
            <li><a href="#download">App Store</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Légal & Support</h4>
          <ul>
            <li><a href="support-fr.html">Centre d'Assistance</a></li>
            <li><a href="privacy.html">Politique de Confidentialité</a></li>
            <li><a href="mailto:ayeneso2023@gmail.com">Contact E-mail</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 Jacoor Logistique. Tous droits réservés.</div>
        <div>Conforme aux directives Apple App Store Review.</div>
      </div>
    </div>
  </footer>

</body>
</html>
"""

# -------------------------------------------------------------
# 6. SUPPORT FRENCH (support-fr.html)
# -------------------------------------------------------------
SUPPORT_FR = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Assistance Officielle — PalletGrid</title>
  <meta name="description" content="Centre d'assistance technique officiel et FAQ pour PalletGrid sur iOS et iPadOS.">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/app-icon.png">
</head>
<body>

  <!-- HEADER -->
  <header class="navbar">
    <div class="container nav-wrap">
      <a href="index-fr.html" class="nav-brand">
        <img src="assets/app-icon.png" alt="PalletGrid Icon" class="nav-logo">
        <div>
          <div class="nav-title">PalletGrid</div>
          <div class="nav-subtitle">Centre d'Assistance</div>
        </div>
      </a>
      <ul class="nav-menu">
        <li><a href="index-fr.html" class="nav-link">Accueil / Marketing</a></li>
        <li><a href="support-fr.html" class="nav-link active">Assistance</a></li>
        <li><a href="privacy.html" class="nav-link">Confidentialité</a></li>
        <li>
          <span style="color: var(--primary-light); font-weight: 700; font-size: 13px;">🌐 FR</span>
          <a href="soporte.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">ES</a>
          <a href="support-en.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">EN</a>
          <a href="support-de.html" style="font-size: 12px; color: var(--text-muted); margin-left: 4px;">DE</a>
        </li>
      </ul>
      <a href="index-fr.html#download" class="nav-btn">
        App Store
      </a>
    </div>
  </header>

  <!-- CONTENT -->
  <main class="legal-page">
    <div class="container">
      <div class="legal-header">
        <span class="section-tag">Assistance et Contact Officiel</span>
        <h1 class="legal-title">Comment pouvons-nous vous aider avec PalletGrid ?</h1>
        <p class="legal-meta">Service officiel d'assistance aux utilisateurs et résolution d'incidents techniques • Développé par Jacoor Logistique</p>
      </div>

      <!-- DIRECT CONTACT CARD -->
      <div class="contact-box" style="margin: 0 0 60px 0; text-align: left; display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 32px; align-items: center;">
        <div>
          <h2 style="font-size: 26px; font-weight: 900; margin-bottom: 12px; color: #FFFFFF;">Support Technique Direct</h2>
          <p style="color: var(--text-muted); font-size: 15px; margin-bottom: 20px;">
            Que vous ayez des questions d'utilisation, un cas particulier à signaler ou besoin d'aide pour l'homologation de vos fiches palettes, notre équipe technique est à votre écoute.
          </p>
          <div style="color: var(--text-main); font-size: 14px; line-height: 2;">
            <div>📧 <strong>E-mail de support :</strong> <a href="mailto:ayeneso2023@gmail.com?subject=PalletGrid%20Support%20iOS%20FR" style="color: var(--primary-light); text-decoration: underline;">ayeneso2023@gmail.com</a></div>
            <div>⏱️ <strong>Délai de réponse :</strong> Moins de 24 heures ouvrées.</div>
            <div>🏢 <strong>Développeur / Titulaire :</strong> Jose Antonio Corrales Ortega (Jacoor Logistique)</div>
          </div>
        </div>
        <div style="text-align: center;">
          <a href="mailto:ayeneso2023@gmail.com?subject=PalletGrid%20Support%20iOS%20FR" class="contact-mail-btn" style="width: 100%; justify-content: center;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            Écrire au Support
          </a>
        </div>
      </div>

      <!-- FAQ -->
      <div class="legal-body">
        <h2 style="font-size: 28px; margin-bottom: 24px;">Foire Aux Questions (FAQ)</h2>
        <div class="faq-list">
          <div class="faq-item">
            <h3 class="faq-q"><span>Q1.</span> Quels types de palettes et dimensions sont pris en charge ?</h3>
            <p class="faq-a">
              PalletGrid gère nativement :
              <br>• <strong>Palette Europe UNE-EN 13698-1</strong> (1200 × 800 mm, bois 145 mm, tare 25,0 kg).
              <br>• <strong>Palette Américaine / ISO UNE-EN 13698-2</strong> (1200 × 1000 mm, bois 150 mm, tare 30,0 kg).
              <br>• <strong>Demi-palette (Display)</strong> (800 × 600 mm, bois 140 mm, tare 15,0 kg).
              <br>• <strong>Palettes sur mesure :</strong> Saisie libre de la longueur, largeur, hauteur de bois et tare.
              <br>Comprend la conversion directe en temps réel entre millimètres ⇄ pouces et kilogrammes ⇄ livres.
            </p>
          </div>
          <div class="faq-item">
            <h3 class="faq-q"><span>Q2.</span> Pourquoi certains plans affichent-ils un badge ⚠️ avec un débord en mm ?</h3>
            <p class="faq-a">
              En pratique logistique, certains cartons dépassent légèrement le périmètre en bois. Si vous cochez <em>"Autoriser un débord jusqu'à +20 mm"</em>, l'algorithme évalue des combinaisons hautement rentables exploitant cette marge. Le badge ⚠️ précise au millimètre près le débord en longueur et en largeur pour validation par le chef de quai.
            </p>
          </div>
          <div class="faq-item">
            <h3 class="faq-q"><span>Q3.</span> Qu'est-ce que la Couche B et pourquoi le croisement est-il crucial ?</h3>
            <p class="faq-a">
              Empiler des cartons de manière identique d'un étage à l'autre crée des colonnes isolées susceptibles de basculer lors du transport. La <strong>Couche B croisée</strong> fait pivoter ou inverse le schéma sur les étages pairs, liant la marchandise comme un mur de briques solidaire.
            </p>
          </div>
          <div class="faq-item">
            <h3 class="faq-q"><span>Q4.</span> Comment exporter ou imprimer la Fiche Technique PDF ?</h3>
            <p class="faq-a">
              Depuis l'onglet <em>Fiche Technique</em> de l'application, touchez <strong>"Télécharger Fiche Technique PDF"</strong>. Le menu de partage iOS s'ouvre pour :
              <br>• Imprimer directement en réseau via <strong>AirPrint</strong>.
              <br>• Partager via <strong>AirDrop</strong> vers un Mac ou un autre appareil.
              <br>• Envoyer en pièce jointe par e-mail ou enregistrer dans Fichiers.
            </p>
          </div>
          <div class="faq-item">
            <h3 class="faq-q"><span>Q5.</span> PalletGrid nécessite-t-il Internet ou un compte utilisateur ?</h3>
            <p class="faq-a">
              <strong>Non.</strong> PalletGrid fonctionne à 100% hors ligne et traite tout localement sur votre iPhone ou iPad. Tous vos calculs et fiches sauvegardées restent strictement privés et confidentiels.
            </p>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container footer-bottom" style="border: none;">
      <div>© 2026 Jacoor Logistique. Tous droits réservés.</div>
      <div>Support & Assistance : ayeneso2023@gmail.com</div>
    </div>
  </footer>

</body>
</html>
"""

def generate_pages():
    files = {
        "index-en.html": MARKETING_EN,
        "marketing-en.html": MARKETING_EN,
        "support-en.html": SUPPORT_EN,
        "index-de.html": MARKETING_DE,
        "marketing-de.html": MARKETING_DE,
        "support-de.html": SUPPORT_DE,
        "index-fr.html": MARKETING_FR,
        "marketing-fr.html": MARKETING_FR,
        "support-fr.html": SUPPORT_FR,
    }
    for fname, content in files.items():
        fpath = os.path.join(WEB_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\\n")
        print(f"Created {fpath}")

if __name__ == "__main__":
    generate_pages()
