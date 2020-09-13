window.onload = getNews;




//homepage part: search button in page
function getNews() {


    document.getElementById("searchPage").style.display = "none";
    document.getElementById("homepage").style.display = "block";

    //load json data:
    function loadJson(url, callBack) {
        let xmlHttpRequest;
        if (window.XMLHttpRequest) {
            xmlHttpRequest = new XMLHttpRequest();
        } else {
            xmlHttpRequest = new ActiveXObject('Microsoft.XMLHTTP');
        }
        xmlHttpRequest.open("GET", url, true);
        xmlHttpRequest.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {

                callBack(this);
            }
        };
        xmlHttpRequest.send();
    }


    //slide show:
    var slideIndex = 0;
    slideDisplay();

    function slideDisplay() {
        let slides = document.getElementsByClassName("singleSlide");
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > slides.length) {
            slideIndex = 1
        }
        slides[slideIndex - 1].style.display = "block";

        let timerId = setTimeout(slideDisplay, 4000); // Change image every 2 seconds
        slides.onmouseover = function () {
            clearTimeout(timerId);
        }
        slides.onmouseout = function () {
            setTimeout(slideDisplay, 4000);
        }

    }




    //allNews callback function:
    loadJson('/allNews', displayNews);
    var topNews;
    var top_articles;

    function displayNews(xmlHttpRequest) {
        topNews = JSON.parse(xmlHttpRequest.responseText);
        top_articles = topNews.articles;
        //console.log(top_articles);

        let aTag = document.querySelectorAll(".aTag");
        let imageTag = document.querySelectorAll(".imageTag");

        let h3_tag = document.querySelectorAll(".h3_tag");
        let p_tag = document.querySelectorAll(".p_tag");


        for (let i = 0; i < top_articles.length; ++i) {
            let img = top_articles[i].urlToImage;
            let title = top_articles[i].title;
            let desc = top_articles[i].description;
            let url = top_articles[i].url;

            aTag[i].href = url;
            imageTag[i].src = img;
            h3_tag[i].innerHTML = title;
            p_tag[i].innerHTML = desc;
        }

    }


    //cnn callback function:
    loadJson('/cnn', displayCnn);
    var cnn;
    var cnn_articles;

    function displayCnn(xmlHttpRequest) {
        cnn = JSON.parse(xmlHttpRequest.responseText);
        cnn_articles = cnn.articles;
        //console.log(cnn_articles);
        //get cnn news image, title and description
        let cnn_container = document.getElementById("cnn_card");
        let cnn_card = cnn_container.querySelectorAll("div#showCard > .card");   //cnn_card type: NodeList
        //console.log(cnn_card);
        for (let i = 0; i < cnn_card.length; ++i) {
            let img = cnn_articles[i].urlToImage;
            let title = cnn_articles[i].title;
            let desc = cnn_articles[i].description;
            let url = cnn_articles[i].url;

            cnn_card[i].children[0].src = img;
            cnn_card[i].children[1].innerHTML = title;
            cnn_card[i].children[2].innerHTML = desc;

            cnn_card[i].onclick = function () {
                window.open(url, "_blank_");
            }
        }
    }

    //fox callback function:
    loadJson('/fox', displayFox);
    var fox;
    var fox_articles;

    function displayFox(xmlHttpRequest) {
        fox = JSON.parse(xmlHttpRequest.responseText);
        fox_articles = fox.articles;

        let fox_container = document.getElementById("fox_card");
        let fox_card = fox_container.querySelectorAll("div#showCard > .card");   //cnn_card type: NodeList

        for (let i = 0; i < fox_card.length; ++i) {
            let img = fox_articles[i].urlToImage;
            let title = fox_articles[i].title;
            let desc = fox_articles[i].description;
            let url = fox_articles[i].url;

            fox_card[i].children[0].src = img;
            fox_card[i].children[1].innerHTML = title;
            fox_card[i].children[2].innerHTML = desc;

            fox_card[i].onclick = function () {
                window.open(url, "_blank_");
            }
        }
    }

    loadJson('/wordcloud', displayCloud);

    function displayCloud(xmlHttpRequest) {
        let wordMap = JSON.parse(xmlHttpRequest.responseText);
        let myWords = [];
        for (let i = 0; i < wordMap.length; ++i) {
            let dict = {};

            dict['word'] = wordMap[i][0];
            dict['size'] = wordMap[i][1];
            myWords[i] = dict;
        }

        var margin = {top: 10, right: 10, bottom: 10, left: 10},
            width = 300 - margin.left - margin.right,
            height = 300 - margin.top - margin.bottom;


        var svg = d3.select("#word_cloud").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

        var layout = d3.layout.cloud()
            .size([width, height])
            .words(myWords.map(function (d) {
                return {text: d.word, size: d.size};
            }))
            .padding(5)        //space between words
            .rotate(function () {
                return ~~(Math.random() * 2) * 90;
            })
            .fontSize(function (d) {
                return d.size;
            })      // font size of words
            .on("end", draw);
        layout.start();

        function draw(words) {
            svg.append("g")
                .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function (d) {
                    return d.size;
                })
                .style("fill", "#69b3a2")
                .attr("text-anchor", "middle")
                .style("font-family", "Impact")
                .attr("transform", function (d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text(function (d) {
                    return d.text;
                });
        }

    }
}


//search form part:

function getSearchForm() {


    document.getElementById("homepage").style.display = "none";
    document.getElementById("searchPage").style.display = "block";

    // document.getElementById("keyword").autofocus = true;
    // document.getElementById("keyword").required = true;
    //set the default date to 'from' and 'to'
    function getDate(day) {
        let dateObj = new Date();
        let untilSetDay = dateObj.getTime() + 1000 * 60 * 60 * 24 * day;
        dateObj.setTime(untilSetDay);
        let today = dateObj.getDate();
        let month = dateObj.getMonth() + 1;
        let year = dateObj.getFullYear();
        if (today < 10) {
            today = '0' + today;
        }
        if (month < 10) {
            month = '0' + month;
        }
        let gottenDate = year + '-' + month + '-' + today;
        return gottenDate;
    }

    document.getElementById('to').value = getDate(0);
    document.getElementById('from').value = getDate(-7);

    let clear_button = document.getElementById("clearButton");
    function clear(){
         document.getElementById('to').value = getDate(0);
         document.getElementById('from').value = getDate(-7);
    }



    //load json data:
    function loadJson(url, callBack) {
        let xmlHttpRequest;
        if (window.XMLHttpRequest) {
            xmlHttpRequest = new XMLHttpRequest();
        } else {
            xmlHttpRequest = new ActiveXObject('Microsoft.XMLHTTP');
        }
        xmlHttpRequest.open("GET", url, true);
        xmlHttpRequest.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                callBack(this);
            }
        }
        xmlHttpRequest.send();
    }






    //deal with the dynamic sources for dropdown box
    loadJson('/source', showSource);

    function showSource(xmlHttpRequest) {
        var sources = JSON.parse(xmlHttpRequest.responseText);
        let category_source = document.getElementById("category_input");
        category_source.onchange = changeCategory;

        //dropdown box:
        function changeCategory() {
            let category_list = document.getElementById("category_input");
            let source_list = document.getElementById("source_input");
            let selectedCategory = category_list.options[category_list.selectedIndex].value;

            while (source_list.options.length > 1) source_list.remove(1);

            let source = sources[selectedCategory];
            if (source) {
                for (let i = 0; i < source.length; ++i) {
                    let singleSource = new Option(source[i]);
                    source_list.options.add(singleSource);
                }
            }
        }
    }

//build url and sent it to backend, and get data from the backend
    let keyword = document.getElementById("keyword");
    let from = document.getElementById("from");
    let to = document.getElementById("to");
    let source_list = document.getElementById("source_input");
    let source = source_list.options[source_list.selectedIndex].text;


    let searchButton = document.getElementById("findButton");
    searchButton.onclick = searchResult;

    function searchResult() {

        let form_Articles;
        loadJson('/SearchResult?keyword=' + keyword + '&from=' + from + '&to=' + to + '&source=' + source, getData);


        function getData(xmlHttpRequest) {
            form_Articles = JSON.parse(xmlHttpRequest.responseText);
            let articles = form_Articles.articles;
            let card = document.getElementsByClassName("initCard");

            for (let i = 0; i < card.length; ++i) {
                let img = articles[i].urlToImage;
                console.log(img);
                let title = articles[i].title;
                let desc = articles[i].description;

                let form_img = document.getElementsByClassName("leftImage");
                form_img[i].src = img;
                let titleTag = document.querySelectorAll(".form_into >h4");
                titleTag[i].innerHTML = title;
                let descTag = document.querySelectorAll(".form_into >p");
                descTag[i].innerHTML = desc;

            }
        }
    }


}




