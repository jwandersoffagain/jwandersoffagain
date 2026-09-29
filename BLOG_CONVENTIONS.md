# J Wanders Off Again, Blog Conventions

A working document for how the blog is structured, styled, and built. Update this over time as things solidify. If a decision keeps coming up, it belongs here. (For how I *write* the words themselves, see VOICE_GUIDE.md.)

---

## Voice & tone (short summary)

**This blog is a personal journal that happens to be public.** Not a travel content creator, not a guidebook, not a lifestyle brand. Everything below flows from that. For the full voice guide, see VOICE_GUIDE.md.

- Warm, honest, conversational
- Anonymous (no face photos, no author cards, no signature sign-offs)
- Honest about the mess and honest about money
- Direct opinions
- 80% polished, 20% raw phrasing preserved

---

## What to include in a post

- **Prices in local currency**, with the local symbol. Yen: ¥1,823. USD: $99. CAD: $135.
- **Practical asides** woven into the paragraphs. Not in boxes. Things like: getting-around tips, when to visit a crowded spot, luggage warnings, "would I go back?"
- **The emotional moments.** The solo shrine visit, the mom guilt, the surrender-to-FamilyMart-dinner nights. These are usually the most valuable parts.
- **Specific place names when I remember them.** Restaurants, shrines, shops, hotels. Naming places gives the post practical value (readers can find them) AND makes the writing feel more concrete and lived-in ("a local motorcycle shop" reads vaguer than "Cook's Motorcycle in Gion"). But NEVER fabricate a name. If I can't remember, just describe the place. "A small local place we can't remember the name of" is honest and journal-like.
- **A cost breakdown at the end that pairs a prose paragraph with a scannable table.** The prose gives the warm reflection ("this was for our anniversary, we chose to splurge"), and the table gives the scannable numbers. Both together — the prose keeps it journal-y, the table gives readers a genuine differentiator vs other travel blogs and pulls people to scroll to the end. Split the table into **Essentials** and **Splurges (worth it)** so readers can see what was necessary vs chosen.
- **A closing reflection line** in italic. Not preachy, just honest. What did this trip actually give me?

---

## What to leave out

- **No photos of me or the kids' faces.** Landscape, food, and back-of-body shots are fine. If a photo has our faces, don't use it.
- **No "About me" content in the posts.** That lives on the homepage. Posts stay focused on the trip.
- **No author cards or sign-offs.** Not "xo J", not "Written by J with photo." The writing does the work.
- **No sponsorships or affiliate pushes** in the post body. (The Wise referral link in NYC is one exception, a genuinely useful tool for the exchange rate problem.)
- **No embedded links to shops/restaurants/places by default.** Naming a place is enough. Readers can Google if they want to visit. Embedded links turn a journal into a directory, and they create an expectation that every place mentioned should be linkable. If I share a URL in chat, it's usually for the writer's reference to understand what the place is, NOT a signal to publish it. Ask before embedding. Exceptions: genuinely useful tools that saved us significant money or hassle (Wise for exchange rates is the model here). Never `share.google` URLs — those are personal share links from a specific device, not canonical URLs, and they can behave unpredictably.
- **No mental health disclosure by name.** The rough moments belong in the writing. The specific label (anxiety, burnout, etc.) stays off the blog for now. People in my circle don't know, and the blog is where I process it, not where I announce it.
- **No forced positivity.** If a trip was hard, the post should reflect that. Redemption arcs (Day 1 rough, Day 2 saved it) are real and land better than pretending everything was great.
- **No bold text anywhere in the post body or captions.** Bolding words breaks the visual flow of a journal and gives the blog a listicle/marketing feel. If a word or phrase truly needs emphasis, italics (`<em>`) can carry it. Otherwise let the writing itself do the work. This applies to place names too — don't bold restaurant names, hotel names, or shop names. Naming them in plain text is enough.

---

## Post structure template

Every post follows this shape:

1. **Hero.** Big photo, tag chip (e.g. "Family Trip · Kyoto, Japan"), city name as headline, italic emphasis subtitle underneath, date and read time.
2. **Opening 1 to 3 paragraphs.** Arrival, context, first impressions. Sets the emotional tone.
3. **Divider** (✦)
4. **Day / section blocks.** Each has a `section-label` (e.g. "Day 1") and an h2 with a specific, evocative subtitle in italic. Not "Day 1: Venice Beach" but "Day 1, Venice Beach Food Tour" with an italic phrase.
5. **Body of the section.** Paragraphs, inline photos, tip callouts, occasionally a pull quote for a punchy emotional line.
6. **One "wide hero photo" per section.** The standout photo of that day gets the `post-img-wide` treatment (880px). Everything else stays standard (540px).
7. **Repeat for each day**, separated by dividers.
8. **Cost breakdown.** Split into Essentials and Splurges, with a short context line above.
9. **Closing paragraph.** A real reflection, not a call to action. What did this trip actually give me?
10. **`closingLine` prop.** One italic line at the very bottom, right before the "Back to blog" button. This is the emotional signoff.

**Length target:** 4 to 7 minute read for a short trip (LA/weekend), 7 to 10 minutes for a longer trip. If a trip is longer than a week, split it into multiple posts by city or by natural narrative chapters.

---

## Design rules

Keep these fixed unless there's a very good reason to change them.

**Fonts:**
- Jost throughout the site. Body, headings, everything. (Gilda Display only for the "J Wanders Off Again" logo.)
- Weight 300 for large headings (matches index page).
- Italic for emphasis (`<em>`), never bold-italic, never handwritten script fonts.

**Colors** (the current palette works, don't keep chasing new ones):
- Background: cream `#F8F6F1`
- Primary accent: denim blue `#5A7E9E` (section labels, buttons, hover states)
- Secondary accent: dusty rose `#D4A8B0` (tag chips, italic emphasis in hero, warm callout borders)
- Text: dark ink `#1A2028`

**Typography ratios:**
- Text column: 660px max (comfortable reading width)
- Wrap container: 1000px max
- Standard photo: 540px max width, natural aspect ratio (no forced cropping)
- Wide "hero" photo: 880px max width, 760px max height
- Photo grid pairs: 4:3 forced with `object-fit: cover`

---

## Photo rules

- **Natural aspect ratios always.** Portrait shots stay portrait, landscape stays landscape. No cropping via CSS.
- **Consistency by choosing well, not by forcing shapes.** Try to shoot mostly one orientation per trip if possible, but if I mix, the code handles it gracefully.
- **Never photos of faces** (mine or the kids'). Backs, hands, feet in shot are fine.
- **All standalone photos use the same 540px max-width.** No "wide hero" photos anymore. Uniform footprint across all standalone shots so nothing dominates unevenly. Heights still vary based on natural aspect ratio (that's fine, we don't crop). Grid pairs are the only exception because they're two-up.
- **Grid pairs when photos naturally pair up** (before/after, two food shots, two views of the same scene).
- **Captions add context, not description.** "The matcha float. Rich, creamy, perfectly balanced. The one drink I'm still thinking about." Not "A green drink."

---

## Money & currency conventions

- **Yen:** `¥1,823` (yen symbol, comma separator, no space)
- **Currency format across all posts: local currency first, CAD in parens.**
  - US posts: `$99 USD ($135 CAD)`
  - Japan posts: `¥6,400 (~$60 CAD)`
  - This is what a reader would experience: they see the local price on a menu/receipt, and the parens tell them what it means in their own currency.
- **CAD approximations use `~$X` prefix.** The tilde signals it's a conversion estimate, not an exact figure.
- **Approximate:** prefix with `~`. Examples: `~¥30 split`, `~$213 USD`
- **Ranges:** use the word "to". Example: `¥880 to ¥2,380`. Never en-dash or em-dash.
- **Cost table structure:** always Essentials first, then Splurges (worth it). If prices weren't recorded for some items, add a note above the table saying so. Don't fabricate numbers.
- **Always round UP.** Prices in the blog should be slight overestimates, never underestimates. Readers should have a buffer to plan with, not get sticker shock. In every post's money paragraph, include a note near the start telling readers this: "Just so you know, I round up when I share prices on the blog so you have a bit of a buffer to work with, better to overestimate than underestimate." Or a natural variation. This is a durable practice, not a one-time note. It builds trust with the reader.

---

## Anti-patterns (already tried, ruled out)

Things we've experimented with and rejected. Don't keep proposing these.

- ❌ **Cormorant Garamond** (too editorial/magazine-y)
- ❌ **Fraunces** (still reads too editorial even with soft variant)
- ❌ **Caveat / handwritten script fonts** (feels cheesy for long text, only OK for very short accent lines)
- ❌ **Drop caps** (serif convention that doesn't fit journal vibe)
- ❌ **By-the-numbers stats line at top** ("3 days · 8 meals · ...") doesn't land, feels forced
- ❌ **Author cards / "hi I'm J" intros in post bodies** (breaks anonymity, unnecessary)
- ❌ **"xo J" sign-offs** (everyone does it, feels performative)
- ❌ **Peach / terracotta / champagne colors** (too warm-boho, doesn't feel like me)
- ❌ **Sage green** (didn't work in mockup)
- ❌ **Burgundy / vintage wine** (pretty color but doesn't work for this blog)
- ❌ **Table of contents at top of posts** (makes it feel too clinical, like a guidebook)
- ❌ **Em dashes and en dashes anywhere in the blog.** These are the strongest AI signature. Use commas, periods, colons, parentheses, or the word "to" for ranges. See VOICE_GUIDE.md for the full rule.

---

## What to do when I'm iterating

- **Stop chasing colors/fonts.** The palette and typography are settled. If something "doesn't feel like me," look at *structure*, *content*, or *whether I've lived with it long enough* first.
- **Give myself time.** Something that feels off after 1 hour of staring often feels fine after a week of not looking.
- **Read the live site as a reader**, not the local preview as a designer. Different mental mode.
- **The writing is the star.** Design should get out of the way. Anything I add should serve the writing, not compete with it.

---

*Last updated: June 2026. Update this doc when I make a lasting decision, otherwise the same conversations will keep repeating.*
