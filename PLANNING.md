# MetDat (Meta Injector) Development Plan

## Core Architecture
### Technology Stack
- **Frontend**: 
  - PyQt for native MacOS GUI (no widgets)
  - Helvetica Neue & Roboto Mono fonts
  - Custom grayscale theme implementation
- **Backend**:
  - Python core
  - ExifTool for metadata manipulation
  - Faker for data generation
  - SQLite for caching and data storage

## Development Phases

### Phase 1: Foundation & UI Setup
1. **Loading Screen**
   - Immediate display on app launch
   - Progress bar with "META INJECTOR" title
   - Grayscale theme compliance
   - Auto-close on full load

2. **Main Window Setup**
   - Single window architecture
   - Light/dark mode implementation
   - Container-based layout
   - Grid system implementation
   - Drag & drop functionality

3. **Typography Implementation**
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

### Phase 2: Core Features
1. **Image Processing**
   - Batch processing system
   - File validation
   - Progress tracking
   - Error handling

2. **EXIF Metadata System**
   - Field-by-field injection control
   - Randomization options
   - Custom data input
   - Validation system

3. **Location System**
   - Address input functionality
   - Location randomization (Faker integration)
   - Address validation
   - Formatting standardization

4. **Time Management**
   - 12/24hr time input
   - Time randomization
   - Device-date consistency validation
   - Time range selection

5. **Device Simulation**
   - iOS/Android device database
   - Version compatibility checking
   - Carrier information
   - IMEI simulation

6. **Audio Metadata**
   - Audio file support
   - Metadata field controls
   - Format validation
   - Custom data support

### Phase 3: Data Generation & Validation
1. **Randomization Engine**
   - Device-specific constraints
   - Time period validation
   - Location verification
   - Data consistency checks

2. **Caching System**
   - Address caching
   - Device data caching
   - Performance optimization

### Phase 4: Testing & Quality Assurance
1. **Automated Testing**
   - Unit tests
   - Integration tests
   - UI tests
   - Metadata validation tests

2. **Manual Testing**
   - File format compatibility
   - EXIF data accuracy
   - UI/UX testing
   - Performance testing

## UI Style Guide
### Color Scheme
- Grayscale palette (as per GrayScalePalette.png)
- 80% minimum grayscale usage
- Harmonic color integration
- Light/dark mode compatibility

### Layout Guidelines
- Container-based organization
- Consistent spacing
- Grid system for tables
- Clear section separation
- Tooltip integration

### Error Handling
- User-friendly error messages
- Input validation
- Process status indicators
- Recovery procedures

## Performance Considerations
- Efficient data caching
- Optimized batch processing
- Memory management
- Response time optimization

## Documentation
- User guide
- API documentation
- Testing documentation
- Maintenance guide
