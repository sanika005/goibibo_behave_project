Feature: Goibibo flight

    Scenario: Search flight from mumbai to delhi and perform assertion of price that all flights should be in ascending order as per price and verify it.
        Given launch chrome browser
        When Open goibibo website
        Then search flight from mumbai to delhi
        