# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    state = models.ForeignKey('States', models.DO_NOTHING)
    district = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class Castors(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    acre = models.CharField(max_length=255)
    hectare = models.CharField(max_length=255)
    castor_produced = models.CharField(max_length=255)
    castor_given_baghiya = models.CharField(max_length=255)
    castor_sold = models.CharField(max_length=225, blank=True, null=True)
    castor_price = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    irrigation = models.ForeignKey('Irrigations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'castors'


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Districts(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.ForeignKey('States', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Fertilizers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    labour_cost = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fertilizers'


class Harbestings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    harbesting_cost = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'harbestings'


class Interculturals(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    machine_cost = models.CharField(max_length=255)
    labour_cost = models.CharField(max_length=255)
    weeding_cost = models.CharField(max_length=255)
    rotavat_cost = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interculturals'


class Irrigations(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    type = models.CharField(max_length=255)
    water_rent = models.CharField(max_length=255)
    number_of_hours = models.CharField(max_length=255)
    labour_cost = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'irrigations'


class Landpreparations(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    machine_cost = models.CharField(max_length=255)
    labour_cost = models.CharField(max_length=255)
    farm_yard_cost = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'landpreparations'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    client_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.PositiveBigIntegerField()
    client_id = models.PositiveBigIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    secret = models.CharField(max_length=100, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class Seeds(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seeds'


class Showingcosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    machine_cost = models.CharField(max_length=255)
    labour_cost = models.CharField(max_length=255)
    number_of_labour = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    manual_cost = models.CharField(max_length=155, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'showingcosts'


class States(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class Threshings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    machine_cost = models.CharField(max_length=255)
    labour_cost = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'threshings'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    farmer_type = models.CharField(max_length=255)
    farmer_code = models.CharField(unique=True, max_length=255)
    gender = models.CharField(max_length=255)
    status = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=55, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    farmer_group = models.CharField(max_length=155, blank=True, null=True)
    role_type = models.CharField(max_length=40, blank=True, null=True)
    role_id = models.BigIntegerField(blank=True, null=True)
    responsible_person = models.CharField(max_length=155, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class WaterExpences(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    plot_type = models.CharField(max_length=155, blank=True, null=True)
    responsible = models.CharField(max_length=155, blank=True, null=True)
    district = models.CharField(max_length=155, blank=True, null=True)
    group_name = models.CharField(max_length=155, blank=True, null=True)
    block = models.CharField(max_length=155, blank=True, null=True)
    village = models.CharField(max_length=155, blank=True, null=True)
    farmer_name = models.CharField(max_length=155, blank=True, null=True)
    farmer_code = models.CharField(max_length=155, blank=True, null=True)
    father_name = models.CharField(max_length=155, blank=True, null=True)
    area_acre = models.CharField(max_length=55, blank=True, null=True)
    category = models.CharField(max_length=155, blank=True, null=True)
    gender = models.CharField(max_length=55, blank=True, null=True)
    landholding = models.CharField(max_length=55, blank=True, null=True)
    number_of_irrigation = models.CharField(max_length=55, blank=True, null=True)
    type_of_irrigation = models.CharField(max_length=155, blank=True, null=True)
    water_meter_irrigation_start = models.CharField(max_length=155, blank=True, null=True)
    water_meter_irrigation_end = models.CharField(max_length=155, blank=True, null=True)
    water_meter_final = models.CharField(max_length=155, blank=True, null=True)
    rainy_days = models.CharField(max_length=155, blank=True, null=True)
    water_source = models.CharField(max_length=155, blank=True, null=True)
    irrigation_hours = models.CharField(max_length=155, blank=True, null=True)
    per_irrigation_cost = models.CharField(max_length=155, blank=True, null=True)
    total_cost_of_irrigation = models.CharField(max_length=155, blank=True, null=True)
    irrigation_in_minute = models.CharField(max_length=155, blank=True, null=True)
    date_of_application = models.CharField(max_length=155, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'water_expences'


class Winowings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    winowing_cost = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'winowings'
