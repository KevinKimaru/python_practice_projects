from django.db import models


# =========choices and verbose names
class PersonShirt(models.Model):
    SHIRT_SIZES = (('S', 'Small'),
                   ('M', 'Medium'),
                   ('L', 'Large'),)
    # verbose name ,,however while using foreign keys and other relationships use verbose_name=...afetr model class
    # eg poll = models.ForeignKey( Poll, on_delete=models.CASCADE, verbose_name="the related poll", )
    name = models.CharField("person's name", max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def save(self, *args, **kwargs):
        if self.name == "Kevin Kimaru":
            return
        else:
            super().save(*args, **kwargs)

            # ==========how to work with choices
            # p = Person(name="Kevin", shirt_size="L")
            # p.save
            # p.shirt_size
            # p.get_shirt_size_display()


# ==========many to onr relationship (Foreign Key)
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


# ================================many to many relationships
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    #     =========================how it works


# ringo = Person.objects.create(name="Ringo Starr")
# paul = Person.objects.create(name="Paul McCartney")
# beatles = Group.objects.create(name="The Beatles")
# m1 = Membership(person=ringo, group=beatles, date_joined=date(1962, 8, 16),invite_reason="Needed a new drummer.")
# m1.save()
# beatles.members.all()
# ringo.group_set.all()
# beatles.members.clear()

# The following statements will not work if through is used
# beatles.members.add(john)
# beatles.members.create(name="George Harrison")
# beatles.members.set([john, paul, ringo, george])
#  beatles.members.remove(ringo)

# queries+
# Group.objects.filter(members__name__startswith='Paul')


# Person.objects.filter(group__name='The beatles', membership__date_joined__gt=date(1961, 1, 1))
# ringos_membership = Membership.objects.get(group=beatles, person=ringo)
# ringos_membership.date_joined
# ringos_membership = ringo.membership_set.get(group=beatles)


# ==================one to one reltionship
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True, )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)


# operations=====
# r.place = p2
# r.save()
# p2.restaurant

# p1.restaurant = r
# p1.restaurant



# =============================================
# =============================================
# =============================================abstract base classes
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    # optional
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'


class Base(models.Model):
    m2m = models.ManyToManyField(
        CommonInfo,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss", )

    class Meta:
        abstract = True


# class ChildA(Base):
#     pass


# =============================================multi table inheritance
# works like one to one relationship
class Area(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


# class Hotel(Area):
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ["serves_pizza"]
#         proxy = True
#
#     def do_something(self):
#         pass


