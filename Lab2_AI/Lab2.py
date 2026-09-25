import random
import time

DEPTH = 6
WIDTH = 2

minimax_nodes = 0
alpha_beta_nodes = 0


def create_tree(depth):
    if depth == 0:
        return random.randint(-10, 10)

    return [create_tree(depth - 1) for _ in range(WIDTH)]


def minimax(node, maximizing):
    global minimax_nodes
    minimax_nodes += 1

    if not isinstance(node, list):
        return node

    values = [minimax(child, not maximizing) for child in node]

    if maximizing:
        return max(values)
    else:
        return min(values)


def alpha_beta(node, alpha, beta, maximizing):
    global alpha_beta_nodes
    alpha_beta_nodes += 1

    if not isinstance(node, list):
        return node

    if maximizing:
        result = -float("inf")

        for child in node:
            result = max(
                result,
                alpha_beta(child, alpha, beta, False)
            )

            alpha = max(alpha, result)

            if alpha >= beta:
                break

        return result

    else:
        result = float("inf")

        for child in node:
            result = min(
                result,
                alpha_beta(child, alpha, beta, True)
            )

            beta = min(beta, result)

            if alpha >= beta:
                break

        return result


tree = create_tree(DEPTH)


start = time.perf_counter()
minimax_result = minimax(tree, True)
minimax_time = time.perf_counter() - start


start = time.perf_counter()
alpha_beta_result = alpha_beta(
    tree,
    -float("inf"),
    float("inf"),
    True
)
alpha_beta_time = time.perf_counter() - start


print("MINIMAX + ALPHA-BETA")

print("\nГлубина дерева:", DEPTH)
print("Ширина дерева:", WIDTH)

print("\nMINIMAX:")
print("Результат:", minimax_result)
print("Проверено узлов:", minimax_nodes)
print("Время:", minimax_time)

print("\nALPHA-BETA:")
print("Результат:", alpha_beta_result)
print("Проверено узлов:", alpha_beta_nodes)
print("Время:", alpha_beta_time)

print("\nСравнение:")
print("Экономия узлов:", minimax_nodes - alpha_beta_nodes)