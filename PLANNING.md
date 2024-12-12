# MetDat (Meta Injector) Development Plan

## Core Architecture
### Technology Stack
- **Frontend**: 
  - Tkinter for native MacOS GUI (minimal dependencies)
  - Custom container implementations
  - Helvetica Neue & Roboto Mono fonts
  - Strict grayscale theme from GrayScalePalette.png
- **Backend**:
  - Python core with minimal external dependencies
  - ExifTool for metadata manipulation
  - Faker for data generation
  - File-based caching for performance

## Development Phases

### Phase 1: Foundation & UI Setup (CRITICAL)
1. **Color Scheme Implementation**
   - Implement exact colors from GrayScalePalette.png
   - Ensure 80% minimum grayscale usage
   - Light/dark mode variants
   - Contrast validation

2. **Typography System**
   - Helvetica Neue BOLD (ALL CAPS) for:
     - Titles
     - Headers
     - Dropdown menus
   - Roboto MONO BOLD (ALL CAPS) for:
     - Buttons
   - Roboto MONO for:
     - Body text
     - Filenames
     - All other content

3. **Loading Screen**
   - Immediate display on launch
   - "META INJECTOR" title
   - Progress bar
   - Grayscale theme compliance
   - Auto-close on full load

4. **Main Window Architecture**
   - Single window design
   - Container-based layout with headers/footers
   - Consistent styling across all containers
   - Grid system with visible lines
   - Mac drag-and-drop implementation
   - No widgets policy

### Phase 2: Core Features
1. **Metadata Control System**
   - Individual controls for each metadata field:
     - Injection checkbox
     - Randomization checkbox
     - Custom data input
   - Apply to both EXIF and Audio metadata
   - Field-specific validation

2. **Location System**
   - Full address input
   - Efficient location randomization
   - Faker integration
   - Address validation/formatting
   - Location caching for performance

3. **Time Management**
   - 12/24hr time input
   - Time randomization within device constraints
   - Device-date consistency validation
   - Custom time range selection

4. **Device Simulation**
   - iOS/Android device database
   - Version compatibility checking
   - Carrier information
   - IMEI simulation
   - Regional variants support

### Phase 3: Data Processing
1. **File Processing**
   - Batch processing
   - Progress tracking
   - Error handling
   - Output directory management

2. **Randomization Engine**
   - Device-specific constraints
   - Time period validation
   - Location verification
   - Data consistency checks

### Phase 4: Testing & Validation
1. **Metadata Testing**
   - Generate test files
   - Verify injected metadata accuracy
   - Validate against device specifications
   - Check time consistency
   - Verify location data

2. **Format Testing**
   - Image format compatibility
   - Audio format compatibility
   - File validation
   - Extension consistency

3. **UI Testing**
   - Color scheme compliance
   - Font usage verification
   - Container styling
   - Grid system
   - Drag-and-drop functionality

4. **Performance Testing**
   - Batch processing efficiency
   - Memory usage
   - Response time
   - Caching effectiveness

## Error Handling
- User-friendly error messages
- Input validation
- Process status indicators
- Recovery procedures

## Documentation
- User guide
- Technical documentation
- Testing documentation
- Maintenance guide
