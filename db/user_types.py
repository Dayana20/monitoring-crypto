Investor = 'Investor'
Investor2 = 'Investor2'
Investor3 = 'Investor3'
SampleUser = 'SampleUser'
NAME = 'name'
FOLLOWERS = 'Followers'
FOLLOWING = 'Following'
EMAIL = 'email'
PASSWORD = 'password'
COINS = 'coins'
REQUIRED_FIELDS = [NAME, PASSWORD, EMAIL, FOLLOWERS, FOLLOWING, COINS]
user_types = {Investor: {NAME: 'user1', PASSWORD: '****',
              EMAIL: 'user@gmail.com', FOLLOWERS: [Investor2],
              FOLLOWING: [], COINS: []},
              Investor2: {NAME: 'user2', PASSWORD: '****',
              EMAIL: 'user2@gmail.com', FOLLOWERS: [],
              FOLLOWING: [Investor], COINS: []},
              Investor3: {NAME: 'user3', PASSWORD: '****',
              EMAIL: 'user3@gmail.com', FOLLOWERS: [],
              FOLLOWING: [], COINS: []},
              SampleUser: {NAME: 'sample', PASSWORD: '****',
              EMAIL: 'sampleuser@gmail.com', FOLLOWERS: [],
              FOLLOWING: [], COINS: []}}


def user_exists(name):
    return name in user_types


def get_users():
    return list(user_types.keys())


def get_user(username):
    if username not in user_types:
        raise ValueError(f'User {username=} does not exist')

    return user_types[username]


def get_user_type_details(type):
    return user_types.get(type, None)


def get_user_email(username):
    if username not in user_types:
        raise ValueError(f'User {username=} does not exist')

    return user_types[username][EMAIL]


def add_user(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FIELDS:
        # print(details.keys())
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    user_types[name] = details


def del_user(name):
    if name not in user_types:
        raise TypeError(f'User: {type(name)=} does not exist.')
    del user_types[name]


def follower_exists(userName, followName):
    print(user_types[userName])
    isFollower = userName in user_types[followName][FOLLOWERS]
    isFollowing = followName in user_types[userName][FOLLOWING]
    return (isFollower and isFollowing)


def add_follower(userName, followName):
    if userName == followName:
        raise ValueError("Use two different users")
    if follower_exists(userName, followName):
        raise ValueError("Follower exists")

    user_types[followName][FOLLOWERS].append(userName)
    user_types[userName][FOLLOWING].append(followName)
    return {userName: user_types[userName], followName: user_types[followName]}


def remove_follower(userName, followName):
    if not follower_exists(userName, followName):
        raise ValueError("Follower does not exists")
    user_types[followName][FOLLOWERS].remove(userName)
    user_types[userName][FOLLOWING].remove(followName)
    return {userName: user_types[userName], followName: user_types[followName]}


def update_email(userName, newEmail):
    currentEmail = user_types[userName][EMAIL]

    if currentEmail == newEmail:
        raise ValueError("New email must be different from the previous!")

    user_types[userName][EMAIL] = newEmail
    return {userName: user_types[userName]}


def get_password(userName):
    return user_types[userName][PASSWORD]


def update_password(userName, newPassword):
    currentPassword = user_types[userName][PASSWORD]

    if currentPassword == newPassword:
        raise ValueError("New password must be different from the previous!")

    user_types[userName][PASSWORD] = newPassword
    return {userName: user_types[userName]}


def user_coin_exists(userName, coin):
    return coin in user_types[userName][COINS]


def add_coin(userName, coin):
    if not user_exists(userName):
        raise ValueError("User does not exists")
    if coin in user_types[userName][COINS]:
        raise ValueError("Already Following Coin")
    user_types[userName][COINS].append(coin)
    return {userName: user_types[userName]}


def remove_coin(userName, coin):
    if not user_exists(userName):
        raise ValueError("User does not exists")
    if coin not in user_types[userName][COINS]:
        raise ValueError("Not Following Coin")
    user_types[userName][COINS].remove(coin)
    return {userName: user_types[userName]}


def follower_count(userName, followName):
    print(user_types[userName])
    isFollowers = followName in user_types[userName][FOLLOWERS]
    return (isFollowers.count())


def following_count(userName, followName):
    print(user_types[userName])
    isFollowing = followName in user_types[userName][FOLLOWING]
    return (isFollowing.count())


def user_coin_valuation(userName):
    if not user_exists(userName):
        raise ValueError("User does not exist")

    value = 0
    for coin in user_types[userName][COINS]:
        print(coin)

    return value


def main():
    users = get_users()
    print(f'{users=}')
    print(f'{get_user_type_details(Investor)=}')


if __name__ == '__main__':
    main()
