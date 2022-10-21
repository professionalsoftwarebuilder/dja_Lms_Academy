from django.urls import include, path

from . import views

# Import custom views.
from student.views import announcement
from student.views import syllabus
from student.views import policy
from student.views import lecture
from student.views import lecture_note
from student.views import assignment
from student.views import quiz
from student.views import exam
from student.views import discussion
from student.views import peer_review
from student.views import credit

urlpatterns = [
    # Announcement
    path('course/<course_id>/announcements/', announcement.announcements_page),
    path('course/<course_id>/announcement/', announcement.announcements_page),

    # Syllabus
    path('course/<course_id>/syllabus', syllabus.syllabus_page),

    # Grades & Policy
    path('course/<course_id>/policy', policy.policy_page),

    # Lecture
    path('course/<course_id>/lectures', lecture.lectures_page),
    path('course/<course_id>/lecture', lecture.lecture),
                       
    # Lecture Notes
    path('course/<course_id>/lecture/(\d+)/notes', lecture_note.lecture_notes_page),
    path('course/<course_id>/lecture/(\d+)/view_lecture_note', lecture_note.view_lecture_note),

    # Assignment(s)
    path('course/<course_id>/assignments', assignment.assignments_page),
    path('course/<course_id>/assignments_table', assignment.assignments_table),
    path('course/<course_id>/delete_assignment', assignment.delete_assignment),
                       
    # Assignment
    path('course/<course_id>/assignment/(\d+)', assignment.assignment_page),
    path('course/<course_id>/assignment/(\d+)/submit_assignment', assignment.submit_assignment),
    path('course/<course_id>/assignment/(\d+)/submit_e_assignment_answer', assignment.submit_e_assignment_answer),
    path('course/<course_id>/assignment/(\d+)/submit_mc_assignment_answer', assignment.submit_mc_assignment_answer),
    path('course/<course_id>/assignment/(\d+)/submit_tf_assignment_answer', assignment.submit_tf_assignment_answer),
    path('course/<course_id>/assignment/(\d+)/submit_r_assignment_answer', assignment.submit_r_assignment_answer),
                       
    # Quiz(zes)
    path('course/<course_id>/quizzes', quiz.quizzes_page),
    path('course/<course_id>/quizzes_table', quiz.quizzes_table),
    path('course/<course_id>/quiz_delete', quiz.delete_quiz),
                       
    # Quiz
    path('course/<course_id>/quiz/<quiz_id>', quiz.quiz_page),
    path('course/<course_id>/quiz/<quiz_id>/submit_quiz', quiz.submit_quiz),
    path('course/<course_id>/quiz/<quiz_id>/submit_tf_quiz_answer', quiz.submit_tf_assignment_answer),

    # Exam(s)
    path('course/<course_id>/exams', exam.exams_page),
    path('course/<course_id>/exams_table', exam.exams_table),
    path('course/<course_id>/delete_exam', exam.delete_exam),
                       
    # Exam
    path('course/<course_id>/exam/<exam_id>', exam.exam_page),
    path('course/<course_id>/exam/<exam_id>/submit_exam', exam.submit_exam),
    path('course/<course_id>/exam/<exam_id>/submit_mc_exam_answer', exam.submit_mc_exam_answer),

    # Peer-Review
    path('course/<course_id>/peer_reviews', peer_review.peer_reviews_page),
    path('course/<course_id>/peer_review/<submission_id>', peer_review.assignment_page),
    path('course/<course_id>/peer_review/<submission_id>/peer_review_modal', peer_review.peer_review_modal),
    path('course/<course_id>/peer_review/<submission_id>/save_peer_review', peer_review.save_peer_review),
    path('course/<course_id>/peer_review/<submission_id>/delete_peer_review', peer_review.delete_peer_review),
    path('course/<course_id>/peer_review/<submission_id>/update_assignment_marks', peer_review.update_assignment_marks),
                       
    # Discussion
    path('course/<course_id>/discussion', discussion.discussion_page),
    path('course/<course_id>/threads_table', discussion.threads_table),
    path('course/<course_id>/new_thread', discussion.new_thread_modal),
    path('course/<course_id>/insert_thread', discussion.insert_thread),
    path('course/<course_id>/delete_thread', discussion.delete_thread),
    path('course/<course_id>/thread/<thread_id>', discussion.thread_page),
    path('course/<course_id>/thread/<thread_id>/posts_table', discussion.posts_table),
    path('course/<course_id>/thread/<thread_id>/new_post', discussion.new_post_modal),
    path('course/<course_id>/thread/<thread_id>/insert_post', discussion.insert_post),
                       
    # Credit
    path('course/<course_id>/credit', credit.credit_page),
    path('course/<course_id>/submit_credit_application', credit.submit_credit_application),
]
