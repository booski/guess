(function() {
    function ajax(path, callback) {
        var request = new XMLHttpRequest()
        request.open('GET', path, true)
        
        request.onreadystatechange = function() {
            if(request.readyState === XMLHttpRequest.DONE) {
                var json_response = ''
                try {
                    json_response = JSON.parse(request.responseText)
                } catch(error) {
                    console.log(request.responseText)
                }
                callback(json_response)
            }
        }
        request.send()
    }
    
    function init() {
        var q = document.getElementById('question')
        var a = document.getElementById('answer')
        var o = document.getElementById('overlay')
        var historyArray = []

        function getNext() {
            if(!o.classList.contains('hidden')) {
                o.classList.add('hidden')
            }
            ajax('./app/random', function(json_result) {
                q.dataset.src = json_result.picture
                if (historyArray.length > 50) {
                    historyArray = historyArray.shift()
                }
                if (historyArray.includes(q.dataset.src)) {
                    getNext()
                }
                else {
                    historyArray.push(q.dataset.src)
                    q.src = '/pictures/' + q.dataset.src
                }
            })
        }

        getNext()
        
        q.addEventListener('click', function reveal(e) {
            ajax('./app/solution/' + q.dataset.src, function(json_response) {
                a.textContent = json_response.solution
                if(o.classList.contains('hidden')) {
                    o.classList.remove('hidden')
                }
            })
        })

        o.addEventListener('click', function next(e) {
            getNext()
        })
        
    }
    document.addEventListener('DOMContentLoaded', init)
})()
