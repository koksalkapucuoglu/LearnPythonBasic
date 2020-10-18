# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GameGame(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    config = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'game_game'


class GameGamesession(models.Model):
    created_at = models.DateTimeField()
    is_active = models.IntegerField()
    game = models.ForeignKey(GameGame, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)
    session = models.ForeignKey('UserSession', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_gamesession'


class GameGamesessiontransaction(models.Model):
    created_at = models.DateTimeField()
    is_end = models.IntegerField()
    game_session = models.ForeignKey(GameGamesession, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_gamesessiontransaction'


class GameGamesubscriber(models.Model):
    created_at = models.DateTimeField()
    is_active = models.IntegerField()
    game = models.ForeignKey(GameGame, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_gamesubscriber'
        unique_together = (('user', 'game', 'is_active'),)


class GenericEntity(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    type = models.ForeignKey('GenericEntitytype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'generic_entity'


class GenericEntitytype(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generic_entitytype'


class GenericHierarchy(models.Model):
    object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    lft = models.PositiveIntegerField()
    rght = models.PositiveIntegerField()
    tree_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generic_hierarchy'


class StatsTransaction(models.Model):
    value = models.DecimalField(max_digits=18, decimal_places=6)
    created_at = models.DateTimeField()
    game = models.ForeignKey(GameGame, models.DO_NOTHING, blank=True, null=True)
    session = models.ForeignKey('UserSession', models.DO_NOTHING, blank=True, null=True)
    transaction_type = models.ForeignKey('StatsTransactiontype', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats_transaction'


class StatsTransactiontype(models.Model):
    name = models.CharField(max_length=255)
    measurement_unit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats_transactiontype'


class UserSession(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_session'


class UserSessiontransaction(models.Model):
    created_at = models.DateTimeField()
    is_end = models.IntegerField()
    session = models.ForeignKey(UserSession, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_sessiontransaction'


class UserTokens(models.Model):
    token_type = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    expire_at = models.DateTimeField(blank=True, null=True)
    is_expired = models.IntegerField()
    user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)
    token = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tokens'


class UserUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    is_active = models.IntegerField()
    is_staff = models.IntegerField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    age = models.PositiveIntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_user'


class UserUserGroups(models.Model):
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_groups'
        unique_together = (('user', 'group'),)


class UserUserUserPermissions(models.Model):
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_user_permissions'
        unique_together = (('user', 'permission'),)


class UserUseractionlog(models.Model):
    remote_adress = models.CharField(max_length=255)
    server_hostname = models.CharField(max_length=255)
    request_method = models.CharField(max_length=255)
    request_path = models.CharField(max_length=255)
    response_status = models.IntegerField()
    runtime = models.DecimalField(max_digits=18, decimal_places=6)
    user = models.ForeignKey(UserUser, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_useractionlog'


class UserUserusagestats(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    usage_min = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(UserUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_userusagestats'
