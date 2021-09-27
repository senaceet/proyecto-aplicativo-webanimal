import pytest
from App1.models import Donation
from App1.models import Adopcion

# @pytest.mark.django_db
# def test_pet():
#     pet = Pet.objects.create(
#         name = 'Mini',
#         pet_age = '2',
#         breed = 'Criollo',
#         description = 'Con manchas',
#     )
#     assert pet.name == 'Mini'

# @pytest.mark.django_db
# def test_donation():
#     donation = Donation.objects.create(
#         description = 'Espuma para camas',
#     )
#     assert donation.description == 'Espuma para camas'

@pytest.mark.django_db
def test_adopcion():
    adopcion = Adopcion.objects.create(
        name = 'Mini',
        pet_age = '2',
        breed = 'Criollo',
        user_name = 'Juan',
        nuDocument = '777777777',
    )
    assert adopcion.name == 'Mini'
    












    



