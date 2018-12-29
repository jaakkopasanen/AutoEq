# Sennheiser RS 220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.5; 31 4.9; 34 4.5; 37 4.0; 41 3.5; 45 3.1; 49 2.7; 54 2.3; 60 1.7; 66 1.9; 72 2.3; 79 0.9; 87 0.2; 96 -0.4; 106 -0.8; 116 -1.0; 128 -1.3; 141 -1.5; 155 -1.5; 170 -1.5; 187 -1.6; 206 -1.7; 227 -1.3; 249 -1.0; 274 -0.9; 302 -0.8; 332 -0.7; 365 -0.4; 402 -0.5; 442 -0.5; 486 -0.1; 535 0.3; 588 0.3; 647 0.4; 712 0.5; 783 0.4; 861 0.3; 947 0.2; 1042 -0.0; 1146 -0.0; 1261 -0.3; 1387 1.2; 1526 3.7; 1678 4.3; 1846 4.1; 2031 1.9; 2234 -1.9; 2457 -3.9; 2703 -2.6; 2973 -0.7; 3270 0.3; 3597 2.8; 3957 5.8; 4353 6.0; 4788 6.0; 5267 4.2; 5793 2.2; 6373 5.1; 7010 0.1; 7711 -0.5; 8482 0.0; 9330 -0.2; 10263 -1.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.51 | 6.3 dB  |
| Peaking | 44 Hz   | 1.98 | 2.3 dB  |
| Peaking | 1809 Hz | 2.72 | 6.9 dB  |
| Peaking | 2448 Hz | 1.97 | -6.4 dB |
| Peaking | 4405 Hz | 1.94 | 7.3 dB  |
| Peaking | 70 Hz   | 4.55 | 1.9 dB  |
| Peaking | 164 Hz  | 0.93 | -1.8 dB |
| Peaking | 6381 Hz | 8.46 | 5.1 dB  |
| Peaking | 6603 Hz | 5.83 | 1.0 dB  |
| Peaking | 6942 Hz | 2.43 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)