# Sennheiser RS 160
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.8; 23 -1.0; 25 -1.2; 28 -1.3; 31 -1.4; 34 -1.5; 37 -1.6; 41 -1.6; 45 -1.6; 49 -1.6; 54 -1.5; 60 -1.5; 66 -1.6; 72 -1.5; 79 -1.4; 87 -1.1; 96 -1.1; 106 -2.3; 116 -3.0; 128 -2.3; 141 -3.1; 155 -3.0; 170 -1.9; 187 -1.9; 206 -2.1; 227 -1.4; 249 -1.0; 274 -0.4; 302 0.0; 332 -0.1; 365 -0.4; 402 -0.7; 442 -0.6; 486 0.0; 535 0.7; 588 1.4; 647 1.6; 712 1.6; 783 1.8; 861 1.7; 947 1.0; 1042 -0.5; 1146 -0.7; 1261 -0.9; 1387 -2.0; 1526 -2.8; 1678 -4.2; 1846 -0.4; 2031 -2.1; 2234 -3.2; 2457 -2.7; 2703 -1.8; 2973 -1.9; 3270 -0.8; 3597 0.3; 3957 1.4; 4353 0.2; 4788 2.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.3; 9330 -6.4; 10263 -4.2; 11289 -0.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 160 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 130 Hz  | 0.98 | -2.8 dB |
| Peaking | 1613 Hz | 5.24 | -3.4 dB |
| Peaking | 2474 Hz | 2.37 | -3.0 dB |
| Peaking | 5862 Hz | 2.49 | 7.2 dB  |
| Peaking | 9344 Hz | 3.93 | -7.8 dB |
| Peaking | 36 Hz   | 1.07 | -0.7 dB |
| Peaking | 42 Hz   | 0.35 | -0.7 dB |
| Peaking | 92 Hz   | 3.6  | 1.5 dB  |
| Peaking | 826 Hz  | 1.58 | 2.9 dB  |
| Peaking | 1103 Hz | 2.09 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20160/Sennheiser%20RS%20160.png)