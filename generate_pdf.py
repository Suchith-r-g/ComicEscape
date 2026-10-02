import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (Top)
        self.drawString(36, 762, "COMICESCAPE: 100-HOUR GAME JAM PROPOSAL")
        self.drawRightString(576, 762, "GAME DESIGN DOCUMENT")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.8)
        self.line(36, 756, 576, 756)
        
        # Footer (Bottom)
        self.line(36, 30, 576, 30)
        self.setFont("Helvetica", 8)
        self.drawString(36, 20, "CONFIDENTIAL & JAM COMPLIANT - GODOT 4.X")
        self.drawRightString(576, 20, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf(filename="Proposal.pdf"):
    # Exactly 2-page document with 36pt (0.5 inch) margins
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=38,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#1A202C"),
        spaceAfter=2
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=5
    )
    
    sec_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13.5,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=3,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=3
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10,
        textColor=colors.HexColor("#2D3748")
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10,
        textColor=colors.HexColor("#1A202C")
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#742A2A")
    )

    story = []

    # ================= PAGE 1 =================
    story.append(Paragraph("ComicEscape", title_style))
    story.append(Paragraph("A 3D First-Person Comic Escape Room with an Anti-Gravity Twist | 100-Hour Game Jam", subtitle_style))
    
    # Team Members Table
    team_data = [
        [
            Paragraph("<b>G. Suchith Reddy</b><br/><font color='#4A5568'>gattusuchithreddy999@gmail.com</font>", table_cell),
            Paragraph("<b>Thadikonda N V V D Malleeswari</b><br/><font color='#4A5568'>thadikondamalleeswari@gmail.com</font>", table_cell),
            Paragraph("<b>Adithya Thakur</b><br/><font color='#4A5568'>yash007adithya@gmail.com</font>", table_cell)
        ]
    ]
    t_team = Table(team_data, colWidths=[180, 190, 170])
    t_team.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_team)
    story.append(Spacer(1, 4))

    # Overview Table
    overview_data = [
        [Paragraph("Genre", table_cell_bold), Paragraph("3D First-Person Escape Room", table_cell),
         Paragraph("Engine", table_cell_bold), Paragraph("Godot 4.x (Compatibility / WebGL)", table_cell)],
        [Paragraph("Target Playtime", table_cell_bold), Paragraph("10 – 15 Minutes (3 Zones)", table_cell),
         Paragraph("Platform", table_cell_bold), Paragraph("Web (Itch.io HTML5) & Windows PC", table_cell)],
        [Paragraph("Visual Style", table_cell_bold), Paragraph("Cel-shaded comic, ink outlines, halftone", table_cell),
         Paragraph("Core Control", table_cell_bold), Paragraph("WASD, Mouse Look, Space (Float), E", table_cell)],
    ]
    t_overview = Table(overview_data, colWidths=[80, 190, 80, 190])
    t_overview.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_overview)
    story.append(Spacer(1, 4))

    # 1. Simple Concept
    story.append(Paragraph("1. The Simple Concept", sec_title))
    story.append(Paragraph(
        "You are trapped inside an interactive, illustrated comic book vault. "
        "A broadcast announces that you must find a legendary <b>'Comic Book Issue #1'</b> to unlock the exit door. "
        "Using regular walking combined with an <b>Anti-Gravity Floating power</b>, you navigate past hazards, reach high shelves, "
        "and solve spatial puzzles to retrieve the comic.",
        body_style
    ))

    # 2. Core Mechanics in Plain Terms
    story.append(Paragraph("2. Core Mechanics in Plain Terms", sec_title))
    mech_data = [
        [Paragraph("First-Person Movement", table_cell_bold),
         Paragraph("Smooth walk, look around, inspect objects, and press buttons using the standard 'E' key.", table_cell)],
        [Paragraph("The Floating Power", table_cell_bold),
         Paragraph("Press <b>Space / F</b> to invert gravity. Your character gently floats upward with high damping, letting you fly over laser tripwires, reach high ventilation shafts, and access upper balconies.", table_cell)],
        [Paragraph("Floating Stamina Bar", table_cell_bold),
         Paragraph("A simple comic gauge restricts infinite flight. You must plan your float paths between safe landing pads.", table_cell)],
        [Paragraph("Comic Feedback", table_cell_bold),
         Paragraph("Sound effects generate bold visual comic onomatopoeia billboards (e.g. <i>*WHOOSH*</i> when floating, <i>*CLICK*</i> on switches, <i>*CREAK*</i> on doors).", table_cell)],
    ]
    t_mech = Table(mech_data, colWidths=[120, 420])
    t_mech.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#EBF8FF")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#BEE3F8")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_mech)
    story.append(Spacer(1, 4))

    # 3. The 3 Playable Zones
    story.append(Paragraph("3. The 3 Playable Zones (10–15 Minutes Total)", sec_title))
    zones_data = [
        [Paragraph("Zone 1: The Gutter (Tutorial)", table_cell_bold),
         Paragraph("A basic two-story archive room. Teaches movement and the float ability to reach a switch high on a catwalk.", table_cell)],
        [Paragraph("Zone 2: The Grid (Navigation)", table_cell_bold),
         Paragraph("A vertical, multi-tiered puzzle room. Use fans, float over tripwires, and place weighted boxes on pressure plates to unlock the safe holding <b>Comic Book Issue #1</b>.", table_cell)],
        [Paragraph("Zone 3: Splash Page (The Exit)", table_cell_bold),
         Paragraph("A dramatic catwalk crossing over an abyss leading to a giant, intimidating steel blast door covered in caution tape.", table_cell)],
    ]
    t_zones = Table(zones_data, colWidths=[140, 400])
    t_zones.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F7FAFC")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_zones)
    story.append(Spacer(1, 4))

    # 4. The Big Meta-Twist
    story.append(Paragraph("4. The Big Meta-Twist (The Punchline)", sec_title))
    callout_data = [[
        Paragraph(
            "<b>The Subversion:</b> After 15 minutes of floating and solving puzzles to bring Issue #1 to the exit, "
            "the player interacts with the monolithic door. The massive metal lock is actually a flat cardboard cutout, "
            "and the door swings open freely with a tiny squeak (<i>*CREAK...*</i>). "
            "<b>The door was never locked all along!</b> The game ends with a humorous comic book splash page celebrating "
            "the player's over-complicated journey.",
            callout_style
        )
    ]]
    t_callout = Table(callout_data, colWidths=[540])
    t_callout.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFF5F5")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#FEB2B2")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_callout)

    # PAGE BREAK TO PAGE 2
    story.append(PageBreak())

    # ================= PAGE 2 =================
    story.append(Paragraph("PROJECT EXECUTION & JAM ROADMAP", title_style))
    story.append(Paragraph("100-Hour Milestone Schedule, Compliance Rules & Technical Stack", subtitle_style))

    # 5. The 100-Hour Jam Schedule
    story.append(Paragraph("5. The 100-Hour Jam Production Schedule", sec_title))
    schedule_data = [
        [Paragraph("Hours", table_cell_bold), Paragraph("Phase", table_cell_bold), Paragraph("Key Deliverables & Milestones", table_cell_bold)],
        [Paragraph("0 – 10", table_cell_bold), Paragraph("Setup & Scope Lock", table_cell),
         Paragraph("Create fresh Git repository, configure Godot 4.x project settings, establish folder architecture, lock mechanics scope.", table_cell)],
        [Paragraph("10 – 40", table_cell_bold), Paragraph("Core Controller & Graybox", table_cell),
         Paragraph("Build first-person character movement, mouse look, raycast interaction (doors, buttons), and block out primitive geometry for all 3 zones.", table_cell)],
        [Paragraph("40 – 70", table_cell_bold), Paragraph("Floating & Puzzle Logic", table_cell),
         Paragraph("Script the anti-gravity float toggle, float meter, laser hazards, fan drafts, pressure plates, and Issue #1 pickup.", table_cell)],
        [Paragraph("70 – 90", table_cell_bold), Paragraph("Assets, Comic Art & Audio", table_cell),
         Paragraph("Implement cel-shade & ink outline post-processing, import CC0 3D models (Kenney.nl), add comic speech bubbles, UI gauge, and sound effects.", table_cell)],
        [Paragraph("90 – 100", table_cell_bold), Paragraph("Testing, Web Export & Itch.io", table_cell),
         Paragraph("Test HTML5 WebGL export across browsers, tune jump/float balance, capture screenshots/GIFs, complete README and CREDITS.md, submit to jam.", table_cell)],
    ]
    t_sched = Table(schedule_data, colWidths=[55, 125, 360])
    t_sched.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F7FAFC")]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_sched)
    story.append(Spacer(1, 5))

    # 6. Jam Compliance & Rules
    story.append(Paragraph("6. Strict Jam Compliance & Asset Provenance", sec_title))
    comp_data = [
        [Paragraph("Rule Requirement", table_cell_bold), Paragraph("Project Adherence & Action Plan", table_cell_bold)],
        [Paragraph("Fresh Codebase", table_cell), Paragraph("Zero pre-existing code templates. All scripts written from scratch after the jam clock begins.", table_cell)],
        [Paragraph("Public GitHub Repo", table_cell), Paragraph("Hosted publicly with clear, incremental commit history demonstrating 100-hour progression.", table_cell)],
        [Paragraph("100% Free / CC0 Assets", table_cell), Paragraph("3D environment props from Kenney.nl (CC0), SFX from Freesound.org (CC0), open fonts (SIL OFL).", table_cell)],
        [Paragraph("Attribution Document", table_cell), Paragraph("Maintained <b>CREDITS.md</b> listing exact URLs, author names, and licenses for every external file.", table_cell)],
    ]
    t_comp = Table(comp_data, colWidths=[130, 410])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 5))

    # 7. Why This Works (Risk & Feasibility)
    story.append(Paragraph("7. Jam Feasibility & Why This Succeeds", sec_title))
    story.append(Paragraph(
        "• <b>Laser-Focused Scope:</b> 3 small rooms and 1 hero mechanic prevent feature creep within 100 hours.<br/>"
        "• <b>Instant Web Playability:</b> Godot 4 Compatibility renderer enables one-click play in browser, maximizing jam judge ratings.<br/>"
        "• <b>Memorable Punchline:</b> The unlocked-door twist creates an emotional and comedic payoff that stands out in game jams.<br/>"
        "• <b>Modular Contingency:</b> If time runs tight, Zone 2's laser puzzle can be simplified without hurting the narrative payoff.",
        body_style
    ))
    story.append(Spacer(1, 5))

    # Sign-off box
    summary_box_data = [[
        Paragraph(
            "<b>Development Team:</b> G. Suchith Reddy | Thadikonda N V V D Malleeswari | Adithya Thakur<br/>"
            "<i>ComicEscape</i> is achievable in 100 hours, visually striking, fully jam-compliant, and delivers an unforgettable meta-twist.",
            body_style
        )
    ]]
    t_sum = Table(summary_box_data, colWidths=[540])
    t_sum.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EBF8FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#3182CE")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_sum)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF build successful.")

if __name__ == "__main__":
    build_pdf("c:/Users/gattu/Desktop/ComicEscape/Proposal.pdf")
