from transformers import pipeline
from scraping import total_content
import warnings
warnings.filterwarnings("ignore")
#summarization goes here
summarizer = pipeline("summarization")


def summarization(singleNews):
    return summarizer(singleNews,max_length=150,min_length=30,do_sample= False)

#summary map stores the news index and news summary corresponding to it
summary_map = {}
for key,value in total_content.items():
    value = "".join(value)
    final = value.replace('"', '"""')   
    summary_map[key] = summarization(final)[0]["summary_text"]
    print(summary_map)

if __name__ == "__main__":
    print(summary_map)
    
