import datetime

from main_app.models import Member, Groupday

peris = Member(name="Peris Wangari")
peris.save()

rose = Member(name="Rose")
rose.save()

#confirm main_group_total

day1 = Groupday(date=datetime.date(2017, 7, 8))
day1.save()

day2 = Groupday(date=datetime.date(2017, 7, 15))
day2.save()

day1.unga_set.create(member=peris, has_paid=True, amount=100)
day1.save()
day2.unga_set.create(member=rose, has_paid=True, amount=250)
day2.save()

# day1 = Groupday.objects.get(date=datetime.date(2017, 7, 8))
# day2 = Groupday.objects.get(date=datetime.date(2017, 7, 15))
# peris = Member.objects.get(name="Peris Wangari")
# rose = Member.objects.get(name="Rose")
day1.unga_set.create(member=rose, has_paid=False)
day2.unga_set.create(member=peris, has_paid=True, amount=400)

day3 = Groupday(date=datetime.date(2017, 7, 22))


