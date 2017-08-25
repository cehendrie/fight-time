from fighttime.roleplayer import RolePlayer


class TestRolePlayer(object):

    def test_calculate_hitpoints_battlefield_1(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints([ 1, 1, 1, -1, -1, -1 ])
        assert actual == 1

    def test_calculate_hitpoints_battlefield_2(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints([ -1, -1, -1, 1, 1, 1 ])
        assert actual == 4

    def test_calculate_hitpoints_battlefield_3(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints([ -1, -1, 1, 1, -1, 1 ])
        assert actual == 3

    def test_calculate_hitpoints_battlefield_4(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints([ -1, -1, 1, 1, 1, -1 ])
        assert actual == 3

    def test_calculate_hitpoints_battlefield_5(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints([ -1, 1, 1, 1, -1, -1 ])
        assert actual == 2

    def test_calculate_hitpoints_battlefield_6(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints([ -1, 1, 1, -1, -1, 1 ])
        assert actual == 2

    def test_calculate_hitpoints_battlefield_7(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints([ 1, -1, -1, 1, -1, 1 ])
        assert actual == 2

    def test_calculate_hitpoints_battlefield_8(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints([ 10, -1, -1, -1 ])
        assert actual == 1

    def test_calculate_hitpoints_zac_style_1(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_style([ 1, 1, 1, -1, -1, -1 ])
        assert actual == 1

    def test_calculate_hitpoints_zac_style_2(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_style([ -1, -1, -1, 1, 1, 1 ])
        assert actual == 4

    def test_calculate_hitpoints_zac_attack_1(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ 1, 1, 1, -1, -1, -1 ])
        assert actual == 1

    def test_calculate_hitpoints_zac_attack_2(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ -1, -1, -1, 1, 1, 1 ])
        assert actual == 4

    def test_calculate_hitpoints_zac_attack_3(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ -1, -1, 1, 1, -1, 1 ])
        assert actual == 3

    def test_calculate_hitpoints_zac_attack_4(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ -1, -1, 1, 1, 1, -1 ])
        assert actual == 3

    def test_calculate_hitpoints_zac_attack_5(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ -1, -1, -1, 1, 1, 1 ])
        assert actual == 4

    def test_calculate_hitpoints_zac_attack_6(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ -1, -1, -1, 1, 1, 1 ])
        assert actual == 4

    def test_calculate_hitpoints_zac_attack_7(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ -1, -1, -1, 1, 1, 1 ])
        assert actual == 4

    def test_calculate_hitpoints_zac_attack_8(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ -1, -1, -1, 10 ])
        assert actual == 4

    def test_calculate_hitpoints_zac_attack_9(self):
        role_player = RolePlayer()
        actual = role_player.calculate_hitpoints_zac_attack([ 10, -1, -1, -1 ])
        assert actual == 1
