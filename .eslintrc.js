module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: ["eslint:recommended"],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: "module",
  },
  rules: {
    // Aquí puedes agregar reglas personalizadas
    "no-unused-vars": "warn",
    "no-console": "off", // o 'warn' si quieres advertir sobre console.log
  },
};
