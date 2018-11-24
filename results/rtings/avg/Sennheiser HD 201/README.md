# Sennheiser HD 201

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.7; 87 5.3; 96 5.1; 106 4.8; 116 4.5; 128 4.3; 141 4.1; 155 4.1; 170 4.1; 187 4.1; 206 4.1; 227 4.3; 249 4.5; 274 4.6; 302 3.1; 332 2.4; 365 1.9; 402 1.2; 442 0.6; 486 0.2; 535 0.1; 588 0.4; 647 0.8; 712 0.8; 783 0.5; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 0.1; 1387 -0.2; 1526 -1.4; 1678 1.9; 1846 -0.6; 2031 -1.3; 2234 -0.8; 2457 0.7; 2703 1.7; 2973 1.3; 3270 0.0; 3597 -0.2; 3957 2.1; 4353 6.0; 4788 6.0; 5267 1.8; 5793 4.7; 6373 2.9; 7010 1.1; 7711 -0.1; 8482 -0.5; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.2  | 6.2 dB  |
| Peaking | 262 Hz  | 1.56 | 3.5 dB  |
| Peaking | 441 Hz  | 0.38 | -1.6 dB |
| Peaking | 726 Hz  | 1.92 | 1.5 dB  |
| Peaking | 4734 Hz | 2.74 | 6.1 dB  |
| Peaking | 2102 Hz | 5.99 | -2.3 dB |
| Peaking | 3604 Hz | 3.54 | -6.5 dB |
| Peaking | 4114 Hz | 1.27 | 7.7 dB  |
| Peaking | 5492 Hz | 1.68 | -8.9 dB |
| Peaking | 6000 Hz | 4.18 | 7.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)