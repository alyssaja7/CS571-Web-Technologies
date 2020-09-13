from flask import Flask, jsonify, request
from newsapi import NewsApiClient

# create flask application object
# __name__ : represents the current module name
application = Flask(__name__)
newsapi = NewsApiClient(api_key='9c6f3609cd6a401fab6306765fbf2b44')  # Init

# 绑定路径：你view function希望跟哪个路径绑定，那么你去更改装饰器route里面的参数
# requesting html page
@application.route('/', methods=["GET"])
def index():
    return application.send_static_file('index.html')


# return all valid news from cnn and fox-news
@application.route('/allNews')
def allNews():
    # allNews = newsapi.get_everything(sources='cnn,fox-news', language='en', page_size=100)
    allNews = newsapi.get_everything(sources='cnn,fox-news', language='en', page_size=100)
    articles = allNews['articles']  # list
    checkedArticle = []

    # filter out articles having null value of the given JSON keys, and copy the valid article to a new list.
    # Jsonify and Return the new valid article list
    for i in range(len(articles)):
        article = articles[i]  # element in list, dictionary type

        # get attribute
        author = article['author']
        description = article['description']
        title = article['title']
        url = article['url']
        urlToImage = article['urlToImage']
        publishedAt = article['publishedAt']
        source = article['source']

        # print(type(url))
        # print(type(author))

        if (author is None) or (description is None) or (title is None) or (url is None) or (urlToImage is None) or (
                publishedAt is None) or (source['name'] is None):
            continue
        else:
            checkedArticle.append(article)
            if len(checkedArticle) == 5: break

    allNews['articles'] = checkedArticle
    return jsonify({'articles': checkedArticle})


# return valid cnn top headlines
@application.route('/cnn', methods=["GET"])
def cnn():
    # cnn_top_articles = newsapi.get_top_headlines(sources='cnn', language='en', page_size=100)
    cnn_top_articles = newsapi.get_top_headlines(sources='cnn', language='en', page_size=100)

    cnn_articles = cnn_top_articles['articles']  # list
    cnn_checkedArticle = []

    # filter out articles having null value of the given JSON keys, and copy the valid article to a new list.
    # Jsonify and Return the new valid article list
    for i in range(len(cnn_articles)):
        cnn_article = cnn_articles[i]  # element in list, dictionary type

        # get attribute
        author = cnn_article['author']
        description = cnn_article['description']
        title = cnn_article['title']
        url = cnn_article['url']
        urlToImage = cnn_article['urlToImage']
        publishedAt = cnn_article['publishedAt']
        source = cnn_article['source']

        # print(type(url))
        # print(type(author))

        if (author is None) or (description is None) or (title is None) or (url is None) or (urlToImage is None) or (
                publishedAt is None) or (source['name'] is None):
            continue
        else:
            cnn_checkedArticle.append(cnn_article)
            if len(cnn_checkedArticle) == 4: break

    cnn_top_articles['articles'] = cnn_checkedArticle
    return jsonify({'articles': cnn_checkedArticle})


# return fox top headlines
@application.route('/fox', methods=["GET"])
def fox():
    # fox_top_articles = newsapi.get_top_headlines(sources='fox-news', language='en', page_size=100)
    fox_top_articles = newsapi.get_top_headlines(sources='fox-news', language='en', page_size=100)

    fox_articles = fox_top_articles['articles']  # list
    fox_checkedArticle = []

    # filter out articles having null value of the given JSON keys, and copy the valid article to a new list.
    # Jsonify and Return the new valid article list
    for i in range(len(fox_articles)):
        fox_article = fox_articles[i]  # element in list, dictionary type

        # get attribute
        author = fox_article['author']
        description = fox_article['description']
        title = fox_article['title']
        url = fox_article['url']
        urlToImage = fox_article['urlToImage']
        publishedAt = fox_article['publishedAt']
        source = fox_article['source']

        # print(type(url))
        # print(type(author))

        if (author is None) or (description is None) or (title is None) or (url is None) or (urlToImage is None) or (
                publishedAt is None) or (source['name'] is None):
            continue
        else:
            fox_checkedArticle.append(fox_article)
            if len(fox_checkedArticle) == 4: break

    fox_top_articles['articles'] = fox_checkedArticle

    return jsonify({'articles': fox_checkedArticle})


@application.route('/source', methods=["GET"])
def topSource():
    dict = {}

    busi_collect = set()
    business = newsapi.get_sources(category='business', language='en', country='us')
    business_list = business['sources']
    for i in range(len(business_list)):
        singleBusiness = business_list[i]
        businessName = singleBusiness['name']
        if businessName is None:
            continue
        else:
            busi_collect.add(businessName)
            if len(busi_collect) == 10: break
    busi = list(busi_collect)
    dict['Business'] = busi

    ent_collect = set()
    entertainment = newsapi.get_sources(category='entertainment', language='en', country='us')
    ent_list = entertainment['sources']
    for i in range(len(ent_list)):
        singleEnt = ent_list[i]
        entName = singleEnt['name']
        if entName is None:
            continue
        else:
            ent_collect.add(entName)
            if len(ent_collect) == 10: break
    ent = list(ent_collect)
    dict['Entertainment'] = ent

    gene_collect = set()
    general = newsapi.get_sources(category='general', language='en', country='us')
    gene_list = general['sources']
    for i in range(len(gene_list)):
        singleGene = gene_list[i]
        geneName = singleGene['name']
        if geneName is None:
            continue
        else:
            gene_collect.add(geneName)
            if len(gene_collect) == 10: break
    gene = list(gene_collect)
    dict['General'] = gene

    health_collect = set()
    health = newsapi.get_sources(category='health', language='en', country='us')
    health_list = health['sources']
    for i in range(len(health_list)):
        singleHealth = health_list[i]
        healthName = singleHealth['name']
        if healthName is None:
            continue
        else:
            health_collect.add(healthName)
            if len(health_collect) == 10: break
    heal = list(health_collect)
    dict['Health'] = heal

    sci_collect = set()
    science = newsapi.get_sources(category='science', language='en', country='us')
    sci_list = science['sources']
    for i in range(len(sci_list)):
        singleScience = sci_list[i]
        sciName = singleScience['name']
        if sciName is None:
            continue
        else:
            sci_collect.add(sciName)
            if len(sci_collect) == 10: break
    sci = list(sci_collect)
    dict['Science'] = sci

    sport_collect = set()
    sport = newsapi.get_sources(category='sports', language='en', country='us')
    sport_list = sport['sources']
    for i in range(len(sport_list)):
        singleSport = sport_list[i]
        sportName = singleSport['name']
        if sportName is None:
            continue
        else:
            sport_collect.add(sportName)
            if len(sport_collect) == 10: break
    sport = list(sport_collect)
    dict['Sport'] = sport

    tech_collect = set()
    technology = newsapi.get_sources(category='technology', language='en', country='us')
    tech_list = technology['sources']
    for i in range(len(tech_list)):
        singleTech = tech_list[i]
        techName = singleTech['name']
        if techName is None:
            continue
        else:
            tech_collect.add(techName)
            if len(tech_collect) == 10: break
    tech = list(tech_collect)

    dict['Technology'] = tech

    return jsonify(dict)


# To get the top 30 words:
#
# 1. Create a map of string vs int
# 2. For each headline
# 3. Split the headline into words (split by space)
# 4. For each word in the split result:
# 5. Increment the frequency by 1, if the word already exists or add the word with frequency 1 if a new word.
# 6. Sort this map
# 7. Return first 30 entries and use these words for the word cloud.

@application.route('/wordcloud', methods=["GET"])
def topWords():
    stopwords = open("static/stopwords_en.txt").read().split()

    top_headlines = newsapi.get_top_headlines(language='en', page_size=100)
    top_articles = top_headlines['articles']

    map = {}
    str = []

    for i in range(len(top_articles)):
        top_article = top_articles[i]
        top_title = top_article['title']
        top_title = top_title.split()

        for word in top_title:
            if word not in str and word not in stopwords:
                str.append(word)
                for j in range(len(str)):
                    map[str[j]] = top_title.count(str[j])

        if i == 500: break

    map = sorted(map.items(), key=lambda x: x[1], reverse=True)

    return jsonify(map)


@application.route('/SearchResult', methods=["GET"])
def serachData():
    keyword = request.args.get('keyword')
    start = request.args.get('start_date')
    end = request.args.get('end_date')
    source = request.args.get('source')


    allArticles = newsapi.get_everything(q=keyword, sources=source, from_param=start, to=end, language='en',
                                         sort_by='publishedAt', page_size=30)
    articles = allArticles['articles']  # list

    form_checkedArticle = []

    # filter out articles having null value of the given JSON keys, and copy the valid article to a new list.
    # Jsonify and Return the new valid article list
    for i in range(len(articles)):
        article = articles[i]  # element in list, dictionary type

        # get attribute
        author = article['author']
        description = article['description']
        title = article['title']
        url = article['url']
        urlToImage = article['urlToImage']
        publishedAt = article['publishedAt']
        source = article['source']

        # print(type(url))
        # print(type(author))

        if (author is None) or (description is None) or (title is None) or (url is None) or (urlToImage is None) or (
                publishedAt is None) or (source['name'] is None):
            continue
        else:
            form_checkedArticle.append(article)
            if len(form_checkedArticle) == 15: break

    allArticles['articles'] = form_checkedArticle
    return jsonify({'articles': form_checkedArticle})




if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    # print(app.url_map);
    # 启动flask程序
    application.run(debug=True)  # 简易测试服务器，最后部署的时候会用别的服务器来对接替换
