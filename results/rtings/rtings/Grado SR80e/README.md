# Grado SR80e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.3; 37 4.6; 41 3.7; 45 2.9; 49 2.3; 54 1.6; 60 0.9; 66 0.3; 72 -0.1; 79 -0.5; 87 -0.8; 96 -1.1; 106 -1.4; 116 -1.5; 128 -1.6; 141 -1.6; 155 -1.6; 170 -1.5; 187 -1.5; 206 -1.3; 227 -1.1; 249 -0.9; 274 -0.9; 302 -1.0; 332 -1.1; 365 -1.0; 402 -1.1; 442 -1.1; 486 -1.1; 535 -1.1; 588 -0.9; 647 -0.7; 712 -0.4; 783 -0.2; 861 0.0; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.4; 1387 -0.9; 1526 -1.6; 1678 -2.9; 1846 -6.8; 2031 -9.3; 2234 -8.1; 2457 -6.3; 2703 -4.6; 2973 -3.0; 3270 -2.3; 3597 -2.7; 3957 -4.3; 4353 -2.1; 4788 1.0; 5267 0.4; 5793 -0.5; 6373 -4.0; 7010 -6.5; 7711 -5.5; 8482 -7.6; 9330 -10.1; 10263 -6.4; 11289 -0.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.65 | 7.5 dB  |
| Peaking | 88 Hz    | 0.35 | -2.5 dB |
| Peaking | 2060 Hz  | 3.7  | -8.5 dB |
| Peaking | 2745 Hz  | 1.65 | -2.6 dB |
| Peaking | 8958 Hz  | 2.53 | -9.9 dB |
| Peaking | 1123 Hz  | 2.66 | 0.8 dB  |
| Peaking | 4093 Hz  | 5.47 | -5.1 dB |
| Peaking | 4804 Hz  | 2.22 | 3.5 dB  |
| Peaking | 6774 Hz  | 6.75 | -4.6 dB |
| Peaking | 12058 Hz | 4.59 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Grado%20SR80e/Grado%20SR80e.png)