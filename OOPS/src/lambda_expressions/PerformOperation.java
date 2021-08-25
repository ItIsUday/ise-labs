package lambda_expressions;

@FunctionalInterface
public interface PerformOperation {
    boolean operate(int operation, int num);
}
