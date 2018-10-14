# AKG Q350 Quincy Jones

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -6.1; 23 -6.5; 25 -6.8; 28 -7.3; 31 -7.6; 34 -7.9; 37 -8.2; 41 -8.5; 45 -8.7; 49 -9.0; 54 -9.2; 60 -9.5; 66 -9.8; 72 -10.1; 79 -10.3; 87 -10.6; 96 -10.8; 106 -10.9; 116 -10.8; 128 -10.9; 141 -10.9; 155 -10.7; 170 -10.5; 187 -10.1; 206 -9.8; 227 -9.3; 249 -8.9; 274 -8.3; 302 -7.7; 332 -7.1; 365 -6.4; 402 -5.7; 442 -4.8; 486 -4.3; 535 -3.5; 588 -2.5; 647 -1.8; 712 -1.3; 783 -0.6; 861 -0.3; 947 -0.1; 1042 0.0; 1146 0.3; 1261 0.5; 1387 0.5; 1526 0.2; 1678 0.1; 1846 0.6; 2031 1.2; 2234 1.7; 2457 2.5; 2703 2.3; 2973 2.2; 3270 1.1; 3597 -2.1; 3957 -3.6; 4353 -5.4; 4788 -7.3; 5267 -9.6; 5793 -12.4; 6373 -8.0; 7010 -4.1; 7711 -3.1; 8482 -5.4; 9330 -7.4; 10263 -4.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -3.3; 16529 -1.9; 18182 0.0; 20000 -1.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.7dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q350 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.33 | -8.1 dB  |
| Peaking | 157 Hz   | 0.75 | -5.9 dB  |
| Peaking | 327 Hz   | 1.34 | -3.5 dB  |
| Peaking | 5719 Hz  | 2.41 | -12.1 dB |
| Peaking | 15712 Hz | 4.37 | -4.0 dB  |
| Peaking | 3076 Hz  | 1.3  | 5.5 dB   |
| Peaking | 3912 Hz  | 1.98 | -4.7 dB  |
| Peaking | 7270 Hz  | 3.92 | 2.7 dB   |
| Peaking | 9422 Hz  | 3    | -8.1 dB  |
| Peaking | 11126 Hz | 2.31 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q350%20Quincy%20Jones/AKG%20Q350%20Quincy%20Jones.png)