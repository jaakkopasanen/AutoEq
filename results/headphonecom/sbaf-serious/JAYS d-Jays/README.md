# JAYS d-Jays

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.4; 25 5.1; 28 4.8; 31 4.6; 34 4.3; 37 4.1; 41 3.8; 45 3.6; 49 3.3; 54 3.0; 60 2.5; 66 2.2; 72 1.9; 79 1.4; 87 1.1; 96 0.8; 106 0.5; 116 0.3; 128 -0.0; 141 -0.6; 155 -0.8; 170 -1.0; 187 -1.1; 206 -1.0; 227 -1.0; 249 -1.2; 274 -1.5; 302 -1.3; 332 -1.0; 365 -0.8; 402 -0.5; 442 -0.4; 486 -0.3; 535 -0.1; 588 0.1; 647 0.5; 712 0.6; 783 0.7; 861 0.6; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.6; 1526 -2.3; 1678 -3.0; 1846 -4.0; 2031 -4.4; 2234 -4.1; 2457 -2.2; 2703 1.5; 2973 5.6; 3270 6.0; 3597 6.0; 3957 5.4; 4353 2.7; 4788 1.4; 5267 4.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS d-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS d-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.09 | 5.3 dB  |
| Peaking | 50 Hz   | 1.62 | 2.3 dB  |
| Peaking | 2164 Hz | 1.73 | -7.1 dB |
| Peaking | 3221 Hz | 2.02 | 8.8 dB  |
| Peaking | 5973 Hz | 4.17 | 6.0 dB  |
| Peaking | 249 Hz  | 1.08 | -1.4 dB |
| Peaking | 770 Hz  | 2.13 | 1.2 dB  |
| Peaking | 6691 Hz | 8.5  | 1.8 dB  |
| Peaking | 7703 Hz | 2.63 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20d-Jays/JAYS%20d-Jays.png)