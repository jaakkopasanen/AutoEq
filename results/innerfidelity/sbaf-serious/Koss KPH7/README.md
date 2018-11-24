# Koss KPH7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 5.1; 141 2.9; 155 1.0; 170 -1.1; 187 -2.7; 206 -4.5; 227 -5.3; 249 -5.9; 274 -5.8; 302 -4.9; 332 -3.7; 365 -3.5; 402 -2.2; 442 -0.8; 486 2.3; 535 -2.2; 588 -0.6; 647 1.1; 712 -1.4; 783 -0.6; 861 -0.2; 947 -0.0; 1042 0.1; 1146 0.2; 1261 -0.2; 1387 -0.8; 1526 -2.1; 1678 -2.5; 1846 -3.1; 2031 -4.5; 2234 -6.9; 2457 -8.0; 2703 -5.8; 2973 -3.0; 3270 -0.3; 3597 0.8; 3957 2.4; 4353 5.7; 4788 3.3; 5267 4.1; 5793 5.7; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.9; 9330 -4.1; 10263 -1.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KPH7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KPH7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 78 Hz   |  0.24 | 7.7 dB   |
| Peaking | 244 Hz  |  1.15 | -11.7 dB |
| Peaking | 2434 Hz |  2.04 | -9.8 dB  |
| Peaking | 5585 Hz |  0.82 | 6.7 dB   |
| Peaking | 8924 Hz |  2.6  | -7.5 dB  |
| Peaking | 16 Hz   |  0.66 | 2.5 dB   |
| Peaking | 112 Hz  |  0.3  | -3.0 dB  |
| Peaking | 150 Hz  |  0.89 | 6.5 dB   |
| Peaking | 167 Hz  |  2.27 | -4.5 dB  |
| Peaking | 480 Hz  | 14.85 | 4.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20KPH7/Koss%20KPH7.png)