# Logitech G930

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 1.9; 28 1.3; 31 0.9; 34 0.7; 37 0.7; 41 0.8; 45 1.0; 49 1.1; 54 1.3; 60 1.7; 66 1.7; 72 1.6; 79 1.2; 87 0.7; 96 0.1; 106 -0.3; 116 -0.5; 128 -0.5; 141 -0.3; 155 0.2; 170 1.0; 187 2.0; 206 3.4; 227 5.4; 249 6.0; 274 6.0; 302 5.9; 332 3.8; 365 1.9; 402 0.7; 442 0.2; 486 -0.4; 535 -0.8; 588 -0.9; 647 -1.0; 712 -0.8; 783 -0.7; 861 -0.5; 947 -0.2; 1042 0.1; 1146 0.9; 1261 1.7; 1387 2.5; 1526 1.8; 1678 1.5; 1846 1.6; 2031 1.9; 2234 2.8; 2457 4.1; 2703 5.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 1.4; 4788 -0.1; 5267 3.0; 5793 3.2; 6373 -2.1; 7010 1.9; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 3 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 263 Hz  | 2.55 | 6.9 dB  |
| Peaking | 2630 Hz | 1.53 | 2.6 dB  |
| Peaking | 3433 Hz | 2.11 | 5.0 dB  |
| Peaking | 19 Hz   | 1.56 | 3.1 dB  |
| Peaking | 62 Hz   | 3.1  | 1.8 dB  |
| Peaking | 646 Hz  | 1.7  | -1.5 dB |
| Peaking | 1369 Hz | 4.41 | 1.9 dB  |
| Peaking | 2052 Hz | 5.04 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Logitech%20G930/Logitech%20G930.png)