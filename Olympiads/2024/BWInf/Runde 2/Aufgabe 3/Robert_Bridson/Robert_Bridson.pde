import java.util.ArrayList;
import processing.core.PVector;
import processing.core.PShape;

PShape polygon; // Global variable for the polygon
ArrayList<PVector> plist; // Global variable for the list of points
float RADIUS = 10; // Define the radius for the Poisson Disk Sampling

boolean isPointInPolygon(PVector point, PShape polygon) {
    int numVertices = polygon.getVertexCount();
    boolean inside = false;
    for (int i = 0, j = numVertices - 1; i < numVertices; j = i++) {
        PVector vi = polygon.getVertex(i);
        PVector vj = polygon.getVertex(j);
        boolean intersect = ((vi.y > point.y) != (vj.y > point.y)) &&
                (point.x < (vj.x - vi.x) * (point.y - vi.y) / (vj.y - vi.y) + vi.x);
        if (intersect) {
            inside = !inside;
        }
    }
    return inside;
}

boolean isValidPoint(PVector[][] grid, float cellsize, int gwidth, int gheight, PVector p, float radius) {
    int xindex = floor(p.x / cellsize);
    int yindex = floor(p.y / cellsize);
    int i0 = max(xindex - 1, 0);
    int i1 = min(xindex + 1, gwidth - 1);
    int j0 = max(yindex - 1, 0);
    int j1 = min(yindex + 1, gheight - 1);

    for (int i = i0; i <= i1; i++) {
        for (int j = j0; j <= j1; j++) {
            if (grid[i][j] != null) {
                if (PVector.dist(grid[i][j], p) < radius) {
                    return false;
                }
            }
        }
    }
    return true;
}



void insertPoint(PVector[][] grid, float cellsize, PVector point) {
  int xindex = floor(point.x / cellsize);
  int yindex = floor(point.y / cellsize);
  grid[xindex][yindex] = point;
}

ArrayList<PVector> poissonDiskSampling(float radius, int k) {
    int N = 2;
    ArrayList<PVector> points = new ArrayList<PVector>();
    ArrayList<PVector> active = new ArrayList<PVector>();

    float cellsize = radius / sqrt(N);

    int ncells_width = ceil(width / cellsize);
    int ncells_height = ceil(height / cellsize);

    PVector[][] grid = new PVector[ncells_width][ncells_height];
    for (int i = 0; i < ncells_width; i++) {
        for (int j = 0; j < ncells_height; j++) {
            grid[i][j] = null;
        }
    }

    PVector p0 = new PVector(random(width), random(height));
    while (!isPointInPolygon(p0, polygon)) {
        p0.set(random(width), random(height));
    }

    insertPoint(grid, cellsize, p0);
    points.add(p0);
    active.add(p0);

    while (active.size() > 0) {
        int random_index = int(random(active.size()));
        PVector p = active.get(random_index);
        boolean found = false;

        for (int tries = 0; tries < k; tries++) {
            float theta = random(TWO_PI);
            float new_radius = random(radius, 2 * radius);
            float pnewx = p.x + new_radius * cos(theta);
            float pnewy = p.y + new_radius * sin(theta);
            PVector pnew = new PVector(pnewx, pnewy);

            if (isPointInPolygon(pnew, polygon) && isValidPoint(grid, cellsize, ncells_width, ncells_height, pnew, radius)) {
                points.add(pnew);
                insertPoint(grid, cellsize, pnew);
                active.add(pnew);
                found = true;
                break;
            }
        }

        if (!found) {
            active.remove(random_index);
        }
    }
    return points;
}



void setup() {
    size(200, 250); // Set the size of the window
    background(255); // Set the background color to white

    // Define the coordinates of the polygon
    float[][] polygonCoords = {
        {0, 0}, // Example coordinates, replace with actual ones
        {200, 0}, // Each pair is an {x, y} coordinate
        {200, 250},
        {150, 100}
        // Add as many coordinates as needed
    };

    // Create the polygon from the hardcoded coordinates
    polygon = createShape();
    polygon.beginShape();
    for (float[] coord : polygonCoords) {
        polygon.vertex(coord[0], coord[1]);
    }
    polygon.endShape(CLOSE);

    plist = poissonDiskSampling(RADIUS, 30); // Perform Poisson Disk Sampling
    println("Number of ellipses: " + plist.size()); // Print the number of points
    noLoop(); // No need to continuously loop since we're not animating
}




void draw() {
    fill(0); // Set fill color for points
    stroke(0); // Set stroke color for points
    for (PVector p : plist) {
        ellipse(p.x, p.y, RADIUS, RADIUS); // Draw each point as an ellipse
    }

    // Optionally, draw the polygon boundary for visual reference
    stroke(255, 0, 0); // Set stroke color for the polygon (red)
    noFill(); // Don't fill the polygon
    beginShape();
    for (int i = 0; i < polygon.getVertexCount(); i++) {
        PVector v = polygon.getVertex(i);
        vertex(v.x, v.y);
    }
    endShape(CLOSE);
}
