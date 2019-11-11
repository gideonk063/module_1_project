# Project to-do

## Cleaning

### bom.movie_gross

remove foreign_gross
remove rows with na values in domestic_gross and studio

### name.basics

remove birth_year and death_year

### rt.movie_info

remove currency studio and box_office
remove rows with na

### rt.reviews

remove rating and review
group by id

### title.akas

remove language region types and attributes
fix na in is_original_title

### title.basics

remove runtime_minutes and genres
set na original_title equal to primary_title

### title.principals

remove job and characters

## Grouping

use title to group different sources
rt won't group with other sources
use title.akas to take different spellings into account
