# Velodyne vPulse

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -13.0; 23 -12.6; 25 -12.2; 28 -11.7; 31 -11.2; 34 -10.7; 37 -10.3; 41 -9.8; 45 -9.3; 49 -8.9; 54 -8.4; 60 -8.0; 66 -7.7; 72 -7.4; 79 -7.1; 87 -6.8; 96 -6.6; 106 -6.2; 116 -5.9; 128 -5.6; 141 -5.3; 155 -4.9; 170 -4.5; 187 -4.1; 206 -3.8; 227 -3.3; 249 -2.9; 274 -2.4; 302 -2.0; 332 -1.6; 365 -1.2; 402 -0.8; 442 -0.4; 486 -0.2; 535 0.1; 588 0.8; 647 0.9; 712 0.6; 783 0.8; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.7; 1526 -2.4; 1678 -3.0; 1846 -3.2; 2031 -3.2; 2234 -3.3; 2457 -3.0; 2703 -3.2; 2973 -3.0; 3270 -2.6; 3597 -2.3; 3957 -2.6; 4353 -2.6; 4788 -0.8; 5267 2.3; 5793 5.2; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Velodyne vPulse ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 15 Hz   | 0.22 | -13.1 dB |
| Peaking | 144 Hz  | 0.88 | -2.8 dB  |
| Peaking | 1985 Hz | 1.95 | -2.8 dB  |
| Peaking | 4556 Hz | 0.96 | -4.1 dB  |
| Peaking | 5973 Hz | 2.79 | 9.4 dB   |
| Peaking | 270 Hz  | 2.72 | -0.5 dB  |
| Peaking | 606 Hz  | 4.29 | 0.6 dB   |
| Peaking | 753 Hz  | 1.37 | 1.2 dB   |
| Peaking | 1501 Hz | 3.97 | -0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Velodyne%20vPulse/Velodyne%20vPulse.png)