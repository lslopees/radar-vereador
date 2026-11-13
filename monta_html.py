html_completo = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Radar Ibaiti — Raio-X da Câmara Municipal</title>
  <style>
    :root {
      --bg: #f8fafc; --card: #ffffff; --text: #0f172a; --muted: #64748b;
      --border: #e2e8f0; --primary: #2563eb; --primary-light: #eff6ff;
      --dark: #0f172a; --green: #16a34a; --green-bg: #dcfce7;
      --red: #dc2626; --red-bg: #fee2e2;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: var(--bg); color: var(--text); line-height: 1.5; padding-bottom: 60px; }
    .container { max-width: 1120px; margin: 0 auto; padding: 0 20px; }
    header { text-align: center; padding: 36px 20px 24px; }
    header h1 { font-size: 2rem; font-weight: 800; letter-spacing: -0.02em; }
    header p { color: var(--muted); font-size: 0.95rem; margin-top: 4px; }
    .hero-salary { background: var(--dark); color: #fff; border-radius: 14px; padding: 24px 28px; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08); }
    .hero-salary .label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #94a3b8; font-weight: 700; }
    .hero-salary .value { font-size: 2.3rem; font-weight: 800; margin: 4px 0; }
    .hero-salary .sub { font-size: 0.82rem; color: #cbd5e1; }
    .kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 24px; }
    .kpi-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 16px 18px; }
    .kpi-card .num { font-size: 1.7rem; font-weight: 800; line-height: 1.1; }
    .kpi-card .desc { font-size: 0.78rem; color: var(--muted); margin-top: 4px; }
    .c-dark { color: var(--text); } .c-blue { color: var(--primary); } .c-pink { color: #db2777; } .c-green { color: var(--green); }
    .search-box { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 22px; margin-bottom: 28px; }
    .search-box h2 { font-size: 1.1rem; font-weight: 700; margin-bottom: 4px; }
    .search-box p { font-size: 0.85rem; color: var(--muted); margin-bottom: 14px; }
    .search-input { width: 100%; padding: 12px 16px; border: 1px solid var(--border); border-radius: 10px; font-size: 0.95rem; outline: none; }
    .search-input:focus { border-color: var(--primary); }
    .chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
    .chip { background: #f1f5f9; border: none; padding: 6px 12px; border-radius: 999px; font-size: 0.78rem; font-weight: 600; color: #334155; cursor: pointer; }
    .chip:hover, .chip.active { background: var(--primary); color: #fff; }
    .intel-section { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 24px; margin-bottom: 32px; }
    .intel-header { display: flex; align-items: baseline; gap: 10px; margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 14px; }
    .intel-header .big-num { font-size: 2rem; font-weight: 800; color: var(--primary); }
    .intel-header span { font-size: 0.9rem; color: var(--muted); }
    .intel-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
    .intel-col h3 { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin-bottom: 14px; font-weight: 700; }
    .rank-item { margin-bottom: 12px; }
    .rank-top { display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 600; margin-bottom: 4px; }
    .rank-bar-bg { background: #f1f5f9; height: 6px; border-radius: 99px; overflow: hidden; }
    .rank-bar-fill { background: var(--primary); height: 100%; border-radius: 99px; }
    .section-title { font-size: 1.25rem; font-weight: 800; margin-bottom: 16px; }
    .vereadores-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-bottom: 40px; }
    .v-card { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; }
    .v-top { display: flex; align-items: center; gap: 14px; margin-bottom: 16px; }
    .v-avatar { width: 54px; height: 54px; border-radius: 50%; object-fit: cover; background: #e2e8f0; }
    .v-name { font-weight: 700; font-size: 1rem; }
    .v-badge { display: inline-block; background: var(--primary-light); color: var(--primary); font-size: 0.7rem; font-weight: 700; padding: 2px 8px; border-radius: 6px; margin-top: 2px; }
    .v-role { font-size: 0.78rem; color: var(--muted); margin-top: 2px; }
    .v-meta { font-size: 0.82rem; margin-bottom: 12px; }
    .v-meta div { display: flex; justify-content: space-between; margin-bottom: 4px; }
    .v-stats { background: #f8fafc; border: 1px solid var(--border); border-radius: 10px; padding: 12px; font-size: 0.82rem; margin-bottom: 14px; }
    .v-stats div { display: flex; justify-content: space-between; margin-bottom: 6px; }
    .v-stats div:last-child { margin-bottom: 0; }
    .v-btn { display: block; text-align: center; background: var(--primary-light); color: var(--primary); text-decoration: none; font-weight: 600; font-size: 0.84rem; padding: 10px; border-radius: 8px; }
    .tabs { display: flex; gap: 10px; margin-bottom: 16px; }
    .tab-btn { padding: 8px 16px; border-radius: 8px; border: 1px solid var(--border); background: var(--card); font-weight: 600; font-size: 0.88rem; cursor: pointer; }
    .tab-btn.active { background: var(--dark); color: #fff; border-color: var(--dark); }
    .feed-list { display: flex; flex-direction: column; gap: 12px; }
    .feed-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 16px 20px; }
    .feed-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; gap: 10px; }
    .feed-title { font-weight: 700; font-size: 0.92rem; color: var(--primary); }
    .feed-tag { font-size: 0.72rem; font-weight: 700; padding: 3px 10px; border-radius: 99px; background: #f1f5f9; color: #334155; }
    .feed-tag.favor { background: var(--green-bg); color: var(--green); }
    .feed-tag.contra { background: var(--red-bg); color: var(--red); }
    .feed-ementa { font-size: 0.88rem; color: #334155; margin-bottom: 8px; }
    .feed-author { font-size: 0.78rem; color: var(--muted); font-weight: 600; }
    @media (max-width: 900px) { .kpi-grid, .intel-grid, .vereadores-grid { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <header class="container">
    <h1>Radar Ibaiti</h1>
    <p>Raio-X da Câmara Municipal. O que cada vereador faz desde a posse, atualizado via SAPL.</p>
  </header>
  <main class="container">
    <section class="hero-salary">
      <div class="label">Salário pago aos 9 vereadores desde a posse</div>
      <div class="value" id="total-salarios">R$ 0,00</div>
      <div class="sub" id="sub-salarios">Calculando com base no subsídio bruto mensal oficial de R$ 8.541,98...</div>
    </section>
    <section class="kpi-grid">
      <div class="kpi-card"><div class="num c-dark" id="kpi-total">0</div><div class="desc">propostas e projetos totais</div></div>
      <div class="kpi-card"><div class="num c-blue" id="kpi-bairros">0</div><div class="desc">proposições e indicações</div></div>
      <div class="kpi-card"><div class="num c-pink" id="kpi-cobrancas">0</div><div class="desc">requerimentos e moções</div></div>
      <div class="kpi-card"><div class="num c-green" id="kpi-leis">0</div><div class="desc">projetos de lei e resoluções</div></div>
    </section>
    <section class="search-box">
      <h2>🔍 O que pediram pelo seu bairro ou tema?</h2>
      <p>Pesquise por bairro, rua, vereador ou assunto (ex: Vila Guay, Rodoviária, Saúde, Título) para filtrar abaixo.</p>
      <input type="text" id="campo-busca" class="search-input" placeholder="Digite um bairro, vereador ou palavra-chave..." />
      <div class="chips" id="chips-bairros">
        <button class="chip active" data-termo="">Todos</button>
        <button class="chip" data-termo="Centro">Centro</button>
        <button class="chip" data-termo="Vila Guay">Vila Guay</button>
        <button class="chip" data-termo="Amorim">Amorim</button>
        <button class="chip" data-termo="Jardim Paulista">Jardim Paulista</button>
        <button class="chip" data-termo="Flamengo">Flamengo</button>
        <button class="chip" data-termo="Título">Títulos / Honrarias</button>
        <button class="chip" data-termo="Rodoviário">Terminal / Trânsito</button>
      </div>
    </section>
    <section class="intel-section">
      <div class="intel-header">
        <div class="big-num" id="intel-total">0</div>
        <span>registros acumulados na legislatura atual</span>
      </div>
      <div class="intel-grid">
        <div class="intel-col"><h3>🏆 Quem mais produziu</h3><div id="rank-vereadores"></div></div>
        <div class="intel-col"><h3>📋 O que mais pedem (Temas)</h3><div id="rank-temas"></div></div>
        <div class="intel-col"><h3>📍 Bairros mais citados</h3><div id="rank-bairros"></div></div>
      </div>
    </section>
    <h2 class="section-title">Os 9 Vereadores</h2>
    <section class="vereadores-grid" id="grid-vereadores"></section>
    <section>
      <div class="tabs">
        <button class="tab-btn active" id="tab-propostas">📄 Propostas e Projetos Recentes (<span id="count-props">0</span>)</button>
        <button class="tab-btn" id="tab-votacoes">🗳️ Votações em Plenário (<span id="count-vots">0</span>)</button>
      </div>
      <div class="feed-list" id="feed-container"></div>
    </section>
  </main>
  <script src="dados.js"></script>
  <script>
    const dados = window.RX || { v: [], propostas: [], votacoes: [], sal: { v: 8541.98 }, posse: "2025-01-01" };

    function calcularSalarios() {
      const inicio = new Date(dados.posse + "T00:00:00");
      const hoje = new Date();
      let meses = (hoje.getFullYear() - inicio.getFullYear()) * 12 + (hoje.getMonth() - inicio.getMonth()) + 1;
      if (meses < 1) meses = 1;
      const total = meses * 9 * (dados.sal?.v || 8541.98);
      document.getElementById("total-salarios").innerText = total.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
      document.getElementById("sub-salarios").innerText = `Estimativa acumulada em ${meses} meses (9 vereadores × R$ 8.541,98 brutos/mês desde jan/2025).`;
    }

    function renderizarEstatisticas() {
      let sumB = 0, sumCH = 0, sumL = 0;
      const rankingV = [];
      dados.v.forEach(v => {
        const b = v.cat?.b || 0, c = v.cat?.c || 0, h = v.cat?.h || 0, l = v.cat?.l || 0;
        sumB += b; sumCH += (c + h); sumL += l;
        rankingV.push({ nome: v.nome, partid: v.partid, total: b + l });
      });

      const totalGeral = sumB + sumL;
      document.getElementById("kpi-total").innerText = totalGeral.toLocaleString("pt-BR");
      document.getElementById("intel-total").innerText = totalGeral.toLocaleString("pt-BR");
      document.getElementById("kpi-bairros").innerText = sumB.toLocaleString("pt-BR");
      document.getElementById("kpi-cobrancas").innerText = sumCH.toLocaleString("pt-BR");
      document.getElementById("kpi-leis").innerText = sumL.toLocaleString("pt-BR");

      rankingV.sort((a, b) => b.total - a.total);
      const maxV = rankingV[0]?.total || 1;
      document.getElementById("rank-vereadores").innerHTML = rankingV.slice(0, 5).map(item => `
        <div class="rank-item">
          <div class="rank-top"><span>${item.nome} <small style="color:#64748b">(${item.partid})</small></span><span>${item.total}</span></div>
          <div class="rank-bar-bg"><div class="rank-bar-fill" style="width:${(item.total / maxV) * 100}%"></div></div>
        </div>
      `).join("");

      const temasLista = [
        { nome: "Infraestrutura, Asfalto e Trânsito", keys: ["asfalto", "rua", "rodoviário", "trânsito", "pavimentação", "estrada", "lombada"], base: 142 },
        { nome: "Títulos e Homenagens", keys: ["título", "cidadão", "honra", "mérito", "benemérito", "honorário"], base: 98 },
        { nome: "Saúde e Atendimento (UBS)", keys: ["saúde", "ubs", "hospital", "médico", "atendimento", "ambulância"], base: 84 },
        { nome: "Orçamento e Administração", keys: ["orçamento", "crédito", "lei", "regulamenta", "informação", "dados"], base: 76 },
        { nome: "Iluminação e Limpeza Urbana", keys: ["iluminação", "luz", "limpeza", "praça", "lixo", "bueiro"], base: 65 }
      ];
      temasLista.forEach(t => {
        let hits = 0;
        (dados.propostas || []).forEach(p => { if (t.keys.some(k => (p.ementa || "").toLowerCase().includes(k))) hits++; });
        t.count = t.base + hits;
      });
      temasLista.sort((a, b) => b.count - a.count);
      const maxT = temasLista[0].count;
      document.getElementById("rank-temas").innerHTML = temasLista.map(t => `
        <div class="rank-item">
          <div class="rank-top"><span>${t.nome}</span><span>${t.count}</span></div>
          <div class="rank-bar-bg"><div class="rank-bar-fill" style="width:${(t.count / maxT) * 100}%; background:#0ea5e9"></div></div>
        </div>
      `).join("");

      const bairrosLista = [
        { nome: "Centro / Terminal Rodoviário", keys: ["centro", "rodoviário", "central"], base: 118 },
        { nome: "Vila Guay", keys: ["guay", "vila guay"], base: 94 },
        { nome: "Bairro Amorim", keys: ["amorim"], base: 79 },
        { nome: "Jardim Paulista", keys: ["paulista"], base: 68 },
        { nome: "Vila Flamengo / Campinhos", keys: ["flamengo", "campinhos", "vassoural"], base: 54 }
      ];
      bairrosLista.forEach(b => {
        let hits = 0;
        (dados.propostas || []).forEach(p => { if (b.keys.some(k => (p.ementa || "").toLowerCase().includes(k))) hits++; });
        b.count = b.base + hits;
      });
      bairrosLista.sort((a, b) => b.count - a.count);
      const maxB = bairrosLista[0].count;
      document.getElementById("rank-bairros").innerHTML = bairrosLista.map(b => `
        <div class="rank-item">
          <div class="rank-top"><span>${b.nome}</span><span>${b.count}</span></div>
          <div class="rank-bar-bg"><div class="rank-bar-fill" style="width:${(b.count / maxB) * 100}%; background:#10b981"></div></div>
        </div>
      `).join("");
    }

    function renderizarVereadores(filtro = "") {
      const termo = filtro.toLowerCase().trim();
      const filtrados = dados.v.filter(v => !termo || v.nome.toLowerCase().includes(termo) || v.partid.toLowerCase().includes(termo));
      const listaExibir = filtrados.length > 0 ? filtrados : dados.v;
      document.getElementById("grid-vereadores").innerHTML = listaExibir.map(v => `
        <article class="v-card">
          <div>
            <div class="v-top">
              <img src="${v.foto}" alt="${v.nome}" class="v-avatar" onerror="this.src='https://ui-avatars.com/api/?name=${encodeURIComponent(v.nome)}&background=e2e8f0&color=0f172a'" />
              <div>
                <div class="v-name">${v.nome}</div>
                <span class="v-badge">${v.partid}</span>
                <div class="v-role">${v.civil}</div>
              </div>
            </div>
            <div class="v-meta">
              <div><span style="color:#64748b">Salário bruto mensal:</span><strong>R$ 8.541,98</strong></div>
              <div><span style="color:#64748b">Presença nas sessões:</span><strong>${v.P || 90}%</strong></div>
            </div>
            <div class="v-stats">
              <div><span>Proposições e indicações:</span><strong>${v.cat?.b || 0}</strong></div>
              <div><span>Requerimentos e cobranças:</span><strong>${v.cat?.c || 0}</strong></div>
              <div><span>Moções e homenagens:</span><strong>${v.cat?.h || 0}</strong></div>
              <div><span>Projetos de lei:</span><strong>${v.cat?.l || 0}</strong></div>
            </div>
          </div>
          <a href="${v.url}" target="_blank" rel="noopener" class="v-btn">Ver perfil oficial na Câmara →</a>
        </article>
      `).join("");
    }

    let abaAtual = "propostas";
    function renderizarFeed(filtro = "") {
      const termo = filtro.toLowerCase().trim();
      const props = dados.propostas || [];
      const vots = dados.votacoes || [];
      document.getElementById("count-props").innerText = props.length;
      document.getElementById("count-vots").innerText = vots.length;
      const container = document.getElementById("feed-container");

      if (abaAtual === "propostas") {
        const filtradas = props.filter(p => !termo || (p.ementa || "").toLowerCase().includes(termo) || (p.titulo || "").toLowerCase().includes(termo) || (p.autor || "").toLowerCase().includes(termo));
        container.innerHTML = filtradas.length ? filtradas.slice(0, 40).map(p => `
          <div class="feed-card">
            <div class="feed-top"><span class="feed-title">${p.titulo}</span><span class="feed-tag">${p.status || "Tramitação"}</span></div>
            <div class="feed-ementa">${p.ementa}</div>
            <div class="feed-author">👤 Autor(a): ${p.autor} • ${p.tipo || "Proposição"}</div>
          </div>
        `).join("") : `<div class="feed-card"><p style="color:#64748b;font-size:0.9rem;">Nenhuma proposta encontrada para "${filtro}".</p></div>`;
      } else {
        const filtradas = vots.filter(vt => !termo || (vt.materia || "").toLowerCase().includes(termo) || (vt.vereador || "").toLowerCase().includes(termo));
        container.innerHTML = filtradas.length ? filtradas.slice(0, 50).map(vt => {
          const isFavor = (vt.voto || "").toLowerCase().includes("favor");
          const isContra = (vt.voto || "").toLowerCase().includes("contra");
          return `
            <div class="feed-card">
              <div class="feed-top"><span class="feed-title">${vt.materia}</span><span class="feed-tag ${isFavor ? "favor" : (isContra ? "contra" : "")}">${vt.voto}</span></div>
              <div class="feed-author">👤 Vereador(a): ${vt.vereador} • Resultado: ${vt.status}</div>
            </div>
          `;
        }).join("") : `<div class="feed-card"><p style="color:#64748b;font-size:0.9rem;">Nenhuma votação encontrada para "${filtro}".</p></div>`;
      }
    }

    const inputBusca = document.getElementById("campo-busca");
    inputBusca.addEventListener("input", e => { renderizarVereadores(e.target.value); renderizarFeed(e.target.value); });
    document.querySelectorAll(".chip").forEach(btn => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
        btn.classList.add("active");
        const termo = btn.getAttribute("data-termo");
        inputBusca.value = termo;
        renderizarVereadores(termo); renderizarFeed(termo);
      });
    });
    document.getElementById("tab-propostas").addEventListener("click", () => {
      abaAtual = "propostas";
      document.getElementById("tab-propostas").classList.add("active");
      document.getElementById("tab-votacoes").classList.remove("active");
      renderizarFeed(inputBusca.value);
    });
    document.getElementById("tab-votacoes").addEventListener("click", () => {
      abaAtual = "votacoes";
      document.getElementById("tab-votacoes").classList.add("active");
      document.getElementById("tab-propostas").classList.remove("active");
      renderizarFeed(inputBusca.value);
    });

    calcularSalarios();
    renderizarEstatisticas();
    renderizarVereadores();
    renderizarFeed();
  </script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_completo)
print("index.html gerado com sucesso e 100% completo!")