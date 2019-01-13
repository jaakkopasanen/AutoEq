# Denon AH-D5000 B2012
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 0.0; 23 -0.4; 25 -1.0; 28 -1.6; 31 -1.9; 34 -2.1; 37 -2.2; 41 -2.3; 45 -2.4; 49 -2.3; 54 -2.3; 60 -2.5; 66 -2.5; 72 -2.3; 79 -2.3; 87 -2.8; 96 -3.2; 106 -3.4; 116 -3.5; 128 -3.6; 141 -3.8; 155 -3.9; 170 -3.7; 187 -3.8; 206 -3.7; 227 -3.5; 249 -3.4; 274 -3.1; 302 -2.9; 332 -2.6; 365 -2.4; 402 -2.1; 442 -1.7; 486 -1.4; 535 -1.0; 588 -0.1; 647 0.5; 712 0.5; 783 -0.7; 861 -1.3; 947 0.5; 1042 -0.4; 1146 -0.8; 1261 -1.3; 1387 -2.1; 1526 -3.2; 1678 -3.8; 1846 -4.2; 2031 -4.1; 2234 -3.1; 2457 1.1; 2703 0.4; 2973 1.6; 3270 0.2; 3597 0.6; 3957 1.6; 4353 1.2; 4788 -0.5; 5267 -1.0; 5793 -1.8; 6373 -2.2; 7010 -3.0; 7711 -0.7; 8482 0.0; 9330 -2.3; 10263 -4.2; 11289 -2.3; 12418 -2.5; 13660 -3.2; 15026 -0.3; 16529 0.0; 18182 -1.7; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 B2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 1.03 | -1.8 dB |
| Peaking | 170 Hz   | 0.6  | -3.9 dB |
| Peaking | 1788 Hz  | 3.12 | -4.7 dB |
| Peaking | 11028 Hz | 1.35 | -3.1 dB |
| Peaking | 19751 Hz | 3.12 | -8.3 dB |
| Peaking | 659 Hz   | 6.11 | 1.5 dB  |
| Peaking | 2853 Hz  | 5.11 | 1.9 dB  |
| Peaking | 4096 Hz  | 5.71 | 2.2 dB  |
| Peaking | 6414 Hz  | 4.04 | -2.1 dB |
| Peaking | 16595 Hz | 3.42 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000%20B2012/Denon%20AH-D5000%20B2012.png)