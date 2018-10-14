# Audio Technica ATH-A2000Z

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 5.2; 25 4.5; 28 3.6; 31 2.9; 34 2.3; 37 1.7; 41 1.1; 45 0.6; 49 0.3; 54 -0.1; 60 -0.4; 66 -0.5; 72 -0.7; 79 -0.8; 87 -1.1; 96 -1.9; 106 -2.5; 116 -2.6; 128 -2.6; 141 -2.6; 155 -2.4; 170 -1.6; 187 -1.8; 206 -1.4; 227 -0.8; 249 -0.4; 274 0.0; 302 0.2; 332 0.2; 365 0.1; 402 -0.1; 442 -0.0; 486 -0.2; 535 -0.2; 588 0.1; 647 0.0; 712 -0.1; 783 0.1; 861 0.3; 947 -0.1; 1042 0.3; 1146 0.2; 1261 0.0; 1387 -0.7; 1526 -2.3; 1678 -3.9; 1846 -4.7; 2031 -5.1; 2234 -4.9; 2457 -2.7; 2703 -0.2; 2973 1.5; 3270 1.4; 3597 -1.7; 3957 -3.4; 4353 -3.2; 4788 0.7; 5267 6.0; 5793 5.7; 6373 5.0; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -4.9; 10263 -3.8; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -4.0; 18182 -2.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A2000Z ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 2.18 | 6.5 dB   |
| Peaking | 2018 Hz  | 2.45 | -6.8 dB  |
| Peaking | 4240 Hz  | 3.22 | -12.5 dB |
| Peaking | 4955 Hz  | 1.17 | 10.0 dB  |
| Peaking | 9529 Hz  | 3.22 | -7.0 dB  |
| Peaking | 33 Hz    | 1.94 | 1.1 dB   |
| Peaking | 130 Hz   | 1.08 | -2.8 dB  |
| Peaking | 303 Hz   | 2.23 | 0.8 dB   |
| Peaking | 3041 Hz  | 8.35 | 1.6 dB   |
| Peaking | 17007 Hz | 3.27 | -4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A2000Z/Audio%20Technica%20ATH-A2000Z.png)