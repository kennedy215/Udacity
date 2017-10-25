import street_fighter

ken_masters = street_fighter.Parent("Masters",
                                    "Brown")
chung_li = street_fighter.Child("Li",
                                "Brown",
                                "Kung Fu")


print(chung_li.last_name),(chung_li.eye_color),(chung_li.fighting_style)

ken_masters.show_info()
chung_li.show_info()
