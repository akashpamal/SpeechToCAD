import adsk.core, adsk.fusion, math, traceback

def run(context):
    ui = None
    try: 
        app = adsk.core.Application.get()
        ui = app.userInterface

        # doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.

        """
        Do not delete this section – it's used for parsing
        """
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))