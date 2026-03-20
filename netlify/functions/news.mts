import type { Context } from "@netlify/functions";

interface NewsItem {
  title: string;
  link: string;
  source: string;
  date: string;
}

function extractCDATA(text: string): string {
  const match = text.match(/<!\[CDATA\[(.*?)\]\]>/s);
  return match ? match[1] : text;
}

function stripHtml(html: string): string {
  return html.replace(/<[^>]*>/g, '').trim();
}

export default async function handler(req: Request, _context: Context) {
  const headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Cache-Control": "public, max-age=900", // Cache 15 minutes
  };

  try {
    // Fetch Google News RSS for Lahaina and Maui
    const queries = ["Lahaina+Maui", "Maui+Hawaii+recovery"];
    const allItems: NewsItem[] = [];

    for (const query of queries) {
      const url = `https://news.google.com/rss/search?q=${query}&hl=en-US&gl=US&ceid=US:en`;
      const resp = await fetch(url, {
        headers: { "User-Agent": "Mozilla/5.0 (compatible; RebuildingLahaina/1.0)" },
      });

      if (!resp.ok) continue;

      const xml = await resp.text();

      // Parse RSS items with simple regex (no XML parser needed)
      const itemRegex = /<item>([\s\S]*?)<\/item>/g;
      let match;
      while ((match = itemRegex.exec(xml)) !== null) {
        const itemXml = match[1];

        const titleMatch = itemXml.match(/<title>([\s\S]*?)<\/title>/);
        const linkMatch = itemXml.match(/<link>([\s\S]*?)<\/link>/);
        const pubDateMatch = itemXml.match(/<pubDate>([\s\S]*?)<\/pubDate>/);
        const sourceMatch = itemXml.match(/<source[^>]*>([\s\S]*?)<\/source>/);

        if (titleMatch && linkMatch) {
          const title = stripHtml(extractCDATA(titleMatch[1]));
          // Skip if title doesn't seem relevant
          if (!title.toLowerCase().includes('maui') &&
              !title.toLowerCase().includes('lahaina') &&
              !title.toLowerCase().includes('hawaii') &&
              !title.toLowerCase().includes('wildfire')) {
            continue;
          }

          allItems.push({
            title,
            link: extractCDATA(linkMatch[1]).trim(),
            source: sourceMatch ? stripHtml(extractCDATA(sourceMatch[1])) : "Google News",
            date: pubDateMatch ? pubDateMatch[1].trim() : "",
          });
        }
      }
    }

    // Deduplicate by title similarity and limit to 8
    const seen = new Set<string>();
    const unique = allItems.filter((item) => {
      const key = item.title.toLowerCase().slice(0, 50);
      if (seen.has(key)) return false;
      seen.add(key);
      return true;
    });

    // Sort by date (newest first)
    unique.sort((a, b) => {
      const dateA = a.date ? new Date(a.date).getTime() : 0;
      const dateB = b.date ? new Date(b.date).getTime() : 0;
      return dateB - dateA;
    });

    return new Response(JSON.stringify({ items: unique.slice(0, 8) }), { headers });
  } catch (error) {
    return new Response(
      JSON.stringify({ items: [], error: "Unable to fetch news" }),
      { status: 200, headers }
    );
  }
}
