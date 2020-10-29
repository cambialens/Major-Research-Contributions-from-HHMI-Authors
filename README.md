# Major Research Contributions from HHMI Authors

A method for identifiying scholarly works in Lens.org with major contibutions from Howard Hughes Medical Institute (HHMI) affiliated authors.

HHMI identifies major contributions to research publications as scholarly works with HHMI affiliated authors that are either:
1. First author, or 
2. Last author, or
3. At least two authors from HHMI on a scholarly work.  

Any of these conditions are considered a major contribution by HHMI. The below steps outline the process to identify scholarly works published in **2019/2020** with major contributions from HHMI authors using [Lens.org](https://www.lens.org/).

## Steps to calculate major contributions

### 1. Create a query for all scholarly works with HHMI affiliations

* Run the following query on Lens.org: `author.affiliation.name:("HHMI") OR author.affiliation.name:("Howard Hughes Medical Institute") OR author.affiliation.name:("Janelia Research Campus")` and filter for `Year Published = ( 2019 - 2020 )` - see [https://link.lens.org/HBk5WkGstph](https://link.lens.org/HBk5WkGstph)
* Export the results in JSON format (e.g. [HHMI-2019-2020.json](https://github.com/cambialens/Major-Research-Contributions-from-HHMI-Authors/blob/main/HHMI-2019-2020.json)). 
  - **NB** You must be logged in to export your results.

### 2. Run the following [JQuery](https://jquery.com/) command on the JSON export file

* `jq --raw-output '.[] | select(.authors | [.[0,-1], .[]] | [.[].affiliations | select(. != null) | .[].name | select(contains("HHMI") or contains("Howard Hughes Medical Institute") or contains("Janelia Research Campus"))] | length > 2) | .lens_id' ~/Downloads/HHMI-2019-2020.json`
* This will generate an output file of `Lens IDs` for scholarly works matching the criteria for major contributions from HHMI authors.

### 3. Create a Lens collection

* The `Lens IDs` can then be imported into a [collection](https://www.lens.org/lens/search/scholar/list?collectionId=184091) on Lens.org for further analysis or export. 
* The collection can also be queried to identify the scholarly works with first/last HHMI authors:
  - HHMI first authors: [author_first.affiliation.name:("Howard Hughes Medical Institute" OR  "HHMI" OR "Janelia Research Campus")](https://link.lens.org/SztavRfCsyi)
  - HHMI last authors: [author_last.affiliation.name:("Howard Hughes Medical Institute" OR  "HHMI" OR "Janelia Research Campus")](https://link.lens.org/WftDLlu6Hok)
