/**
 * Created by chenpy on 17-2-5.
 */
$(function () {
    // Set up the live Markdown demo instances
    Converter();
});

function mathify(mathcode) {
    return '<img src="https://chart.googleapis.com/chart?cht=tx&chl={urlmathcode}" alt="{mathcode}">'
        .replace(/\{mathcode\}/ig, mathcode)
        .replace(/\{urlmathcode\}/ig, encodeURIComponent(mathcode));
}


function highlightSyntax(targetDocument, syntaxHighlighter, codeText, codeLanguage) {
    var codeElem, preElem, textNode;

    preElem = targetDocument.createElement('pre');
    codeElem = targetDocument.createElement('code');
    textNode = targetDocument.createTextNode(codeText);
    codeElem.appendChild(textNode);
    preElem.appendChild(codeElem);

    if (codeLanguage && codeLanguage.length > 0) {
        codeElem.setAttribute('class', 'language-' + codeLanguage);
    }
    else {
        codeElem.setAttribute('class', 'no-highlight');
    }
    syntaxHighlighter.highlightBlock(codeElem);
    return codeElem.innerHTML;
}

function Converter() {

    $('.article_content').each(function () {
        var $article = $(this);
        var markdown = $('script[converter="' + $article.attr('id') + '"]').text().trim();

        var markedOptions = {
            gfm: true,
            pedantic: false,
            sanitize: false,
            tables: true,
            smartLists: true,
            breaks: true,
            langPrefix: 'language-',
            math: mathify,
            highlight: function (codeText, codeLanguage) {
                return highlightSyntax(
                    $article.get(0).ownerDocument,
                    hljs,
                    codeText,
                    codeLanguage);
            }
        };

        var html = marked(markdown, markedOptions);
        $article.html(html)
        $article.find('a').attr('target', '_blank');
        console.log(markdown)
    });
}
