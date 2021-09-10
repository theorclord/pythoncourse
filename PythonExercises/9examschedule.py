import datetime
exam_st_date = (11, 12, 2014)

date = datetime.datetime(exam_st_date[2],exam_st_date[1],exam_st_date[0])
# date object
print("The examination will start from", date.strftime("%d / %m / %Y"))
#Non date object
print( "The examination will start from : %i / %i / %i"%exam_st_date)
