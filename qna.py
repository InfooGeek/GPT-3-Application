import openai

openai.api_key = "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"
 
document_list = ["Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.",
"Amazon is an American multinational technology company based in Seattle, Washington, which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as 'one of the most influential economic and cultural forces in the world', as well as the world's most valuable brand. Jeff Bezos founded Amazon from his garage in Bellevue, Washington on July 5, 1994. It started as an online marketplace for books but expanded to sell electronics, software, video games, apparel, furniture, food, toys, and jewelry. In 2015, Amazon surpassed Walmart as the most valuable retailer in the United States by market capitalization."]
a = 0
while a!=1:
	response = openai.Answer.create(
 	search_model="davinci",
 	model="curie",
 	question=input("enter question : "),
 	documents=document_list,
 	examples_context="In 2017, U.S. life expectancy was 78.6 years.",
 	examples=[["What is human life expectancy in the United States?","78 years."]],
 	max_tokens=100,
 	stop=["\n", "<|endoftext|>"],
	)
 
	print(response)
	a=int(input("value of a : "))
