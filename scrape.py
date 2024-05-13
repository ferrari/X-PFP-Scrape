import requests

headers = {
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "Content-Type": "application/json",
    "Cookie": "guest_id_marketing=v1%3A171561426458690674; guest_id_ads=v1%3A171561426458690674; guest_id=v1%3A171561426458690674; gt=1790042120335810565; att=1-UyCH1cCB2XOaUmGydg9kR6vcNXr9dYgT5YmDkins; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCPpWlHKPAToMY3NyZl9p%250AZCIlMjk1ODU1MGE2MGNhNGE2ZGQwYmMwZTU2M2NjNDE3N2U6B2lkIiU5NTAy%250AYjM2MDU5MzdmZDFjODYzMDFkNGY4MWQwNDM4ZA%253D%253D--f8699a3b8c578ddd39b23a2db0ff88cfdd4ece86; personalization_id=\"v1_vpgX7+/tUmRmqHKxVZY0Zg==\"",
    "Origin": "https://twitter.com",
    "Priority": "u=1, i",
    "Referer": "https://twitter.com/",
    "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "X-Client-Transaction-Id": "c/xvj6Z9w1WIST4ddAtMtBWt1OlnxkAexKxi08XBdJza0dCZj2tUp05Pk/UozzdYFg+jgXKjll92cnBLYzQiREbE1FCacA",
    "X-Guest-Token": "1790042120335810565",
    "X-Twitter-Active-User": "yes",
    "X-Twitter-Client-Language": "en-GB"
}

def scrape_picture(username: str) -> str:
    url = "https://api.twitter.com/graphql/qW5u-DAuXpMEG0zA1F7UGQ/UserByScreenName"
    params = {
        "variables": '{"screen_name":"' + username + '","withSafetyModeUserFields":true}',
        "features": '{"hidden_profile_likes_enabled":true,"hidden_profile_subscriptions_enabled":true,"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"subscriptions_verification_info_is_identity_verified_enabled":true,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"responsive_web_twitter_article_notes_tab_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
        "fieldToggles": '{"withAuxiliaryUserLabels":false}'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        try:
            data = response.json()
            picture_url = data["data"]["user"]["result"]["legacy"]["profile_image_url_https"]
            return picture_url.replace("normal.jpg", "400x400.jpg")
        except Exception as e:
            return None
    return None
    
profile_image_url = scrape_picture("my_profile_name")
