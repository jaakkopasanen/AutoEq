# Grado SR225i Small Flat Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.2; 49 4.1; 54 2.9; 60 1.7; 66 0.8; 72 0.1; 79 -0.5; 87 -0.9; 96 -1.3; 106 -1.4; 116 -1.6; 128 -1.9; 141 -1.9; 155 -2.0; 170 -2.0; 187 -2.0; 206 -1.9; 227 -1.7; 249 -1.6; 274 -1.2; 302 -1.3; 332 -1.3; 365 -1.0; 402 -0.9; 442 -0.7; 486 -0.7; 535 -0.5; 588 -0.1; 647 0.0; 712 0.0; 783 0.2; 861 0.1; 947 0.1; 1042 0.1; 1146 0.1; 1261 -0.1; 1387 -0.7; 1526 -1.2; 1678 -1.3; 1846 -1.9; 2031 -5.3; 2234 -4.7; 2457 -1.1; 2703 1.6; 2973 2.9; 3270 4.1; 3597 3.1; 3957 4.7; 4353 6.0; 4788 5.9; 5267 4.9; 5793 5.9; 6373 4.3; 7010 0.5; 7711 -0.8; 8482 -1.4; 9330 -0.7; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Small Flat Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Small Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.56 | 9.3 dB  |
| Peaking | 81 Hz    | 0.4  | -4.6 dB |
| Peaking | 2130 Hz  | 3.74 | -7.6 dB |
| Peaking | 5424 Hz  | 0.82 | 8.1 dB  |
| Peaking | 7861 Hz  | 1.54 | -6.3 dB |
| Peaking | 73 Hz    | 3.65 | -0.4 dB |
| Peaking | 1505 Hz  | 6.81 | -1.1 dB |
| Peaking | 2934 Hz  | 5.5  | 0.9 dB  |
| Peaking | 10744 Hz | 1    | 0.5 dB  |
| Peaking | 12706 Hz | 1.01 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Small%20Flat%20Pads/Grado%20SR225i%20Small%20Flat%20Pads.png)