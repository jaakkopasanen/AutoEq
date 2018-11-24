# HiFiMAN HE-300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -1.5; 23 -1.9; 25 -2.2; 28 -2.5; 31 -2.7; 34 -3.0; 37 -3.2; 41 -3.3; 45 -3.5; 49 -3.7; 54 -3.0; 60 -1.8; 66 -2.8; 72 -3.8; 79 -4.0; 87 -4.2; 96 -4.5; 106 -4.4; 116 -4.2; 128 -3.7; 141 -3.2; 155 -4.2; 170 -4.3; 187 -3.9; 206 -3.2; 227 -2.6; 249 -2.2; 274 -1.5; 302 -0.7; 332 -0.2; 365 0.5; 402 1.1; 442 1.9; 486 2.6; 535 3.4; 588 4.7; 647 5.3; 712 4.6; 783 5.3; 861 3.7; 947 1.4; 1042 -1.0; 1146 -3.2; 1261 -5.3; 1387 -6.5; 1526 -8.2; 1678 -7.6; 1846 -4.8; 2031 -4.7; 2234 -2.2; 2457 -3.6; 2703 -5.3; 2973 -7.3; 3270 -8.3; 3597 -7.2; 3957 -6.0; 4353 -6.1; 4788 -5.6; 5267 -4.7; 5793 -2.7; 6373 2.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -1.7; 11289 -0.2; 12418 0.0; 13660 -1.0; 15026 -0.7; 16529 0.0; 18182 0.0; 20000 -0.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.34 | -2.5 dB |
| Peaking | 158 Hz  | 0.69 | -3.1 dB |
| Peaking | 700 Hz  | 1.13 | 6.9 dB  |
| Peaking | 1453 Hz | 1.83 | -9.0 dB |
| Peaking | 3552 Hz | 1.7  | -7.7 dB |
| Peaking | 3111 Hz | 8    | -2.0 dB |
| Peaking | 3722 Hz | 3.08 | 2.0 dB  |
| Peaking | 5210 Hz | 2.45 | -3.3 dB |
| Peaking | 6628 Hz | 5.23 | 6.5 dB  |
| Peaking | 9989 Hz | 7.64 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300/HiFiMAN%20HE-300.png)