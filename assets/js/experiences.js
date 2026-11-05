// Preserve technical links shared before the portfolio entrance was introduced.
(() => {
  if (document.body.dataset.page !== 'entrance' || !location.hash) return;
  const sections = new Set(["main", "top", "about", "projects", "infrastructure", "problems", "impact", "industries", "stack", "experience", "evidence", "credentials", "current-focus", "contact", "signature-it-student", "drabpe-it-consultant", "signature-summer-intern", "drabpe-community-relations", "cdcd-device-management", "freelance-web-designer", "drabpe-website-designer", "drabpe-content-developer"]);
  if (sections.has(location.hash.slice(1))) location.replace('it.html' + location.hash);
})();
