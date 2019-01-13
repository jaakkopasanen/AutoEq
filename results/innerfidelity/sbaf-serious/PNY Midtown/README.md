# PNY Midtown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.4; 23 -10.4; 25 -10.3; 28 -10.3; 31 -10.3; 34 -10.3; 37 -10.2; 41 -10.2; 45 -10.2; 49 -10.2; 54 -10.1; 60 -10.1; 66 -10.2; 72 -10.2; 79 -10.3; 87 -10.3; 96 -10.3; 106 -10.2; 116 -10.0; 128 -9.9; 141 -9.6; 155 -9.3; 170 -9.0; 187 -8.5; 206 -8.1; 227 -7.5; 249 -7.0; 274 -6.4; 302 -5.9; 332 -5.2; 365 -4.5; 402 -3.9; 442 -3.2; 486 -2.6; 535 -2.1; 588 -1.2; 647 -0.8; 712 -0.4; 783 0.2; 861 0.2; 947 -0.2; 1042 0.3; 1146 0.4; 1261 -0.0; 1387 -0.7; 1526 -1.5; 1678 -2.4; 1846 -3.8; 2031 -4.5; 2234 -4.3; 2457 -3.6; 2703 -1.5; 2973 1.7; 3270 4.6; 3597 6.0; 3957 5.4; 4353 3.0; 4788 1.7; 5267 -0.3; 5793 -4.7; 6373 -8.2; 7010 -2.7; 7711 0.2; 8482 0.0; 9330 -0.6; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PNY Midtown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Midtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  0.18 | -10.1 dB |
| Peaking | 180 Hz  |  0.66 | -4.5 dB  |
| Peaking | 2235 Hz |  2.26 | -6.1 dB  |
| Peaking | 3630 Hz |  2.14 | 7.4 dB   |
| Peaking | 6220 Hz |  5.77 | -9.9 dB  |
| Peaking | 382 Hz  |  1.82 | -0.8 dB  |
| Peaking | 910 Hz  |  1    | 1.3 dB   |
| Peaking | 1758 Hz |  4.21 | -1.3 dB  |
| Peaking | 7612 Hz | 10.96 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Midtown/PNY%20Midtown.png)