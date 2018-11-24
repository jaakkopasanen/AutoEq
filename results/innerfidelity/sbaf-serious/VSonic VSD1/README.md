# VSonic VSD1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.3; 23 -0.6; 25 -0.9; 28 -1.3; 31 -1.6; 34 -1.9; 37 -2.1; 41 -2.3; 45 -2.5; 49 -2.7; 54 -2.9; 60 -3.1; 66 -3.3; 72 -3.5; 79 -3.8; 87 -4.0; 96 -4.2; 106 -4.3; 116 -4.2; 128 -4.3; 141 -4.3; 155 -4.2; 170 -4.0; 187 -3.8; 206 -3.5; 227 -3.2; 249 -3.0; 274 -2.6; 302 -2.3; 332 -2.0; 365 -1.6; 402 -1.3; 442 -0.9; 486 -0.7; 535 -0.4; 588 0.1; 647 0.3; 712 0.3; 783 0.6; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.3; 1526 -2.0; 1678 -2.5; 1846 -2.1; 2031 -2.2; 2234 -1.9; 2457 -0.6; 2703 1.2; 2973 4.0; 3270 5.9; 3597 6.0; 3957 5.6; 4353 2.4; 4788 -0.3; 5267 -2.0; 5793 -0.2; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.0; 10263 -0.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 86 Hz    | 0.55 | -3.6 dB |
| Peaking | 196 Hz   | 1.02 | -2.0 dB |
| Peaking | 1975 Hz  | 1.86 | -3.2 dB |
| Peaking | 3445 Hz  | 2.75 | 7.4 dB  |
| Peaking | 23892 Hz | 2.23 | 0.9 dB  |
| Peaking | 789 Hz   | 2.14 | 1.1 dB  |
| Peaking | 1511 Hz  | 6.04 | -0.7 dB |
| Peaking | 4054 Hz  | 6.08 | 2.5 dB  |
| Peaking | 5410 Hz  | 2.29 | -3.8 dB |
| Peaking | 6511 Hz  | 5.12 | 6.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD1/VSonic%20VSD1.png)