#!/bin/sh

themes='amelia cerulean cosmo cyborg darkly flatly journal lumen paper readable sandstone simplex slate spacelab superhero united yeti'

static_dir=kotti_bootswatch_theme/static

for theme in $themes; do
    echo $theme
    bootswatch_theme_dir="$static_dir/bootswatch/$theme"
    kotti_dir="$static_dir/kotti"
    kotti_theme_dir="$static_dir/kotti/$theme"

    [ -d $bootswatch_theme_dir ] || echo $bootswatch_theme_dir not found
    mkdir -p $kotti_theme_dir
    for component in base view edit upload; do
        lessc --include-path="$bootswatch_theme_dir" "$kotti_dir/$component.less" > "$kotti_theme_dir/$component.css"
    done
done
