score_PHQ4 <- function(A1, A2, D1, D2, method="basic") {

  # Rescore ----
  int_to_char <- function(x) {
    x <- as.character(x)
    x[x=="0"] <- "Not at all"
    x[x=="1"] <- "Once or twice"
    x[x=="2"] <- "Several days"
    x[x=="3"] <- "More than half the days"
    x[x=="4"] <- "Nearly every day"
    x[x=="NA"] <- NA
    x
  }
  if(is.numeric(A1)) A1 <- int_to_char(A1)
  if(is.numeric(A2)) A2 <- int_to_char(A2)
  if(is.numeric(D1)) D1 <- int_to_char(D1)
  if(is.numeric(D2)) D2 <- int_to_char(D2)

  df <- data.frame(A1 = A1, A2 = A2, D1 = D1, D2 = D2)
  df <- as.data.frame(sapply(df, tolower, simplify=FALSE))

  # Sanity check
  for(i in names(df)) {
    if(!all(df[[i]] %in% c("not at all",
                    "once or twice",
                    "several days",
                    "more than half the days",
                    "nearly every day"))){
      stop(paste0("Non-allowed answers in ",
                  i,
                  ". Answers should be 'not at all', 'once or twice'",
                  ", 'several days', 'more than half the days'",
                  ", or 'nearly every day'."))
    }
  }

  if (method == "basic") {
    df <- data.frame(sapply(df, function(x) {
      dplyr::case_when(
        x == "not at all" ~ 0,
        x == "once or twice" ~ 0.5,
        x == "several days" ~ 1,
        x == "more than half the days" ~ 2,
        TRUE ~ 3
      )
    }, simplify=FALSE))
    df$Anxiety <- df$A1 + df$A2
    df$Depression <- df$D1 + df$D2
  } else {
    df$A1 <- dplyr::case_when(
      df$A1 == "not at all" ~ 0,
      df$A1 == "once or twice" ~ 0.34,
      df$A1 == "several days" ~ 0.55,
      df$A1 == "more than half the days" ~ 0.71,
      TRUE ~ 1
    )
    df$A2 <- dplyr::case_when(
      df$A2 == "not at all" ~ 0,
      df$A2 == "once or twice" ~ 0.44,
      df$A2 == "several days" ~ 0.58,
      df$A2 == "more than half the days" ~ 0.71,
      TRUE ~ 1
    )
    df$D1 <- dplyr::case_when(
      df$D1 == "not at all" ~ 0,
      df$D1 == "once or twice" ~ 0.38,
      df$D1 == "several days" ~ 0.51,
      df$D1 == "more than half the days" ~ 0.62,
      TRUE ~ 1
    )
    df$D2 <- dplyr::case_when(
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
