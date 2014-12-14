#!/bin/sh

themes='amelia cerulean cosmo cyborg darkly flatly journal lumen paper readable sandstone simplex slate spacelab superhero united yeti'

static_dir=kotti_bootswatch_theme/static

for theme in $themes; do
    echo $theme
    bootswatch_theme_dir="$static_dir/bootswatch/$theme"
    override_dir="$static_dir/kotti_override"
    override_theme_dir="$static_dir/kotti_override/$theme"

    [ -d $bootswatch_theme_dir ] || echo $bootswatch_theme_dir not found
    mkdir -p $override_theme_dir
    for component in base view edit upload; do
        lessc --include-path="$bootswatch_theme_dir" "$override_dir/$component.less" > "$override_theme_dir/$component.css"
    done

    tree $override_dir
done
