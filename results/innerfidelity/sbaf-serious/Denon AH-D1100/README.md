# Denon AH-D1100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.1; 23 -4.9; 25 -5.6; 28 -6.2; 31 -6.8; 34 -7.4; 37 -7.9; 41 -8.4; 45 -8.9; 49 -9.3; 54 -9.8; 60 -10.2; 66 -10.5; 72 -10.8; 79 -11.1; 87 -11.4; 96 -11.4; 106 -11.2; 116 -10.8; 128 -11.2; 141 -11.5; 155 -11.9; 170 -10.3; 187 -10.9; 206 -11.4; 227 -11.1; 249 -10.3; 274 -8.9; 302 -7.1; 332 -4.8; 365 -2.3; 402 0.5; 442 2.5; 486 2.8; 535 2.0; 588 1.0; 647 0.0; 712 -0.8; 783 -0.8; 861 -0.8; 947 -0.4; 1042 0.3; 1146 0.8; 1261 1.2; 1387 1.0; 1526 0.4; 1678 0.2; 1846 0.2; 2031 -0.2; 2234 -2.8; 2457 -2.0; 2703 0.0; 2973 2.6; 3270 1.4; 3597 1.6; 3957 5.9; 4353 4.3; 4788 1.8; 5267 3.3; 5793 2.3; 6373 1.9; 7010 2.0; 7711 0.1; 8482 -2.0; 9330 -3.4; 10263 -3.6; 11289 -2.0; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.57 | -9.8 dB |
| Peaking | 143 Hz  | 1.35 | -6.7 dB |
| Peaking | 237 Hz  | 2.68 | -7.6 dB |
| Peaking | 4124 Hz | 3.55 | 5.7 dB  |
| Peaking | 309 Hz  | 4.07 | -2.6 dB |
| Peaking | 462 Hz  | 2.86 | 4.9 dB  |
| Peaking | 2306 Hz | 7.09 | -3.3 dB |
| Peaking | 6368 Hz | 2.59 | 2.5 dB  |
| Peaking | 9679 Hz | 2.73 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)