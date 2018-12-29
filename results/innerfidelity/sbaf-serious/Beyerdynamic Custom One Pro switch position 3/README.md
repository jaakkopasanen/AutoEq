# Beyerdynamic Custom One Pro switch position 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.2; 25 -0.2; 28 -0.7; 31 -1.2; 34 -1.5; 37 -1.7; 41 -1.9; 45 -2.1; 49 -2.1; 54 -1.7; 60 -1.2; 66 -1.0; 72 -1.4; 79 -0.8; 87 1.8; 96 3.7; 106 1.9; 116 -0.7; 128 -2.7; 141 -3.5; 155 -2.2; 170 -1.3; 187 -2.4; 206 -2.2; 227 -2.0; 249 -2.1; 274 -2.1; 302 -2.0; 332 -1.9; 365 -1.7; 402 -1.6; 442 -1.4; 486 -1.4; 535 -1.3; 588 -1.0; 647 -1.0; 712 -1.0; 783 -0.1; 861 0.2; 947 0.0; 1042 0.0; 1146 0.1; 1261 -0.1; 1387 -0.7; 1526 -1.5; 1678 -2.3; 1846 -2.6; 2031 -2.5; 2234 -1.7; 2457 0.4; 2703 2.1; 2973 3.9; 3270 4.8; 3597 5.7; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro switch position 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro switch position 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 96 Hz   | 3.11 | 8.5 dB  |
| Peaking | 103 Hz  | 0.72 | -4.5 dB |
| Peaking | 378 Hz  | 1.05 | -1.3 dB |
| Peaking | 1963 Hz | 2.34 | -4.5 dB |
| Peaking | 4272 Hz | 1.1  | 7.1 dB  |
| Peaking | 45 Hz   | 1.86 | -0.9 dB |
| Peaking | 64 Hz   | 4.31 | 1.1 dB  |
| Peaking | 6340 Hz | 3.41 | 4.0 dB  |
| Peaking | 7458 Hz | 3.05 | -1.7 dB |
| Peaking | 7776 Hz | 1.03 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%203/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%203.png)