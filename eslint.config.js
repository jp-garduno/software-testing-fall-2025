export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: { console: "readonly" },
    },
    rules: { "no-undef": "error", "no-unused-vars": "error" },
  },
];
