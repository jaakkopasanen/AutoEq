# Turtle Beach Stealth 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.9; 25 0.4; 28 -0.2; 31 -0.7; 34 -1.0; 37 -1.3; 41 -1.5; 45 -1.7; 49 -1.8; 54 -1.8; 60 -1.8; 66 -1.8; 72 -1.7; 79 -1.4; 87 -1.3; 96 -1.2; 106 -1.1; 116 -1.1; 128 -1.1; 141 -0.9; 155 -0.7; 170 -0.4; 187 -0.2; 206 0.1; 227 0.5; 249 1.0; 274 1.4; 302 1.8; 332 2.1; 365 2.6; 402 3.2; 442 3.5; 486 3.5; 535 3.3; 588 3.0; 647 2.9; 712 2.7; 783 2.1; 861 1.2; 947 0.3; 1042 -0.1; 1146 -0.0; 1261 0.3; 1387 0.3; 1526 0.8; 1678 1.7; 1846 2.8; 2031 3.5; 2234 4.5; 2457 4.8; 2703 5.2; 2973 6.0; 3270 6.0; 3597 6.0; 3957 2.4; 4353 1.3; 4788 3.0; 5267 5.9; 5793 6.0; 6373 4.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.19 | 3.0 dB  |
| Peaking | 48 Hz   | 0.38 | -2.2 dB |
| Peaking | 465 Hz  | 1.19 | 3.8 dB  |
| Peaking | 2891 Hz | 1.65 | 6.1 dB  |
| Peaking | 5749 Hz | 3.95 | 5.9 dB  |
| Peaking | 715 Hz  | 3.34 | 1.5 dB  |
| Peaking | 1576 Hz | 0.76 | -1.8 dB |
| Peaking | 1931 Hz | 2.29 | 2.6 dB  |
| Peaking | 3589 Hz | 7.09 | 2.4 dB  |
| Peaking | 4191 Hz | 7.96 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Turtle%20Beach%20Stealth%20600/Turtle%20Beach%20Stealth%20600.png)