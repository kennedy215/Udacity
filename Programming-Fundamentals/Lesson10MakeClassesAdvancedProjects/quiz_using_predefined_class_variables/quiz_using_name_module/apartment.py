import tenant

tenant1 = tenant.Apartment("1000.00",
                      "Bobby Jones",
                      "Ends 10/1/2018",
                      "https://youtu.be/Ets0xkUk17Y")
tenant2 = tenant.Apartment("1200.00",
                      "Jean Mean",
                      "Ends 10/1/2019",
                      "https://youtu.be/ffeOw_bWI98")
tenant3 = tenant.Apartment("2000.00",
                      "Jeanie Jackson",
                      "Ends 12/1/2018",
                      "https://youtu.be/wvu2u-CLYjs")

print(tenant3.lease)
tenant3.show_commercial()
print(tenant.Apartment.__doc__)
print(tenant.Apartment.__name__)
print(tenant.Apartment.__module__)
