# Grado RS1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.6; 45 4.6; 49 3.7; 54 2.5; 60 1.1; 66 -0.1; 72 -1.2; 79 -2.1; 87 -2.7; 96 -3.2; 106 -3.6; 116 -3.8; 128 -3.8; 141 -3.6; 155 -3.4; 170 -3.0; 187 -2.8; 206 -2.7; 227 -2.4; 249 -2.0; 274 -1.5; 302 -0.5; 332 -0.8; 365 -1.6; 402 -1.2; 442 -0.9; 486 -0.6; 535 -0.4; 588 -0.2; 647 0.1; 712 0.2; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.5; 1526 -2.5; 1678 -4.8; 1846 -9.2; 2031 -8.3; 2234 -7.3; 2457 -6.2; 2703 -4.6; 2973 -2.6; 3270 -0.8; 3597 0.5; 3957 -0.9; 4353 -8.3; 4788 -13.8; 5267 -9.4; 5793 -9.0; 6373 -3.6; 7010 0.0; 7711 -3.3; 8482 -9.6; 9330 -12.9; 10263 -10.1; 11289 -4.5; 12418 -2.7; 13660 -4.7; 15026 -4.0; 16529 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.53 | 8.1 dB   |
| Peaking | 98 Hz    | 0.64 | -6.5 dB  |
| Peaking | 2013 Hz  | 2.83 | -9.3 dB  |
| Peaking | 4885 Hz  | 4.64 | -13.4 dB |
| Peaking | 9483 Hz  | 2.72 | -13.2 dB |
| Peaking | 2581 Hz  | 6.33 | -2.1 dB  |
| Peaking | 3651 Hz  | 6.31 | 4.2 dB   |
| Peaking | 5786 Hz  | 7.57 | -4.5 dB  |
| Peaking | 6978 Hz  | 6.41 | 4.9 dB   |
| Peaking | 14332 Hz | 3.65 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS1/Grado%20RS1.png)