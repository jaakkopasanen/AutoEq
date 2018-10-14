# Audeze EL8 Closed

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.2; 25 2.1; 28 2.1; 31 2.1; 34 2.2; 37 2.3; 41 2.3; 45 2.3; 49 2.8; 54 3.0; 60 1.8; 66 0.8; 72 0.4; 79 0.1; 87 -0.3; 96 -0.8; 106 -1.0; 116 -0.8; 128 -0.5; 141 0.3; 155 1.1; 170 1.5; 187 1.9; 206 2.6; 227 3.2; 249 3.4; 274 3.6; 302 3.4; 332 3.3; 365 3.2; 402 2.9; 442 2.7; 486 2.4; 535 2.2; 588 2.2; 647 1.8; 712 1.2; 783 0.9; 861 0.5; 947 0.2; 1042 0.0; 1146 -0.0; 1261 -0.5; 1387 -1.1; 1526 -1.8; 1678 -2.5; 1846 -2.5; 2031 -1.9; 2234 -1.2; 2457 -0.2; 2703 0.0; 2973 -0.6; 3270 -1.2; 3597 -1.6; 3957 -1.4; 4353 -2.6; 4788 -4.5; 5267 1.8; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -2.8; 16529 -1.5; 18182 -0.0; 20000 -3.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 1.01 | 4.0 dB  |
| Peaking | 351 Hz   | 0.58 | 5.7 dB  |
| Peaking | 936 Hz   | 0.03 | -2.2 dB |
| Peaking | 4825 Hz  | 4.19 | -9.1 dB |
| Peaking | 5662 Hz  | 2.1  | 10.7 dB |
| Peaking | 112 Hz   | 3.32 | -1.2 dB |
| Peaking | 217 Hz   | 2.96 | 0.8 dB  |
| Peaking | 1775 Hz  | 4.52 | -1.5 dB |
| Peaking | 2588 Hz  | 5.95 | 1.7 dB  |
| Peaking | 11984 Hz | 3.66 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Closed/Audeze%20EL8%20Closed.png)