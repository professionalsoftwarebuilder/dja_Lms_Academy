from django.urls import  include, path

from . import views

# Import custom views.
from teacher.views import announcement
from teacher.views import syllabus
from teacher.views import policy
from teacher.views import lecture
from teacher.views import lecture_note
from teacher.views import assignment
from teacher.views import quiz
from teacher.views import exam
from teacher.views import overview
from teacher.views import discussion
from teacher.views import peer_review
from teacher.views import setting

app_name = 'teachers'

urlpatterns = [
    # Syllabus
    path('teacher/course/<course_id>/overview', overview.overview_page),
    path('teacher/course/<course_id>/submit_course_for_review', overview.submit_course_for_review),

    # Announcement
    path('teacher/course/<course_id>/', announcement.announcements_page),
    path('teacher/course/<course_id>/home', announcement.announcements_page),
    path('teacher/course/<course_id>/announcement', announcement.announcements_page),
    path('teacher/course/<course_id>/announcements_table', announcement.announcements_table),
    path('teacher/course/<course_id>/announcement_modal', announcement.announcement_modal),
    path('teacher/course/<course_id>/save_announcement', announcement.save_announcement),
    path('teacher/course/<course_id>/delete_announcement', announcement.delete_announcement),

    # Syllabus
    path('teacher/course/<course_id>/syllabus', syllabus.syllabus_page),
    path('teacher/course/<course_id>/syllabus_modal', syllabus.syllabus_modal),
    path('teacher/course/<course_id>/save_syllabus', syllabus.save_syllabus),
    path('teacher/course/<course_id>/delete_syllabus', syllabus.delete_syllabus),

    # Policy
    path('teacher/course/<course_id>/policy', policy.policy_page),
    path('teacher/course/<course_id>/policy_modal', policy.policy_modal),
    path('teacher/course/<course_id>/save_policy', policy.save_policy),
    path('teacher/course/<course_id>/delete_policy', policy.delete_policy),

    # Lecture
    path('teacher/course/<course_id>/lectures', lecture.lectures_page),
    path('teacher/course/<course_id>/lectures_table', lecture.lectures_table),
    path('teacher/course/<course_id>/lecture_modal', lecture.lecture_modal),
    path('teacher/course/<course_id>/save_lecture', lecture.save_lecture),
    path('teacher/course/<course_id>/delete_lecture', lecture.delete_lecture),

    # Lecture Note(s)
    path('teacher/course/<course_id>/lecture/<lecture_id>/notes', lecture_note.lecture_notes_page),
    path('teacher/course/<course_id>/lecture/<lecture_id>/lecture_notes_table', lecture_note.lecture_notes_table),
    path('teacher/course/<course_id>/lecture/<lecture_id>/lecture_note_modal', lecture_note.lecture_note_modal),
    path('teacher/course/<course_id>/lecture/<lecture_id>/save_lecture_note', lecture_note.save_lecture_note),
    path('teacher/course/<course_id>/lecture/<lecture_id>/delete_lecture_note', lecture_note.delete_lecture_note),
                       
    # Assignment(s)
    path('teacher/course/<course_id>/assignments', assignment.assignments_page),
    path('teacher/course/<course_id>/assignments_table', assignment.assignments_table),
    path('teacher/course/<course_id>/assignment_modal', assignment.assignment_modal),
    path('teacher/course/<course_id>/save_assignment', assignment.save_assignment),
    path('teacher/course/<course_id>/delete_assignment', assignment.delete_assignment),

    # Assignment
    path('teacher/course/<course_id>/assignment/<assignment_id>', assignment.assignment_page),
    path('teacher/course/<course_id>/assignment/<assignment_id>/questions_table', assignment.questions_table),
    path('teacher/course/<course_id>/assignment/<assignment_id>/question_type_modal', assignment.question_type_modal),
    path('teacher/course/<course_id>/assignment/<assignment_id>/question_essay_modal', assignment.question_essay_modal),
    path('teacher/course/<course_id>/assignment/<assignment_id>/question_multiple_choice_modal', assignment.question_multiple_choice_modal),
    path('teacher/course/<course_id>/assignment/<assignment_id>/question_true_false_modal', assignment.question_true_false_modal),
    path('teacher/course/<course_id>/assignment/<assignment_id>/question_response_modal', assignment.question_response_modal),
    path('teacher/course/<course_id>/assignment/<assignment_id>/save_question', assignment.save_question),
    path('teacher/course/<course_id>/assignment/<assignment_id>/delete_question', assignment.delete_question),

    # Quiz(es)
    path('teacher/course/<course_id>/quizzes', quiz.quizzes_page),
    path('teacher/course/<course_id>/quizzes_table', quiz.quizzes_table),
    path('teacher/course/<course_id>/quiz_modal', quiz.quiz_modal),
    path('teacher/course/<course_id>/save_quiz', quiz.save_quiz),
    path('teacher/course/<course_id>/delete_quiz', quiz.delete_quiz),

    # Quiz
    path('teacher/course/<course_id>/quiz/<quiz_id>', quiz.quiz_page),
    path('teacher/course/<course_id>/quiz/<quiz_id>/questions_table', quiz.questions_table),
    path('teacher/course/<course_id>/quiz/<quiz_id>/question_type_modal', quiz.question_type_modal),
    path('teacher/course/<course_id>/quiz/<quiz_id>/question_true_false_modal', quiz.question_true_false_modal),
    path('teacher/course/<course_id>/quiz/<quiz_id>/save_question', quiz.save_question),
    path('teacher/course/<course_id>/quiz/<quiz_id>/delete_question', quiz.delete_question),

    # Exam(s)
    path('teacher/course/<course_id>/exams', exam.exams_page),
    path('teacher/course/<course_id>/exams_table', exam.exams_table),
    path('teacher/course/<course_id>/exam_modal', exam.exam_modal),
    path('teacher/course/<course_id>/save_exam', exam.save_exam),
    path('teacher/course/<course_id>/delete_exam', exam.delete_exam),
    
    # # Exam
    path('teacher/course/<course_id>/exam/<exam_id>', exam.exam_page),
    path('teacher/course/<course_id>/exam/<exam_id>/questions_table', exam.questions_table),
    path('teacher/course/<course_id>/exam/<exam_id>/question_type_modal', exam.question_type_modal),
    path('teacher/course/<course_id>/exam/<exam_id>/question_multiple_choice_modal', exam.question_multiple_choice_modal),
    path('teacher/course/<course_id>/exam/<exam_id>/save_question', exam.save_question),
    path('teacher/course/<course_id>/exam/<exam_id>/delete_question', exam.delete_question),
                       
    # Discussion
    path('teacher/course/<course_id>/discussion', discussion.discussion_page),
    path('teacher/course/<course_id>/discussions_table', discussion.discussions_table),
    path('teacher/course/<course_id>/new_thread', discussion.new_thread_modal),
    path('teacher/course/<course_id>/insert_thread', discussion.insert_thread),
    path('teacher/course/<course_id>/delete_thread', discussion.delete_thread),
    path('teacher/course/<course_id>/thread/<thread_id>', discussion.posts_page),
    path('teacher/course/<course_id>/thread/<thread_id>/posts_table', discussion.posts_table),
    path('teacher/course/<course_id>/thread/<thread_id>/new_post', discussion.new_post_modal),
    path('teacher/course/<course_id>/thread/<thread_id>/insert_post', discussion.insert_post),
                       
    # Peer-Review
    path('teacher/course/<course_id>/peer_reviews', peer_review.peer_reviews_page),
    path('teacher/course/<course_id>/peer_review/<assignment_id>', peer_review.assignment_page),
    path('teacher/course/<course_id>/peer_review/<assignment_id>/peer_review_modal', peer_review.peer_review_modal),
    path('teacher/course/<course_id>/peer_review/<assignment_id>/save_peer_review', peer_review.save_peer_review),
    path('teacher/course/<course_id>/peer_review/<assignment_id>/delete_peer_review', peer_review.delete_peer_review),
    path('teacher/course/<course_id>/peer_review/<submission_id>/update_assignment_marks', peer_review.update_assignment_marks),
                       
    # Settings
    path('teacher/course/<course_id>/settings', setting.settings_page),
    path('teacher/course/<course_id>/suspend_course', setting.suspend_course),

    # $# 010 add 2
    # Module
    path('teacher/course/<course_id>/modules', lecture.modules_page, name='modules'),
    path('teacher/course/<module_id>/<course_id>/<unit_id>/module', lecture.module, name='module'),
    path('teacher/course/<course_id>/module_modal', lecture.module_modal, name='module_modal'),

]
