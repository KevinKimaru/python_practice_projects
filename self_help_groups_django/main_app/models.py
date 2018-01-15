from django.db import models
from django.shortcuts import get_object_or_404


# ===========================Members
from main_app import calc_interest


class Member(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        main_group_total_count = Main_group_total.objects.all().count()
        if main_group_total_count == 0:
            main_group_total = Main_group_total(current_amount=0)
            main_group_total.save()
        get_main_group_total = get_object_or_404(Main_group_total, pk=1)
        get_main_group_total.current_amount += 1000
        get_main_group_total.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Member: %s" % self.name


# ================================Group days
class Groupday(models.Model):
    date = models.DateField(primary_key=True)
    is_merrygoround_registration = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_merrygoround_registration == True:
            amount = Member.objects.all().count() * 300
            main_group_object = get_object_or_404(Main_group_total, pk=1)
            main_group_object.current_amount += amount
            main_group_object.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Group Day: %s" % self.date


# ================================Unga
class Unga(models.Model):
    date = models.ForeignKey(Groupday, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    has_paid = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        unga_total_count = Unga_total.objects.all().count()
        if unga_total_count == 0:
            unga_total = Unga_total(current_amount=0)
            unga_total.save()

        if self.has_paid == True:
            amount = self.amount
            unga_total_object = get_object_or_404(Unga_total, pk=1)
            unga_total_object.current_amount += amount
            unga_total_object.save()
        else:
            fine = Unga_fines_interests(date=self.date,
                                        name=self.member,
                                        penalty_interest_amount="PENALTY: Delay of Merry go round contribution.",
                                        amount=50)
            fine.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Unga: %s: %s" % (self.date, self.member)


class Unga_loan(models.Model):
    date = models.ForeignKey(Groupday, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        amount = self.amount
        unga_total_object = get_object_or_404(Unga_total, pk=1)
        if unga_total_object.current_amount < amount:
            return
        else:
            unga_total_object.current_amount -= amount
            unga_total_object.save()
            super().save(*args, **kwargs)

    def __str__(self):
        return "Unga Loan: %s: %s" % (self.date, self.member)


class Unga_loan_progress(models.Model):
    loan = models.ForeignKey(Unga_loan, on_delete=models.CASCADE)
    date = models.ForeignKey(Groupday, on_delete=models.CASCADE)
    month = models.CharField(max_length=1, choices=((i, i) for i in range(1, 4)))
    has_paid_interest = models.BooleanField()
    has_paid_all = models.BooleanField(default=False)

    @property
    def amount_paid(self):
        interest = calc_interest.calculate_interest(self.loan.amount)
        if self.has_paid_interest == True:
            interest = Unga_fines_interests(date=self.date,
                                            name=self.loan.name,
                                            penalty_interest_amount="INTEREST",
                                            amount=interest,
                                            has_paid=True)
            interest.save()
            return interest
        elif self.has_paid_all == True:
            amount = interest + self.loan.amount
            total_return = Unga_fines_interests(date=self.date,
                                                name=self.loan.name,
                                                penalty_interest_amount="AMOUNT",
                                                amount=amount,
                                                has_paid=True)
            total_return.save()
            return amount
        elif self.has_paid_interest == False and self.has_paid_all == False:
            penalty = Unga_fines_interests(date=self.date,
                                           name=self.loan.name,
                                           penalty_interest_amount="PENALTY: Delay of interest payment",
                                           amount=100)
            penalty.save()
            return 0

    def __str__(self):
        return "Unga Loan Progress: %s:\n Month:%s: Date: %s " % (self.loan, self.month, self.date)


class Unga_fines_interests(models.Model):
    date = models.ForeignKey(Groupday, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    penalty_interest_amount = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    has_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.has_paid == False:
            return
        else:
            amount = self.amount
            unga_total_object = get_object_or_404(Unga_total, pk=1)
            unga_total_object.current_amount += amount
            unga_total_object.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Unga Fines, Interests and Amounts: %s: %s :%s" % (self.member, self.penalty_interest_amount, self.date)


class Unga_total(models.Model):
    current_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Unga Total: %s" % (self.current_amount)


# ===================================Main Group
class Main_group_merrygoround(models.Model):
    date = models.ForeignKey(Groupday, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    has_paid = models.BooleanField(default=True)
    has_won = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.has_paid == False:
            fine = Main_group_fines_interest(date=self.date,
                                             name=self.member,
                                             penalty_interest_amount="PENALTY: Delay of Merry go round contribution.",
                                             amount=50)
            fine.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Merry go round:%s: %s' % (self.member, self.date)


class Main_group_loan(models.Model):
    date = models.ForeignKey(Groupday, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        amount = self.amount
        main_group_total_object = get_object_or_404(Main_group_total, pk=1)
        if main_group_total_object.current_amount < amount:
            return
        else:
            main_group_total_object.current_amount -= amount
            main_group_total_object.save()
            super().save(*args, **kwargs)

    def __str__(self):
        return "Main group loan: %s: %s" % (self.member, self.date)


class Main_group_loan_proress(models.Model):
    loan = models.ForeignKey(Main_group_loan, on_delete=models.CASCADE)
    date = models.ForeignKey(Groupday, on_delete=models.CASCADE)
    month = models.CharField(max_length=1, choices=((i, i) for i in range(1, 4)))
    has_paid_interest = models.BooleanField()
    has_paid_all = models.BooleanField(default=False)

    @property
    def amount_paid(self):
        interest = calc_interest.calculate_interest(self.loan.amount)
        if self.has_paid_interest == True:
            interest = Main_group_fines_interest(date=self.date,
                                                 name=self.loan.name,
                                                 penalty_interest="INTEREST",
                                                 amount=interest,
                                                 has_paid=True)
            interest.save()
            return interest
        elif self.has_paid_all == True:
            amount = interest + self.loan.amount
            total_return = Main_group_fines_interest(date=self.date,
                                                     name=self.loan.name,
                                                     penalty_interest="AMOUNT",
                                                     amount=amount,
                                                     has_paid=True)
            total_return.save()
            return amount
        elif self.has_paid_interest == False and self.has_paid_all == False:
            penalty = Main_group_fines_interest(date=self.date,
                                                name=self.loan.name,
                                                penalty_interest="PENALTY: Delay of interest payment",
                                                amount=100)
            penalty.save()
            return 0

    def __str__(self):
        return "Main group loan progress: %s:\n %s: %s" % (self.loan, self.month, self.date)


class Main_group_fines_interest(models.Model):
    date = models.ForeignKey(Groupday, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    penalty_interest = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    has_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.has_paid == False:
            return
        else:
            amount = self.amount
            unga_total_object = get_object_or_404(Unga_total, pk=1)
            unga_total_object.current_amount += amount
            unga_total_object.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Main group fines, interests and amounts: %s: %s: %s" % (self.member, self.penalty_interest, self.date)


class Main_group_total(models.Model):
    current_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Main group total amount: %s:" % (self.current_amount)
