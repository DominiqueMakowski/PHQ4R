score_PHQ4 <- function(A1=0, A2=0, D1=0, D2=0, method="basic") {
  df <- data.frame(A1 = A1, A2 = A2, D1 = D1, D2 = D2)
  df <- as.data.frame(sapply(df, tolower))
  if (method == "basic") {
    df <- data.frame(sapply(df, function(x) {
      case_when(
        x == "not at all" ~ 0,
        x == "once or twice" ~ 0.5,
        x == "several days" ~ 1,
        x == "more than half the days" ~ 2,
        TRUE ~ 3
      )
    }))
    df$Anxiety <- df$A1 + df$A2
    df$Depression <- df$D1 + df$D2
  } else {
    df$A1 <- case_when(
      df$A1 == "not at all" ~ 0,
      df$A1 == "once or twice" ~ 0.34,
      df$A1 == "several days" ~ 0.55,
      df$A1 == "more than half the days" ~ 0.71,
      TRUE ~ 1
    )
    df$A2 <- case_when(
      df$A2 == "not at all" ~ 0,
      df$A2 == "once or twice" ~ 0.44,
      df$A2 == "several days" ~ 0.58,
      df$A2 == "more than half the days" ~ 0.71,
      TRUE ~ 1
    )
    df$D1 <- case_when(
      df$D1 == "not at all" ~ 0,
      df$D1 == "once or twice" ~ 0.38,
      df$D1 == "several days" ~ 0.51,
      df$D1 == "more than half the days" ~ 0.62,
      TRUE ~ 1
    )
    df$D2 <- case_when(
      df$D2 == "not at all" ~ 0,
      df$D2 == "once or twice" ~ 0.35,
      df$D2 == "several days" ~ 0.52,
      df$D2 == "more than half the days" ~ 0.66,
      TRUE ~ 1
    )
    df$Anxiety <- (df$A1 + df$A2) / 2
    df$Depression <- (df$D1 + df$D2) / 2
  }
  df
}
