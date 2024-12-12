# MetaInjector Development Notes

## Main Features
- Target platform Desktop for MacOSX
- GUI with light/dark mode
- Grayscale color scheme with harmonic colors for light and dark mode and optimal contrast. ***Please see the file GrayScalePalette.png for the palette***
- Image selection and batch processing
- EXIF metadata injection
- iOS and Android device simulation
- Location data injection
- Output directory selection
- Simplified code wherever possible 
- Reduce dependency bloat ***EVERYWHERE***
- Use Faker for realistic data generation
- Enable the ability to add custom data to the metadata via an text input boxes
- Allow for Audio metadata injection
- Keep the UI clean and simple, with a focus on functionality and user experience., but keep it strict to the guidelines listed under UI.
- Almost all of the data should be randomized **if** the user chooses to randomize it, but all of the data should be consistent with the device model release date, and the current date. as well as the current time.
- Simple loading screen that appears immediately once the app opens and shows the status of the loading as a progress bar with the title "META INJECTOR" above it. Close the loading window once the app is fully loaded.
- Loading screen must have a thick stroke (border) that adapts to system light/dark mode
- Never use widgets
- Single window for the entire app.

### UI ***CRITICAL***
- [ ] Harmonic color scheme
- [ ] See /GrayScalePalette.png for the color values **CRITICAL**
- [ ] Use Helvetica Neue BOLD all caps for titles, headers and drop down menus.     
- [ ] Use Roboto MONO BOLD all caps for the buttons. 
- [ ] Use Roboto MONO for **ALL** other fonts in the body, including file names. 
- [ ] Light and dark mode
- [ ] Containers should be used for all of the UI elements, and the UI should be organized into sections with headers and footers.
- [ ] Each container should have a consistent style, and the style should be applied to all of the containers.  The containers should be styled with a consistent color scheme, and the color scheme should be consistent with the color scheme of the palette file.
- [ ] Grayscale color scheme. Must be consistent with the palette file. At least 80% of the UI should be in grayscale.
- [ ] The loading screen should be a simple progress bar with the title "META INJECTOR" above it. And it must match the color scheme of the palette file. As well as the rest of the UI.
- [ ] Mac drag and drop functionality
- [ ] Add visible grid lines to table **IMPORTANT**
- [ ] Always use Helvetica Neue BOLD all caps for titles, headers and drop down menus.
- [ ] Always use Roboto MONO for **ALL** other fonts in the body, including file names.  Please use Roboto MONO BOLD all caps for the buttons. 

### Location Features
- [ ] Add full address input box, so user can input a specific address
- [ ] Location randomizer, that can be used to generate a random address that exists in a database. Please figure out how to do this most effectively **and** efficiently  
- [ ] Use Faker library for realistic addresses
- [ ] Add address validation/formatting

### Time Features
- [ ] Add time input field, with the option to switch between 12hr and 24hr
- [ ] Add time randomizer
- [ ] Ensure time is consistent with device model release date
- [ ] Add time range selection

### Device Features
- [ ] Add phone model randomizer
- [ ] Ensure iOS version matches phone model
- [ ] Ensure Android version matches phone model
- [ ] Add carrier information
- [ ] Add IMEI simulation

### Code Structure
- [ ] Separate UI and business logic
- [ ] Add error handling for all user inputs
- [ ] Add logging for debugging
- [ ] Add unit tests

## Implementation Notes

### Location Randomization
- Use Faker's address provider
- Ensure addresses are valid for selected country
- Format addresses consistently
- Cache generated addresses for performance

### Time Randomization
- Consider device release date as minimum
- Consider current date as maximum
- Add option for custom date ranges
- Ensure consistent timestamps across EXIF data

### EXIF Metadata Injection
- Add a checkbox for each metadata field, so the user can choose which fields to inject.
- Add a checkbox for each metadata field, so the user can choose which fields to randomize.
- Add a checkbox for each metadata field, so the user can choose which fields to add custom data to.
- Add a checkbox for each metadata field, so the user can choose which fields to add custom data to.
- Add a checkbox for each metadata field, so the user can choose which fields to add custom data to.    

### Audio Metadata Injection
- Add a checkbox for each metadata field, so the user can choose which fields to inject.
- Add a checkbox for each metadata field, so the user can choose which fields to randomize.
- Add a checkbox for each metadata field, so the user can choose which fields to add custom data to.
- Add a checkbox for each metadata field, so the user can choose which fields to add custom data to.
- Add a checkbox for each metadata field, so the user can choose which fields to add custom data to.    


### Device and File Randomization
- Match iOS versions to device capabilities
- Match Android versions to device capabilities
- Consider regional variants
- Generate realistic IMEI numbers
- Include carrier-specific metadata
- Audio metadata injection, and validation of the file type, consistent with the file extension.

### UI REQUIREMENTS
- Use Helvetica Neue for all headers
- Use Roboto Mono for all other text
- Implement proper spacing
- Add tooltips for complex features
- Improve error messaging

## Testing Plan
- [ ] Test with various image formats
- [ ] Verify EXIF data accuracy
- [ ] Check address validation
- [ ] Verify time consistency
- [ ] Test device/iOS compatibility 
- [ ] Test audio metadata injection
- [ ] Test EXIF metadata injection
- [ ] Test location randomization
- [ ] Test time randomization
- [ ] Test device randomization
- [ ] Test file randomization
- [ ] Test UI requirements
- [ ] Test audio metadata injection
- [ ] Generate a test file with the metadata injected, and then use the tool to verify that the metadata is accurate.