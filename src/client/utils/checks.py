import discord


def embed_perms(m):
    try:
        check = m.author.permissions_in(m.channel).embed_links
    except:
        check = True

    return check