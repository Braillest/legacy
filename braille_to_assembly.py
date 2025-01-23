import adsk.core, adsk.fusion, adsk.cam, traceback

class UiLogger:
    def __init__(self, forceUpdate):
        app = adsk.core.Application.get()
        ui  = app.userInterface
        palettes = ui.palettes
        self.textPalette = palettes.itemById("TextCommands")
        self.forceUpdate = forceUpdate
        self.textPalette.isVisible = True

    def print(self, text):
        self.textPalette.writeText(text)
        if (self.forceUpdate):
            adsk.doEvents() 

logger = UiLogger(True)

def get_braille_body_by_name(selection_set, body_name):
    for entity in selection_set.entities:
        if isinstance(entity, adsk.fusion.BRepBody) and entity.name == body_name:
            return entity

def union_all_bodies_in_component(component):

    # Validate component body count
    bodies = component.bRepBodies
    if bodies.count < 2:
        return

    # Needed vars to create feature input
    combine_features = component.features.combineFeatures
    target_body = bodies.item(0)
    tool_bodies = adsk.core.ObjectCollection.create()
    for z in range(1, bodies.count):
        tool_bodies.add(bodies.item(z))

    # Create feature input
    combine_input = combine_features.createInput(target_body, tool_bodies)
    combine_input.isKeepToolBodies = False
    combine_input.isNewComponent = False
    combine_input.operation = adsk.fusion.FeatureOperations.JoinFeatureOperation
    combine_features.add(combine_input)

braille_character_width = 6
braille_character_height = 10

def run(context):

    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        design = app.activeProduct
        if not isinstance(design, adsk.fusion.Design):
            ui.messageBox('No active Fusion 360 design.')
            return

        design.isPreViewEnabled = False

        selection_sets = design.selectionSets
        selection_set = selection_sets.itemByName("Braille Characters")

        root_comp = design.rootComponent
        features = root_comp.features

        transform = adsk.core.Matrix3D.create()

        braille_file_path = "C:\\Users\\ramit\\AppData\\Roaming\\Autodesk\\Autodesk Fusion 360\\API\\Scripts\\Braille Processor\\test"

        with open(braille_file_path, "r", encoding="utf8") as infile:

            y = 0

            lines = infile.readlines()
            line_count = len(lines)

            for line_position, line in enumerate(lines):

                x = 0

                logger.print(f'{line_position} / {line_count}')

                # Create new component for the line of characters
                transform.translation = adsk.core.Vector3D.create(x / 10, y / 10, 0)
                new_occurrence = root_comp.occurrences.addNewComponent(transform)
                new_component = new_occurrence.component
                new_component.name = f'{line_position}'

                for char_position, char in enumerate(line):

                    # Compute the name of the existing body to copy for the incoming braille character
                    desired_body_name = "U+" + str(hex(ord(char)))[2:].upper()

                    # Skip newline char
                    if desired_body_name == "U+A":
                        continue

                    # Skip if computed name is too small
                    if len(desired_body_name) < 6:
                        logger.print(f'{desired_body_name} {line_position} {char_position} skipped - computed body name length less than 6')
                        x += braille_character_width
                        continue

                    # Find desired body
                    body = get_braille_body_by_name(selection_set, desired_body_name)

                    # Handle case where body not found
                    if not body:
                        logger.print(f'{desired_body_name} {line_position} {char_position} skipped - computed body name not found')
                        x += braille_character_width
                        continue

                    new_body = new_component.bRepBodies.add(body)
                    new_bodies = adsk.core.ObjectCollection.create()
                    new_bodies.add(new_body)

                    if x == 0 and y == 0:
                        x += braille_character_width
                        continue

                    move_features = new_component.features.moveFeatures
                    move_feature_input = move_features.createInput2(new_bodies)
                    transform.translation = adsk.core.Vector3D.create(x / 10, y / 10, 0)
                    move_feature_input.defineAsFreeMove(transform)
                    move_features.add(move_feature_input)

                    # Update X value
                    x += braille_character_width

                union_all_bodies_in_component(new_component)

                # Update Y value
                y += 5

                # Temporarily break at 400 lines (performance issue)
                if line_position >= 400:
                    break

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
