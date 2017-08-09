public static class FTP extends LayoutFocusTraversalPolicy {
    @Override
    protected boolean accept ( Component comp ) {
        JFrame window = ( JFrame ) SwingUtilities.windowForComponent ( comp );
        if ( hasVisibleGlassPane ( window ) ) {
            return comp.getParent() == window.getGlassPane();
        }
        return super.accept ( comp );
    }
    private boolean hasVisibleGlassPane ( JFrame window ) {
        return window != null && window.getGlassPane() != null
               && window.getGlassPane().isVisible();
    }
}
