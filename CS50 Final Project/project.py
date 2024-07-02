from math import tan, cos, atan, sqrt, pow, pi, inf
from matplotlib.pyplot import plot, savefig, xticks, yticks, figure, arrow, text
from matplotlib.patches import Arc
import numpy as np
import sys

def main(dx_target, dy_target, v_initial, dy_initial):
    traj_angle = trajectory_angle(dx_target, v_initial, dy_initial, dy_target)
    Zeros = inverse_trajectory_function(traj_angle[0], 0, v_initial, dy_initial)
    Zeros2 = inverse_trajectory_function(traj_angle[1], 0, v_initial, dy_initial)
    if dy_target <= dy_initial and (dx_target < ((Zeros[0] + Zeros[1])/2) or dx_target < ((Zeros2[0] + Zeros2[1])/2)):
        sys.exit("Invalid target position. Target should require projectile to be thrown at a positive angle in both possible cases.")

    points = get_plotting_points(traj_angle[0], v_initial, dy_initial, trajectory_function)
    points2 = get_plotting_points(traj_angle[1], v_initial, dy_initial, trajectory_function)
    xlen, ylen = abs(int(round(sorted(points[0] + points2[0], reverse=True)[0]))), abs(int(round(sorted(points[1] + points2[1], reverse=True)[0])))
    pl = figure(figsize=(xlen, ylen))
    ax = pl.add_subplot(1,1,1)
    arc = Arc(xy=(0, dy_initial), width=1.8*0.25*xlen, height=1.8*0.25*xlen, angle=0, theta1=0, theta2=traj_angle[0]*(180/pi), color='red', lw=1)
    arc2 = Arc(xy=(0, dy_initial), width=1.7*0.2*xlen, height=1.8*0.2*xlen, angle=0, theta1=0, theta2=traj_angle[1]*(180/pi), color='blue', lw=1)
    ax.add_patch(arc2)
    ax.add_patch(arc)
    plot(points[0], points[1])
    plot(points2[0], points2[1])
    vectPoints = get_plotting_points(traj_angle[0], v_initial, dy_initial, trajectory_derivative, 0.25*xlen)
    # print(vectPoints[0][0], vectPoints[1][0], 0.25*xlen)
    # print(vectPoints[0][-1] - vectPoints[0][0], vectPoints[1][-1] - vectPoints[1][0])
    arrow(vectPoints[0][0], vectPoints[1][0], vectPoints[0][-1] - vectPoints[0][0], vectPoints[1][-1] - vectPoints[1][0], width=xlen/192, head_width=xlen/48, head_length=xlen/48, color="red", zorder=100)
    text(vectPoints[0][-1], vectPoints[1][-1] - 0.025*xlen - (traj_angle[0]/(pi/2))*0.1*xlen, f"θ = {round(traj_angle[0]*(180/pi), 2)}°", fontsize=xlen, zorder=101)
    vectPoints2 = get_plotting_points(traj_angle[1], v_initial, dy_initial, trajectory_derivative, 0.2*xlen)
    arrow(vectPoints2[0][0], vectPoints2[1][0], vectPoints2[0][-1] - vectPoints2[0][0], vectPoints2[1][-1] - vectPoints2[1][0], width=xlen/192, head_width=xlen/48, head_length=xlen/48, color="blue", zorder=100)
    text(vectPoints2[0][-1], vectPoints2[1][-1] - 0.025*xlen - (traj_angle[1]/(pi/2))*0.1*xlen, f"θ = {round(traj_angle[1]*(180/pi), 2)}°", fontsize=xlen, zorder=101)
    # print(vectPoints2[0][0], vectPoints2[1][0], 0.2*xlen)
    # print(vectPoints2[0][-1] - vectPoints2[0][0], vectPoints2[1][-1] - vectPoints2[1][0])
    # plot(vectPoints[0], vectPoints[1])
    # plot(vectPoints2[0], vectPoints2[1])
    # plot([trajectory_derivative_inverse(traj_angle[0], 0, dy_initial, v_initial, dy_initial), trajectory_derivative_inverse(traj_angle[0], 0, 1, v_initial, dy_initial)], [dy_initial, 1])
    # plot([trajectory_derivative_inverse(traj_angle[1], 0, dy_initial, v_initial, dy_initial), trajectory_derivative_inverse(traj_angle[1], 0, 2, v_initial, dy_initial)], [dy_initial, 2])
    # plot([0, 1], [trajectory_derivative_inverse(traj_angle[0], 0, 0, v_initial, dy_initial), trajectory_derivative_inverse(traj_angle[0], 0, 5, v_initial, dy_initial)])
    # plot( [0, 2], [trajectory_derivative_inverse(traj_angle[1], 0, 0, v_initial, dy_initial), trajectory_derivative_inverse(traj_angle[1], 0, 3, v_initial, dy_initial)])
    # arc = Arc(((0, dy_initial), 10.0, 10.0, traj_angle))
    xticks(np.arange(0, sorted(points[0] + points2[0], reverse=True)[0], step=1), np.arange(0, sorted(points[0] + points2[0], reverse=True)[0], step=1))
    if dy_initial >= 0:
        yticks(np.arange(0, sorted(points[1] + points2[1], reverse=True)[0], step=1), np.arange(0, sorted(points[1] + points2[1], reverse=True)[0], step=1))
    else:
        yticks(np.arange(dy_initial, sorted(points[1] + points2[1], reverse=True)[0], step=1), np.arange(0, sorted(points[1] + points2[1], reverse=True)[0], step=1))
    savefig("plot.pdf")


def get_plotting_points(trajectory_angle, v0, d0y, func, max=inf):
    xcoords = []
    ycoords = []
    dy = d0y
    dx = 0
    while (dy >= 0 or 0 > dy >= d0y) and (dy <= max and dx <= max):
        dy = func(trajectory_angle, dx=dx, v0=v0, d0y=d0y)
        if dy < d0y < 0 or dy < 0 < d0y:
            break
        xcoords.append(dx)
        ycoords.append(dy)
        dx += 0.01
    return xcoords, ycoords

def trajectory_function(trajectory_angle, dx, v0, d0y, g=-9.8):
    dy = (g*pow(dx, 2))/(2*pow(v0, 2)*pow(cos(trajectory_angle), 2)) + tan(trajectory_angle)*dx + d0y
    return dy

def trajectory_derivative(trajectory_angle, dx, v0, d0y, g=-9.8, dxP=0, ):
    α = g/((2*pow(v0, 2))*pow(cos(trajectory_angle), 2))
    β = tan(trajectory_angle)
    # return (dy - d0y + pow(dxP, 2))/(2*α*dxP + β)
    return (2*α*dxP + β)*dx + d0y - pow(dxP, 2)

def inverse_trajectory_function(trajectory_angle, dy, v0, d0y, g=-9.8):
    return (-tan(trajectory_angle) + sqrt(pow(tan(trajectory_angle), 2) - 4*(g/((2*pow(v0, 2))*pow(cos(trajectory_angle), 2)))*(d0y - dy)))/(2*(g/((2*pow(v0, 2))*pow(cos(trajectory_angle), 2)))), (-tan(trajectory_angle) - sqrt(pow(tan(trajectory_angle), 2) - 4*(g/((2*pow(v0, 2))*pow(cos(trajectory_angle), 2)))*(d0y - dy)))/(2*(g/((2*pow(v0, 2))*pow(cos(trajectory_angle), 2))))

def trajectory_angle(dx, v0, d0y, dy, g=-9.8):
    try:
        α = (g*pow(dx, 2))/(2*pow(v0, 2))
    except ZeroDivisionError:
        raise ZeroDivisionError("initial velocity = 0 m/s ⇒ Projectile is stationary and will never reach its target")
    β = dx
    γ = α + d0y - dy
    try:
        tanθ = ((-β + sqrt(pow(β, 2) - 4*α*γ))/(2*α), (-β - sqrt(pow(β, 2) - 4*α*γ))/(2*α))
        return (atan(tanθ[0]), atan(tanθ[1]))
    except ValueError:
        raise ValueError("Target is too far and cannot be reached by projectile at any angle")
    except ZeroDivisionError:
        raise ZeroDivisionError("Target is right under or above the projectile")


if __name__ == "__main__":
    main(float(input("horizontal distance of target point in meters: ")), float(input("vertical distance of target point in meters: ")), float(input("initial velocity in meters/second: ")), float(input("initial vertical distance (height) in meters: ")))
