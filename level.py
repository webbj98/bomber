class Level:
    def __init__(self):

        self.curr_lvl = 0  # indicy controls how levels are picked

        self.lvl_1 = [  # level layout is in a list of strings "W" is a wall
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W              W                                    W",
                "W              W                                    W",
                "W              W          V          WCWWCW         W",
                "W              W       V             W ++ W         W",
                "W              C          WWWWWWWWWWWW    W   c     W",
                "W    G         W          WWWWWWWWWWWW   +W         W",
                "W              W          WWWWWWWWWWWW+   W         W",
                "W              W          WWWWWWWWWWWWW   W         W",
                "W              W          WWWWWWWWWWWW    W         W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWCW   +   WWW",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                    W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW          C     C   W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW            WWWWWWWWW",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW            WWWWWWWWW",
                "WWWWWWWWWWW               W                 WWWWWWWWW",
                "W                      W  W                 WWWWWWWWW",
                "W                      W+ C                 WWWWWWWWW",
                "W        WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W       HW                                 C        W",
                "W   + +  W                                 C+ +  ++ W",
                "W   CCC  W                                 C       +W",
                "W        W              WWWWWWWW      WWWWWW        W",
                "W        W                     W      WWWWWW        W",
                "W        W                     W      WWWWWW        W",
                "W                              W      WWWWWW        W",
                "W      c                       W           W        W",
                "W                c             WWWWWWWWWWWWW        W",
                "W                              W                    W",
                "W                              W                    W",
                "WWWWWWWWWWWWWWWWWWWW           W     WWWWWWWWWWWWWWWW",
                "W                  W           W    +W              W",
                "W                  WWWWWWWWWWWWW            c       W",
                "W                  W           W    +W              W",
                "W                  W        V  WWWWWWWWW            W",
                "W                  W                   W       V    W",
                "W                  W                   W            W",
                "W                  C                   C            W",
                "WP                VC         H         W            W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",

            ]


        self.lvl_2 = [
                    "W                                                      WWWWWWWWWWWWWWWWWWWWW",
                    "                                                       WWWWWWWWWWWWWWWWWWWW ",
                    "W                                                      WWWWWWWWWWWWWWWWWWWWW",
                    "W                                                      WWWWWWWWWWWWWWWWWWWWW",
                    "W                                                      WWWWWWWWWWWWWWWWWWWWW",
                    "W                                                                WWWWWWWWWWW",
                    "W                    W                                             WWWWWWWWW",
                    "                       W                               WWWWWWWWWWWWWWWWWWWW ",
                    "                         W                             WWWWWWWWWWWWWWWWWWWW ",
                    "                           W                           WWWWWWWWWWWWWWWWWWWW ",
                    "                                                       WWWWWWWWWWWWWWWWWWWW ",
                    "                                                       WWWWWWWWWWWWWWWWWWWW ",
                    "                                                       WWWWWWWWWWWWWWWWWWWW ",
                    "                                                       WWWWWWWWWWWWWWWWWWWW ",
                    "                             P                          WWWWWWWWWWWWWWWWWWWW",
                    "                                                        WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "                                     G                  WWWWWWWWWWWWWWWWWWWW ",
                    "WWWWWWWWWWWc+VHWCWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "WW                                                   W  WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWWW",
                    "W                                                                  WWWWWWWWW",
                    "                        W                               WWWWWWWWWWWWWWWWWWWW",
                    "                         W                              WWWWWWWWWWWWWWWWWWWW",
                    "                           W                            WWWWWWWWWWWWWWWWWWWW",
            ]
        self.level_list = [self.lvl_1,self.lvl_2]

    def next_lvl(self):
        self.curr_lvl +=1

    def load_lvl(self):
        return self.level_list[self.curr_lvl]

    def get_curr_lvl(self):
        return self.curr_lvl
    def get_map_width(self):
        return len(self.level_list[self.curr_lvl])*15
    def get_map_height(self):
        return len(self.level_list[self.curr_lvl][0]) *15