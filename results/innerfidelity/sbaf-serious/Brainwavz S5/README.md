# Brainwavz S5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 21 -9.1; 23 -9.3; 25 -9.4; 28 -9.5; 31 -9.6; 34 -9.7; 37 -9.7; 41 -9.8; 45 -9.9; 49 -10.0; 54 -10.0; 60 -10.2; 66 -10.3; 72 -10.4; 79 -10.5; 87 -10.7; 96 -10.8; 106 -10.7; 116 -10.6; 128 -10.5; 141 -10.3; 155 -10.1; 170 -9.7; 187 -9.3; 206 -8.9; 227 -8.3; 249 -7.8; 274 -7.2; 302 -6.6; 332 -5.9; 365 -5.2; 402 -4.6; 442 -3.9; 486 -3.4; 535 -2.7; 588 -1.7; 647 -1.1; 712 -0.6; 783 0.0; 861 0.2; 947 0.1; 1042 -0.0; 1146 0.0; 1261 0.3; 1387 -0.2; 1526 -0.1; 1678 -0.1; 1846 0.4; 2031 0.9; 2234 1.3; 2457 2.1; 2703 1.9; 2973 1.6; 3270 0.6; 3597 -1.7; 3957 -4.1; 4353 -7.1; 4788 -9.0; 5267 -11.4; 5793 -10.5; 6373 -6.6; 7010 -3.7; 7711 -4.2; 8482 -7.8; 9330 -8.6; 10263 -2.8; 11289 0.0; 12418 0.0; 13660 -1.8; 15026 -6.1; 16529 -3.9; 18182 -2.3; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.3dB` and instead set Global volume in the UI for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.25 | -9.2 dB  |
| Peaking | 140 Hz   | 0.72 | -5.6 dB  |
| Peaking | 294 Hz   | 1.28 | -3.1 dB  |
| Peaking | 5368 Hz  | 2.79 | -11.2 dB |
| Peaking | 15820 Hz | 0.33 | -3.3 dB  |
| Peaking | 2876 Hz  | 1.47 | 3.4 dB   |
| Peaking | 4250 Hz  | 3.01 | -3.6 dB  |
| Peaking | 9140 Hz  | 3.36 | -10.9 dB |
| Peaking | 11484 Hz | 0.91 | 6.5 dB   |
| Peaking | 14988 Hz | 2.79 | -6.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S5/Brainwavz%20S5.png)