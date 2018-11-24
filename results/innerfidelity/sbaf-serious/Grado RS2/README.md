# Grado RS2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.8; 54 4.7; 60 3.4; 66 2.5; 72 1.6; 79 0.5; 87 -0.4; 96 -1.2; 106 -1.6; 116 -1.8; 128 -2.0; 141 -2.0; 155 -1.8; 170 -1.6; 187 -1.3; 206 -1.4; 227 -1.3; 249 -1.1; 274 -0.7; 302 -0.4; 332 -0.2; 365 -0.5; 402 -0.2; 442 0.1; 486 -0.1; 535 -0.0; 588 0.3; 647 0.5; 712 0.3; 783 0.5; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.9; 1387 -2.0; 1526 -3.5; 1678 -4.1; 1846 -6.0; 2031 -9.2; 2234 -7.0; 2457 -5.3; 2703 -4.4; 2973 -2.2; 3270 -1.2; 3597 -0.8; 3957 -5.1; 4353 -8.1; 4788 -9.0; 5267 -6.2; 5793 -6.4; 6373 -7.8; 7010 -9.4; 7711 -9.4; 8482 -10.7; 9330 -10.8; 10263 -4.5; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.8; 18182 -1.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 44 Hz    |  0.35 | 8.2 dB   |
| Peaking | 105 Hz   |  0.71 | -7.0 dB  |
| Peaking | 2052 Hz  |  2.91 | -8.6 dB  |
| Peaking | 4645 Hz  |  3.88 | -7.6 dB  |
| Peaking | 8095 Hz  |  1.91 | -11.2 dB |
| Peaking | 3481 Hz  | 10.74 | 2.4 dB   |
| Peaking | 6460 Hz  |  3.47 | -2.9 dB  |
| Peaking | 9456 Hz  |  4.52 | -8.9 dB  |
| Peaking | 9873 Hz  |  1.38 | 5.7 dB   |
| Peaking | 17807 Hz |  3.02 | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS2/Grado%20RS2.png)