import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double num1, num2, result;
        char operator;

        System.out.println("Введите первое число:");
        num1 = scanner.nextDouble();
        System.out.println("Введите оператор (+, -, *, /):");
        operator = scanner.next().charAt(0);
        System.out.println("Введите второе число:");
        num2 = scanner.nextDouble();

        switch (operator) {
            case '+':
                result = num1 + num2;
                System.out.println("Результат: " + result);
                break;
            case '-':
                result = num1 - num2;
                System.out.println("Результат: " + result);
                break;
            case '*':
                result = num1 * num2;
                System.out.println("Результат: " + result);
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                    System.out.println("Результат: " + result);
                } else {
                    System.out.println("Ошибка: деление на ноль!");
                }
                break;
            default:
                System.out.println("Ошибка: некорректный оператор");
        }
    }
}