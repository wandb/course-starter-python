def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert ".shape" in __solution__, "Did you call .shape on train_images?"
    assert total_test_images == len(
        test_images), "Are you getting the correct length?"

    __msg__.good("Well done!")
