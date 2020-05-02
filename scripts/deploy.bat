cd frontend
call yarn build
cd ..
gcloud app deploy --quiet app.yaml --project covid19-romania