import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

function quietGlob(options: Parameters<typeof glob>[0]) {
  const loader = glob(options);

  return {
    ...loader,
    async load(context: Parameters<typeof loader.load>[0]) {
      const originalWarn = context.logger.warn.bind(context.logger);
      const filteredLogger = Object.assign(
        Object.create(Object.getPrototypeOf(context.logger)),
        context.logger,
        {
          warn(message: string) {
            if (message.startsWith('Duplicate id "') && message.includes('Later items with the same id will overwrite earlier ones.')) {
              return;
            }
            originalWarn(message);
          },
        },
      ) as typeof context.logger;

      await loader.load({
        ...context,
        logger: filteredLogger,
      });
    },
  };
}

const topicEnum = z.enum([
  'water', 'mobility', 'housing', 'coastal', 'cultural-heritage',
  'zoning', 'fire', 'recovery', 'ecology', 'infrastructure', 'policy',
]);

const scaleEnum = z.enum([
  'regional', 'district', 'town', 'site', 'node',
]);

const typeEnum = z.enum([
  'analysis', 'proposal', 'precedent', 'data', 'documentation',
]);

const chapterEnum = z.enum([
  'ch1-introduction', 'ch2-overview', 'ch3-analysis',
  'ch4-principles', 'ch5-design',
]);

const tagsSchema = z.object({
  topic: z.array(topicEnum).min(1),
  scale: z.array(scaleEnum).min(1).optional(),
  type: z.array(typeEnum).min(1).optional(),
});

const sections = defineCollection({
  loader: quietGlob({ pattern: '**/*.md', base: './src/content/sections' }),
  schema: z.object({
    title: z.string(),
    chapter: chapterEnum,
    order: z.number().int(),
    summary: z.string(),
    relatedDrawings: z.array(z.string()).default([]),
    relatedSources: z.array(z.string()).default([]),
    relatedTerms: z.array(z.string()).default([]),
    tags: tagsSchema.extend({
      scale: z.array(scaleEnum).min(1),
      type: z.array(typeEnum).min(1),
    }),
  }),
});

const drawings = defineCollection({
  loader: quietGlob({ pattern: '**/*.md', base: './src/content/drawings' }),
  schema: z.object({
    title: z.string(),
    image: z.string(),
    alt: z.string(),
    scaleLevel: scaleEnum,
    drawingType: z.string(),
    display: z.object({
      variant: z.enum(['default', 'board', 'full']).default('default'),
    }).default({ variant: 'default' }),
    pageIntroTitle: z.string().optional(),
    pageIntroText: z.string().optional(),
    relatedSections: z.array(z.string()).default([]),
    tags: tagsSchema.extend({
      scale: z.array(scaleEnum).min(1),
      type: z.array(typeEnum).min(1),
    }),
  }),
});

const sources = defineCollection({
  loader: quietGlob({ pattern: '**/*.md', base: './src/content/sources' }),
  schema: z.object({
    title: z.string(),
    author: z.string(),
    publisher: z.string().optional(),
    date: z.string().optional(),
    sourceType: z.enum(['book', 'report', 'government-doc', 'research-note']),
    relevance: z.string(),
    tags: tagsSchema.extend({
      type: z.array(typeEnum).min(1),
    }),
  }),
});

const terms = defineCollection({
  loader: quietGlob({ pattern: '**/*.md', base: './src/content/terms' }),
  schema: z.object({
    term: z.string(),
    definition: z.string(),
    category: z.enum(['concept', 'hawaiian', 'acronym']),
    relatedSections: z.array(z.string()).default([]),
    tags: tagsSchema,
  }),
});

const maps = defineCollection({
  loader: quietGlob({ pattern: '**/*.md', base: './src/content/maps' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    layers: z.array(z.object({
      name: z.string(),
      file: z.string(),
      color: z.string(),
    })).min(1),
    defaultCenter: z.tuple([z.number(), z.number()]),
    defaultZoom: z.number().int(),
    relatedSections: z.array(z.string()).default([]),
    relatedDrawings: z.array(z.string()).default([]),
    tags: tagsSchema.extend({
      scale: z.array(scaleEnum).min(1),
      type: z.array(typeEnum).min(1),
    }),
  }),
});

const timeline = defineCollection({
  loader: quietGlob({ pattern: '**/*.md', base: './src/content/timeline' }),
  schema: z.object({
    date: z.string(),
    era: z.string(),
    title: z.string(),
    description: z.string(),
    sortOrder: z.number().int(),
    relatedSections: z.array(z.string()).default([]),
    tags: tagsSchema,
  }),
});

const topics = defineCollection({
  loader: quietGlob({ pattern: '**/*.md', base: './src/content/topics' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
  }),
});

const scales = defineCollection({
  loader: quietGlob({ pattern: '**/*.md', base: './src/content/scales' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
  }),
});

export const collections = {
  sections,
  drawings,
  sources,
  terms,
  maps,
  timeline,
  topics,
  scales,
};
