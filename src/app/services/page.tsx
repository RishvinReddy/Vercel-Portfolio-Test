import React from 'react';

export const metadata = {
  title: 'Services | Rishvin Labs',
};

export default function Services() {
  return (
    <>
      {/*  ── Header v2 Scripts ──  */}
    

    {/*  ===== Header Spacer (since header is fixed) =====  */}
    <div className="h-12 shrink-0"></div>




    {/*  ─ Section Divider ─  */}
    <div className="section-divider" aria-hidden="true"><span className="divider-gem"></span></div>

    {/*  ===========================
     SERVICES — Upgraded & Personalized for Rishvin Reddy
     Replace your existing services block with this code.
     Tailwind CSS utilities assumed (colors: primary, bg-card-background, etc.).
     Accessible, spacious, and includes accurate SVG icons for each service.
     ===========================  */}
    <main className="flex-1">
      <div className="mx-auto max-w-7xl px-6 py-16 sm:px-8 lg:px-10 lg:py-24">
        {/*  Header  */}
        <div className="text-center max-w-3xl mx-auto scroll-reveal">
          <h1
            className="text-4xl font-extrabold tracking-tight text-slate-900 sm:text-5xl lg:text-6xl text-transparent bg-clip-text bg-gradient-to-r from-slate-900 via-purple-900 to-slate-900">
            Services I Offer
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-lg text-slate-600">
            I deliver end-to-end solutions across IoT, Blockchain, Cyber Security and Full-Stack Engineering — from
            prototyping hardware to shipping secure, production-ready software.
          </p>
        </div>

        {/*  Services grid  */}
        <div className="scroll-reveal mt-16 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3" data-stagger-list>
          {/*  IoT & Embedded Systems  */}
          <div
            className="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div className="text-primary">
              {/*  microcontroller + sensor svg  */}
              <svg className="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <rect x="2.5" y="6" width="19" height="12" rx="2.5"></rect>
                <path d="M8 3v4M16 3v4"></path>
                <circle cx="9" cy="12" r="1.6"></circle>
                <circle cx="15" cy="12" r="1.6"></circle>
                <path d="M12 7v10"></path>
              </svg>
            </div>
            <div className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold text-slate-900">IoT & Embedded Systems</h2>
              <p className="text-slate-600 text-sm">Hardware prototyping (Arduino/ESP), sensor integration, firmware and
                edge-to-cloud communication (MQTT).</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Arduino</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">ESP8266/ESP32</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">MQTT</span>
              </div>
            </div>
          </div>

          {/*  Blockchain Development  */}
          <div
            className="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div className="text-primary">
              {/*  blockchain / chain svg  */}
              <svg className="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <rect x="3" y="7" width="7" height="7" rx="1.5"></rect>
                <rect x="14" y="10" width="7" height="7" rx="1.5"></rect>
                <path d="M10 10l4-1.5"></path>
                <path d="M10 14l4 1.5"></path>
              </svg>
            </div>
            <div className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold text-slate-900">Blockchain & Decentralized Systems</h2>
              <p className="text-slate-600 text-sm">Smart contract prototypes, transaction flows, and proofs-of-concept for
                secure, auditable interactions.</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Smart Contracts</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">dApps</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Token Flows</span>
              </div>
            </div>
          </div>

          {/*  Cyber Security & Auth  */}
          <div
            className="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div className="text-primary">
              {/*  lock / shield svg  */}
              <svg className="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <path d="M12 1l7 4v5a7 7 0 01-14 0V5l7-4z"></path>
                <path d="M8 12h8"></path>
              </svg>
            </div>
            <div className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold text-slate-900">Cyber Security & Authentication</h2>
              <p className="text-slate-600 text-sm">Threat-aware architecture, encryption (AES/SHA), TOTP, hybrid biometric
                + OTP solutions and secure key handling.</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">AES / SHA</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">TOTP</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Biometrics</span>
              </div>
            </div>
          </div>

          {/*  Full-Stack Development  */}
          <div
            className="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div className="text-primary">
              {/*  backend / web svg  */}
              <svg className="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <path d="M3 7h18M7 7v10M17 7v10"></path>
                <rect x="4" y="17" width="16" height="4" rx="1.5"></rect>
              </svg>
            </div>
            <div className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold text-slate-900">Full-Stack Development</h2>
              <p className="text-slate-600 text-sm">APIs (Flask), web frontends, realtime features, and database-backed
                services for reliable product delivery.</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Python / Flask</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">MySQL</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Firebase</span>
              </div>
            </div>
          </div>

          {/*  System Architecture & DevOps  */}
          <div
            className="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div className="text-primary">
              {/*  architecture diagram svg  */}
              <svg className="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
                <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
                <rect x="14" y="14" width="7" height="7" rx="1.5"></rect>
                <path d="M6.5 10.5V14M17.5 10.5V14"></path>
              </svg>
            </div>
            <div className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold text-slate-900">System Architecture & DevOps</h2>
              <p className="text-slate-600 text-sm">Designing scalable architectures, CI/CD ideas and deployment-ready
                handoffs with monitoring and logging in mind.</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">CI/CD</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Monitoring</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Cloud-ready</span>
              </div>
            </div>
          </div>

          {/*  Prototyping & Hardware Integration  */}
          <div
            className="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div className="text-primary">
              {/*  prototype / wrench svg  */}
              <svg className="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <path d="M3 21l6-6"></path>
                <path d="M14 3a4 4 0 016 6l-7 7-6-6 7-7z"></path>
              </svg>
            </div>
            <div className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold text-slate-900">Prototyping & Hardware Integration</h2>
              <p className="text-slate-600 text-sm">Rapid breadboard prototypes, Proteus simulation, PCB iteration guidance
                and integration testing.</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Breadboards</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Proteus</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">PCB Guidance</span>
              </div>
            </div>
          </div>

          {/*  Data, AI & Vision  */}
          <div
            className="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div className="text-primary">
              {/*  AI / brain-eye svg  */}
              <svg className="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <path d="M12 2v20"></path>
                <circle cx="12" cy="10" r="3"></circle>
                <path d="M2 12c2-6 6-8 10-8s8 2 10 8c-2 6-6 8-10 8s-8-2-10-8z"></path>
              </svg>
            </div>
            <div className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold text-slate-900">Data, AI & Computer Vision</h2>
              <p className="text-slate-600 text-sm">Model prototyping, OpenCV-based vision modules and basic TensorFlow
                workflows for embedded/edge inference.</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">OpenCV</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">TensorFlow</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Edge AI</span>
              </div>
            </div>
          </div>

          {/*  UX, Product & Mentoring  */}
          <div
            className="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div className="text-primary">
              {/*  user + chart svg  */}
              <svg className="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <path d="M3 21v-2a4 4 0 014-4h10a4 4 0 014 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <div className="flex flex-col gap-2">
              <h2 className="text-xl font-semibold text-slate-900">Product Design & Mentoring</h2>
              <p className="text-slate-600 text-sm">UI/UX design, prototyping, usability testing, documentation and peer
                mentoring for student teams and junior engineers.</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Figma</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">User Research</span>
                <span className="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Mentoring</span>
              </div>
            </div>
          </div>
        </div>

        {/*  Footer note  */}
        <div className="mt-10 max-w-3xl mx-auto text-center">
          <p className="text-sm text-slate-600">
            Interested in a custom solution? <a href="#contact" className="text-primary underline">Get in touch</a> — I’m
            based in Hyderabad, Telangana, India and available for internships, freelance work and research
            collaborations.
          </p>
        </div>
      </div>
    </main>
    </>
  );
}
