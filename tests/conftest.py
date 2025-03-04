import pytest

from status_map_validator import StatusMap

@pytest.fixture
def transitions_with_conditions():
    def condition_draft_to_pending():
        print("condition_draft_to_pending")
    def condition_pending_to_approved():
        print("condition_pending_to_approved")

    return {
        "draft": {"pending": {"validation": [condition_draft_to_pending]}},
        "pending": {"approved": {"validation": [condition_pending_to_approved]}},
        "approved": {"processed": {}},
    }


@pytest.fixture
def transitions():
    return {
        "pending": ["processing"],
        "processing": ["approved", "rejected"],
        "approved": ["processed"],
        "rejected": [],
        "processed": [],
    }


@pytest.fixture
def cycle_transitions():
    return {
        "pending": {"processing"},
        "processing": {"approved", "rejected"},
        "approved": {"processed"},
        "rejected": {"pending"},
        "processed": set(),
    }


@pytest.fixture
def complex_transitions():
    return {
        "pending": {"shipped"},
        "shipped": {
            "stolen",
            "seized_for_inspection",
            "returned_to_sender",
            "shipped",
            "delivered",
            "awaiting_pickup_by_receiver",
            "returning_to_sender",
            "lost",
        },
        "lost": {
            "stolen",
            "returned_to_sender",
            "seized_for_inspection",
            "delivered",
            "awaiting_pickup_by_receiver",
            "returning_to_sender",
            "lost",
        },
        "stolen": {
            "seized_for_inspection",
            "returned_to_sender",
            "lost",
            "delivered",
            "returning_to_sender",
            "stolen",
            "awaiting_pickup_by_receiver",
        },
        "seized_for_inspection": {
            "stolen",
            "returned_to_sender",
            "seized_for_inspection",
            "delivered",
            "awaiting_pickup_by_receiver",
            "returning_to_sender",
            "lost",
        },
        "awaiting_pickup_by_receiver": {
            "stolen",
            "returned_to_sender",
            "seized_for_inspection",
            "delivered",
            "awaiting_pickup_by_receiver",
            "returning_to_sender",
            "lost",
        },
        "delivered": set(),
        "returning_to_sender": {
            "stolen",
            "returned_to_sender",
            "seized_for_inspection",
            "delivered",
            "returning_to_sender",
            "lost",
        },
        "returned_to_sender": set(),
    }


@pytest.fixture
def complex_transitions_map(complex_transitions):
    return StatusMap(complex_transitions)


@pytest.fixture
def transitions_map(transitions):
    return StatusMap(transitions)

@pytest.fixture
def transitions_with_conditions_map(transitions_with_conditions):
    return StatusMap(transitions_with_conditions)


@pytest.fixture
def cycle_transitions_map(cycle_transitions):
    return StatusMap(cycle_transitions)


@pytest.fixture
def repeated_statuses():
    return (
        "pending",
        "pending",
        "pending",
        "processing",
        "processing",
        "rejected",
        "rejected",
        "rejected",
        "approved",
        "approved",
        "processed",
        "processed",
        "processed",
    )
