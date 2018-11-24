# Sennheiser HD 598

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.2; 41 4.4; 45 3.7; 49 3.1; 54 2.4; 60 1.6; 66 0.9; 72 0.3; 79 -0.3; 87 -0.9; 96 -1.5; 106 -2.1; 116 -2.6; 128 -3.0; 141 -3.3; 155 -3.6; 170 -3.6; 187 -3.6; 206 -3.4; 227 -3.1; 249 -2.9; 274 -2.8; 302 -2.6; 332 -2.4; 365 -2.2; 402 -1.9; 442 -1.8; 486 -1.9; 535 -1.6; 588 -0.8; 647 -0.7; 712 -0.5; 783 -0.4; 861 -0.2; 947 -0.0; 1042 0.1; 1146 0.2; 1261 0.1; 1387 -0.1; 1526 0.0; 1678 0.1; 1846 -0.2; 2031 -0.8; 2234 -1.2; 2457 -1.0; 2703 -0.9; 2973 -0.7; 3270 -1.5; 3597 -1.8; 3957 -2.1; 4353 -3.3; 4788 -0.8; 5267 1.6; 5793 1.1; 6373 1.0; 7010 2.0; 7711 0.3; 8482 -2.1; 9330 -4.9; 10263 -1.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.0; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.55 | 6.6 dB  |
| Peaking | 159 Hz  |  0.51 | -4.1 dB |
| Peaking | 4317 Hz |  1.74 | -6.0 dB |
| Peaking | 5360 Hz |  1.39 | 4.9 dB  |
| Peaking | 9286 Hz |  5.64 | -6.0 dB |
| Peaking | 489 Hz  |  5.41 | -0.8 dB |
| Peaking | 2343 Hz |  1.73 | -2.0 dB |
| Peaking | 2425 Hz |  0.56 | 1.3 dB  |
| Peaking | 4355 Hz | 10.15 | -1.4 dB |
| Peaking | 6094 Hz | 10.86 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)