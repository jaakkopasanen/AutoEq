# LG Quadbeat HSS-F420

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -1.3; 23 -1.3; 25 -1.4; 28 -1.5; 31 -1.6; 34 -1.7; 37 -1.8; 41 -1.9; 45 -2.1; 49 -2.2; 54 -2.4; 60 -2.7; 66 -3.0; 72 -3.3; 79 -3.6; 87 -4.0; 96 -4.4; 106 -4.7; 116 -4.8; 128 -5.0; 141 -5.2; 155 -5.4; 170 -5.4; 187 -5.3; 206 -5.3; 227 -5.0; 249 -4.9; 274 -4.6; 302 -4.2; 332 -3.9; 365 -3.5; 402 -3.1; 442 -2.5; 486 -2.2; 535 -1.7; 588 -0.9; 647 -0.6; 712 -0.3; 783 0.2; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -0.8; 1526 -1.3; 1678 -1.6; 1846 -1.5; 2031 -1.3; 2234 -1.3; 2457 -1.0; 2703 -0.7; 2973 0.3; 3270 1.7; 3597 2.5; 3957 2.2; 4353 0.8; 4788 0.6; 5267 1.3; 5793 0.9; 6373 0.8; 7010 0.6; 7711 0.0; 8482 -1.0; 9330 -1.3; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.3; 16529 -2.7; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6dB` and instead set Global volume in the UI for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `LG Quadbeat HSS-F420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 119 Hz   | 0.52 | -4.3 dB |
| Peaking | 262 Hz   | 1.02 | -2.5 dB |
| Peaking | 2160 Hz  | 1.68 | -1.9 dB |
| Peaking | 3649 Hz  | 2.4  | 2.9 dB  |
| Peaking | 16117 Hz | 4.41 | -3.4 dB |
| Peaking | 21 Hz    | 1.52 | -0.8 dB |
| Peaking | 842 Hz   | 1.39 | 2.5 dB  |
| Peaking | 842 Hz   | 0.75 | -1.5 dB |
| Peaking | 6305 Hz  | 2.65 | 0.9 dB  |
| Peaking | 8906 Hz  | 4.98 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/LG%20Quadbeat%20HSS-F420/LG%20Quadbeat%20HSS-F420.png)