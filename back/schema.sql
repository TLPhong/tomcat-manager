create table users
(
    user_name text constraint user_pk primary key,
    user_pass text,
    note text
);

create table user_roles
(
    user_name text,
    role_name text,
    constraint user_roles_pk unique (user_name, role_name)
)
