# Final Submission

<!-- GUIDE: Start the outline of the final report in Phase 4, not Phase 5. If you documented
     as you went, most sections are assembly and editing of documents you already have. -->

## What to submit

| Deliverable | File | Status |
|---|---|---|
| Final report (source) | [final-report.md](final-report.md) | TODO |
| Final report (PDF) | `final-report.pdf` | TODO |
| Presentation slides (PDF) | `final-presentation.pdf` | TODO |
| Demo video | TODO: link | TODO |
| Repository in its final state | This repository, tagged `v1.0-final` | TODO |

Use the [presentation outline](presentation-outline.md) to plan your slides. Build the slides in any tool (PowerPoint, Google Slides, Keynote, Canva) and export a PDF here. If your examiners require editable slides, also commit the `.pptx`.

## Exporting the report to PDF or Word

Option 1: [pandoc](https://pandoc.org/installing.html). Run it from this folder so image paths resolve:

```bash
cd docs/06-reports/final
pandoc final-report.md -o final-report.pdf --toc     # PDF, needs a LaTeX install
pandoc final-report.md -o final-report.docx --toc    # Word, no LaTeX needed
```

Option 2: open the file in VS Code with a Markdown PDF extension, or print the rendered GitHub page to PDF.

Mermaid diagrams do not render in pandoc. Export them as images first (for example with the [Mermaid Live Editor](https://mermaid.live)) and link the images in the report.

## Tag the final version

```bash
git tag -a v1.0-final -m "Final submission"
git push origin v1.0-final
```

## Final checklist

- [ ] Every section of the final report filled in; no `TODO` or `EXAMPLE` left
- [ ] Every figure has a caption and is referred to in the text
- [ ] Every claim of performance cites a test and its evidence
- [ ] References complete and in one consistent style
- [ ] Spelling and grammar checked; read aloud once by someone who did not write it
- [ ] PDF exported and opened to check formatting
- [ ] Slides PDF committed; demo video plays from the link
- [ ] `python tools/check_docs.py --strict` passes
- [ ] Repository tagged
