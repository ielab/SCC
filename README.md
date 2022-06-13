# SCC
# SCC — A Test Collection for Search in Chat Conversations
## Paper
This work is currently under review as a resource paper at CIKM 2022.
```
@inproceedings{Sabei2022SCC,
 title={ SCC — A Test Collection for Search in Chat Conversations},
 author={Sabei, Ismail and Mourad, Ahmed and Zuccon, Guido},
 booktitle={},
 year={2022}
}
```
## Overview

SCC is a new test collection for both message and conversation retrieval in chat conversations domain.

The source of the test collection was this work [Software-related Slack Chats with Disentangled Conversations](https://github.com/preethac/Software-related-Slack-Chats-with-Disentangled-Conversations.git)

To generate an Information Retrieval test collection from abov work, the preprocessing task was essential in order to create a complete test collection for the sake of evaluating fairly Information Retrieval systems. The preprocessing we have performed was to extract each message from the XML file as a JSON document with a new generated document\_id for each message by utilising its conversation label and timestamp to guarantee that each message is given a uniqu id. Similarly, we extracted each conversation as a JSON document with a new generated document\_id for each conversation. The content of conversation document is the dialogue of participants. Each message in the dialogue carries the same message id on which we  use later for an evaluation and annotation purpose. From here, we output two JSON files one contains 38956 conversations and the other one contains 437884 messages distributed over these conversations as plotted in the following figure 

![the following Figure](https://user-images.githubusercontent.com/79240808/173351765-0071e998-301a-4705-b73d-de95c1fbe99e.png)





SCC provides a rich resource with  variety of uses: message or conversation  retrieval and query variation. To demonstrate the utility of SCC, we conducted experiments for two types of indexing granularity, message based index and conversation based index as per the following figure, using state-of-the-art neural rankers, reporting the effectiveness and providing the code with the collection. 
 
![indexing granularity](https://user-images.githubusercontent.com/79240808/173352145-e2f60057-bca0-4941-8d14-07c355f31348.png)

## Query Topics

A total of 114 topics were created out of 300 conversations; the rest were discarded because of the low quality of disentanglement.

Looking at the nature of the specific chat corpus, a conversation is usually initiated with a question. The assessors were recommended to avoid relying on the conversation initial question and to generate keyword search queries from the middle of conversations based on their understanding of the context of conversations. However, a conversation initial question more often had the most representative keywords for a search query. After analysis of the natural language questions and queries, this yielded two keyword search query sets derived from: ***Conversation Initial Question (CIS)*** and ***Conversation Context (CC)***


