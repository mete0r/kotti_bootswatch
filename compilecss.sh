#!/bin/sh

themes='amelia cerulean cosmo cyborg darkly flatly journal lumen paper readable sandstone simplex slate spacelab superhero united yeti'

static_dir=kotti_bootswatch/static

for theme in $themes; do
    echo $theme
    bootswatch_theme_dir="$static_dir/bootswatch/$theme"
    kotti_dir="$static_dir/kotti"
    kotti_theme_dir="$static_dir/kotti/$theme"

    [ -d $bootswatch_theme_dir ] || echo $bootswatch_theme_dir not found
    mkdir -p $kotti_theme_dir
    for src_path in $kotti_dir/*.less; do
        src_file=`basename $src_path`
        component=`echo $src_file | sed -e 's/[.]less$//g'`
        lessc --include-path="$bootswatch_theme_dir" "$kotti_dir/$component.less" > "$kotti_theme_dir/$component.css"
        minify "$kotti_theme_dir/$component.css" > "$kotti_theme_dir/$component.min.css"
    done
done
