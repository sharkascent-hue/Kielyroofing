#!/usr/bin/env python3
"""Builds the Kiely Roofing & Construction site: every page shares one header, footer and set of sections.
Edit the content below, then run:  python3 build.py   (writes the .html files next to this script)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://kielyconstruction.ie'
PHONE, TEL, EMAIL = '087 359 2163', 'tel:+353873592163', 'info@kielyroofing.ie'
WAURL = 'https://wa.me/353873592163'

# ---------- icons ----------
def svg(body, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
I = {
    'arrow': svg('<path d="M5 12h14M13 6l6 6-6 6"/>', 'arr'),
    'arrowup': svg('<path d="M7 17L17 7M8 7h9v9"/>'),
    'phone': svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>'),
    'mail': svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>'),
    'pin': svg('<path d="M12 22s-8-6.6-8-12a8 8 0 0 1 16 0c0 5.4-8 12-8 12z"/><circle cx="12" cy="10" r="3"/>'),
    'check': svg('<path d="M20 6L9 17l-5-5"/>'),
    'chev': svg('<path d="M6 9l6 6 6-6"/>'),
    'x': svg('<path d="M18 6L6 18M6 6l12 12"/>'),
    'left': svg('<path d="M15 18l-6-6 6-6"/>'),
    'right': svg('<path d="M9 18l6-6-6-6"/>'),
    'bolt': svg('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'),
    'shield': svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>'),
    'quote': svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>'),
    'star': svg('<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>'),
    'clock': svg('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
    'house': svg('<path d="M3 11l9-8 9 8"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>'),
    'wrench': svg('<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8z" transform="scale(.9) translate(1.3 1.3)"/>'),
    'layers': svg('<path d="M12 2l10 5-10 5L2 7z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>'),
    'drop': svg('<path d="M12 2.7l5.7 5.6a8 8 0 1 1-11.4 0z"/>'),
    'chimney': svg('<path d="M3 12l9-8 9 8"/><path d="M15 6.5V3h3v6"/><path d="M5 10.5V21h14V10.5"/>'),
    'gutter': svg('<path d="M3 6h18v3a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3z"/><path d="M17 12v9M7 15v2M11 15v4"/>'),
    'storm': svg('<path d="M19 16.9A5 5 0 0 0 18 7h-1.3A8 8 0 1 0 4 15.3"/><path d="M13 11l-4 6h6l-4 6"/>'),
    'roof': svg('<path d="M2 12L12 3l10 9"/><path d="M6 8.5V5h3"/><path d="M5 12v9h14v-9"/>'),
    'hammer': svg('<path d="M15 12l-8.5 8.5a2.1 2.1 0 0 1-3-3L12 9"/><path d="M17.6 15L22 10.6M20.9 11.7l-4.6-4.6a3 3 0 0 0-2.1-.9h-1.8L10 4l1.8-1.8h3.5a6 6 0 0 1 4.2 1.8l2.6 2.6"/>'),
    'chat': svg('<path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 21l2-5.4A8.4 8.4 0 1 1 21 11.5z"/>'),
    'search': svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>'),
    'broom': svg('<path d="M19.4 2.6l-7.8 7.8"/><path d="M11 9l4 4-3.5 8.5L3 13z"/><path d="M7 17l-2 2"/>'),
    'fb': svg('<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>'),
}
WA = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c0-.2-.3-.3-.6-.5z"/></svg>'
HOUSE_SVG = '<svg class="house" viewBox="0 0 400 260" fill="none" stroke="#fff" stroke-width="22" stroke-linejoin="miter"><path d="M10 250L170 40l160 210"/><path d="M215 60l45-35 130 225"/><path d="M290 70V20h34v95"/></svg>'
I['search'] = svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>')
I['euro'] = svg('<path d="M17 6.5A7 7 0 1 0 17 17.5"/><path d="M4 10h9M4 14h9"/>')
I['users'] = svg('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>')
I['leaf'] = svg('<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/>')
I['heart'] = svg('<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>')
I['fire'] = svg('<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3.4.2 1.6 1.5 2.9 2.5 2.9z"/>')
I['trend'] = svg('<path d="M23 6l-9.5 9.5-5-5L1 18"/><path d="M17 6h6v6"/>')
I['sun'] = svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>')
I['wind'] = svg('<path d="M9.6 4.6A2 2 0 1 1 11 8H2M12.6 19.4A2 2 0 1 0 14 16H2M17.7 7.7A2.5 2.5 0 1 1 19.5 12H2"/>')
I['sparkle'] = svg('<path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2z"/>')

I['paint'] = svg('<rect x="3" y="3" width="15" height="7" rx="1.5"/><path d="M18 6.5h2.5V12H11v3"/><rect x="9" y="15" width="4" height="6" rx="1"/>')
I['trowel'] = svg('<path d="M3 21l7-7"/><path d="M14 4l6 6-8 8-6-6z"/>')
I['attic'] = svg('<path d="M2 20L12 4l10 16z"/><path d="M8 20v-5h8v5"/><path d="M12 9v2"/>')
I['ext'] = svg('<path d="M2 11l7-6 7 6"/><path d="M4 9.5V20h10V9.5"/><path d="M14 13h8v7h-8"/>')
I['reno'] = svg('<path d="M3 11l9-8 9 8"/><path d="M5 9.5V21h14V9.5"/><path d="M9 14l2 2 4-4"/>')
I['verge'] = svg('<path d="M2 18L12 6l10 12"/><path d="M5 18L12 9.5 19 18"/>')
I['camera'] = svg('<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>')
I['map'] = svg('<path d="M1 6v16l7-4 8 4 7-4V2l-7 4-8-4z"/><path d="M8 2v16M16 6v16"/>')
I['gauge'] = svg('<path d="M12 14l4-4"/><path d="M3.3 19a10 10 0 1 1 17.4 0"/>')

# ---------- content (all from kielyroofing.ie) ----------
def S(slug, name, group, icon, hero, eyebrow, h2, intro, list_h, list_intro, items, list_outro, cta, details, reviews, imgs, gallery=None, ba=None, title=None, desc=None):
    return dict(slug=slug, name=name, group=group, icon=icon, hero=hero, eyebrow=eyebrow, h2=h2, intro=intro, list_h=list_h, list_intro=list_intro,
                items=items, list_outro=list_outro, cta=cta, details=details, reviews=reviews, imgs=imgs, gallery=gallery or [], ba=ba or [], title=title, desc=desc)

SERVICES = [
 S('roof-repairs', 'Roof Repairs', 'roof', 'hammer', 'roof-repair2.jpg', 'Leak finding & repairs', 'Roof Repair',
   ['Kiely Roofing & Construction provides roof repair services across Meath, Kildare, Dublin and surrounding areas.',
    'If your roof is leaking, tiles have slipped or storm damage has left part of the roof exposed, getting the problem dealt with early can help prevent more expensive damage inside the property.',
    'We carry out repairs for a range of common roofing problems, from smaller localised issues to more extensive damage affecting larger sections of the roof.'],
   'Roof Repairs for Leaks, Damage & General Wear', 'Roof problems can develop for a lot of different reasons. Some are caused by weather, while others come down to age, movement or worn roofing materials. We can help with issues including:',
   ['Leaking roofs', 'Slipped or broken tiles', 'Storm damage', 'Damaged flashing', 'Problems around chimneys', 'Damaged roof sections', 'General wear and deterioration'], '', 'Get Your Roof Checked',
   [('Emergency Roof Repairs', ['Some roofing problems cannot wait.', 'If high winds, heavy rain or sudden damage have left your roof exposed, emergency repair work can help make the property secure and reduce the risk of further water damage.', 'Kiely Roofing includes emergency roof repairs within its roofing services.'], []),
    ('Repair or Replace?', ['Not every damaged roof needs to be replaced.', 'In many cases, a focused repair may be enough to extend the life of the existing roof. Where the roof is older, badly deteriorated or suffering from repeated problems, replacement may be the better long-term option.', 'Not sure? Take our <a href="{p}roof-health-check/">60-second roof check</a> or view our <a href="{p}roof-replacement/">Roof Replacement</a> service.'], []),
    ('Other Roofing Services', ['Roof problems can sometimes involve more than one part of the roof. Kiely Roofing also carries out:'], ['Chimney Repairs', 'Flat Roofing', 'Guttering', 'Dry Verge Systems', 'Roof Replacement'])],
   [('Brian Farrell', 'We noticed a leak after heavy rain and contacted them to have a look. They found the problem, explained what was causing it and carried out the repair quickly. No problems with the roof since.'),
    ('Orla Fitzpatrick', 'We called Kiely Roofing after finding a few damaged tiles on our roof. They were straightforward about what actually needed doing and had everything repaired quickly. Very good service.')],
   ('roof-repair-before-after.jpg', 'roof-replacement-mkd.jpg'), ['roof-repairs-mkd-2.jpg', 'roof-repair-dublin.jpg', 'roof-replace-1.jpg'],
   title='Roof Repairs in Meath, Kildare & Dublin', desc='Roof repairs across Meath, Kildare & Dublin from Kiely Roofing & Construction. Leaks, slipped tiles, flat roofs & storm damage fixed fast.'),
 S('roof-replacement', 'Roof Replacement', 'roof', 'roof', 'roof-replacement-3b.jpg', 'Full roof replacements', 'Roof Replacement',
   ['If you’re patching the same leak every winter, it’s time to stop paying for repairs and start planning a new roof. Kiely Roofing & Construction replaces pitched and flat roofs for homeowners, landlords and businesses right across Meath, from Navan and Trim to Ashbourne, Ratoath and the coast at Laytown and Bettystown.',
    'We survey your roof, explain exactly what needs doing and give you a fixed written quote. No pressure, no vague estimates.'],
   'When to Replace Your Roof', 'Not every problem needs a new roof, and we’ll always tell you if a repair will do the job. Replacement is usually the right call when you see:',
   ['Leaks appearing in different places', 'Slipped, cracked or missing slates and tiles across large areas', 'Sagging along the ridge or roof line', 'Damp, mould or daylight in the attic', 'Heavy moss lifting tiles and holding water', 'Old felt that has perished or torn'], '', 'Get a Free Quote',
   [('Roof Replacement Services', ['<b>Slate roofs.</b> Natural and fibre cement slate, fixed to stand up to exposed rural sites and Atlantic weather.', '<b>Tiled roofs.</b> Concrete and clay tile re-roofs with new breathable membrane and battens throughout.', '<b>Flat roofs.</b> Full flat roof installation for extensions, garages, dormers and commercial units.', '<b>Dry verge systems.</b> Fitted as standard on re-roofs to replace mortar verges that crack and fall away over time.'], []),
    ('Roof Replacement Cost in Meath', ['There’s no fixed price to replace a roof because no two roofs are the same. The main things that affect the cost are:'], ['The size and pitch of the roof', 'Your choice of slate, tile or flat roof system', 'The condition of the rafters and timbers underneath', 'Scaffolding and access around the property', 'Valleys, dormers and roof windows']),
    ('How It Works', ['<b>1. Free survey.</b> We inspect the roof, attic and timbers and talk you through your options.', '<b>2. Fixed written quote.</b> A clear, itemised price with materials and timescale.', '<b>3. Scaffolding and protection.</b> Your property, garden and driveway are protected before work starts.', '<b>4. Strip and inspect.</b> Old coverings come off and we check rafters and timbers, repairing anything rotten.', '<b>5. New roof fitted.</b> Membrane, battens, slates or tiles, ridge, verges, leadwork and ventilation.', '<b>6. Clean up and sign off.</b> All waste removed and a final walk round with you.'], [])],
   [('John O’Connell', 'We contacted Kiely Roofing about replacing our old roof as it had started causing problems over the past few years. They talked us through the options and gave us a clear quote before starting. The work was completed to a high standard and everything was left clean and tidy. Very pleased with the new roof.'),
    ('Elaine Murray', 'Delighted with our new roof from Kiely Roofing. The work was organised well, the site was kept tidy and everything was completed to a very high standard. We’d have no hesitation recommending them.')],
   ('slate-roof-replacement.jpg', 'roof-replacement-mkd-2.jpg'), ba=[('roof-replacement-2a.jpg', 'roof-replacement-2b.jpg'), ('roof-replacement-3a.jpg', 'roof-replacement-3b.jpg'), ('roof-replacement-1a.jpg', 'roof-replacement-1b.jpg')],
   title='Roof Replacement Meath, Kildare & Dublin', desc='New roofs and full roof replacements across Meath, Kildare & Dublin. Slate, tile & flat roofs with a free survey and fixed written quote.'),
 S('chimney-repairs', 'Chimney Repairs', 'roof', 'chimney', 'chimney-1.jpg', 'Chimney repairs & restoration', 'Chimney Repairs',
   ['Chimneys take the full force of the weather all year round. Over time, cracked mortar, loose brickwork and worn flashing let water into your home, often long before you spot anything from the ground.',
    'Kiely Roofing & Construction repairs chimneys across Meath, Kildare, Dublin and surrounding counties. Every job starts with a free survey and a fixed written quote.'],
   'Signs Your Chimney Needs Repair', '', ['Cracked or crumbling mortar', 'Loose or damaged brickwork', 'Leaks or damp patches near the chimney breast', 'Lifted, cracked or missing flashing', 'Damp in the attic around the chimney stack'], '', 'Get a Free Quote',
   [('Chimney Repointing', ['Weathered mortar lets water soak into the chimney stack. We rake out the damaged joints and repoint them to make the stack weathertight again and stop further damage.'], []),
    ('Chimney Flashing Repairs', ['Flashing seals the joint where your chimney meets the roof, and it’s one of the most common causes of chimney leaks. We repair or replace damaged flashing so water runs off the roof instead of into your home.'], []),
    ('Leaks Around the Chimney', ['A leak near the chimney doesn’t always mean the chimney is the problem. Flashing, slipped slates or the roof around the stack can all let water in. We find the actual source before we start, so you only pay for the repair you need.'], [])],
   [('Patrick Byrne', 'We had a problem with our chimney that had been getting worse for a while. The lads identified what needed to be repaired, explained everything clearly and got the work sorted without any fuss. Very happy with the result.'),
    ('Aoife Brennan', 'Kiely Roofing repaired and repointed our chimney and did an excellent job. They arrived when arranged, worked efficiently and left everything clean afterwards. Would happily use them again.')],
   ('chimney-services-6.jpg', 'chimney-repair.jpg'), ['chimey-repairs-mkd-2.jpg', 'chimney-repair-copy.jpg', 'chimey-repairs-mkd.jpg'],
   title='Chimney Repairs Meath, Kildare & Dublin | Repointing, Flashing', desc='Chimney repairs, repointing and flashing repairs across Meath, Kildare & Dublin. Free survey and fixed written quote from Kiely Roofing.'),
 S('flat-roofing', 'Flat Roofing', 'roof', 'layers', 'flat-roof1.jpg', 'Flat roofing & repairs', 'Flat Roofing Contractors',
   ['Kiely Roofing & Construction provides flat roofing repairs and installation across Meath, Kildare, Dublin and surrounding areas.',
    'Flat roofs need to be properly installed and maintained to prevent water from pooling or finding its way into the property. Whether you have a leak, visible surface damage or an older flat roof that is starting to fail, we can assess the condition of the roof and recommend the work required.'],
   'Flat Roof Repairs', 'Flat roof problems can develop gradually or appear suddenly after heavy rain or bad weather. Common issues can include:',
   ['Leaking flat roofs', 'Cracks or splits in the roof covering', 'Damaged or worn sections', 'Water pooling on the surface', 'Deterioration around roof edges', 'Recurring leaks', 'Ageing roofing materials'], '', 'Get a Free Quote',
   [('Flat Roof Installation', ['Where a flat roof is badly deteriorated or forms part of a new extension or renovation, a replacement or new installation may be the better option.', 'The exact work required will depend on the condition of the existing roof, the structure underneath and the size and layout of the area being covered.'], []),
    ('Repair or Replace a Flat Roof?', ['Not every leaking flat roof needs to be completely replaced.', 'A targeted repair may be suitable where the damage is limited to one area. If the roof has widespread deterioration, repeated leaks or ongoing problems, replacement may provide a better long-term solution.', 'Kiely Roofing can assess the condition of the roof and advise on the most appropriate option.'], []),
    ('Related Roofing Services', [], ['Roof Repairs', 'Roof Replacement', 'Chimney Repairs', 'Guttering', 'Dry Verge Systems'])],
   [('Michael Keane', 'Our old flat roof had started giving us problems and needed replacing. The new roof looks excellent and, most importantly, we’ve had no issues since. The team were reliable and easy to deal with throughout.'),
    ('Laura Nolan', 'Kiely Roofing replaced our flat roof and we couldn’t be happier with the work. They explained the different options clearly, gave us a straightforward price and completed everything to a very high standard.')],
   ('flat-roof-before-after.jpg', 'flat-roof-1.jpg'), ['flat-roof-2.jpg', 'flat-roof-installers-mkd-2.jpg', 'flat-roof-installers-mkd.jpg'],
   title='Flat Roofing Contractors Meath, Kildare & Dublin', desc='Flat roof repairs, replacement and new installations across Meath, Kildare & Dublin from Kiely Roofing & Construction.'),
 S('guttering', 'Guttering', 'roof', 'gutter', 'gutter-1.jpg', 'Gutter repairs & installation', 'Guttering Contractors',
   ['Leaking, damaged or worn-out gutters? Kiely Roofing & Construction provides gutter repairs and new installations across Meath, Kildare, Dublin and surrounding areas.',
    'Whether you need a small repair, replacement guttering or a completely new system, get in touch for a free quote.'],
   'Signs Your Gutters Need Attention', 'Some gutter problems only become obvious during heavy rain. Common warning signs include:',
   ['Water overflowing from the gutters', 'Leaks or dripping at gutter joints', 'Gutters pulling away from the roofline', 'Cracked or broken gutter sections', 'Water running down exterior walls', 'Sagging gutters or damaged downpipes'], 'Getting these problems checked early can help prevent further damage to your home.', 'Get Your Gutters Checked',
   [('Gutter Repairs for Leaking, Loose & Damaged Gutters', ['Kiely Roofing & Construction repairs leaking joints, cracked guttering, loose fittings and damaged downpipes.', 'Whether it’s a small leak or a section of guttering that has come away from the roofline, we’ll assess the problem and repair the affected area where possible.', 'Not every problem requires new guttering, and we’ll advise if a repair is all that’s needed.'], []),
    ('New Gutter Installations', ['If your existing guttering is badly damaged, ageing or no longer draining properly, installing new gutters may be the better long-term solution.', 'We provide gutter installations and replacements for homeowners, whether you’re upgrading old guttering, replacing damaged sections or having new gutters fitted as part of a roofing or renovation project. We can help you choose suitable guttering for your property and take care of the installation.'], []),
    ('Other Roofing Services', ['Roof problems can sometimes involve more than one part of the roof. Kiely Roofing also carries out:'], ['Chimney Repairs', 'Flat Roofing', 'Dry Verge Systems', 'Roof Replacement'])],
   [('Mary O’Sullivan', 'We contacted Kiely Roofing after noticing water overflowing from our gutters during heavy rain. They found the problem quickly and repaired the damaged section without any fuss. Very happy with the work and would definitely recommend them.'),
    ('Patrick Murphy', 'We had Kiely Roofing replace the old guttering on our house as it was starting to leak in several places. They explained what needed to be done, arrived when they said they would and left everything neat and tidy. Great job from start to finish.')],
   ('guttering-services-2.jpg', 'gutters-2.jpg'), ba=[('b1.jpg', 'a1.jpg'), ('b5-1.jpg', 'a5.jpg'), ('b3.jpg', 'a3.jpg')],
   title='Gutter Repairs & Installations Meath, Kildare & Dublin', desc='Gutter repairs, replacement guttering and new gutter installations across Meath, Kildare & Dublin. Free quotes from Kiely Roofing.'),
 S('dry-verge', 'Dry Verge Systems', 'roof', 'verge', 'roof-verges1.jpg', 'Dry verge installation & repairs', 'Dry Verge Installation',
   ['Kiely Roofing provides dry verge installation across Meath, Kildare, Dublin and surrounding areas.',
    'Dry verge systems help protect the exposed edges of a tiled roof from wind and weather while giving the roofline a cleaner, more finished appearance. They are a low-maintenance alternative to traditional mortar verges and can be fitted to suitable existing roofs.'],
   'When Might Dry Verge Be Needed?', 'Dry verge installation may be suitable if you are dealing with:',
   ['Cracked or failing mortar at the roof edge', 'Loose or exposed verge tiles', 'Weather damage', 'Repeated maintenance around the gable', 'An untidy or deteriorating roofline', 'An older roof being upgraded'], '', 'Get a Free Quote',
   [('What Is a Dry Verge System?', ['A dry verge system uses secure verge caps to protect the edge of the roof where the tiles meet the gable.', 'Unlike traditional mortar, which can crack and deteriorate over time, dry verge systems are designed to provide a more durable and weather-resistant finish.'], []),
    ('Dry Verge for Existing Roofs', ['Dry verge systems can often be fitted as part of roof repair or improvement work.', 'Where the existing verge is damaged or deteriorating, the area can be assessed to determine whether dry verge installation is suitable for the roof.'], []),
    ('Part of a Wider Roofing Project', ['Dry verge work is often carried out alongside other roofing or roofline improvements. Kiely Roofing also provides:'], ['Roof Repairs', 'Roof Replacement', 'Guttering', 'Chimney Repairs', 'Flat Roofing'])],
   [('Declan Walsh', 'We had the verge and roofline tidied up and the difference is brilliant. The whole roof looks much neater and more finished now. The work was carried out quickly and everything was cleaned up afterwards.'),
    ('Ciara Kelly', 'Very pleased with the dry verge work completed by Kiely Roofing. From the first visit through to finishing the job, everything was straightforward and professionally handled.')],
   ('dry-verge-replacement.jpg', 'dry-verge-roofline-mkd-1.jpg'), ['dry-verge.jpg', 'dry-verge-2.jpg', 'dry-verge-roofline-mkd-2.jpg'],
   title='Dry Verge Installation Meath, Kildare & Dublin', desc='Dry verge installation and roofline repairs across Meath, Kildare & Dublin. A low-maintenance alternative to mortar verges.'),
 S('house-renovations', 'House Renovations', 'home', 'reno', 'house-renovation1.jpg', 'House renovations & remodelling', 'House Renovations',
   ['Kiely Roofing carries out house renovation work across Meath, Kildare, Dublin and surrounding areas.',
    'Whether you are updating an older property, improving the layout of your home or combining several areas of work into one project, we can help with both the structural and finishing work involved.'],
   'House Renovation Services', 'Depending on the project, renovation work can include:',
   ['Roofing work', 'Plastering', 'Interior painting', 'Exterior painting', 'Alterations to existing rooms', 'Repairs to damaged areas', 'Improvements to walls and finishes', 'Work carried out alongside extensions or attic conversions'], '', 'Get a Free Quote',
   [('Renovating More Than One Part of the Property', ['Larger renovation projects often involve several different types of work at the same time. Kiely Roofing also carries out:'], ['House Extensions', 'Attic Conversions', 'Plastering', 'Interior & Exterior Painting', 'Roof Repairs']),
    ('Renovation Work for Older and Existing Homes', ['Renovation projects can range from improving one part of a property to carrying out more substantial work across the home.', 'The aim is to make the property work better for the people living in it, while dealing with any existing issues that need attention along the way.'], []),
    ('Planning a Home Renovation?', ['If you are updating an older property or planning improvements across several parts of your home, Kiely Roofing can discuss the work involved and provide a quote for the project.'], [])],
   [('David Reilly', 'We had quite a bit of renovation work carried out and the whole house feels transformed. Everything was well organised and the quality of the finish is excellent. We’re delighted with how it all came together.'),
    ('Aisling Doyle', 'Very happy with the renovation completed by Kiely Roofing. They were helpful with decisions along the way and nothing ever felt like too much trouble. The finished house looks brilliant.')],
   ('house-rennovation-before-after.jpg', 'house-renovation-mkd-2.jpg'), ['house-renovation2.jpg', 'house-renovation-1.jpg', 'house-renovation-mkd-1.jpg'],
   title='House Renovations Meath, Kildare & Dublin', desc='House renovation work across Meath, Kildare & Dublin, from structural work to plastering and painting, all with one team.'),
 S('house-extensions', 'House Extensions', 'home', 'ext', 'house-extension11.jpg', 'House extensions & conversions', 'House Extensions',
   ['Kiely Roofing carries out house extension work across Meath, Kildare, Dublin and surrounding areas.',
    'A well-planned extension can give you the extra space you need without having to move, whether that means a larger kitchen, additional living space, a home office or another room for a growing household.'],
   'House Extension Work', 'The work involved will depend on the size and type of extension being planned. Projects can include:',
   ['Single-storey extensions', 'Kitchen extensions', 'Additional living space', 'Roofing work', 'Plastering and finishing', 'Exterior work', 'Alterations to existing parts of the property'], '', 'Get a Free Quote',
   [('Extensions as Part of a Larger Renovation', ['House extensions are often carried out alongside other improvements to the property. Kiely Roofing also provides:'], ['House Renovations', 'Attic Conversions', 'Plastering', 'Interior & Exterior Painting', 'Roof Repairs']),
    ('Create More Space at Home', ['An extension can completely change how a home works day to day.', 'The right design can add useful floor space, improve the layout of the property and make better use of areas that currently feel cramped or underused.'], []),
    ('Planning a Home Extension?', ['If you are considering adding more space to your home, Kiely Roofing can discuss the project and the work involved and provide a quote.'], [])],
   [('Conor McCarthy', 'We are absolutely delighted with our new extension. It has completely changed how we use the back of the house and gives us so much more space and light. The workmanship throughout was excellent.'),
    ('Emma Kavanagh', 'Kiely Roofing did a fantastic job on our extension. Communication was good from the beginning and we always knew what stage the work was at. The finished extension has turned out even better than we expected.')],
   ('house-extensions-mkd-2.jpg', 'house-extension.jpg'), ['house-extension-copy.jpg', 'house-extensions-mkd-1.jpg', 'house-extension-2.jpg'],
   title='House Extensions Meath, Kildare & Dublin', desc='House extensions across Meath, Kildare & Dublin: kitchen extensions, single-storey extensions and extra living space.'),
 S('attic-conversions', 'Attic Conversions', 'home', 'attic', 'attic-1.jpg', 'Attic conversions & renovations', 'Attic Conversions',
   ['Kiely Roofing & Construction carries out attic conversion work across Meath, Kildare, Dublin and surrounding areas.',
    'An attic conversion can make better use of space already within your home, whether you need an extra bedroom, office, storage area or more usable living space.'],
   'Attic Conversion Work', 'The work required will depend on the size, layout and condition of the existing attic. Projects can involve:',
   ['Improving access to the attic', 'Creating usable floor space', 'Roofing and structural work', 'Insulation', 'Plastering and finishing', 'Preparing the space for its intended use'], '', 'Get a Free Quote',
   [('Part of a Larger Home Improvement Project', ['Attic conversions are often carried out alongside other work to the property. Kiely Roofing also provides:'], ['House Extensions', 'House Renovations', 'Plastering', 'Interior & Exterior Painting', 'Roof Repairs']),
    ('Make Better Use of Your Attic Space', ['Many homes have attic space that is underused or difficult to access.', 'A well-planned conversion can turn that space into a much more practical part of the property while making better use of the existing footprint of the house.'], []),
    ('Planning an Attic Conversion?', ['If you are considering making better use of your attic space, Kiely Roofing can discuss the project and the work involved.'], [])],
   [('Sean Murphy', 'We were delighted with how the attic conversion turned out. The whole space feels completely different now and has given us a really useful extra room. Everything was kept tidy and the work was finished to a very high standard.'),
    ('Niamh O’Connor', 'Really pleased with the work from Kiely Roofing. They talked us through the attic conversion beforehand, kept us updated as the job progressed and the finished room is exactly what we were hoping for.')],
   ('attic-converstion-before-after.jpg', 'attic-conversion.jpg'), ['attic-conversions-mkd-1.jpg', 'attick-conversion.jpg', 'attic-conversions-mkd-2.jpg'],
   title='Attic Conversions Meath, Kildare & Dublin', desc='Attic conversions across Meath, Kildare & Dublin: extra bedrooms, home offices and usable living space.'),
 S('interior-exterior-painting', 'Interior & Exterior Painting', 'home', 'paint', 'exterior-painting-1.jpg', 'Interior & exterior painting', 'Painting Services',
   ['Kiely Roofing & Construction provides interior and exterior painting services across Meath, Kildare, Dublin and surrounding areas.',
    'Whether you are refreshing the inside of your home, repainting the exterior or finishing a larger renovation project, we can carry out the painting work needed to complete the job.'],
   'Interior Painting & Decorating', 'We carry out painting and decorating work for a range of interior spaces, including:',
   ['Living rooms', 'Bedrooms', 'Hallways and stairs', 'Kitchens', 'Newly plastered rooms', 'Renovated spaces', 'Attic conversions', 'House extensions'], '', 'Get a Free Quote',
   [('House Painters for Renovations & Home Improvements', ['Painting is often one of the final stages of a larger home improvement project. Kiely Roofing also carries out:'], ['House Extensions', 'Attic Conversions', 'Plastering', 'House Renovations', 'Roof Repairs']),
    ('Exterior House Painting', ['Exterior painting can improve the appearance of your home while helping protect suitable surfaces from ongoing weather exposure.', 'We can carry out exterior painting as a standalone job or as part of wider renovation or repair work.'], []),
    ('Need a Painter for Your Home?', ['If you need interior or exterior painting, either as a standalone job or as part of a larger project, Kiely Roofing can discuss the work involved and provide a quote.'], [])],
   [('Paul Gallagher', 'We had several rooms painted and the finish is excellent. Everything was properly prepared beforehand and the house was left clean and tidy each evening. A very professional job from start to finish.'),
    ('Claire O’Sullivan', 'Kiely Roofing did a great job painting the interior of our home. The difference is huge and the finish around the doors, skirting and walls is particularly neat. Very pleased with the result.')],
   ('interior-exterior-painting-2.jpg', 'interior-exterior-painting-mkd.jpg'), ['exterior-painting-services.jpg', 'image4.jpg', 'interior-exterior-painting-mkd-2.jpg'],
   title='Interior & Exterior Painting Meath, Kildare & Dublin', desc='Interior and exterior house painting across Meath, Kildare & Dublin, standalone or as part of a renovation.'),
 S('plastering', 'Plastering', 'home', 'trowel', 'plastering1.jpg', 'Plastering & skimming', 'Plastering Services',
   ['Kiely Roofing & Construction provides plastering services across Meath, Kildare, Dublin and surrounding areas.',
    'Whether the work forms part of a renovation, extension, attic conversion or a standalone repair, plastering helps create a clean, even finish ready for decorating.'],
   'Interior Plastering', 'Interior plastering can help improve walls and ceilings that are damaged, uneven or being updated as part of wider renovation work. Plastering may be needed for:',
   ['Walls and ceilings', 'Repaired or altered areas', 'Newly created rooms', 'Attic conversions', 'House extensions', 'Renovation projects'], '', 'Get a Free Quote',
   [('Plastering as Part of Renovation Work', ['Plastering is often one of the final stages of a larger project. Kiely Roofing can carry out plastering alongside other work, including:'], ['House Extensions', 'Attic Conversions', 'House Renovations', 'Interior & Exterior Painting', 'Roof Repairs']),
    ('Preparing Surfaces for Painting', ['A smooth plaster finish gives walls and ceilings a better base for decorating.', 'Where plastering and painting are both required, the work can be planned together as part of the same project.'], []),
    ('Need Plastering Work Done?', ['If you need plastering as part of a renovation, extension or other home improvement project, Kiely Roofing can discuss the work involved and provide a quote.'], [])],
   [('Kevin Molloy', 'We needed several walls replastered as part of our renovation and the finish is incredibly smooth. The work was completed quickly and everything was left ready for decorating. Would definitely recommend.'),
    ('Fiona McGrath', 'Excellent plastering work from Kiely Roofing. Some of the walls were in fairly rough condition beforehand but you wouldn’t know it now. Really neat finish and very little mess afterwards.')],
   ('plastering-before-after.jpg', 'plastering-1.jpg'), ['plastering-mkd.jpg', 'plastering-mkd-2.jpg', 'plastering2.jpg'], ba=[('plastering-1a.jpg', 'plastering-1b.jpg')],
   title='Plastering Services Meath, Kildare & Dublin', desc='Interior plastering and skimming across Meath, Kildare & Dublin, ready for decorating.'),
]
BYNAME = {s['name']: s for s in SERVICES}
BYNAME.update({'Dry Verge Installation': BYNAME['Dry Verge Systems'], 'Roofing Services': BYNAME['Roof Repairs']})
ROOF = [s for s in SERVICES if s['group'] == 'roof']
HOME = [s for s in SERVICES if s['group'] == 'home']
HOME_REVIEWS = [('John O’Neill', 'roof', 'Our old roof had reached the stage where repairs were no longer really worthwhile. The team replaced it and kept us informed throughout the job. The new roof looks fantastic and the whole house looks much better.'),
                ('Brendan Ryan', 'roof', 'We had leaking gutters in a couple of places and they were sorted quickly. The team checked the rest of the guttering while they were there and made sure everything was running properly before leaving.')]
ALL_REVIEWS = HOME_REVIEWS + [(n, s['group'], t, s['name']) for s in SERVICES for n, t in s['reviews']]
ALL_REVIEWS = [r if len(r) == 4 else (r[0], r[1], r[2], 'Roof Replacement' if 'roof' in r[2].lower() else 'Guttering') for r in ALL_REVIEWS]
STEPS = [('Get in Touch', 'Call, WhatsApp or send us an enquiry to tell us about your roofing or home improvement needs. A photo of the job is usually plenty to get started.'),
         ('Free Inspection', 'We offer a free, no-obligation inspection to assess your property, identify any issues & explain what work may be required.'),
         ('Free Callout & Clear Quote', 'A clear, fixed price upfront with no callout fee, no obligation, no hidden charges and no messing around.'),
         ('Job Done, Mess Gone', 'We turn up when we say, get the work done and take the mess with us when we finish.'),
         ('Final Walkthrough', 'We’ll review the completed work with you to ensure everything has been carried out properly.')]
WHY = [('pin', 'Local Contractors', 'Proudly serving homeowners and businesses across Meath, Kildare, Dublin and the surrounding areas.'),
       ('shield', 'Free Callout & Fully Insured', 'Free callouts and same-day inspections, with clear quotes and fully insured work for complete peace of mind.'),
       ('star', 'Quality Workmanship', 'Skilled, dependable service with careful attention to detail and a commitment to getting every job done right.')]
TRUST = ['Fully Insured', 'Quality Work & Materials Guaranteed', 'Competitive Pricing', 'Free Quotes & No Callout Fee']
BRANDS = ['redland-roofing', 'marley-eternit', 'klober-logo', 'kingspan-logo', 'cure-it-logo', 'velux', 'iko-logo', 'bostik-logo', 'dulux']
CERTS = [('safetcert-2', 'SafetCert'), ('national-guild-of-master-craftsmen1', 'National Guild of Master Craftsmen'), ('cro-logo', 'Companies Registration Office')]
BA_HOME = [('roof-replacement-1a.jpg', 'roof-replacement-1b.jpg', 'Roof replacement'), ('b1.jpg', 'a1.jpg', 'Gutter repairs'), ('plastering-1a.jpg', 'plastering-1b.jpg', 'Plastering')]

# ---------- building blocks ----------
def link(p, name):
    s = BYNAME.get(name)
    return f'<a href="{p}{s["slug"]}/">{name}</a>' if s else name

def head(p, title, desc, path, extra_ld='', kw=''):
    canon = SITE + '/' + path.rstrip('/')
    ld = {"@context": "https://schema.org", "@type": "RoofingContractor", "name": "Kiely Roofing & Construction", "url": SITE + "/",
          "telephone": "+353873592163", "email": EMAIL, "image": SITE + "/img/van-front.jpg", "logo": SITE + "/img/logo.png",
          "address": {"@type": "PostalAddress", "addressLocality": "Longwood", "addressRegion": "Co. Meath", "addressCountry": "IE"},
          "areaServed": [{"@type": "City", "name": "Dublin"}, {"@type": "AdministrativeArea", "name": "County Dublin"}, {"@type": "AdministrativeArea", "name": "County Meath"}, {"@type": "AdministrativeArea", "name": "County Kildare"}] + [{"@type": "Place", "name": t} for t in ["Lucan", "Blanchardstown", "Castleknock", "Swords", "Clondalkin", "Tallaght", "Navan", "Trim", "Ashbourne", "Maynooth", "Celbridge", "Naas"]], "knowsAbout": ["Roof repairs", "Roof replacement", "Flat roofing", "Chimney repairs", "Guttering", "Dry verge", "Attic conversions", "House extensions"], "openingHours": "Mo-Su 07:00-22:00", "priceRange": "Free quotes",
          "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5", "bestRating": "5", "reviewCount": str(len(ALL_REVIEWS))}}
    import json as _j
    return f'''<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{(kw + " Dublin, " + kw + " Meath, " + kw + " Kildare, ") if kw else ""}roofers Dublin, roofing contractors Dublin, roof repairs Dublin, roof replacement Dublin, flat roofing Dublin, chimney repairs Dublin, guttering Dublin, roofers Meath, roofers Kildare, Kiely Roofing">
<meta name="geo.region" content="IE-D"><meta name="geo.placename" content="Dublin, Meath, Kildare">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#131316">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/img/van-front.jpg"><meta property="og:url" content="{canon}"><meta property="og:locale" content="en_IE">
<link rel="icon" href="{p}img/icon-192.png"><link rel="apple-touch-icon" href="{p}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin><link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" onload="this.onload=null;this.rel='stylesheet'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap"></noscript>
<link rel="stylesheet" href="{p}assets/style.css?v=5"><link rel="stylesheet" href="{p}assets/kiely.css?v=5">
<script type="application/ld+json">{_j.dumps(ld, ensure_ascii=False)}</script>{extra_ld}'''

def header(p, active):
    def on(k): return ' class="on" aria-current="page"' if k == active else ''
    roof = ''.join(f'<a href="{p}{s["slug"]}/"><i>{I[s["icon"]]}</i>{s["name"]}</a>' for s in ROOF)
    home = ''.join(f'<a href="{p}{s["slug"]}/"><i>{I[s["icon"]]}</i>{s["name"]}</a>' for s in HOME)
    msubs = lambda grp: ''.join(f'<a href="{p}{s["slug"]}/">{s["name"]}</a>' for s in grp)
    ron = ' class="on"' if active == 'roof' else ''; hon = ' class="on"' if active == 'home-imp' else ''
    return f'''<div class="topbar"><div class="wrap"><span><span class="dot"></span><span data-open>Open 7am – 10pm, 7 days</span></span>
<span class="tb-r"><a href="mailto:{EMAIL}">{I['mail']}{EMAIL}</a><a href="{TEL}">{I['phone']}Free quote: <b>{PHONE}</b></a></span></div></div>
<header class="hdr"><div class="wrap">
<a class="brand" href="{p}" aria-label="Kiely Roofing & Construction home"><img src="{p}img/logo-white.png" alt="Kiely Roofing & Construction" width="612" height="352"></a>
<nav class="nav" aria-label="Main">
<a href="{p}"{on('home')}>Home</a>
<a href="{p}about-us/"{on('about')}>About</a>
<div class="dd"><a href="{p}roof-repairs/"{ron}>Roofing {I['chev']}</a><div class="menu">{roof}<a href="{p}roof-health-check/"><i>{I['gauge']}</i>Roof Health Check</a></div></div>
<div class="dd"><a href="{p}house-renovations/"{hon}>Home Improvements {I['chev']}</a><div class="menu">{home}</div></div>
<a href="{p}gallery/"{on('gallery')}>Gallery</a>
<a href="{p}reviews/"{on('reviews')}>Reviews</a>
<a href="{p}contact-us/"{on('contact')}>Contact</a>
</nav>
<button class="btn btn-blue qbtn" type="button" data-qdrop aria-expanded="false" aria-controls="qdrop">Get a free quote {I['chev']}</button>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
</div>{qdrop(p)}</header>
<nav class="mnav" aria-label="Mobile">
<a class="ml" href="{p}">Home <small>01</small></a>
<a class="ml" href="{p}about-us/">About Us <small>02</small></a>
<div class="macc"><button class="ml mtog" type="button" aria-expanded="false">Roofing <i>{I['right']}</i></button><div class="subs">{msubs(ROOF)}<a href="{p}roof-health-check/">Roof Health Check</a></div></div>
<div class="macc"><button class="ml mtog" type="button" aria-expanded="false">Home Improvements <i>{I['right']}</i></button><div class="subs">{msubs(HOME)}</div></div>
<a class="ml" href="{p}gallery/">Gallery <small>03</small></a>
<a class="ml" href="{p}reviews/">Reviews <small>04</small></a>
<a class="ml" href="{p}contact-us/">Contact <small>05</small></a>
<a class="btn btn-blue" href="#quote" data-qdrop>Get a free quote</a>
<a class="btn btn-ghost" href="{TEL}" style="margin-top:12px">{I['phone']} Call {PHONE}</a>
<div class="mfoot">Longwood, Co. Meath · Mon–Sun 7am–10pm</div>
</nav>'''

OPTS = ['Roof Repairs', 'Roof Replacement', 'Chimney Repairs', 'Flat Roofing', 'Guttering', 'Dry Verge Systems', 'House Renovations', 'House Extensions', 'Attic Conversions', 'Interior & Exterior Painting', 'Plastering', 'Other']
def form(p, title='Get a Free Quote', sub='Free, no-obligation quote. No callout fee.', compact=False, svc=None):
    sel = ''.join(f'<option{" selected" if o == svc else ""}>{o}</option>' for o in OPTS)
    return f'''<form class="formcard{' compact' if compact else ''}" data-form novalidate>
<h3>{title}</h3><p class="sub">{sub}</p>
<div class="fmsg" role="status"></div>
<div class="fgrid">
<label class="f"><span>Name *</span><input name="name" autocomplete="name" required></label>
<label class="f"><span>Phone *</span><input name="phone" type="tel" autocomplete="tel" required></label>
<label class="f full"><span>Email *</span><input name="email" type="email" autocomplete="email" required></label>
<label class="f full"><span>Service</span><select name="service"><option value="">Choose a service</option>{sel}</select></label>
<label class="f full"><span>How can we help? *</span><textarea name="message" placeholder="Tell us about the job" required></textarea></label>
</div>
<input class="hp" name="botcheck" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn btn-blue" type="submit">Send enquiry {I['arrow']}</button>
<p class="fnote">Prefer WhatsApp? <a href="{WAURL}" target="_blank" rel="noopener">Send us a photo of the job</a> · <a href="{p}privacy-policy/">Privacy</a></p>
</form>'''

def wizard(p):
    svc = ''.join(f'<button type="button" class="wopt" data-v="{s["name"]}"><i>{I[s["icon"]]}</i>{s["name"]}</button>' for s in SERVICES)
    def opts(items): return ''.join(f'<button type="button" class="wopt" data-v="{v}"><i>{I[ic]}</i><span>{v}<small>{d}</small></span></button>' for ic, v, d in items)
    prop = opts([('house', 'House', 'Semi, detached or terrace'), ('roof', 'Bungalow', 'Single storey'), ('ext', 'Extension / garage', 'Flat or pitched'), ('users', 'Commercial / landlord', 'Business or rental')])
    urg = opts([('storm', 'Emergency', 'Leak or damage right now'), ('clock', 'This week', 'Needs sorting soon'), ('quote', 'This month', 'Getting quotes'), ('search', 'Just planning', 'Advice for later')])
    return f'''<div class="wiz" id="wiz" role="dialog" aria-modal="true" aria-label="Free quote wizard"><div class="scrim" data-wclose></div>
<div class="wcard"><button class="x" type="button" data-wclose aria-label="Close">{I['x']}</button>
<div class="whead"><span class="wcount">Step 1 of 4</span><div class="wbar"><i></i></div></div>
<div class="wstep on" data-key="service"><h3>What do you need?</h3><p>Pick the closest match. You can add details at the end.</p><div class="wgrid">{svc}</div></div>
<div class="wstep" data-key="property"><h3>What type of property?</h3><div class="wgrid two">{prop}</div></div>
<div class="wstep" data-key="urgency"><h3>How soon do you need it?</h3><div class="wgrid two">{urg}</div></div>
<div class="wstep" data-key="details"><h3>Where should we send your free quote?</h3><div class="wsum"></div>
<form novalidate><div class="fgrid">
<label class="f"><span>Name *</span><input name="name" autocomplete="name" required></label>
<label class="f"><span>Phone *</span><input name="phone" type="tel" autocomplete="tel" required></label>
<label class="f full"><span>Town / area *</span><input name="town" required placeholder="e.g. Navan, Maynooth, Lucan"></label>
<label class="f full"><span>Anything else? (optional)</span><textarea name="details" placeholder="e.g. leak above the back bedroom after the storm"></textarea></label>
</div>
<div class="wbtns"><button class="btn wwa" type="button">{WA_ICON} Send on WhatsApp</button><button class="btn btn-line wmail" type="button">{I['mail']} Send by email</button></div>
<p class="fnote">{I['camera'].replace('<svg', '<svg width="16" height="16" style="display:inline;vertical-align:-3px"')} Tip: on WhatsApp you can attach photos of the roof. It speeds up your quote.</p></form>
<div class="wdone"><span class="ico">{I['check']}</span><h3>Thanks, nearly done!</h3><p>Just press send in WhatsApp or your email app. We’ll come back to you with your free quote. Urgent? Call <a href="{TEL}">{PHONE}</a>.</p></div>
</div>
<button class="wback" type="button">{I['left'].replace('<svg', '<svg width="18" height="18"')} Back</button>
</div></div>'''

WA_ICON = WA.replace('<svg', '<svg width="22" height="22"')

def footer(p):
    lst = lambda grp: ''.join(f'<li><a href="{p}{s["slug"]}/">{s["name"]}</a></li>' for s in grp)
    return f'''<section class="certs"><div class="wrap"><span class="eyebrow">Highly qualified, registered &amp; insured</span>
<div class="certrow">{''.join(f'<img src="{p}img/logos/{f}.png" alt="{a}" loading="lazy">' for f, a in CERTS)}</div></div></section>
<footer class="ftr"><div class="wrap">
<div class="cols">
<div><img class="fl" src="{p}img/logo-white.png" alt="Kiely Roofing & Construction" width="612" height="352" loading="lazy">
<p>Roofers serving Dublin, Meath &amp; Kildare. Roof repairs, new roofs and home improvements. Based in Longwood, Co. Meath. Free quotes and no callout fee.</p>
<span class="h247">{I['clock'].replace('<svg', '<svg width="14" height="14"')} <span data-open>MON–SUN 7AM–10PM</span></span></div>
<div><h4>Roofing Services</h4><ul>{lst(ROOF)}<li><a href="{p}roof-health-check/">Roof Health Check</a></li></ul></div>
<div><h4>Home Improvements</h4><ul>{lst(HOME)}</ul></div>
<div><h4>Contact</h4><ul class="ci">
<li>{I['phone']}<a href="{TEL}" data-cfg="phone">{PHONE}</a></li>
<li>{I['mail']}<a href="mailto:{EMAIL}" data-cfg="email">{EMAIL}</a></li>
<li>{I['pin']}<span>Longwood, Co. Meath<br>Serving Meath, Kildare &amp; Dublin</span></li>
<li>{I['clock']}<span>Mon–Sun: 7am–10pm</span></li></ul>
<ul style="margin-top:18px"><li><a href="{p}roofers-dublin/">Roofers Dublin</a></li><li><a href="{p}about-us/">About Us</a></li><li><a href="{p}gallery/">Gallery</a></li><li><a href="{p}reviews/">Reviews</a></li><li><a href="{p}contact-us/">Contact Us</a></li></ul></div>
</div>
<div class="base"><span>Copyright © <span data-cfg="year">2026</span> Kiely Roofing &amp; Construction. All Rights Reserved.</span>
<nav><a href="{p}privacy-policy/">Privacy Policy</a></nav></div>
</div></footer>
<div class="fab"><a class="wa" href="{WAURL}" data-href="whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp us">{WA}</a></div>
<div class="mbar"><a href="{TEL}">{I['phone']}<span>Call</span></a><a href="{WAURL}" target="_blank" rel="noopener">{WA_ICON}<span>WhatsApp</span></a><a href="#quote" data-qdrop class="q">{I['quote']}<span>Free quote</span></a></div>'''

def scripts(p):
    return f'''<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>
<script src="{p}assets/site.js?v=5" defer></script><script src="{p}assets/tools.js?v=5" defer></script>'''

def page(path, active, title, desc, body, intro=False, extra_ld='', kw=''):
    p = '../' * path.count('/')
    h = head(p, title, desc, path, extra_ld, kw)
    loader = ''
    if intro:
        h += '\n<script>try{if(!sessionStorage.getItem("kiely_intro")||/[?&]intro/.test(location.search))document.documentElement.classList.add("intro")}catch(e){document.documentElement.classList.add("intro")}</script>'
        loader = f'''<div id="loader" aria-hidden="true" data-apex="0.322,0.03" data-l="0.02,0.5" data-r="0.98,0.5"><div class="sky"></div><i class="glow"></i>
<i class="ring"></i><i class="ring r2"></i>
<div class="box"><div class="logo"><img class="off" src="{p}img/logo-white.png" alt=""><img class="on" src="{p}img/logo-white.png" alt=""></div><div class="lt">Roofing &amp; home improvements</div></div>
<svg class="bolt"><defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter></defs></svg>
<div class="flash"></div></div>'''
    intro_js = ('<script>' + open(os.path.join(ROOT, 'assets', 'intro.js'), encoding='utf-8').read() + '</script>') if intro else ''
    out = f'''{h}
</head>
<body>
{loader}{intro_js}
{header(p, active)}
<main>
{body(p)}
</main>
{footer(p)}
{quote_drawer(p)}
{wizard(p)}
{scripts(p)}
</body>
</html>
'''
    fn = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, 'w', encoding='utf-8').write(out)
    print('wrote', os.path.relpath(fn, ROOT))

def quote_drawer(p):
    f = form(p).replace('<form class="formcard"', '<form class="formcard" id="quote"').replace('<h3>', f'<button class="x" type="button" data-close aria-label="Close">{I["x"]}</button><h3>', 1)
    return f'<div class="qd" id="qd" role="dialog" aria-modal="true" aria-label="Request a quote"><div class="scrim" data-close></div>{f}</div>'

# ---------- image helpers ----------
from PIL import Image as _Img
_DIM = {}
def dims(f):
    if f not in _DIM: _DIM[f] = _Img.open(os.path.join(ROOT, 'img', f)).size
    return _DIM[f]
def pic(p, f, alt, chip='', cls=''):
    """A photo shown whole: the box takes the photo's own shape, so nothing is cut off."""
    w, h = dims(f)
    return f'<div class="ph fit {cls}" style="aspect-ratio:{w}/{h}" data-clip><img src="{p}img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy">{chip}</div>'
# his side-by-side before/after photos, split into proper slider pairs (True = labels already on the photo)
COMP = {'roof-repair-before-after.jpg': ('ba-roof-repair-before.jpg', 'ba-roof-repair-after.jpg', False),
        'flat-roof-before-after.jpg': ('ba-flat-roof-before.jpg', 'ba-flat-roof-after.jpg', False),
        'dry-verge-replacement.jpg': ('ba-dry-verge-before.jpg', 'ba-dry-verge-after.jpg', False),
        'house-rennovation-before-after.jpg': ('ba-house-rennovation-before.jpg', 'ba-house-rennovation-after.jpg', False),
        'attic-converstion-before-after.jpg': ('ba-attic-converstion-before.jpg', 'ba-attic-converstion-after.jpg', False),
        'interior-exterior-painting-2.jpg': ('ba-interior-exterior-painting-2-before.jpg', 'ba-interior-exterior-painting-2-after.jpg', False),
        'plastering-before-after.jpg': ('ba-plastering-before.jpg', 'ba-plastering-after.jpg', False)}
SKIP = set(COMP) | {'roof-repairs-collage-600x600.jpg'}

def qdrop(p):
    f = form(p, 'Get a free quote', 'We aim to reply the same day. No callout fee.', compact=True).replace('<form class="formcard compact"', '<form class="formcard compact" id="qdform"')
    perks = '<ul class="qperks">' + ''.join(f'<li>{I["check"]}{t}</li>' for t in ['No callout fee', 'Fixed price upfront', 'Fully insured', 'Same-day inspections']) + '</ul>'
    f = f.replace('<div class="fmsg"', perks + '<div class="fmsg"', 1)
    return f'''<div class="qdrop" id="qdrop" aria-hidden="true" data-lenis-prevent><div class="wrap qdgrid">
<div class="qdside"><span class="eyebrow">Free quotes · no callout fee</span><h3>Tell us about the job.</h3>
<p>Free, no-obligation inspection and a clear, fixed price upfront. Serving Dublin, Meath &amp; Kildare.</p>
<a class="qdl" href="{TEL}">{I['phone']}<span><b>Call {PHONE}</b><small data-open>Mon–Sun 7am–10pm</small></span></a>
<a class="qdl wa" href="{WAURL}" target="_blank" rel="noopener">{WA_ICON}<span><b>WhatsApp a photo</b><small>Quickest way to a price</small></span></a>
<a class="qdl" href="#quote-wizard" data-wizard>{I['quote']}<span><b>Step-by-step quote</b><small>4 quick questions</small></span></a>
<button class="qdx" type="button" data-qclose>{I['x']} Close</button></div>
{f}</div></div>'''

# ---------- sections ----------
def stars(n=5): return '<span class="stars" aria-label="5 stars">' + '★' * n + '</span>'

def trustlist():
    return '<ul class="trust">' + ''.join(f'<li>{I["check"]}{t}</li>' for t in TRUST) + '</ul>'

def phero(p, crumb, h1, sub, img, extra=''):
    trail = ''.join(f'<span>/</span><a href="{p}{u}">{t}</a>' for t, u in crumb[:-1])
    return f'''<section class="phero" data-rain>
<img class="bg" src="{p}img/{img}" alt="" fetchpriority="high">
<div class="wrap phero-grid">
<div><div class="crumb"><a href="{p}">Home</a>{trail}<span>/</span><b>{crumb[-1][0]}</b></div>
<h1>{h1}</h1>
<p class="lead">{sub}</p>
<div class="rate">{stars()} <b>5 / 5</b> Excellent reviews rating</div>
{trustlist()}
<div class="btn-row"><a class="btn btn-blue" href="#quote" data-qdrop{extra}>Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{p}gallery/">View our work</a></div>
</div></div></section>'''

def marquee():
    items = ['Roof repairs', 'Roof replacement', 'Chimney repairs', 'Flat roofing', 'Guttering', 'Dry verge', 'Attic conversions', 'Extensions', 'Renovations', 'Plastering', 'Painting', 'Meath · Kildare · Dublin']
    s = ''.join(f'<span>{t}</span>' for t in items)
    return f'<div class="marquee" aria-hidden="true"><div class="track">{s}{s}</div></div>'

def compare(p, b, a, t='', sub='', notags=False):
    w, h = dims(b)
    tags = '' if notags else '<span class="tag l">Before</span><span class="tag r">After</span>'
    return f'''<figure class="ba"><div class="compare" style="aspect-ratio:{w}/{h}"><img class="after" src="{p}img/{a}" alt="{t or 'Project'} after, by Kiely Roofing" loading="lazy"><img class="before" src="{p}img/{b}" alt="{t or 'Project'} before" loading="lazy">
{tags}<span class="handle"></span>
<input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after"></div>
{f'<figcaption>{t}<span>{sub}</span></figcaption>' if t else ''}</figure>'''

def ba_section(p, pairs, soft=True, title='See the transformation.'):
    items = ''.join(compare(p, b, a, t, 'Drag to compare') for b, a, t in pairs)
    return f'''<section class="sec{' soft' if soft else ''}"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">The difference</span><h2 data-split>{title}</h2></div>
<a class="btn btn-line" href="{p}gallery/">View our gallery {I['arrow']}</a></div>
<div class="ba-grid g3" data-reveal="group">{items}</div></div></section>'''

def svc_cards(p, grp, dark=False):
    return '<div class="sgrid" data-reveal="group">' + ''.join(f'''<a class="scard" href="{p}{s['slug']}/"><img src="{p}img/{s['imgs'][1]}" alt="{s['name']} by Kiely Roofing" loading="lazy">
<span class="num">{I[s['icon']]}</span><span class="go">{I['arrow']}</span><h3>{s['name']}</h3><p>{s['intro'][-1][:150].rsplit(' ', 1)[0]}…</p><span class="tlink">View service {I['arrow']}</span></a>''' for s in grp) + '</div>'

def process(p, soft=True):
    st = ''.join(f'<div class="step"><div class="n">0{i}</div><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(STEPS, 1))
    return f'''<section class="sec{' soft' if soft else ''}"><div class="wrap">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">Our process</span><h2 data-split>Five simple steps, no hassle.</h2></div>
<div class="steps s5" data-reveal="group">{st}</div></div></section>'''

def why():
    c = ''.join(f'<div class="card"><span class="ico">{I[a]}</span><h3>{b}</h3><p>{t}</p></div>' for a, b, t in WHY)
    return f'''<section class="sec deep" data-rain><div class="wrap" style="position:relative;z-index:2">
<div class="center" style="margin-bottom:48px"><span class="eyebrow">Why choose us</span><h2 data-split>Why choose Kiely Roofing &amp; Construction.</h2></div>
<div class="cards c3" data-reveal="group">{c}</div></div></section>'''

def review_cards(rs, cls='rgrid'):
    return f'<div class="{cls}" data-reveal="group">' + ''.join(f'''<div class="review" data-cat="{g}"><div class="stars">★★★★★</div><q>{t}</q>
<div class="who"><span class="av">{n[0]}</span><div><b>{n}</b><span>{svc}</span></div></div></div>''' for n, g, t, svc in rs) + '</div>'

def reviews_sec(p, rs):
    return f'''<section class="sec dark" data-rain><div class="wrap" style="position:relative;z-index:2">
<div class="sec-head"><div><span class="eyebrow">What our customers say</span><h2 data-split>Rated 5 / 5 by homeowners.</h2></div>
<a class="btn btn-ghost" href="{p}reviews/">Read more reviews {I['arrow']}</a></div>
{review_cards(rs, 'rgrid r2' if len(rs) == 2 else 'rgrid')}</div></section>'''

def brands(p):
    b = ''.join(f'<img src="{p}img/logos/{f}.png" alt="{f.replace("-logo", "").replace("-", " ").title()} logo" loading="lazy">' for f in BRANDS)
    return f'''<section class="brands"><div class="wrap"><span class="eyebrow">Quality materials &amp; professional equipment</span></div>
<div class="bmarq"><div class="btrack">{b}{b}</div></div></section>'''

def area_box(dark=False):
    return f'''<form class="areabox{' dark' if dark else ''}" data-area><label for="areain"><b>{I['map']} Do we cover your area?</b><span>Type your town</span></label>
<div class="arow"><input id="areain" list="areas" placeholder="e.g. Navan, Maynooth, Lucan" autocomplete="off"><button class="btn btn-blue" type="submit">Check</button></div>
<datalist id="areas"></datalist><div class="area-out" aria-live="polite"></div></form>'''

def health_teaser(p):
    return f'''<section class="sec deep hteaser" data-rain><div class="wrap split" style="position:relative;z-index:2">
<div><span class="eyebrow">Free online tool</span><h2 data-split>Repair or replace? Take the 60-second roof check.</h2>
<p class="lead">Answer six quick questions about your roof and we’ll tell you whether it sounds like a repair job or time to start planning a new roof. Then book a free inspection to be sure.</p>
<a class="btn btn-blue" href="{p}roof-health-check/">Start the roof check {I['arrow']}</a></div>
<div class="gaugecard" data-reveal><div class="gauge"><svg viewBox="0 0 200 120"><path d="M20 110a80 80 0 0 1 160 0" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="18" stroke-linecap="round"/><path d="M20 110a80 80 0 0 1 160 0" fill="none" stroke="url(#gg)" stroke-width="18" stroke-linecap="round" stroke-dasharray="251" stroke-dashoffset="70"/><defs><linearGradient id="gg"><stop offset="0" stop-color="#35c46a"/><stop offset=".5" stop-color="#ffb81c"/><stop offset="1" stop-color="#f96d30"/></linearGradient></defs><line x1="100" y1="110" x2="150" y2="60" stroke="#fff" stroke-width="5" stroke-linecap="round"/><circle cx="100" cy="110" r="9" fill="#fff"/></svg></div>
<div class="glabels"><span>Repair</span><span>Plan ahead</span><span>Replace</span></div></div>
</div></section>'''

def cta(p):
    return f'''<section class="cta">{HOUSE_SVG}<div class="wrap">
<div><span class="eyebrow">Free quotes · no callout fee</span><h2 data-split>Need roofing work done?</h2>
<p>Whether you have noticed a leak, need damaged roofing repaired or are considering a roof replacement, talk to Kiely Roofing about the work required.</p></div>
<div class="btn-row"><a class="btn btn-white" href="#quote" data-qdrop>Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{TEL}">{I['phone']} {PHONE}</a></div>
</div></section>'''

# ---------- pages ----------
def home(p):
    rc = ''.join(f'<a href="{p}{s["slug"]}/">{I[s["icon"]]}{s["name"]}</a>' for s in ROOF)
    return f'''<section class="hero hvid">
<video class="bg" poster="{p}video/hero-poster.jpg" data-poster-m="{p}video/hero-m-poster.jpg" autoplay muted loop playsinline preload="auto" aria-hidden="true"><source src="{p}video/hero-m.mp4" type="video/mp4" media="(max-width:760px)"><source src="{p}video/hero-m.webm" type="video/webm" media="(max-width:760px)"><source src="{p}video/hero.webm" type="video/webm"><source src="{p}video/hero.mp4" type="video/mp4"></video>
<div class="wrap">
<div>
<div class="gbadge">{stars()}<b>5 / 5</b> Excellent reviews rating</div>
<span class="eyebrow">Roofing · Home improvements</span>
<h1>Roofers in <span class="blue">Dublin, Meath &amp; Kildare.</span></h1>
<p class="lead">Roof repairs, replacements and roofing work for homeowners dealing with leaking roofs, storm damage and ageing roofs. Based in Longwood. Free quotes and no callout fee.</p>
<div class="btn-row"><a class="btn btn-blue" href="#quote" data-qdrop>Get a free quote {I['arrow']}</a><a class="btn btn-ghost" href="{p}gallery/">View our work</a></div>
{trustlist()}
</div>
<div class="hcard" data-reveal><span class="openb" data-open></span>
<h3>Free inspection &amp; quote</h3>
<ul class="ticks">{''.join(f'<li>{I["check"]}{t}</li>' for t in ['No callout fee', 'Clear, fixed price upfront', 'Fully insured', 'Same-day inspections'])}</ul>
<button class="btn btn-blue" type="button" data-qdrop>Get a free quote {I['chev']}</button>
<a class="btn btn-ghost" href="{TEL}">{I['phone']} {PHONE}</a>
<div class="hrev">{stars()}<q>The new roof looks fantastic and the whole house looks much better.</q><span>John O’Neill</span></div></div>
</div>
<div class="scroll">Scroll</div>
</section>
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">Roofing · Home improvements</span>
<h2 data-split>Roofing contractors you can rely on.</h2>
<p class="lead" style="color:var(--ink)">Roof repairs, replacements and roofing work carried out across Meath, Kildare, Dublin and surrounding areas.</p>
<p>Based in Longwood, Kiely Roofing &amp; Construction helps homeowners deal with leaking roofs, storm damage, ageing roofs and other roofing problems. Whether the issue needs a straightforward repair or more extensive work, we can assess what is happening and advise on the right next step.</p>
{area_box()}
<div class="btn-row" style="margin-top:24px"><a class="btn btn-line" href="{p}about-us/">About us {I['arrow']}</a></div></div>
{pic(p, 'van-front.jpg', 'Kiely Roofing & Construction van, roofers serving Dublin, Meath and Kildare', f'<span class="chip">{I["pin"]}Based in Longwood, Co. Meath</span>')}
</div></section>
<section class="sec soft"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Roofing services</span><h2 data-split>Roofing work we carry out.</h2></div>
<p>Explore our range of professional roofing services, from essential repairs to complete installations.</p></div>
{svc_cards(p, ROOF)}</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">The details matter</span><h2 data-split>Small problems, sorted properly.</h2></div></div>
<div class="cards c3 numbered" data-reveal="group">
<div class="card"><span class="bign">01</span><h3>Something wrong with your roof?</h3><p>Most roofing problems start with something small. A leak after heavy rain, a few loose tiles, damp around the chimney or a section of roof that has started to deteriorate. Left alone, these issues can quickly lead to more serious damage inside the property.</p></div>
<div class="card"><span class="bign">02</span><h3>Why choose Kiely Roofing?</h3><p>When you are bringing someone in to work on your home, you want to know the job will be handled properly. We focus on practical solutions, clear communication and completing the work required to keep your property protected.</p></div>
<div class="card"><span class="bign">03</span><h3>Need roofing work done?</h3><p>Whether you have noticed a leak, need damaged roofing repaired or are considering a roof replacement, talk to Kiely Roofing about the work required.</p><a class="tlink" href="#quote" data-qdrop style="margin-top:16px">Get a free quote {I['arrow']}</a></div>
</div></div></section>
{ba_section(p, BA_HOME)}
{health_teaser(p)}
<section class="sec"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">What we do</span><h2 data-split>Complete roofing &amp; home improvements.</h2></div>
<p>From the roof above your head to the rooms inside your home, we provide complete roofing, renovation and home improvement solutions.</p></div>
{svc_cards(p, HOME)}</div></section>
{process(p)}
{reviews_sec(p, [(n, g, t, s) for n, g, t, s in ALL_REVIEWS[:2]] + [r for r in ALL_REVIEWS if r[0] in ('Brian Farrell', 'Conor McCarthy')])}
{why()}
{areas_sec(p)}
{brands(p)}
{cta(p)}'''

def intro_visual(p, s):
    f = s['imgs'][0]
    if f in COMP:
        b, a, nt = COMP[f]
        return f'<div data-reveal>{compare(p, b, a, s["name"], "Drag to compare", notags=nt)}</div>'
    return pic(p, f, s['name'] + ' by Kiely Roofing & Construction, Dublin, Meath and Kildare')

def service_page(s):
    def body(p):
        items = ''.join(f'<li>{I["check"]}{x}</li>' for x in s['items'])
        det = ''
        for i, (t, paras, bl) in enumerate(s['details'], 1):
            ps = ''.join(f'<p>{x.replace("{p}", p)}</p>' for x in paras)
            ul = ('<ul class="links">' + ''.join(f'<li>{link(p, x)}</li>' for x in bl) + '</ul>') if bl else ''
            det += f'<div class="card"><span class="bign">0{i}</span><h3>{t}</h3>{ps}{ul}</div>'
        rv = [(n, s['group'], t, s['name']) for n, t in s['reviews']]
        if s['ba']:
            vis = f'''<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">The difference</span><h2 data-split>See the transformation.</h2></div><a class="btn btn-line" href="{p}gallery/">View our gallery {I['arrow']}</a></div>
<div class="ba-grid g3" data-reveal="group">{''.join(compare(p, b, a, s['name'], 'Drag to compare') for b, a in s['ba'])}</div></div></section>'''
        else:
            vis = f'''<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Recent work</span><h2 data-split>See the transformation.</h2></div><a class="btn btn-line" href="{p}gallery/">View our gallery {I['arrow']}</a></div>
<div class="boxes b3" data-reveal="group">{''.join(f'<a class="tile" href="{p}img/{g}"><img src="{p}img/{g}" alt="{s["name"]} by Kiely Roofing" loading="lazy"></a>' for g in s['gallery'])}</div></div></section>'''
        others = [o for o in (ROOF if s['group'] == 'roof' else HOME) if o is not s]
        oc = ''.join(f'<a class="mini" href="{p}{o["slug"]}/"><img src="{p}img/{o["imgs"][1]}" alt="" loading="lazy"><span>{I[o["icon"]]}{o["name"]}</span></a>' for o in others)
        return f'''{phero(p, [(s['name'], s['slug'] + '/')], s['name'] + '<br><span class="blue">Dublin, Meath &amp; Kildare.</span>', s['intro'][0], s['hero'], f' data-svc="{s["name"]}"')}
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">{s['eyebrow']}</span><h2 data-split>{s['h2']}</h2>{''.join(f'<p>{x}</p>' for x in s['intro'][1:])}
<div class="callrow"><a class="btn btn-blue" href="#quote-wizard" data-qdrop data-svc="{s['name']}">Get a free quote {I['arrow']}</a><div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div></div>
{intro_visual(p, s)}
</div></section>
<section class="sec soft"><div class="wrap split rev">
<div><h2 data-split>{s['list_h']}</h2>{f'<p>{s["list_intro"]}</p>' if s['list_intro'] else ''}<ul class="ticks cols2">{items}</ul>{f'<p>{s["list_outro"]}</p>' if s['list_outro'] else ''}
<a class="btn btn-line" href="#quote-wizard" data-qdrop data-svc="{s['name']}">{s['cta']} {I['arrow']}</a></div>
{pic(p, s['imgs'][1], s['name'] + ' in progress across Dublin, Meath and Kildare')}
</div></section>
<section class="sec"><div class="wrap"><div class="center" style="margin-bottom:48px"><span class="eyebrow">The details matter</span><h2 data-split>What you need to know.</h2></div>
<div class="cards c3 numbered" data-reveal="group">{det}</div></div></section>
{reviews_sec(p, rv)}
{vis}
<section class="sec"><div class="wrap split" style="align-items:start">
<div><span class="eyebrow">Free quote</span><h2 data-split>Tell us about the job.</h2><p>Free, no-obligation inspection and a clear, fixed price upfront. No callout fee and no hidden charges.</p>
{area_box()}<div class="contactmini"><a href="{TEL}">{I['phone']}{PHONE}</a><a href="{WAURL}" target="_blank" rel="noopener">{WA_ICON}WhatsApp a photo</a></div></div>
<div data-reveal>{form(p, 'Get a Free Quote', 'We aim to reply the same day.', svc=s['name'])}</div></div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">{'Roofing services' if s['group'] == 'roof' else 'Home improvements'}</span><h2 data-split>More ways we can help.</h2></div></div>
<div class="minis" data-reveal="group">{oc}</div></div></section>
{process(p, soft=False)}
{cta(p)}'''
    return body

def about(p):
    rv = [r for r in ALL_REVIEWS if r[0] in ('David Reilly', 'Aisling Doyle')]
    return f'''{phero(p, [('About Us', 'about-us/')], 'About <span class="blue">Kiely Roofing &amp; Construction.</span>', 'Roofing and home improvement work for residential properties, from individual repairs to larger renovation projects.', 'van-front.jpg')}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">About us</span><h2 data-split>About Kiely Roofing &amp; Construction.</h2>
<p class="lead" style="color:var(--ink)">Kiely Roofing carries out roofing and home improvement work for residential properties, from individual repairs to larger renovation projects.</p>
<p>Roofing is at the heart of the business, with work covering {link(p, 'Roof Repairs').lower().replace('roof repairs', 'roof repairs')}, replacement roofs, chimney repairs, flat roofing, guttering and dry verge systems. Alongside this, Kiely Roofing also undertakes attic conversions, house extensions, renovations, plastering and interior and exterior painting.</p>
<a class="btn btn-blue" href="{p}contact-us/">Contact us {I['arrow']}</a></div>
{pic(p, 'van-rear.jpg', 'Kiely Roofing & Construction van: roofing, tiling, felting, roof repairs, flat roofs')}
</div></section>
<section class="sec soft"><div class="wrap split rev">
<div><h2 data-split>From roof repairs to larger projects.</h2>
<p>Some jobs begin with a single problem, such as a leaking roof or damaged chimney. Others involve replacing an ageing roof or carrying out wider improvements to the property.</p>
<p>Kiely Roofing works across both, giving homeowners access to roofing and home improvement services through one business.</p>
<h2 data-split style="margin-top:40px">Roofing &amp; home improvements under one roof.</h2>
<p>As well as roofing work, Kiely Roofing carries out attic conversions, extensions, renovations, plastering and painting.</p>
<p>This wider range of services is useful where a project involves more than one part of the property and helps keep the work with one team from start to finish.</p></div>
{pic(p, 'roof-repair2.jpg', 'Chimney and pitched roof repair work from scaffolding')}
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">The difference</span><h2 data-split>See the transformation.</h2></div><a class="btn btn-line" href="{p}gallery/">View our gallery {I['arrow']}</a></div>
<div class="ba-grid g3" data-reveal="group">{compare(p, 'ba-house-rennovation-before.jpg', 'ba-house-rennovation-after.jpg', 'House renovation', 'Drag to compare')}{compare(p, 'ba-attic-converstion-before.jpg', 'ba-attic-converstion-after.jpg', 'Attic conversion', 'Drag to compare')}{compare(p, 'ba-plastering-before.jpg', 'ba-plastering-after.jpg', 'Plastering', 'Drag to compare')}</div></div></section>
{reviews_sec(p, rv)}
{process(p)}
{why()}
{brands(p)}
{cta(p)}'''

GAL = [('roof-replacement-mkd-2.jpg', 'roof'), ('roof-replacement-mkd.jpg', 'roof'), ('roof-replace-1.jpg', 'roof'), ('roof-replace-copy.jpg', 'roof'), ('roof-repairs-mkd-2.jpg', 'roof'), ('roof-repairs-mkd-1.jpg', 'roof'),
       ('roof-repair2.jpg', 'roof'), ('roof-repair.jpg', 'roof'), ('roof-repair-dublin.jpg', 'roof'), ('slate-roof-replacement.jpg', 'roof'), ('chimney-services-6.jpg', 'roof ba'), ('chimney-repair.jpg', 'roof'),
       ('flat-roof-installers-mkd.jpg', 'flat'), ('flat-roof-1.jpg', 'flat'), ('flat-roof-2.jpg', 'flat'), ('flat-roof-before-after.jpg', 'flat ba'),
       ('guttering-repairs-mkd-2.jpg', 'gutters'), ('guttering-repairs-mkd-1.jpg', 'gutters'), ('gutter-1.jpg', 'gutters'), ('dry-verge-replacement.jpg', 'gutters ba'), ('dry-verge.jpg', 'gutters'),
       ('house-extension-copy.jpg', 'home'), ('house-extensions-mkd-2.jpg', 'home'), ('house-renovation2.jpg', 'home ba'), ('house-renovation-mkd-1.jpg', 'home'), ('attic-conversions-mkd-2.jpg', 'home'), ('attic-converstion-before-after.jpg', 'home ba'),
       ('image4.jpg', 'home'), ('exterior-painting-services.jpg', 'home'), ('interior-exterior-painting-mkd-2.jpg', 'home'), ('interior-exterior-painting-mkd.jpg', 'home'), ('interior-exterior-painting-2.jpg', 'home'),
       ('plastering2.jpg', 'home'), ('plastering-1.jpg', 'home'), ('plastering-mkd-2.jpg', 'home'), ('plastering-mkd.jpg', 'home'), ('plastering-before-after.jpg', 'home ba')]
GAL_BA = [('roof-replacement-1a.jpg', 'roof-replacement-1b.jpg', 'Roof replacement'), ('roof-replacement-2a.jpg', 'roof-replacement-2b.jpg', 'Roof replacement'), ('roof-replacement-3a.jpg', 'roof-replacement-3b.jpg', 'Roof replacement'),
          ('b1.jpg', 'a1.jpg', 'Gutter repairs'), ('b5-1.jpg', 'a5.jpg', 'Gutter repairs'), ('b3.jpg', 'a3.jpg', 'Gutter repairs'), ('plastering-1a.jpg', 'plastering-1b.jpg', 'Plastering')]
def gallery(p):
    tiles = [(f, c) for f, c in GAL if f not in SKIP and 0.7 <= dims(f)[0] / dims(f)[1] <= 1.45]
    g = ''.join(f'<a class="tile" href="{p}img/{f}" data-cat="{c}"><img src="{p}img/{f}" alt="Roofing and building project by Kiely Roofing & Construction, Dublin, Meath and Kildare" loading="lazy"></a>' for f, c in tiles)
    fb = ''.join(f'<button type="button" data-f="{k}"{" class=\"on\"" if k == "all" else ""}>{v}</button>' for k, v in [('all', 'All work'), ('roof', 'Roofing'), ('flat', 'Flat roofs'), ('gutters', 'Gutters & verges'), ('home', 'Home improvements')])
    pairs = GAL_BA + [(COMP[k][0], COMP[k][1], t, COMP[k][2]) for k, t in [('roof-repair-before-after.jpg', 'Roof repair'), ('flat-roof-before-after.jpg', 'Flat roof'), ('dry-verge-replacement.jpg', 'Dry verge'), ('house-rennovation-before-after.jpg', 'House renovation'), ('attic-converstion-before-after.jpg', 'Attic conversion'), ('interior-exterior-painting-2.jpg', 'Exterior painting'), ('plastering-before-after.jpg', 'Plastering')]]
    sl = ''.join(compare(p, x[0], x[1], x[2], 'Drag to compare', notags=(x[3] if len(x) > 3 else False)) for x in pairs)
    return f'''{phero(p, [('Gallery', 'gallery/')], 'Recent projects <span class="blue">across Dublin, Meath &amp; Kildare.</span>', 'Explore our gallery of completed roofing and home improvement projects, featuring before and after images that showcase the quality of our work.', 'roof-replacement-2b.jpg')}
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Project gallery</span><h2 data-split>Our work.</h2></div><p>Tap any photo to see it full size.</p></div>
<div class="filters" data-filters="#galgrid">{fb}</div>
<div class="boxes" id="galgrid">{g}</div></div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Drag to compare</span><h2 data-split>Before &amp; after.</h2></div><p>Drag the slider across each photo to see the difference.</p></div>
<div class="ba-grid g3" data-reveal="group">{sl}</div></div></section>
{cta(p)}'''

def reviews(p):
    fb = ''.join(f'<button type="button" data-f="{k}"{" class=\"on\"" if k == "all" else ""}>{v}</button>' for k, v in [('all', f'All reviews ({len(ALL_REVIEWS)})'), ('roof', 'Roofing'), ('home', 'Home improvements')])
    ld = '\n<script type="application/ld+json">' + __import__('json').dumps({"@context": "https://schema.org", "@type": "RoofingContractor", "name": "Kiely Roofing & Construction", "url": SITE + "/",
        "review": [{"@type": "Review", "author": {"@type": "Person", "name": n}, "reviewRating": {"@type": "Rating", "ratingValue": "5"}, "reviewBody": t} for n, g, t, s in ALL_REVIEWS]}, ensure_ascii=False) + '</script>'
    body = lambda p: f'''{phero(p, [('Reviews', 'reviews/')], 'Customer <span class="blue">reviews.</span>', 'At Kiely Roofing &amp; Construction, we take pride in our commitment to customer satisfaction. Here’s what some of our customers have to say.', 'house-extensions-mkd-2.jpg')}
<section class="sec"><div class="wrap">
<div class="revtop"><div class="big5"><b>5.0</b>{stars()}<span>Excellent reviews rating</span></div><div class="filters" data-filters="#revwall">{fb}</div></div>
<div id="revwall">{review_cards(ALL_REVIEWS, 'rwall')}</div></div></section>
{cta(p)}'''
    return body, ld

def contact(p):
    return f'''<section class="phero chero" data-rain>
<img class="bg" src="{p}img/roofing-guttering-slider.jpg" alt="" fetchpriority="high">
<div class="wrap chgrid">
<div data-reveal>{form(p, 'Get a Free Quote', 'Free quotes and no callout fee. We aim to reply the same day.')}</div>
<div><div class="crumb"><a href="{p}">Home</a><span>/</span><b>Contact Us</b></div>
<h1>Contact <span class="blue">Kiely Roofing &amp; Construction.</span></h1>
<p class="lead">Contact us for any enquiries you may have regarding our services. We also provide free quotes. Fill out the form and we will get back to you as soon as possible.</p>
<ul class="clist">
<li><a href="{TEL}">{I['phone']}<span><small>Call</small><b data-cfg="phone">{PHONE}</b></span></a></li>
<li><a href="mailto:{EMAIL}">{I['mail']}<span><small>Email</small><b data-cfg="email">{EMAIL}</b></span></a></li>
<li><a href="{WAURL}" target="_blank" rel="noopener">{WA_ICON}<span><small>WhatsApp</small><b>Send us a photo of the job</b></span></a></li>
<li><span class="nolink">{I['clock']}<span><small>Hours</small><b>Mon–Sun: 7am–10pm</b></span></span></li>
</ul></div>
</div></section>
<section class="sec"><div class="wrap split" style="align-items:start">
<div><span class="eyebrow">Service areas</span><h2 data-split>Roofers across Dublin, Meath &amp; Kildare.</h2>
<p>We provide services across Meath, Kildare &amp; Dublin and surrounding areas. Based in Longwood, Co. Meath.</p>
{area_box()}</div>
<div class="map"><iframe title="Kiely Roofing location: Longwood, Co. Meath" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=Longwood%2C%20Co.%20Meath%2C%20Ireland&amp;z=9&amp;output=embed"></iframe></div>
</div></section>
{cta(p)}'''

AREAS = {'Dublin': ['Lucan', 'Blanchardstown', 'Castleknock', 'Clonsilla', 'Ongar', 'Finglas', 'Clondalkin', 'Tallaght', 'Saggart', 'Rathcoole', 'Swords', 'Malahide', 'Balbriggan', 'Skerries', 'Rush', 'Lusk', 'Donabate', 'Santry', 'Glasnevin', 'Drumcondra', 'Cabra', 'Palmerstown', 'Ballyfermot', 'Mulhuddart', 'Dundrum', 'Rathfarnham', 'Terenure', 'Crumlin', 'Raheny', 'Clontarf', 'Howth', 'Portmarnock'],
         'Meath': ['Longwood', 'Navan', 'Trim', 'Ashbourne', 'Ratoath', 'Dunboyne', 'Kells', 'Laytown', 'Bettystown', 'Enfield', 'Athboy', 'Dunshaughlin', 'Clonee', 'Stamullen', 'Duleek', 'Slane', 'Summerhill'],
         'Kildare': ['Maynooth', 'Celbridge', 'Leixlip', 'Naas', 'Newbridge', 'Kildare Town', 'Clane', 'Kilcock', 'Edenderry', 'Carbury', 'Johnstownbridge', 'Prosperous', 'Sallins', 'Straffan', 'Athy', 'Monasterevin']}

def areas_sec(p, soft=False):
    cols = ''.join(f'<div class="area"><h3>{I["pin"]}{"Roofers " + c if c == "Dublin" else "Co. " + c}</h3><div class="chips">{"".join(f"<span>{t}</span>" for t in ts)}</div></div>' for c, ts in AREAS.items())
    return f'''<section class="sec{' soft' if soft else ''}"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">Areas we cover</span><h2 data-split>Roofers in Dublin, Meath &amp; Kildare.</h2></div>
<p>Roof repairs, roof replacements, flat roofing, chimney repairs, guttering and home improvements across Dublin, Meath, Kildare and surrounding areas.</p></div>
<div class="areas" data-reveal="group">{cols}</div>
<div class="btn-row" style="margin-top:28px"><a class="btn btn-line" href="{p}roofers-dublin/">Roofers in Dublin {I['arrow']}</a><a class="btn btn-blue" href="#quote" data-qdrop>Get a free quote {I['arrow']}</a></div>
</div></section>'''

DUB_FAQ = [('Do you cover all of Dublin?', 'Yes. Kiely Roofing &amp; Construction carries out roofing work across Dublin, from Lucan, Blanchardstown, Castleknock and Clondalkin to Swords, Malahide, Tallaght and Dublin city, as well as Meath, Kildare and surrounding areas.'),
           ('Do you charge a callout fee?', 'No. We offer free callouts and a free, no-obligation inspection, followed by a clear, fixed price upfront with no hidden charges.'),
           ('Do you carry out emergency roof repairs in Dublin?', 'Yes. If high winds, heavy rain or sudden damage have left your roof exposed, emergency repair work can help make the property secure and reduce the risk of further water damage.'),
           ('Should I repair or replace my roof?', 'Not every damaged roof needs to be replaced. A focused repair may be enough to extend the life of the existing roof. Where the roof is older, badly deteriorated or suffering from repeated problems, replacement may be the better long-term option. We will always tell you if a repair will do the job.'),
           ('Are you insured?', 'Yes. All work is fully insured, and quality work and materials are guaranteed.')]
def dublin_ld():
    import json as _j
    return '\n<script type="application/ld+json">' + _j.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace('&amp;', '&')}} for q, a in DUB_FAQ]}, ensure_ascii=False) + '</script>'

def dublin(p):
    faq = ''.join(f'<details class="faq"><summary>{q}<i>{I["chev"]}</i></summary><p>{a}</p></details>' for q, a in DUB_FAQ)
    chips = ''.join(f'<span>{t}</span>' for t in AREAS['Dublin'])
    rv = [r for r in ALL_REVIEWS if r[0] in ('Brian Farrell', 'John O’Connell', 'Mary O’Sullivan', 'Patrick Byrne')]
    return f'''{phero(p, [('Roofers Dublin', 'roofers-dublin/')], 'Roofers in <span class="blue">Dublin.</span>', 'Roof repairs, roof replacements, flat roofing, chimney repairs, guttering and dry verge systems for homes across Dublin. Free quotes and no callout fee.', 'roof-replacement-mkd-2.jpg')}
{marquee()}
<section class="sec"><div class="wrap split">
<div><span class="eyebrow">Roofing contractors Dublin</span><h2 data-split>Dublin roofers you can rely on.</h2>
<p>Kiely Roofing &amp; Construction carries out roof repairs, replacements and roofing work for homeowners and landlords right across Dublin. Based nearby in Longwood, Co. Meath, we work throughout Dublin city and county, as well as Meath and Kildare.</p>
<p>Whether you have a leaking roof after heavy rain, slipped or broken tiles, storm damage, a damaged chimney or an ageing roof that keeps causing problems, we can assess what is happening and advise on the right next step. Every job starts with a free inspection and a clear, fixed written quote.</p>
<ul class="ticks cols2">{''.join(f'<li>{I["check"]}{t}</li>' for t in ['Free inspection & quote', 'No callout fee', 'Fully insured', 'Quality work & materials guaranteed', 'Emergency roof repairs', 'Rated 5 / 5 by customers'])}</ul>
<div class="callrow"><a class="btn btn-blue" href="#quote" data-qdrop>Get a free quote {I['arrow']}</a><div><small>Prefer to call?</small><a class="num" href="{TEL}">{PHONE}</a></div></div></div>
{pic(p, 'roof-replacement-mkd-2.jpg', 'New roof installation in Dublin by Kiely Roofing')}
</div></section>
<section class="sec soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Roofing services in Dublin</span><h2 data-split>Roofing work we carry out.</h2></div></div>
{svc_cards(p, ROOF)}</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Home improvements in Dublin</span><h2 data-split>Extensions, attics &amp; renovations.</h2></div></div>
{svc_cards(p, HOME)}</div></section>
<section class="sec soft"><div class="wrap"><span class="eyebrow">Areas we cover in Dublin</span><h2 data-split>From Lucan to Howth.</h2>
<div class="chips big" data-reveal>{chips}</div>{area_box()}</div></section>
{reviews_sec(p, rv)}
<section class="sec"><div class="wrap split" style="align-items:start">
<div><span class="eyebrow">FAQs</span><h2 data-split>Roofing in Dublin: your questions.</h2><div class="faqs">{faq}</div></div>
<div data-reveal>{form(p, 'Get a Free Quote', 'Free roof inspection anywhere in Dublin. No callout fee.')}</div></div></section>
{process(p)}
{cta(p)}'''

HQ = [('How old is your roof?', [('Under 10 years', 0), ('10–20 years', 1), ('20–30 years', 2), ('30+ years / not sure', 3)]),
      ('Any leaks?', [('No leaks', 0), ('One area', 1), ('Leaks in different places', 3)]),
      ('Slates and tiles?', [('All look fine', 0), ('A few slipped or broken', 1), ('Cracked or missing across large areas', 3)]),
      ('Any sagging along the ridge or roof line?', [('No', 0), ('Not sure', 1), ('Yes', 3)]),
      ('Damp, mould or daylight in the attic?', [('No', 0), ('A little damp', 1), ('Yes, daylight or mould', 2)]),
      ('Moss on the roof?', [('Little or none', 0), ('Some', 0), ('Heavy moss lifting tiles', 1)])]
def health(p):
    qs = ''.join(f'<div class="hq"><span class="hn">0{i}</span><h3>{q}</h3><div class="hopts">{"".join(f"<button type=button data-s={s}>{t}</button>" for t, s in o)}</div></div>' for i, (q, o) in enumerate(HQ, 1))
    return f'''{phero(p, [('Roof Health Check', 'roof-health-check/')], 'Roof health check: <span class="blue">repair or replace?</span>', 'Answer six quick questions about your roof. We’ll tell you what it sounds like, then you can book a free inspection to be sure.', 'roof-repairs-mkd-1.jpg')}
<section class="sec"><div class="wrap health" id="health">
<div class="hqs"><div class="hhead"><span class="hcount">0 of 6 answered</span><div class="hprog"><i></i></div><button class="hreset" type="button">Start again</button></div>{qs}</div>
<aside class="hside"><div class="hres"><span class="eyebrow">Your result</span><h3></h3><div class="hscore"><i></i></div><div class="glabels"><span>Repair</span><span>Plan ahead</span><span>Replace</span></div><p></p>
<div class="btn-row"><a class="btn btn-blue" href="#quote" data-qdrop>Book a free inspection {I['arrow']}</a><a class="btn btn-line hlink" data-base="{p}" href="{p}roof-repairs/">About roof repairs</a></div>
<p class="fnote" style="text-align:left">This is a guide only. Not every problem needs a new roof, and we’ll always tell you if a repair will do the job.</p></div>
<div class="hwait"><span class="ico">{I['gauge']}</span><h3>Your result appears here</h3><p>Answer all six questions to see whether your roof sounds like a repair or a replacement.</p></div></aside>
</div></section>
{cta(p)}'''

def privacy(p):
    secs = [('What information do you hold on me?', 'Whenever you use one of the forms on this website to contact us or send us other information we keep a record of these form transmissions in our secure online database and in our email inbox. We may collect your personal details as name, email, and any other information you sent to us by either using a form on this website or by using a direct email link in other offline ways such as an Excel spreadsheet or custom made database.'),
            ('Why do you keep my personal data?', 'We keep record of your personal data to be able to contact you now or in the future. We only contact you in relation to your original request. We will not use your personal data for any other purposes like newsletters (unless you explicitly told us to do so) or sell/give your personal data to third parties.'),
            ('Who has access to my personal data?', 'Anyone who works at Kiely Roofing &amp; Construction can have access to your personal data.'),
            ('What happens in case of a security breach?', 'In the unlikely event your data is lost, stolen or accessed without authority you and the Data Protection Commissioner will be notified within 72 hours.'),
            ('How can I control my personal data?', f'To see the exact information we hold on you, email <a class="blue" href="mailto:{EMAIL}">{EMAIL}</a> and we will send you a copy of all data we have stored. You can also email us requesting us to completely remove your data from our database.'),
            ('How do we handle your personal data?', 'Kiely Roofing &amp; Construction fully respects your right to privacy and actively seeks to preserve the privacy rights of those who share information on this site. We will not collect any personal information about you on this website without your permission save in cases where it’s required by law to do so. Any personal information which you volunteer will be treated with the highest standards of security and confidentiality, in accordance with Data Protection. We do not share any individual’s personal data for third party marketing purposes. We do not engage in cross-marketing or link-referral programs. We do not send unsolicited communications for marketing purposes.'),
            ('Collection of personal information', 'Kiely Roofing &amp; Construction only collects personal data about you which you volunteer (for example by emailing the company or using a form). Any information which you provide in this way is not made available to any third party, other than those working with Kiely Roofing &amp; Construction, and is used only in line with the purpose for which you provided it.'),
            ('Cookies and technical information', 'This website does not use advertising or tracking cookies. It stores one item in your browser’s session storage so the opening animation only plays once per visit. The map on the contact page is provided by Google, which may set its own cookies. Technical details in connection with visits may be logged by our hosting provider for security and administrative purposes.'),
            ('Security', 'Your personal data is held securely. The nature of the Internet is such that we cannot guarantee the security of any information you transmit to us via the Internet. However, we will take all reasonable steps (including appropriate technical and organisational measures) to protect your personal data.')]
    return f'''{phero(p, [('Privacy Policy', 'privacy-policy/')], 'Privacy policy.', 'How we handle your personal data.', 'gutter-1.jpg')}
<section class="sec"><div class="wrap article"><p>As of May 25th, 2018, every European company has to comply with the European General Data Protection Regulation, or GDPR.</p>
{''.join(f'<h2>{a}</h2><p>{b}</p>' for a, b in secs)}</div></section>
{cta(p)}'''

if __name__ == '__main__':
    page('', 'home', 'Roofers Dublin, Meath & Kildare | Roof Repairs & Replacement | Kiely Roofing', 'Kiely Roofing & Construction: trusted roofers in Dublin, Meath and Kildare. Roof repairs, new roofs, flat roofing, chimney repairs and guttering. Free quotes, no callout fee.', home, intro=True)
    page('roofers-dublin/', 'roof', 'Roofers Dublin | Roof Repairs & Roofing Contractors Dublin | Kiely Roofing', 'Looking for roofers in Dublin? Kiely Roofing carries out roof repairs, roof replacements, flat roofing, chimney repairs and guttering across Dublin. Free quotes, no callout fee.', dublin, extra_ld=dublin_ld(), kw='Roofers Dublin')
    for s in SERVICES:
        page(s['slug'] + '/', 'roof' if s['group'] == 'roof' else 'home-imp', f"{s['name']} Dublin, Meath & Kildare | Kiely Roofing", s['desc'].replace('Meath, Kildare & Dublin', 'Dublin, Meath & Kildare'), service_page(s), kw=s['name'])
    page('about-us/', 'about', 'About Us | Roofing & Home Improvements | Kiely Roofing', 'Kiely Roofing & Construction: roofing and home improvement work across Meath, Kildare & Dublin, from repairs to larger renovation projects.', about)
    page('gallery/', 'gallery', 'Gallery - Kiely Roofing & Construction', 'Before and after photos of roofing, guttering, flat roof, extension, renovation, plastering and painting projects by Kiely Roofing.', gallery)
    rb, rld = reviews(None)
    page('reviews/', 'reviews', 'Customer Reviews - Kiely Roofing & Construction', 'Read customer reviews of Kiely Roofing & Construction. Rated 5/5 for roofing and home improvements across Meath, Kildare & Dublin.', rb, extra_ld=rld)
    page('contact-us/', 'contact', 'Contact Us - Kiely Roofing & Construction', 'Contact Kiely Roofing & Construction for a free quote. Call 087 359 2163 or email info@kielyroofing.ie.', contact)
    page('roof-health-check/', 'roof', 'Roof Health Check: Repair or Replace? | Kiely Roofing', 'Free 60-second roof check: answer six questions to see whether your roof sounds like a repair or a replacement.', health)
    page('privacy-policy/', '', 'Privacy Policy - Kiely Roofing & Construction', 'How Kiely Roofing & Construction handles your personal data.', privacy)
    # sitemap + robots
    urls = ['', 'roofers-dublin'] + [s['slug'] for s in SERVICES] + ['about-us', 'gallery', 'reviews', 'contact-us', 'roof-health-check', 'privacy-policy']
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}/{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
