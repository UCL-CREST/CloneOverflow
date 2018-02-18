public class Test {
    public static void main ( String[] args ) throws ParseException, SchedulerException {
        String groupName = "group";
        String cronExpression = "0 13 13 ? * THUR";
        CronTrigger cronTrigger = new CronTrigger ( "trigger_" + groupName, groupName, cronExpression );
        cronTrigger.setStartTime ( new Date ( 0 ) );
        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        JobDetail detail = new JobDetail ( "testJob", groupName, TestJob.class );
        scheduler.scheduleJob ( detail, cronTrigger );
        scheduler.start();
        try {
            Thread.sleep ( 50001 );
        } catch ( Exception ignore ) {
        }
    }
    public static class TestJob implements Job {
        public void execute ( JobExecutionContext context ) throws JobExecutionException {
            System.out.println ( "TEST" );
        }
    }
}
