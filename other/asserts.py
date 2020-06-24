import unittest


#heredo de la clase TestCase que pertenece a unittest
#empieza la clase
class TestGeneral(unittest.TestCase):

#empiezan los métodos
    def test_sum(self):
        a = 45 + 20
        b = 65
        #verifica igualdad de dos elementos
        self.assertEqual(a, b)

    def test_sum_two(self):
        a = 25 + 25
        b = 23 + 23
        #verifica que dos elementos NO sean iguales
        self.assertNotEqual(a, b)

    def test_equals_true(self):
        a = 34
        b = 2
        c = a + b
        d = 36
        #verifica que una afirmación sea verdadera
        #si falla, dispara un mensaje
        self.assertTrue(c == d, "C y D deberían ser iguales")

    def test_assert_true_two(self):
        #se puede evaluar la veracidad de algo sin crear variables externas
        self.assertTrue(2 + 3 == 5)

    def test_assert_false(self):
        #se evalua que una afrimación sea falsa
        #si falla, dispara un mensaje
        self.assertFalse(2 + 56 == 45, "Esta afirmación debería ser falsa.")

    def test_greater_than(self):
        a = 56
        b = 8
        #evalua que el primero sea mayor que el segundo
        self.assertGreater(a, b)

    def test_less_than(self):
        a = 78
        b = 96
        #verifica que el primero sea menos que el segundo
        self.assertLess(a, b)

    def test_less_or_equal(self):
        a = 56
        b = 94
        #Verifica que el primero sea menor o igual al segundo
        self.assertLessEqual(a, b)

    def test_assert_lisy(self):
        days = ["Monday", "Tuesday", "Wednesay"]
        days_two = ["Thurday", "Friday", "Saturday"]
        #compara dos listas, este test fallaría
        self.assertListEqual(days, days_two)

    def test_assert_tuple(self):
        a = (1, 2, 3)
        b = (1, 2, 3)
        #compara dos tuplas
        self.assertTupleEqual(a, b)

    def test_assert_dictionary(self):
        a = {"id": 1, "account": 12345, "user": "user1"}
        b = {"id": 1, "account": 12345, "user": "user1"}
        #compara dos diccionarios
        self.assertDictEqual(a, b)

if __name__ == '__main__' :
    unittest.main()