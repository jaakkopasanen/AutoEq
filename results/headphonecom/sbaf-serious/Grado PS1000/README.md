# Grado PS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.1; 37 4.2; 41 2.8; 45 1.7; 49 0.7; 54 -0.6; 60 -1.9; 66 -3.0; 72 -3.9; 79 -4.6; 87 -5.1; 96 -5.3; 106 -5.3; 116 -5.1; 128 -4.7; 141 -4.2; 155 -3.8; 170 -3.3; 187 -2.7; 206 -2.3; 227 -1.8; 249 -1.6; 274 -1.3; 302 -0.8; 332 -0.2; 365 0.4; 402 -0.0; 442 0.0; 486 0.1; 535 0.3; 588 0.5; 647 0.5; 712 0.6; 783 0.5; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.4; 1526 -2.4; 1678 -2.2; 1846 -1.3; 2031 -1.1; 2234 -1.0; 2457 -1.0; 2703 -1.1; 2973 -1.2; 3270 -0.7; 3597 -1.0; 3957 -8.2; 4353 -7.2; 4788 -6.5; 5267 -7.6; 5793 -8.3; 6373 -12.1; 7010 -10.8; 7711 -9.4; 8482 -8.7; 9330 -7.8; 10263 -4.8; 11289 -0.6; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 27 Hz    |  0.84 | 7.3 dB   |
| Peaking | 95 Hz    |  0.82 | -6.5 dB  |
| Peaking | 1579 Hz  |  5.29 | -2.4 dB  |
| Peaking | 4142 Hz  |  6.78 | -5.5 dB  |
| Peaking | 6912 Hz  |  1.5  | -11.9 dB |
| Peaking | 613 Hz   |  1.22 | 0.9 dB   |
| Peaking | 3441 Hz  | 10.15 | 3.3 dB   |
| Peaking | 7598 Hz  |  3.46 | 4.0 dB   |
| Peaking | 9412 Hz  |  1.33 | -6.6 dB  |
| Peaking | 11437 Hz |  1.53 | 5.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)