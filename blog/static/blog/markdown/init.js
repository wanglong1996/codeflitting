/**
 * Created by chenpy on 17-1-18.
 */
/*global marked:false, hljs:false, $:false, _:false*/


$(function () {
    // Set up the live Markdown demo instances
    initLiveDemos();
});


// Adapted from markdown-render.js
function mathify(mathcode) {
    return '<img src="https://chart.googleapis.com/chart?cht=tx&chl={urlmathcode}" alt="{mathcode}">'
        .replace(/\{mathcode\}/ig, mathcode)
        .replace(/\{urlmathcode\}/ig, encodeURIComponent(mathcode));
}


// Adapted from markdown-render.js
function highlightSyntax(targetDocument, syntaxHighlighter, codeText, codeLanguage) {
    var codeElem, preElem, textNode;

    // highlight.js requires a `<code>` element to be passed in that has a
    // `<pre>` parent element.

    preElem = targetDocument.createElement('pre');
    codeElem = targetDocument.createElement('code');
    textNode = targetDocument.createTextNode(codeText);
    codeElem.appendChild(textNode);
    preElem.appendChild(codeElem);

    // If we're told the language, set it as a class so that the highlighter
    // doesn't have to guess it. This is part of the HTML5 standard. See:
    // http://www.whatwg.org/specs/web-apps/current-work/multipage/text-level-semantics.html#the-code-element
    if (codeLanguage && codeLanguage.length > 0) {
        codeElem.setAttribute('class', 'language-' + codeLanguage);
    }
    else {
        codeElem.setAttribute('class', 'no-highlight');
    }

    syntaxHighlighter.highlightBlock(codeElem);

    return codeElem.innerHTML;
}


function initLiveDemos() {
    $('.livedemo').each(function () {
        var $container = $(this);
        var $raw = $(this).find('.livedemo-raw');
        var $raw_textarea = $raw.find('textarea');
        var $rendered = $(this).find('.livedemo-rendered');
        var $parent = $(this).parent();

        // Load the text from the associated script/text element
        var livedemo_text = $('script[data-livedemo="' + $parent.attr('id') + '"]').text().trim();
        // If there's no text block, use the default
        if (livedemo_text) {
            $raw_textarea.val(livedemo_text);
        }

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
                    $rendered.get(0).ownerDocument,
                    hljs,
                    codeText,
                    codeLanguage);
            }
        };

        $raw_textarea.keyup(function () {
            var html = marked($raw_textarea.val(), markedOptions);
            $rendered.html(html);

            // Make links in the rendered view open in a new tab.
            $rendered.find('a').attr('target', '_blank');
        });

        // The height of the rendered view is determined by the hight of the raw
        $raw.resize(function () {
            $rendered.outerHeight($raw.outerHeight());
        });

        // Trigger the size match
        $raw.resize();

        // Trigger the first render
        $raw_textarea.keyup();
    });
}

