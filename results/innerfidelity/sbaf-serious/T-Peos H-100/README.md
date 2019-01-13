# T-Peos H-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -6.6; 23 -6.3; 25 -6.0; 28 -5.6; 31 -5.3; 34 -4.9; 37 -4.5; 41 -4.1; 45 -3.8; 49 -3.4; 54 -3.1; 60 -2.7; 66 -2.6; 72 -2.3; 79 -2.2; 87 -2.1; 96 -2.0; 106 -1.8; 116 -1.5; 128 -1.4; 141 -1.3; 155 -1.0; 170 -0.8; 187 -0.6; 206 -0.3; 227 0.0; 249 0.2; 274 0.5; 302 0.7; 332 1.0; 365 1.2; 402 1.4; 442 1.7; 486 1.7; 535 1.8; 588 2.0; 647 2.0; 712 1.8; 783 1.8; 861 1.2; 947 0.6; 1042 -0.3; 1146 -1.2; 1261 -2.1; 1387 -3.5; 1526 -4.7; 1678 -6.0; 1846 -7.4; 2031 -8.5; 2234 -9.1; 2457 -8.0; 2703 -6.9; 2973 -5.7; 3270 -5.4; 3597 -0.6; 3957 3.5; 4353 3.0; 4788 2.4; 5267 4.3; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.3; 9330 -6.4; 10263 -9.6; 11289 -7.4; 12418 -3.2; 13660 -0.5; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos H-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos H-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.24 | -7.1 dB  |
| Peaking | 2287 Hz  | 1.52 | -9.8 dB  |
| Peaking | 4031 Hz  | 6.59 | 5.1 dB   |
| Peaking | 5985 Hz  | 2.22 | 7.6 dB   |
| Peaking | 10354 Hz | 2.87 | -10.9 dB |
| Peaking | 658 Hz   | 0.87 | 2.8 dB   |
| Peaking | 1650 Hz  | 1.49 | -2.7 dB  |
| Peaking | 2416 Hz  | 1.24 | 1.7 dB   |
| Peaking | 3233 Hz  | 6.81 | -3.1 dB  |
| Peaking | 14291 Hz | 4.59 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20H-100/T-Peos%20H-100.png)