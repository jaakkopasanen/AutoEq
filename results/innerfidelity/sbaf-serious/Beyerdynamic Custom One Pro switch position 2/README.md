# Beyerdynamic Custom One Pro switch position 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.5; 28 -1.0; 31 -1.3; 34 -1.5; 37 -1.6; 41 -1.7; 45 -1.7; 49 -1.3; 54 -0.5; 60 0.8; 66 1.2; 72 1.1; 79 2.6; 87 4.9; 96 5.8; 106 4.4; 116 3.0; 128 1.1; 141 -0.7; 155 -1.0; 170 -1.2; 187 -3.7; 206 -3.8; 227 -3.6; 249 -3.5; 274 -3.5; 302 -3.2; 332 -2.9; 365 -2.6; 402 -2.3; 442 -2.0; 486 -1.9; 535 -1.7; 588 -1.3; 647 -1.1; 712 -1.2; 783 -0.1; 861 0.1; 947 0.0; 1042 0.1; 1146 0.1; 1261 -0.1; 1387 -0.7; 1526 -1.4; 1678 -2.2; 1846 -2.7; 2031 -2.7; 2234 -2.0; 2457 -0.0; 2703 1.7; 2973 3.5; 3270 4.3; 3597 5.2; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro switch position 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro switch position 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 1.71 | -2.1 dB |
| Peaking | 97 Hz   | 2.07 | 7.1 dB  |
| Peaking | 237 Hz  | 0.78 | -4.1 dB |
| Peaking | 1982 Hz | 2.47 | -4.4 dB |
| Peaking | 4393 Hz | 1.16 | 7.0 dB  |
| Peaking | 1028 Hz | 1.86 | 1.0 dB  |
| Peaking | 2931 Hz | 0.2  | -0.5 dB |
| Peaking | 3052 Hz | 3.51 | 1.2 dB  |
| Peaking | 6322 Hz | 3.42 | 4.5 dB  |
| Peaking | 7317 Hz | 1.74 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%202/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%202.png)