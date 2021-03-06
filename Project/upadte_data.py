####################################################################################
# Authors: Jackson O'Donnell, Grant Gasser
#
# Purpose: Functions to update data in the tables
####################################################################################

####################################################################################
# Function: updateCurriculum
#
# Purpose: updates the curriculum table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        curric: A dictionary containing the primary key for the curriculum to edit
#        mycursor: A cursor to do the updates
#        mydb: The database in which the table lies
####################################################################################
def updateCurriculum(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE curriculum SET """ + attr + """ = %s WHERE curric_name = %s"""

    vals = (update_data['New Value:'], update_data['curric_name'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe curriculum has been updated')


##################################################################################
# Function: updateCourses
#
# Purpose: Updates the courses table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        course: A dictionary of the primary key for the course
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateCourses(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE courses SET """+ attr +""" = %s
             WHERE course_name = %s"""

    vals = (update_data['New Value:'], update_data['course_name'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe course has been updated')


##################################################################################
# Function: updateReqs
#
# Purpose: Updates the course_reqs table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        req: A dictionary for the primary key of the curric_req (name and req)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateReqs(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE curric_reqs SET """+attr+""" = %s
             WHERE course_name = %s AND req_for = %s
             AND course_name NOT IN (SELECT course_name
                                       FROM curric_ops
                                       WHERE course_name = %s)"""

    vals = (update_data['New Value:'], update_data['course_name'], update_data['req_for'],
            update_data['course_name'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe course requirement has been edited.')


##################################################################################
# Function: updateOps
#
# Purpose: Updates the curric_ops table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        op: A dictionary for the primary key of the curric_op (name and op)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateOps(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE curric_ops SET """+attr+""" = %s
             WHERE course_name = %s AND op_for = %s
               AND course_name NOT IN (SELECT course_name
                                       FROM curric_reqs
                                       WHERE course_name = %s)"""

    vals = (update_data['New Value:'], update_data['course_name'], update_data['op_for'],
            update_data['course_name'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe course option has been edited.')


##################################################################################
# Function: updateTopic
#
# Purpose: Updates the topic table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        topic: A dictionary for the primary key of the topic (id, name)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateTopic(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE topic SET """+attr+""" = %s
             WHERE topic_name = %s AND topic_id = %s"""

    vals = (update_data['New Value:'], update_data['topic_name'], update_data['topic_id'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe topic has been edited.')


##################################################################################
# Function: updateTopicCurric
#
# Purpose: Updates the topic_curric table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        topic: A dictionary for the primary key of the topic_curric (id)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateTopicCurric(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE topic_curric SET """+attr+""" = %s
             WHERE topic_id = %s AND curric_assoc = %s AND lvl = %s"""

    vals = (update_data['New Value:'], update_data['topic_id'], update_data['curric_assoc'],
            update_data['lvl'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe topic-curriculum relationship has been edited.')


##################################################################################
# Function: updateGoals
#
# Purpose: Updates the goals table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        goal: A dictionary for the primary key of the goal (id)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateGoals(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE goals SET """+attr+""" = %s
             WHERE goal_id = %s"""

    vals = (update_data['New Value:'], update_data['goal_id'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe goal has been edited.')


##################################################################################
# Function: updateSection
#
# Purpose: Updates the section table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        section: A dictionary for the primary key of the section (id)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateSection(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE section SET """+attr+""" = %s
             WHERE section_id = %s"""

    vals = (update_data['New Value:'], update_data['section_id'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe section has been edited.')


##################################################################################
# Function: updateSecGrades
#
# Purpose: Updates the sec_grades table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        section: A dictionary for the primary key of the sec_grade (id)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateSecGrades(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE sec_grades SET """+attr+""" = %s
             WHERE section_id = %s"""

    vals = (update_data['New Value:'], update_data['section_id'], update_data['course_name'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe section_grade has been edited.')


##################################################################################
# Function: updateGoalGrades
#
# Purpose: Updates the goal_grades table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        goal: A dictionary for the primary key of the goal_grade (id)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateGoalGrades(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE goal_grades SET """+attr+""" = %s
             WHERE goal_id = %s"""

    vals = (update_data['New Value:'], update_data['goal_id'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe goal_grade has been edited.')


##################################################################################
# Function: updateCourseGoals
#
# Purpose: Updates the course_goals table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        goal: A dictionary for the primary key of the course_goal (g_id, c_name)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateCourseGoals(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE course_goals SET """+attr+""" = %s
             WHERE goal_id = %s AND course_name = %s"""

    vals = (update_data['New Value:'], update_data['goal_id'], update_data['course_name'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe course-goal relationship has been edited.')


##################################################################################
# Function: updateCourseTopic
#
# Purpose: Updates the course_topic table
#
# Parameters:
#        attr: The attribute to be edited
#        data: The new value for the attribute
#        topic: A dictionary for the primary key of the course_topic (topic_id, course_name)
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def updateCourseTopic(update_data, mycursor, mydb):
    attr = update_data['Attribute:'].replace("'", '')
    sql = """UPDATE course_topic SET """+attr+""" = %s
             WHERE topic_id = %s AND course_name = %s"""

    vals = (update_data['New Value:'], update_data['topic_id'], update_data['course_name'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe coursetopic relationship has been edited.')
