# 521 · Session 01 — cleaned transcript

Teams recording, 26 Jul 2026, 08:20. Instructor: Prof. Bharathi R.

> Noise removed: audio checks, attendance. Instructor content and substantive student questions kept.

### [0:07] **INSTRUCTOR**

Way good morning. Hope I am audible. Let me give you. mic access. Yes. Yeah, good morning. So, um... Okay. Welcome to, yeah, good morning. So I have unmuted. So I have unmuted you all and you can discuss with me and possibly like if you have any other detailed clarifications that we can. I mean, put it in the end of the session. So. So glad you've chosen Conversational AI as one of your endic two, which is the need of the hour. So it's one of the, you know, fastest moving fields in the technology. And you know, the, it's like, you know, it's growing really fast. That means architecture that where the cutting edge in 2022 and 2023. are already considered as a legacy now. So now when we start discussing about the course across all the session, we will discuss all the sort of state of art techniques that is related in the field of Conversational AI. So to begin with, let me share the. Course plan. Yeah, I think the screen is visible for you all. So you can see the course plan. You would have already gone through this course plan. So here, yeah, thank you. So here, like, you know, the course, I mean, the prerequisites, like, you know, it's Python programming, not like just, I mean, You should know comfortable Python coding, not, I mean, a deeper knowledge in the coding is required and machine learning basics and deep learning fundamentals. Of course, these are all your code papers that you have already studied in your previous semesters. And API basics and basic statistics. So these are all the prerequisites which you meet. And the course objectives are, let us discuss when we get into the slides. So I have reframed there in the slides all as well. And you know, with respect to the session plan, we do have 16 sessions. So the pre-mid sem, we have will complete 7 session and 8 session is dedicated for revising the contents from the session 1 to session 8, session 7. So in the pre-mid term, we will discuss about the foundations of Conversational AI. Then in session two, we will discuss about what are all the embedding strategies available and what are all the vector databases and what exactly is a vector search and what are all the retrieval strategies, not only on the dense, we'll discuss about the sparse and the combination of dense and sparse. That's called the hybrid retrieval, and then we will discuss about what are the different models available, like, you know, right from LLMs. Not only we stop with LLMs, we'll discuss about the small language models and mixture of experts and state space models and which model we have to make a choice of. using when we develop a product on any system. And also we will, I mean, we study about LLM and studying about LLM does not stop there. So we have to discuss about what is a function calling. And this is actually a base to get into the AI agents. Okay. So how to connect with the APIs and how to call and what is the React framework. And also we'll discuss about how to fine tune any model, LLM model, that as per our requirement and we can deploy for our project. And then we will discuss about the context engineering. In the context engineering, we'll discuss about what is a long-term memory. So in context sessions, how the memory is handled and also long-term memory across the sessions, how a more an agent can remember across the sessions. So that also we will discuss in detail. Then we have a DE, we have a detailed discussion about rag from building a naive rag.

### [4:46] **INSTRUCTOR**

Yeah, naive rag to the advanced rag until the agentic rag, and not only building the rag, we will discuss about, you know, how to evaluate the rag framework, right, from individual metrics as a system, how to evaluate. So, once the rag is done and once the react framework is done, we will get into the agentic. you know, systems, how to build AI agents. We'll start with a simple AI agent, then we will stretch towards how to build a multi-agents and what are all the existing frameworks available to build a multi-agent system and how to evaluate the agent, AI agents or as well. What are the frameworks available? What are the benchmarks available to evaluate the AI agents? Then, like, we will discuss about the, you know, the production side when we get into the discussion of how to optimise using, you know, optimization strategies.

### [5:46] **INSTRUCTOR**

Yes, that would be a great help if you unmute yourself if you have any, your conversations at your side. And thank you. And cost optimization, like how to handle the tokens, what is the token economics, what are the hidden costs that's happening when we use these, you know, proprietary models, LLM models. And also we will discuss about prompt caching and then model routing, when to strategically use a selection of models to deploy in our projects. Then by ethically, how to AI ethics, how to use ethically all these systems, how to safeguard our documents, proprietary, I mean, IPC, intellectual properties, and how to, you know, avoid the prompt injection, how to make, how to build a defence mechanism, and or red teaming strategies. All these things will be discussed in the security and advisor of business. Then we will discuss about the protocols. What are the standard protocols as and when now this, you know, AI agents, this, I mean, accessing the APIs is growing. So there are many organisations they have come out with, like, how do we have HTTP protocol? Likewise, we do have protocol across these, you know, AI models. Like, we do have a model context protocol called MCP and agent to agent protocol, and also it is agent network protocol, so all these protocols will be discussed. This is how the course is framed, and also we have we do have hands-on on every sessions. OK, and with regarding with you know this evaluation scheme, let me open in the directly in the PPT, so I have added all those. I mean, the evaluation scheme for EC1. So what about the quiz and what about the, you know, the assignments? So those things let us discuss in the slides.

### [7:53] **INSTRUCTOR**

So let me share the slide now. Yeah, hope the slides are visible.

### [8:20] *Komaravolu Ram Kiran*

Yes, ma'am, we can say it.

### [8:21] **INSTRUCTOR**

Yeah, thank you, thank you. So, you know, what exactly is a Conversational AI? Any system that we build, any system that can interact with the human beings in a natural language is said to be a conversational AI system. So to be like, when we read the statement over here, You can see any AI system that engages. that engages humans through natural language to understand the intent and retain context, retrieve the knowledge and deliver information, or to take real world action. It's a Conversational AI. So generally people assume that Conversational AI is a chat bot. It is not a chat bot alone. It is in a simple terms, it is a reasoning system that happens to speak your language. So, what are the core capabilities of, I mean, the Conversational AI? So, these are all, I mean, 6 capabilities are listed over here. The first one is, you know, the natural language understanding, so it is just but the ear of the system, so it interprets not just words, but... intents and entities. You would have come across what is intent and what is entity in NLP. In a simple terms, intent is a verb of a sentence. What is an action? An entity is, you know, like the nouns that is there in the natural language, correct? So that is the natural language understanding by. by doing intent, I mean classification and entity extraction. That's the first component. The second one is a dialogue management, which is the working memory. And you know, it tracks where you are in a conversation. So managing conversation flow and a context. And the third. Core capability is a natural language generation. You know, it's like it generates a fluent, so when you converse with any of the, you know, the proprietary models, like you know, Gemini or ChatGPT or you know, the cloud or you know, Quen model, it generates human-like responses, right? It has a capability of generating a fluent. contextually appropriate replies it can generate, right? And then the third, 4th one is a context awareness. It is nothing but your short-term memory of the system. So you can see that, like how long it can remember the conversation history. So that's one question that depends upon the. The, you know, the window, that number of tokens, right? So, while now, right now, we do have one, 2 million tokens available in several models, right? That's a context awareness, remembering the conversation instead. It depends completely upon the context window. And the 6th, the 5th property, sorry, but.

### [11:24] **INSTRUCTOR**

Yes, the multi-turn interaction. So here, the ability to handle conversations, multi-turn conversations. One turn means, you know, right? One query and one response is called one turn, right? So. Uh, here you know that, uh, uh, in the multi-term, like we do have some significant set of questions. And. And the corresponding answers, right? This is a multi-turn interaction, so it can handle complex dialogues.

### [12:02] *Keerthana B*

Understanding and generating the response, but what really changed is... This part is VEENA. Now, modern chatbots can do the reasoning, and modern chatbots can take the action.

### [12:16] *Arunim Roy*

KRISHNA, I think there is a video running.

### [12:19] *Keerthana B*

Which is a context awareness, which is used to do the reasoning, multi-tour interaction.

### [12:24] **INSTRUCTOR**

Where is this running? No, it's not running here. Somebody, I can just tell you, tell you.

### [12:28] *Arunim Roy*

And could you mute? Yeah, please.

### [12:30] *Anil Kumar Diwedi*

Ma'am, please mute everyone.

### [12:35] *Anil Kumar Diwedi*

If anyone has question, they can raise their hand.

### [12:37] **INSTRUCTOR**

Yes, yes. Yeah, so please raise your hand. So, if you have anything you want to discuss in between, so adapting, you have personalization. This is like actually a thing, but the long-term memory, so the chatbots can remember as right over several instances, right, over a long period of time, so...

### [13:22] **INSTRUCTOR**

This is called a long-term memory adapting to the user preferences. So I can make it like this. This is actually the short-term memory. Within the session. And this is the long-term memory. Across the sessions, it remembers us, right? Due to that, it has the, you know, personalization adapting to user preferences.

### [13:56] **INSTRUCTOR**

Okay, so you know when you look at the 2025 benchmark.

### [14:03] **INSTRUCTOR**

study, it is found that the context awareness alone increased the task completion rates in customer support bots from 54% to 81%. This is 1 statistics. So in short, means the Conversational AI can understand, it can reason, and it can act, right?

### [14:30] **INSTRUCTOR**

So, this is the, you know, examples.

### [14:33] **INSTRUCTOR**

So, already I have muted why I think I muted correct, and yeah, and yeah.

### [14:40] *Tripurana Tirumala Rao*

No, but they are not disabled.

### [14:42] **INSTRUCTOR**

Yeah, yeah, now I think I muted.

### [14:48] *Swarnali Deb*

No, I am still not muted. I can unmute myself.

### [14:55] *Swarnali Deb*

Still, I am able to unmute.

### [14:59] **INSTRUCTOR**

No, I just, I mean, actually, I'm actually doing the mute all.

### [15:00] *Anil Kumar Diwedi*

Thanks. But disable the mute, then only then only it will work, huh?

### [15:07] *Arunim Roy*

Yeah, not disable the mute, disable the mics. Disable the mics, there should be an option there.

### [15:13] **INSTRUCTOR**

No, that's what I did now.

### [15:17] *Arunim Roy*

we are able to speak, which means that the mics are not disabled.

### [15:21] **INSTRUCTOR**

Yeah, wait, wait one second. Yeah. Yeah. Yeah, it's done. So, you know, this is, you know, very something interesting. Like, we are not, we are already using the Conversational AI systems, you know, in our daily life. Like, we call Alexa, right? A wake up word, wake word detection, right? Hey, Siri. Okay, hey, Google, right? A Siri. Also, all these are wake up detections when we do this wake, I mean, wake word using this word called Alexa. So, and it has an automatic speech organisation; it detects our speech and it will understand NLU (natural language understanding) happens, it can take action, and you have text to speech, so this is... Speech recognization, automatic speech recognization is in the input, and it has text to. Speech, so we get to reply back from Alexa, Siri, and even when you look at the customer support, for example, a banking robot that is and a bot in banking chat bots or in under medical or healthcare hospitals. So it can handle tier one queries, right, 24 by 7, and escalate only complex cases to humans. And we do have healthcare assistants, right? Virtual assistants and HR assistants. Ask symptom questions in healthcare, and it will recommend the care pathway is a live critical conversation AI application. It's already in the system now. Currently, we are using you. So, here, this is the rise of Conversational AI in the, you know, market trends and industry, and this is all the statistics taken. So, what will be the condition in 2030? And you know, ChatGPT users, I mean, let's keep adding, I mean, 100 million. So, the fastest growing app in the industry, that's what the Wikipedia data says, and you know, the 80%... for the, you know, Fortune 500 using this 80 AI agents. So, for example, you know, if I take this, the first one, the industry applications, if a bank handles, okay, suppose, for example, if it handles, File that. A random number, I'm just taking support calls per month. In a bank, okay? Hyd. Uh, you know, um... One dollar per call. because of the human agent. So that is approximately what, how many, I mean, there is support causes file access, it is $5,000, right? This will happen. At 70% AI handling, with, for example, it could be $0.05 per conversation. Conversational of AI cost. So imagine what will be the cost reduction if suppose for a human employing human agent it is $1 per call and you know it is $0.05 per if I use an AI agent. So how much is the cost reduction? So that is why that's the impact across industries and All domains, right? Healthcare, enterprise software, e-commerce, and so on, and these are all the statistics collected. You can go through later. And this is the evolution journey. It started very interestingly at this is all the the chat bots. OK, journey in 1960s. So over a period of almost 60 years, you can see the evolution journey. So this is in NLP you would have studied that is Elisa. It's a very rule based chat bot and it moved to statistical building. through ML models like SPMs, conditional random field, and hidden Markov models. Then in 2010 and 2017, it moves to deep learning error. So one, it's moved to deep learning error, the biggest advantage is no feature extraction. So no need of, I mean, what to call. handheld features, generating a feature input data, I mean, data, input data for training the model is completely remote. When we move to a deep learning era, then it moved to a very interesting and, you know, ice-breaking strategy that's called the transformers in 2017 and 2020. And then the 22-23 we have the LLMs, the generative AI, all these models came into existence. Then currently we are in a year into KI era and along with on device and multi-modal. inputs it can accept and it can generate multimodal data. That is, it can accept, you know, videos, it can accept audios, it can generate videos, it can generate audios. And on-device also, I mean, production is also happening because of the small language models. Okay. And many models are come with native multimodality. Okay. So, even in drag, also, we have called Cole Pali is one of the model RAG framework, so which can accept multi-modal data. So we have a native multi-modality. It's coming up now. So we can see that there are three simultaneous breakthroughs made LLM possible. One of the biggest breakthrough is this transformers. And the second breakthrough is the LLMs and the third breakthrough is the SLMs. And we are going to get into, you know, in detail of right from the rule-based systems. So this is actually a first conventional invention. This is developed at MIT. So this Eliza is a simulated psychotherapist. Okay, it was entirely, it is there in the YouTube also. It's very interesting to watch that, how Eliza interacts with the patients. So it was entirely a pattern matching. So it does not have any, no understanding. Okay, no learning and no word knowledge, nothing. Okay, so if user input contains mother, the bot will respond to tell more about your family. That's how the pattern are matched, and if the user input contains bad, the response will be, "Why do you feel sad?" Okay, and this... particular Eliza is approximately 200 lines of code. When you compare with the current, you know, GPTs, which have, you know, approximately 3 to 4 million lines of code. Then, this machine learning error, right? The machine learning error, the biggest, I mean, of course, a lot of advantages when you compare with the rule base, but here, generating. Labels. So we want to generate data set always, right? Extract the features, X1 to XN, and develop the Y. So this is the biggest headache when we deal with the machine learning models. So you have to build many classifiers, one for intent classification, and you have to build, I mean, a tool for named entity organisation, NER. using conditional random field or HMM and so on. So to build a chatbot using machine learning model, we have to go for multiple models, not one single ML model, go for a multiple models. So the limitations are this feature engineering, building this training data, okay, and limited context understanding. So, example frameworks are Microsoft at Louise and IBM Watson; these are all the early versions. So if you want to train an SVM, okay, on a 10 class, suppose very limited, suppose if I want to build a classifier for intent classification, for example, if I can build a small model that can classify, for example, 10 intents. So to develop a classifier that can have a multi classification of 10 intents, at least I should have a data set of 1 to 1000 rows instances, right? Labelled examples per class. So also for one class, so for 10 classes I should have into 10, so I should create 10,000 labelled the data sets. So this is one of the overhead of the machine learning model. So a data scientist has to handcraft these features, like bag of words, TF-IDF scores, character ingrams, and so on. But now when you use a modern, fine-tuned bot, Okay, so you can fine-tune any apple-trained model with only with limited to some 200 to 500 examples. OK, per class and 200 is also per class, 200 is also quite good, and it is if you go for a bot, it is 0 feature engineering because the deep learning model. And accuracy also improves A lot. It achieves BERT model. When you build a model, it can be 95% accuracy can be achieved when you compare with the machine learning models. And there comes a deep learning model that is the, you know, no need of. Featured Engineering. So, we could talk about features to representations. So, deep learning eliminated feature engineering by learning the hierarchical representations directly from the raw text. So here you can see the key architectures. That is the first one is RN and LSTM. This is for sequence to sequence modelling. So it will do word by word, token by token it was doing. Then it moves to encoder decoder model for response generation. And then the third model is the attention mechanism. It focus on relevant parts of the input. OK, so when you talk about this encoder-decoder model, we always have an encoder, and the encoder will produce a context vector, and that will be given to a decoder, right? So, this was one of the this context vector was very difficult to remember what and what what kind of inputs we are given in the encoder to get a relevant output. So, that was so difficult, that's why attention mechanism, you know, emerged. So attention is like being allowed to flip back to any page while translating. So example frameworks are Rasa open source. Of course, Rasa has now, it has tremendously evolved. Now it is into AI agents and so on. And Google Dialogflow. These are all built using this deep learning architectures. But the limitations are it is data-hangry, task-specific models, and limited transfer learning. Then the, you know, the transformer era came in 2017. And always when you talk about transformer era, we can't miss this paper called attention is all you need. OK, so rather in the previous models like RNN, LSTM, sequence to sequence model attention mechanism, We were processing the information sequentially, like humans read, right? But attention processes all the relationship simultaneously. That is what this attention. So, moving from... Sequential. To attention models. So, this will do it process simultaneously. OK, and this is, and it has many pre-trained model exists like a Bird, GPT2, T5, like Google and Roberta, and some few examples are listed here. And the second, I mean, thing is the transfer learning. This actually, you know, when you use a transfer learning, you can A pre-trained on a massive data, and you can fine-tune for a task. For example, if you take a BERT model, let me take a BERT model. It's already... a pre-trained on the book corpus and Wikipedia. Okay, so pre-trained on, let me write here. On Wikipedia and Book Pop Corpus. So, when you do a fine tuning on the bird. On task specific. specific. For example, I want to convert this bird as a sentiment classifier. Classifier, so this fine tuning can be done with a few examples, some for example, some 100 to 200 examples is sufficient. OK, and this BERT model will be completely fine-tuned on this. sentiment classifications. Okay, so that is a very big advantage. It's actually, you can see a killer application, this transfer learning is. So you can train, fine tune any pre-trained model according to your requirement. And top of it, this has contextual embedding. So you would have learned, right? What is a static embody and what is a contextual embody? Right, static embedding means once you suppose if I say the word bank, the popular example, it always gives a fixed vector. So this vector will never change. The value of this vector never change. Generated by, you know, what to work or a glow, any model, okay, or a cbab, any architecture, by using any architecture, you generate a static embedding. And though this vector, for example, this vector can be of any 1024, for example, let that dimension is 1024, can be of any length, it never changes. But the transformer era has brought this contextual embody; that means the word meaning changes when the context also changes. OK, so, for example, looking at the sentence that whether... Bank account. Or I sat. In the riverbank. So depending upon the context. B. the embedding, the vector values also changes. So that was a biggest, I mean, breakthrough when this attention model came. So that is, we use a pre-trained model and we can use transfer learning, deploy transfer learning, and of course, the embedding is a contextual embedding. Word meaning depends on the context. So this is actually a groundbreaking, you know, technology that completely changed, you know, the behaviour of these machine learning models. So, once this transformer era came, then we have a better Conversational AI, like better intent classification with fewer examples. improved entity organisation. So without doing this intent and classification entity, we can't build any conversational system, Conversational AI system, and it can give a very good response, a human-like response it can generate. And now the error that is large language model error, exactly from 2020 to 2023, if you say. So the very huge models right from, it started from GPT-1. In 2018, and you know the size of the model is almost 100 and I think 110 plus parameters size. parameters. So when you take about GPT-2, it is I think 150 parameters, I guess, billion. Sorry, I missed the word billion. It's not 150, 150 billion parameters. That's a size. So when you take GPT-3, it is 175 billion parameters. And GPT-4, I think, 1.9 something. And these are all the, you know, the... As and when the parameter increases, OK, the learning capability of the model also got increased. So it's a massive scale, billions to trillions of parameters at the size of the model we say. So what exactly is the size of the model? How do we say, when I say the model is of, you know, 4 billion parameters, that means what? What exactly is this 4 billion parameters? A model size. Is equal to 4 billion environment.

### [34:15] *Rajesh. R. Shenoi*

The the weights, the weights in the model that converts.

### [34:17] **INSTRUCTOR**

The weights, exactly, fantastic. The weights, the weights and biases of the model. So number of weights and biases of the model is called the parameters, right? So this 4 billion parameters, it's called as a small language models. It's a language model, of course, it's a small language models. So now the small language models are the, you know, The models of the agentic era, so you can when you want to build a multi-agent. Right, and also it has got a huge chart learning, right? So, the, it's actually a game changer, right? So, here you can make the model to understand. By giving examples, suppose I will say that you know I can give an example, so I want a result like this, so 3 + 3 is equal to six. I will ask giving this as an example to the prompt, OK? I will ask, what is a 5 + 2? That means I'm asking the model, I want, this is my query and I want the answer like this. So this is a kind of a prompt, right? So here you are making the model to learn. Prompting is a technique that you are making the model to learn without gradient updates. and no weight changes. That's a prompting. So this is called in-context learning, actually. So, prompting is a biggest boom, wherein you can make the model to learn. I will write it here: model to learn. Use it with no gradient updates. Right? So then there's a general purpose. So many models are built for a general purpose only. And when you fine-tune the model further, you can use for a use a model for a specific purpose. And of course, it can generate responses in a human-like fluency. That's one another big advantage. Of these, you know, large language models. Then the revolution for conversation AI is no fine tuning needed for a general task. And it can understand complex and it can hold the multi-turn conversations and it's a generative, creative and contextual response it can take. But not only that we always look at the capabilities, we have to look at the limitations. That is. No real-time data. Knowledge cutoff. What is I think I have visible? What is that? It's not visible.

### [37:13] *Arunim Roy*

It is, it is me. There may be some network issue on her end.

### [37:47] *Rajesh. R. Shenoi*

And it was visible, actually.

### [37:51] *Tripurana Tirumala Rao*

Yeah, you can share them.

### [37:56] **INSTRUCTOR**

Yes, yeah, because few of them have texted that it's not visible. OK.

### [38:07] *C R Bhargavi*

It is visible, ma'am. Please go ahead.

### [38:08] **INSTRUCTOR**

Thank you, thank you so much. Thank you. So no real-time data is the knowledge cutoff. So generally, you know, the bottle will be trained, they say trained till. Knowledge cutoff, I should write. That means what model? Trained till you can see that in the any proprietary any models free more open source models are in the proprietary models you can say they'll mention that model trained until October 2024, so the model will have knowledge till what has happened till 2024 only, so that is a biggest, I mean the the. limitation of the large language models, the GPTs. That's why the agentic things have come into picture that is extending, connecting these models with the tools to fetch the real-time data. So, and also it can hallucinate. Okay, so you know hallucination is a You know, the biggest one of the characteristics of models, it will, I mean, give the wrong answer confidently. Any, I mean, these LLMs, I mean, GPTs, if you communicate, it will give the wrong answer very confidently. Right, so that is why the RAO architecture came. Right? So they generate most likely the next token. This is all generative models, right? They generate tokens, right? And the water, given all the previous token, it generates the next token. So based on the probability mission also. So it generates the most likely next token. Not most accurate one, right? So, it's give a plausible token, so plausible and true or not same grid. is not equal to true. And also, it cannot take actions. A base LLM can discuss booking a flight, but cannot actually book one. So this is a core motivation for agentic architectural limitations. So whenever we study about the characteristics of a model or the benefits of the model, uses of models, We have to look on what are all the limitations of a particular model. And that comes because to overcome these limitations, knowledge cut off, it cannot take actions, it has hallucinations. This agentic era came. So agentic architecture, you know, is Of. Uh, is an LLM. Model given access. To get tools, and it has memory. And it can plan. That. Right, so this is an agent, so we give tools, we give memory, and it can plug. This is the agent, so this is a basic component of an any AI agent. three fundamental components very much required to build an agent. So it can call APIs, it can search databases, it can execute code, it can take multiple multi-step reasoning. So break down the complex task. Memory systems, remember user preferences, conversation history, so it has a long-term memory by default, must have. That is long-term memory means always an external memory, then autonomous actions. It can book appointments, it can send emails, it can create documents, and so on. So this is the difference between... An LLM and an agent and LLM wrapped with some with the I mean or supported with these other components tools and memory is it will become an agent. And now the evolution here is multi-agent and resetting systems. So beyond agents, we do have, you know, I mean, the orchestration and deep reasoning. So given a complex task, there will be an orchestrator. This itself an LLM, and given the user query, this orchestrator LLM, like a manager LLM, will decide, will decompose the complex task into subtask, and it will decide. How many agents will be required and how to delegate the task subtask one to this agent, subtask to this agent, subagent one? Subagent 2, subagent 3, and subagent N. So, this is a multi-agent, and there are many, very standard frameworks available, like, you know, the Crew AI is one of the free source, open source, and Auto Journal is another open source, right? And the Lang. Land Graph, Land Chain, these are all the frameworks that can be used to, because there are all the abstractions available, so we can deploy these multi-agents not to build from the scratch, and we can build this particular multi-agent system very easily. So then agents spawn and supervise sub-agents for parallel task execution. And models reason step by step before responding. And it has a long context window. There are specialised models available called coding agents, size models, domain specific, and so on. So now AI moves from assistant to autonomous collaborator, working alongside humans on complex multi-day projects. So you would be experiencing how You know, the cloud core, cloud core work, and so on, right? So this is the architecture evolution then and now. So we were pre-2020, it was a traditional architecture. What are the traditional architecture is? So these traditional architectures are pipelined, pipelines are specialised components. So you can have a user input, you will have an ASR. that is speech organisation and you have an NLU. I'll write here user input, it goes to ASR, it goes to NLU, NLU will understand the intent and entity. step by step. And you need a classifier also to do, to have an intent classification and entity extraction. Then it goes to dialogue manager, then it goes to state tracking, then natural language generation and go on. So you need multiple ML models there required to build and traditional architecture. like you have Rasa, Dialogflow, Microsoft Bot Framework, Amazon X, and so on. But when you move on to this, you know, modern agentic architecture, the training of multiple models and maintaining the multiple models are completely removed. No need of an intent, maintaining an intent taxonomy. redefined intent taxonomy and that too. And it is for these models cannot recognise new intents, it cannot understand new intents, okay, post-launch. But here after the modern Majantic architecture, a single LLM handles. And value, because that was a key features, right? A single. LLM here you need multiple ML models. To do intent classification one model, to do entity organisation one model, isn't it? We need speech organisation one model, so multiple models were required to build a traditional was were required when traditional architecture was used, but here in single LLM can handle this NLU. It can do the dialogue management, it can do the generation, okay, and it can have an open-ended intent reorganisation. Intent understanding, not organisation to understanding, and a fluent contextual generation. All the words are listed over here, you can read it. So this is all possible with modern agile architecture. So this is one of the on the use case, you can see the how for a banking customer support chat bot, how this role based, how this intent based, how the LLM based on how agentic AI can handle this banking customer support. Okay, so so LLM knows what to do, right? And agentic system actually do. It knows. It does. That's a difference. between LLM and Agent with AI. So already we know what are the difficulties for intent-based, right? We need multiple models for classification, extraction model, dialogue flow, we need to have our own model and so on. Here it is a frequently matching questions, FAQ questions, right? So this is the evolution of for any kind of application when you, I mean, go around the traditional models and to the recent models. So here you can see that I use a, I lost my card at City Mall, but I have immediately blocked a card ending one, two, three, 4. I see transactions at City Mall. Last one was somewhere around some shop. Should I order a replacement card to your home address? So it's a proactive and action-oriented. But in LLM it says, like, let me help you to block. It will tell you what are the steps to block the cloud, right? Natural, but no action. So, this already be discussed, so let me that I mean the competence of modern Conversational AI in the beginning itself, so let me move on.

### [48:35] *Tripurana Tirumala Rao*

From what is turn-taking and dialogue management?

### [48:40] **INSTRUCTOR**

Yeah, turn taking here is see one turn means suppose in a ChatGPT user query. For one user query, you'll get one response, correct? any chatbot. So this is called one query and one response is called one turn.

### [49:08] **INSTRUCTOR**

So when you converse with any chat bots or any these any of the models, recent model also, you go for multi-turn, right? Multi-turn conversation. Like, we ask what questions, right? Next query, that the bot will respond, third query, third response, and goes on, right, multi-turn. It's called turn-thinking. Generally in these bots, one turn means one for one, one query and one response. Pair is called one turn. Yeah, is it clear?

### [49:51] *Tripurana Tirumala Rao*

Okay. So, when we have agent key, can and when there are many agents, can we say it is a multi-turn taking system?

### [50:01] **INSTRUCTOR**

Mm. Ohh. No, no, I this, I'm not talking about multi-agent.

### [50:10] *Tripurana Tirumala Rao*

Okay, no, no, I'm just asking.

### [50:11] **INSTRUCTOR**

See, no, no, see, in this any conversation, we ask one query, it will respond, right? The bot will respond, correct?

### [50:25] **INSTRUCTOR**

So that is called a multi turns. You take multiple turns, correct? Multi turns. To complete your task, correct? It can take right, you know, when one context in one instance, or suppose if you are opening your cloud, OK, cloud bot, and you start conversing with the bot, it takes you go for a conversation for multi turns, right? You ask several queries on every query, you get response, correct?

### [51:00] **INSTRUCTOR**

And the knowledge access, this is an, I mean, the long-term memory, long-term memory, this is. So because once you open any bot and you register USLs, so it will remembers you over multiple instances, right? How it will remembers you? What are all the actions? Suppose you always ask the cloud code to do some, you know, Java programming. So it will remember your persona. So next time when you ask some statement to do the coding, it will not ask which language you want. It automatically remembers that you always prefers Java. It gives you a Java code. Either you insisted I want a Python coding, otherwise it will give you the pattern of your style of code. coding your persona and it will give you what and all it is there registered in the memory that only it will give. Now, all the, you know, these models, right? That is because of the long-term memory. So the long-term memory, actually, we do have three kinds of memory. One is episodic memory. Now, in the current, I know all these models have episodic memory, it has semantic memory, it has procedural memory. So, of course, we will learn in detail the post mid sem. So, how where this memory about our persona will be stored? Suppose if I log in to my cloud account or log in to my Gemini account, it remembers me, right? So, who I am, what are all my habitual things, what I do? All these things that you will remember on my right because of these three different memory strategies. So how my details are stored, it's stored in an external database that is using vector databases. And it does using semantic search and it also has a rag also. These are all the knowledge access that is happening. And how it will do some actions it has, it is given hands, hands given to LLM. It can access the real world and has got now we give a quick hands on what does an LLM. And what is a real the chat bot? OK, and what is an agent? OK, these three differences, let us see through a small hands-on, OK, and a few lines of code. So, we can do the natural response, generate a natural response responses like a human-like responses, and it has a memory system, right? As it told you, short-term, long-term, episodic, semantic, procedure, and all these memories it has. And traditional frameworks are, you know, it's a Rasa, Google Dialogflow, Microsoft Bramework, Amazon Lex, but of course now they all have been have adopted, yes.

### [54:00] *Kalpana Fatawat*

Ma'am, what is multimodal output previous slide?

### [54:04] **INSTRUCTOR**

Multi, yeah, multi-modal means. There it is, yeah. Generally, multi-modality. Modality means not only text, it can give a image. You can give audio. It can be a video. This is called multimodality.

### [54:33] **INSTRUCTOR**

Now it gives, right? Isn't it? It can take text as input, it can take images and input, correct?

### [54:44] **INSTRUCTOR**

That's a recent advancement, okay?

### [54:47] **INSTRUCTOR**

And also we have a native models having this native capability. Built-in models are there. I mean, the model that's being trained to accept the images, trained to accept the audios, trained to accept the videos, it can generate any things, right? That's A multi-modal output. This is all the components of modern Conversational AI. So we have moved from intent-based dialogue systems to LLM-powered agentic systems with tool use and planning capabilities. So now let us, I mean, after a few slides, let me go to one simple hands-on. to understand what exactly and how all these things work in a very basic format, let us understand that. Okay. So the key, I mean, the limitations of this traditional frameworks that I want to repeat again, we have to build these models, multiple models separately. Okay. But because of this agentic framework, you know. by evolution. So we can, I mean, a single model can do all the tasks simultaneously. So these are all the very famous frameworks now, LangChain, LAXMI Index, Semantic Kernel, HasteTag, Autogen, of course, I add crew AI also. So, this is the, you know, state of art in 2026. So, you can see the context window, the number of tokens the model can take in one session is 10 million plus. This is a LAXMI 4 scout model context window tokens. OK, and you can see that Gemini 3 point. one pro has a benchmark of accuracy of 94.3% on the data set called GPQA Diamond Data Set. And this is the questions that this model can answer is a PhD level questions actually, where the human PhD students, that is the domain specific students, with a top score was 65%, whereas the Gemini 3.1 score was 94.3% and 5 plus modalities. Not only on the model can, any model can accept, understand code, it can understand image, it can not only understand, it generates as well, right? It can understand audio and generates audio, it can understand video. generates video, of course, understand code and it can generate code also. So 5 plus modalities are available and you have native, all the, most all the systems now be, I mean, you look at ChatGPT or look at any, you know, Gemini or Cloud, it has a native, this are all agentic workforce is now native. And it's a browser-based agent browsers are available, and it is all having multi-agent and it has it has adapted multi I mean model context protocols, and these are all you know the model, the providers, the model names and the providers, and you know the the... the context window size from 5.4 and you know, the cloud, I mean the cloud now we have 2 million tokens also, right? And what are all the strengths of these models? So whenever you look at a model, you have to look into which model is good for what. Of course, these are all the proprietary models, generally very good general reasoning models. In specific, when you want to deploy any model, look at how good it is on which a data set it has been trained, what is a pre-trained data set for any particular model, and what are all the, I mean, the use cases are good for Which use cases it is so that you know every model will have now is having a model card, like how do we had our, you know? a personal card, business card, model is also coming with the model card. It will tell to which data it has been trained, what are the strengths, what are the limitations and what is best for this is available. This is now it is becoming getting standardised. So before choosing any model, we have to look this model card and we have to get used for our purpose.

### [59:20] *Kalpana Fatawat*

Choosing the model depends on the vocabulary size of whatever dataset we are preferring.

### [59:31] *Kalpana Fatawat*

or or model training. Is it so?

### [59:34] **INSTRUCTOR**

No, no, no. How there are many things, right? Are you going to build, I mean, fine-tune your own model? That is the one question first, or... Already there are fine-tuned, pre-trained and fine-tuned models are there in the market. Are you directly going to use that model and deploy, build agents, build, I mean, any system for your purpose? OK, that's a third thing. Or are you going to build, are you going to, because every time you can't go for LLMs, right? LLMs are huge. You need a lot of computer power resource you is required, and also when you go for property models, you have to pay for tokens. API costing is there. So now like you can use those these models, but when you want to deploy the model, what is the amount of token consumption it happens? So there are many strategies you have to look into. So first thing is what is your, you know, the requirements, what you are going to do. What's the first question? It's fine. It's fine. Fine, fine.
