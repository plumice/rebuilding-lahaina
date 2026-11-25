/**
 * Fetches Lahaina/Maui news from Google News RSS and writes a static JSON file.
 * Runs via GitHub Actions on a cron schedule.
 */
import { writeFileSync } from 'fs';

function extractCDATA(text) {
  const match = text.match(/<!\[CDATA\[(.*?)\]\]>/s);
  return match ? match[1] : text;
}

function stripHtml(html) {
  return html.replace(/<[^>]*>/g, '').trim();
}

// Lahaina recovery and redevelopment only. Google News `when:` limits results by age.
const QUERIES = [
  'Lahaina rebuild',
  'Lahaina recovery',
  'Lahaina wildfire',
  'Lahaina housing',
  'Lahaina permits',
  'Maui wildfire recovery',
  'Maui fire rebuilding',
].map((q) => encodeURIComponent(`${q} when:60d`));

const MAX_AGE_DAYS = 60;

// A headline counts when it names Lahaina, or names Maui/West Maui together with a recovery term.
const RECOVERY_TERMS = [
  'wildfire', 'fire', 'burn', 'rebuild', 'recover', 'housing', 'permit', 'survivor',
  'displaced', 'fema', 'debris', 'settlement', 'redevelop', 'long-term', 'resilien',
  'temporary', 'kauhale', 'zoning', 'water', 'land use', 'reconstruct',
];
// Sports and tourism promotion that share the word "Maui".
const EXCLUDE_TERMS = [
  'invitational', 'basketball', 'football', 'ncaa', 'prediction', 'pick', ' vs ', 'vs.',
  'golf', 'pga', 'sentry', 'tournament', 'semifinal', 'semis', 'bracket', 'ole miss',
  'odds', 'betting', 'volleyball', 'surf contest',
];

function isRelevant(title) {
  const t = ` ${title.toLowerCase()} `;
  if (EXCLUDE_TERMS.some((w) => t.includes(w))) return false;
  if (t.includes('lahaina')) return true;
  const placeHit = t.includes('maui') || t.includes('hawaii') || t.includes('hawaiʻi');
  return placeHit && RECOVERY_TERMS.some((w) => t.includes(w));
}

async function fetchNews() {
  const queries = QUERIES;
  const allItems = [];

  for (const query of queries) {
    const url = `https://news.google.com/rss/search?q=${query}&hl=en-US&gl=US&ceid=US:en`;
    try {
      const resp = await fetch(url, {
        headers: { 'User-Agent': 'Mozilla/5.0 (compatible; RebuildingLahaina/1.0)' },
        signal: AbortSignal.timeout(5000),
      });
      if (!resp.ok) continue;
      const xml = await resp.text();

      const itemRegex = /<item>([\s\S]*?)<\/item>/g;
      let match;
      while ((match = itemRegex.exec(xml)) !== null) {
        const itemXml = match[1];
        const titleMatch = itemXml.match(/<title>([\s\S]*?)<\/title>/);
        const linkMatch = itemXml.match(/<link>([\s\S]*?)<\/link>/);
        const pubDateMatch = itemXml.match(/<pubDate>([\s\S]*?)<\/pubDate>/);
        const sourceMatch = itemXml.match(/<source[^>]*>([\s\S]*?)<\/source>/);

        if (titleMatch && linkMatch) {
          const source = sourceMatch ? stripHtml(extractCDATA(sourceMatch[1])) : 'Google News';
          let title = stripHtml(extractCDATA(titleMatch[1]));
          if (title.endsWith(` - ${source}`)) title = title.slice(0, -(source.length + 3));
          title = title.replace(/^News:\s*/i, '');
          if (!isRelevant(title)) continue;
          const date = pubDateMatch ? pubDateMatch[1].trim() : '';
          const ageDays = date ? (Date.now() - new Date(date).getTime()) / 86400000 : Infinity;
          if (!(ageDays <= MAX_AGE_DAYS)) continue;
          allItems.push({
            title,
            link: extractCDATA(linkMatch[1]).trim(),
            source,
            date: pubDateMatch ? pubDateMatch[1].trim() : '',
          });
        }
      }
    } catch (err) {
      console.error(`Failed to fetch ${query}:`, err.message);
    }
  }

  // Sort newest first so the earliest copy of a repeated story is dropped
  allItems.sort((a, b) => (b.date ? Date.parse(b.date) : 0) - (a.date ? Date.parse(a.date) : 0));

  // Deduplicate: the same story often runs at several outlets under slightly different headlines
  const STOP = new Set(['the', 'a', 'an', 'of', 'to', 'in', 'on', 'for', 'and', 'news', 'maui', 'lahaina', 'with', 'at', 'is', 'as', 'by']);
  const words = (t) => new Set(t.toLowerCase().replace(/[^a-z0-9ʻāēīōū ]/g, ' ').split(/\s+/).filter((w) => w.length > 2 && !STOP.has(w)));
  const kept = [];
  const unique = allItems.filter((item) => {
    const w = words(item.title);
    for (const k of kept) {
      const inter = [...w].filter((x) => k.has(x)).length;
      if (inter / Math.min(w.size, k.size || 1) >= 0.6) return false;
    }
    kept.push(w);
    return true;
  });

  // Sort newest first
  unique.sort((a, b) => {
    const dateA = a.date ? new Date(a.date).getTime() : 0;
    const dateB = b.date ? new Date(b.date).getTime() : 0;
    return dateB - dateA;
  });

  if (unique.length === 0) {
    console.log('No relevant items found; keeping the existing news.json.');
    return;
  }

  const output = {
    items: unique.slice(0, 8),
    updated: new Date().toISOString(),
  };

  writeFileSync('public/data/news.json', JSON.stringify(output, null, 2));
  console.log(`Wrote ${output.items.length} news items (${new Date().toISOString()})`);
}

fetchNews();
