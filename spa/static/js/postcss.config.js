module.exports = {
  plugins: [
    require("postcss-import"),
    require("autoprefixer"),
    require("@fullhuman/postcss-purgecss")({
      content: ["./spa/templates/**/*.html", "./spa/static/js/**/*.js"],
      defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
    }),
    require("cssnano")({
      preset: "default",
    }),
  ],
};
