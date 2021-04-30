function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.container>.row');
    div.innerHTML = output;
}

let html = '\
{{#movie}}\
    <div class="container">\
              <div class="row">\
                  <div class="col-sm-3 col-md-3">\
                      <div class="card p-0">\
                          <div class="card-image"> <img src="{{ poster }}" alt=""> </div>\
                          <div class="card-content d-flex flex-column align-items-center">\
                              <h4 class="pt-2"><a href="{{ url }}">{{title}}</a>\
                              </h4>\
                              <h5>{{year}}</h5>\
                              <ul class="social-icons d-flex justify-content-center">\
                                  <li style="--i:1"> <span class="fa fa-imdb fa-2x"> </span>: 7.5</li>\
                              </ul>\
                          </div>\
                      </div>\
                  </div>\
              </div>\
{{/movie}}'