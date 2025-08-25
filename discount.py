def discount(total):
  if total > 500:
    return total - (total * 0.20)
  elif 100 <= total <= 500:
    return total - (total * 0.10)
  else:
    return 0.0