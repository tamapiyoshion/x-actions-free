import os, sys, tweepy

def get_client():
    return tweepy.Client(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        access_token=os.environ['ACCESS_TOKEN'],
        access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
    )

def pop_first_line(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    return (lines[0].strip(), lines[1:]) if lines else (None, lines)

def write_lines(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        for l in lines: f.write(l + '\n')

def main():
    q = 'data/queue.txt'
    if not os.path.exists(q): print('queue.txt not found'); sys.exit(0)
    text, rest = pop_first_line(q)
    if not text: print('no text to post'); sys.exit(0)

    client = get_client()
    resp = client.create_tweet(text=text)  # v2 endpoint
    tweet_id = resp.data.get('id')
    print('posted:', tweet_id)
    write_lines(q, rest)

if __name__ == '__main__':
    main()
