
from django import template


register = template.Library()

@register.filter
def participe(user, quete):
    liste = quete.participants.all()
    return (user in liste)


@register.filter
def listeParticipants(quete):
    return quete.participants.all()


@register.filter
def username(user):
    profil = user.profil
    if profil.personnagePrincipal == None:
        if profil.prenom == "":
            return user.username
        else:
            return profil.prenom + " " + profil.nom
    else:
        return profil.personnagePrincipal.nom
