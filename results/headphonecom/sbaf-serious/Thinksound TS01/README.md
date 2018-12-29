# Thinksound TS01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 -7.3; 23 -7.4; 25 -7.4; 28 -7.5; 31 -7.7; 34 -7.7; 37 -7.8; 41 -7.9; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.6; 66 -8.7; 72 -9.0; 79 -9.3; 87 -9.5; 96 -9.7; 106 -9.8; 116 -9.8; 128 -9.9; 141 -9.9; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.3; 227 -8.9; 249 -8.5; 274 -8.0; 302 -7.4; 332 -6.7; 365 -6.0; 402 -5.2; 442 -4.7; 486 -4.1; 535 -3.3; 588 -2.5; 647 -1.7; 712 -1.0; 783 -0.4; 861 -0.1; 947 0.2; 1042 -0.1; 1146 1.0; 1261 1.1; 1387 0.8; 1526 0.6; 1678 0.6; 1846 0.8; 2031 1.1; 2234 1.3; 2457 1.4; 2703 1.1; 2973 0.8; 3270 2.0; 3597 3.8; 3957 3.8; 4353 1.7; 4788 0.1; 5267 -2.0; 5793 -7.4; 6373 -6.2; 7010 -1.6; 7711 -0.2; 8482 -2.7; 9330 -5.2; 10263 -0.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound TS01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound TS01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.23 | -7.3 dB |
| Peaking | 153 Hz  | 0.7  | -5.5 dB |
| Peaking | 312 Hz  | 1.18 | -3.5 dB |
| Peaking | 3843 Hz | 1.68 | 4.1 dB  |
| Peaking | 5987 Hz | 3.99 | -9.5 dB |
| Peaking | 1195 Hz | 2.11 | 1.3 dB  |
| Peaking | 2310 Hz | 2.09 | 0.7 dB  |
| Peaking | 2971 Hz | 5.46 | -1.6 dB |
| Peaking | 7727 Hz | 2.71 | 1.9 dB  |
| Peaking | 9146 Hz | 5.26 | -6.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Thinksound%20TS01/Thinksound%20TS01.png)