const base_url = `https://api.urls3.kreimben.com`;
// const base_url = `http://localhost:8000`;

const get_utc_time = () => {
    let date = new Date();
    const now_utc = Date.UTC(date.getUTCFullYear(), date.getUTCMonth(),
        date.getUTCDate(), date.getUTCHours(),
        date.getUTCMinutes(), date.getUTCSeconds());

    date = new Date(now_utc);
    console.log(`date: ${date.toISOString()}`)
    return date.toISOString();
}

let initial_loaded_time = get_utc_time();
let page_loaded_time;
let page_leave_time;


window.addEventListener('load', function () {
    page_loaded_time = get_utc_time()
})

window.onbeforeunload = () => {
    page_leave_time = get_utc_time()

    make_clean();
    // FIXME below message.
    return 'you are going to out of this page!';
}

const make_clean = () => {
    console.log(`on make_clean function`);
    const body_content = {
        "s3": window.location,
        "js_reqeust_time_UTC": initial_loaded_time,
        "page_loaded_time": page_loaded_time,
        "page_leave_time": page_leave_time,
        "referer_url": document.referrer
    };
    const fetch_init = {
        method: 'post',
        // mode: 'no-cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body_content)
    }
    console.log(`fetch_init: ${JSON.stringify(fetch_init)}`);
    fetch(`${base_url}/collect/`,
        fetch_init
    )
        .then(res => res.json())
        .then(json => {
            console.log(`result json: ${JSON.stringify(json)}`);
        });
};

/// https://skalman.github.io/UglifyJS-online/