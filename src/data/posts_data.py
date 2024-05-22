from src.generators.post import PostBuilder

fake_posts = {
    "post": PostBuilder().delete("id").build(),

    "post_negative_id": PostBuilder().set_id(-1).build(),
    "post_zero_id": PostBuilder().set_id(0).build(),
    "post_string_id": PostBuilder().set_id("string_id").build(),

    "post_negative_user_id": PostBuilder().set_user_id(-1).build(),
    "post_string_user_id": PostBuilder().set_user_id("string_user_id").build(),
    "post_zero_user_id": PostBuilder().set_user_id(0).build(),

    "post_without_title": PostBuilder().delete("title").build(),
    "post_without_body": PostBuilder().delete("body").build(),
    "post_without_user_id": PostBuilder().delete("userId").build(),
    "post_without_id": PostBuilder().delete("id").build(),
    "post_empty": {},
}
