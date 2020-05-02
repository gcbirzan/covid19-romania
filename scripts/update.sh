#!/bin/bash


while true; do
    f_name=$(date +%s)
    curl -o "$f_name" "https://services7.arcgis.com/I8e17MZtXFDX9vvT/arcgis/rest/services/Coronavirus_romania/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Judete%20asc&resultOffset=0&resultRecordCount=42&cacheHint=true"
    /home/gcbirzan/.virtualenvs/covid19-romania/bin/python /home/gcbirzan/PycharmProjects/covid19-romania/adjust_json.py "$f_name"
    /home/gcbirzan/.virtualenvs/covid19-romania/bin/python /home/gcbirzan/PycharmProjects/covid19-romania/get_changes.py
    gsutil -h "Cache-Control:public,max-age=30" cp -z json  new_fixed.json gs://covid19-romania/data/latest_data_fixed_new_2.json
    gsutil -h "Cache-Control:public,max-age=30" cp -z json latest_log.json gs://covid19-romania/data/
    sleep 300
done
