# AKG K812
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.2; 28 -0.1; 31 -0.4; 34 -0.6; 37 -0.7; 41 -0.9; 45 -1.1; 49 -1.2; 54 -1.4; 60 -1.6; 66 -1.8; 72 -2.0; 79 -2.2; 87 -2.7; 96 -3.1; 106 -3.4; 116 -3.6; 128 -4.1; 141 -4.2; 155 -4.4; 170 -4.3; 187 -4.4; 206 -4.5; 227 -4.4; 249 -4.3; 274 -4.2; 302 -4.1; 332 -4.0; 365 -3.8; 402 -3.6; 442 -3.2; 486 -3.1; 535 -2.8; 588 -2.2; 647 -1.9; 712 -1.6; 783 -0.9; 861 -0.6; 947 -0.3; 1042 0.2; 1146 0.5; 1261 0.7; 1387 0.3; 1526 -0.3; 1678 -0.2; 1846 0.8; 2031 0.9; 2234 0.5; 2457 2.4; 2703 2.3; 2973 -1.4; 3270 -2.5; 3597 -2.5; 3957 -0.3; 4353 2.1; 4788 -0.1; 5267 -4.5; 5793 -8.2; 6373 -5.7; 7010 -0.8; 7711 -2.0; 8482 -3.6; 9330 -3.2; 10263 -0.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -2.1; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 219 Hz   | 0.39 | -4.6 dB |
| Peaking | 1545 Hz  | 1.29 | 3.2 dB  |
| Peaking | 1568 Hz  | 3.53 | -3.2 dB |
| Peaking | 5940 Hz  | 4.92 | -9.2 dB |
| Peaking | 19889 Hz | 2.14 | -7.3 dB |
| Peaking | 18 Hz    | 1.55 | 1.5 dB  |
| Peaking | 2601 Hz  | 7.75 | 4.1 dB  |
| Peaking | 3344 Hz  | 2.59 | -3.4 dB |
| Peaking | 4361 Hz  | 6.09 | 4.2 dB  |
| Peaking | 8867 Hz  | 5.92 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812/AKG%20K812.png)