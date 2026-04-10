---
title: "Lahaina Map Explorer"
description: "Interactive GIS layers covering water systems, infrastructure, transportation, hazards, and ecology across the Lahaina recovery area"
layers:
  - name: "Existing Streams (DAR)"
    file: "/data/geojson/streams.geojson"
    color: "#4488cc"
  - name: "Historic Ditches (CWRM)"
    file: "/data/geojson/ditches.geojson"
    color: "#c4a265"
  - name: "Streams with Aquatic Resources"
    file: "/data/geojson/streams_aquatic.geojson"
    color: "#2299cc"
  - name: "Streams with Cultural Resources"
    file: "/data/geojson/streams_cultural.geojson"
    color: "#cc6633"
  - name: "Aquifer Boundaries (DLNR)"
    file: "/data/geojson/aquifers.geojson"
    color: "#2ca89a"
  - name: "Watersheds (CWRM)"
    file: "/data/geojson/watersheds.geojson"
    color: "#8855aa"
  - name: "Hydrologic Units"
    file: "/data/geojson/hydro_units.geojson"
    color: "#6677bb"
  - name: "Dams"
    file: "/data/geojson/dams.geojson"
    color: "#884444"
  - name: "Wastewater Treatment"
    file: "/data/geojson/wwtp.geojson"
    color: "#aa6622"
  - name: "SLR 3.2ft Flood Exposure"
    file: "/data/geojson/slr_exposure.geojson"
    color: "#cc4444"
  - name: "Roads"
    file: "/data/geojson/roads_maui.geojson"
    color: "#888888"
  - name: "Sidewalks and Paths"
    file: "/data/geojson/sidewalks.geojson"
    color: "#44aa66"
  - name: "Existing Bikeways"
    file: "/data/geojson/bikeways_existing.geojson"
    color: "#33bb55"
  - name: "Proposed Bikeways"
    file: "/data/geojson/bikeways_proposed.geojson"
    color: "#33bb55"
  - name: "Public Schools"
    file: "/data/geojson/schools_public.geojson"
    color: "#dd6699"
  - name: "Private Schools"
    file: "/data/geojson/schools_private.geojson"
    color: "#bb4477"
defaultCenter: [20.8900, -156.6600]
defaultZoom: 13
relatedSections: ["pioneer-mill-water-infrastructure", "environmental-analysis", "water-crisis", "fire-analysis", "mobility-street-design", "cultural-heritage-strategy"]
relatedDrawings: ["composite-regional-analysis", "regional-streams-ditches", "sea-level-rise"]
tags:
  topic: [water, infrastructure, coastal, mobility, ecology]
  scale: [regional, district, town]
  type: [analysis]
---

Interactive map of the Lahaina recovery area from coast to mountain summit. Toggle GIS layers to explore the water systems, infrastructure, transportation networks, and hazard zones that define the recovery analysis. All data sourced from Hawaii State GIS ([geoportal.hawaii.gov](https://geoportal.hawaii.gov)), DLNR, CWRM, and FEMA.

16 layers organized by topic:

**Water Systems:** Existing streams (DAR), historic plantation ditches (CWRM), streams with aquatic resources, streams with cultural resources, aquifer boundaries (DLNR), watersheds (CWRM), hydrologic units, dams, wastewater treatment plants

**Hazards:** Sea level rise 3.2ft flood exposure zone (Maui)

**Transportation:** Roads, sidewalks and paths, existing bikeways, proposed bikeways

**Community:** Public schools, private schools
