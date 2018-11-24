# Teac CT-H02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.4; 25 0.3; 28 0.2; 31 0.1; 34 0.1; 37 0.0; 41 0.0; 45 0.0; 49 0.0; 54 0.0; 60 -0.1; 66 -0.3; 72 -0.5; 79 -0.7; 87 -0.6; 96 -0.4; 106 -1.1; 116 -1.2; 128 -0.7; 141 0.2; 155 -1.4; 170 -0.6; 187 -1.8; 206 -2.4; 227 -2.6; 249 -2.6; 274 -2.3; 302 -2.2; 332 -2.0; 365 -1.8; 402 -1.4; 442 -1.4; 486 -1.3; 535 -1.5; 588 -1.5; 647 -1.5; 712 -1.3; 783 -1.2; 861 -0.9; 947 -0.3; 1042 0.0; 1146 -0.5; 1261 -0.6; 1387 -0.8; 1526 -1.1; 1678 -0.9; 1846 0.1; 2031 1.7; 2234 2.5; 2457 4.0; 2703 5.3; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.3; 8482 -6.7; 9330 -7.6; 10263 -3.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teac CT-H02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 341 Hz  |  0.48 | -2.2 dB  |
| Peaking | 1447 Hz |  1.97 | -1.9 dB  |
| Peaking | 1756 Hz |  3.07 | -2.2 dB  |
| Peaking | 4651 Hz |  0.51 | 7.5 dB   |
| Peaking | 8943 Hz |  2.84 | -13.1 dB |
| Peaking | 139 Hz  | 10.16 | 1.4 dB   |
| Peaking | 224 Hz  |  5.08 | -0.9 dB  |
| Peaking | 2918 Hz |  3.84 | 1.4 dB   |
| Peaking | 5096 Hz |  0.81 | -1.1 dB  |
| Peaking | 6203 Hz |  3.57 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)