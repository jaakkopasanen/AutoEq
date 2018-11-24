# Teac CT-H02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.1; 25 1.9; 28 1.7; 31 1.6; 34 1.6; 37 1.6; 41 1.6; 45 1.6; 49 1.6; 54 1.5; 60 1.4; 66 1.3; 72 1.2; 79 0.9; 87 0.8; 96 0.7; 106 0.4; 116 0.0; 128 0.2; 141 0.7; 155 -0.1; 170 0.2; 187 -0.4; 206 -1.2; 227 -1.6; 249 -1.5; 274 -1.3; 302 -1.5; 332 -1.5; 365 -1.4; 402 -1.4; 442 -1.3; 486 -1.4; 535 -1.4; 588 -1.2; 647 -1.3; 712 -1.0; 783 -0.6; 861 -0.7; 947 -0.2; 1042 -0.2; 1146 -0.4; 1261 -0.2; 1387 -0.2; 1526 -0.3; 1678 -0.4; 1846 0.3; 2031 1.5; 2234 2.4; 2457 4.4; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 5.2; 4788 6.0; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.4; 8482 -5.6; 9330 -6.3; 10263 -2.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teac CT-H02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 19 Hz   |  0.13 | 1.9 dB   |
| Peaking | 369 Hz  |  0.34 | -1.7 dB  |
| Peaking | 3004 Hz |  2.09 | 4.6 dB   |
| Peaking | 5947 Hz |  0.96 | 7.2 dB   |
| Peaking | 8796 Hz |  2.61 | -11.0 dB |
| Peaking | 180 Hz  |  2.88 | 1.7 dB   |
| Peaking | 202 Hz  |  2.26 | -1.5 dB  |
| Peaking | 1538 Hz |  0.74 | 0.8 dB   |
| Peaking | 1681 Hz |  2.48 | -1.8 dB  |
| Peaking | 5352 Hz | 12.64 | -0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)