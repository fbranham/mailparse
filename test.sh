cd docker/mailparse/tests/samples
for i in `ls`
do
curl -X POST --data-binary @$i http://127.0.0.1:8080/post
done
