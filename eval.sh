# nohup sh target/appassembler/bin/IndexCollection -collection TrecCollection -generator JsoupGenerator -threads 16 -input ../disk45 -index lucene-index.robust04.pos+docvectors -storePositions -store Docvectors -storeRawDocs >& log.robust04.pos+docvectors+rawdocs

cd Anserini

# map                   	all	0.2501
# P_30                  	all	0.3123

# nohup target/appassembler/bin/SearchCollection -topicreader Trec -index lucene-index.robust04.pos+docvectors -topics src/main/resources/topics-and-qrels/topics.robust04.301-450.601-700.txt -output run.robust04.bm25.topics.robust04.301-450.601-700.txt -bm25

# eval/trec_eval.9.0.4/trec_eval -m map -m P.30 src/main/resources/topics-and-qrels/qrels.robust2004.txt run.robust04.bm25.topics.robust04.301-450.601-700.txt

for i in {85..100}; do
    echo i=$i

    nohup target/appassembler/bin/SearchCollection -topicreader Trec -index lucene-index.robust04.pos+docvectors -topics ../query-synonyms-sim-$i.txt -output synonym.output.txt -bm25

    eval/trec_eval.9.0.4/trec_eval -m map -m P.30 src/main/resources/topics-and-qrels/qrels.robust2004.txt synonym.output.txt
done
