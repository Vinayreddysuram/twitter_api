import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Authenticate to Twitter using OAuth1
def authenticate_twitter_api():
    auth = tweepy.OAuth1UserHandler(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    return tweepy.API(auth)

# Function to delete a tweet by its ID
def delete_tweet(api, tweet_id):
    try:
        api.destroy_status(tweet_id)  # Use destroy_status to delete the tweet
        print(f"Tweet with ID {tweet_id} deleted successfully!")

    except tweepy.NotFound:
        print(f"Error: No tweet found with ID {tweet_id}. Please verify the Tweet ID.")
    except tweepy.Forbidden:
        print("Error: You do not have permission to delete this tweet.")
    except tweepy.TooManyRequests:
        print("Error: Rate limit exceeded. Please wait and try again later.")
    except tweepy.TweepyException as e:
        print(f"Failed to delete tweet: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to run the deletion process
if __name__ == "__main__":
    api = authenticate_twitter_api()  # Authenticate and create API object
    tweet_id_to_delete = input('Enter the Tweet ID you want to delete: ')  # Prompt for tweet ID
    delete_tweet(api, tweet_id_to_delete)  # Attempt to delete the specified tweet
