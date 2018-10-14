# Torque t096z Bass Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -11.5; 23 -11.5; 25 -11.4; 28 -11.3; 31 -11.2; 34 -11.1; 37 -11.0; 41 -10.9; 45 -10.7; 49 -10.5; 54 -10.4; 60 -10.2; 66 -10.1; 72 -10.0; 79 -9.9; 87 -9.8; 96 -9.7; 106 -9.4; 116 -9.0; 128 -8.7; 141 -8.4; 155 -8.0; 170 -7.6; 187 -7.0; 206 -6.5; 227 -5.9; 249 -5.3; 274 -4.7; 302 -4.1; 332 -3.5; 365 -2.8; 402 -2.2; 442 -1.5; 486 -1.0; 535 -0.5; 588 0.2; 647 0.6; 712 0.7; 783 1.0; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.8; 1261 -1.6; 1387 -2.8; 1526 -4.2; 1678 -5.6; 1846 -7.0; 2031 -7.5; 2234 -6.4; 2457 -3.1; 2703 -0.0; 2973 3.2; 3270 4.7; 3597 4.4; 3957 1.4; 4353 -1.7; 4788 1.5; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 26 Hz    |  0.23 | -11.2 dB |
| Peaking | 157 Hz   |  0.8  | -4.0 dB  |
| Peaking | 1986 Hz  |  2.34 | -8.5 dB  |
| Peaking | 3234 Hz  |  3.97 | 6.5 dB   |
| Peaking | 5846 Hz  |  3.73 | 7.0 dB   |
| Peaking | 313 Hz   |  1.85 | -0.9 dB  |
| Peaking | 755 Hz   |  1.23 | 1.9 dB   |
| Peaking | 1481 Hz  |  3.9  | -1.4 dB  |
| Peaking | 4376 Hz  | 11.08 | -3.7 dB  |
| Peaking | 21649 Hz |  1.72 | -0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Bass%20Boost%20Filter/Torque%20t096z%20Bass%20Boost%20Filter.png)