# Skullcandy Hesh 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 5.2; 31 4.5; 34 4.1; 37 3.8; 41 3.6; 45 3.3; 49 3.0; 54 2.7; 60 2.3; 66 1.9; 72 1.5; 79 1.2; 87 0.8; 96 0.3; 106 -0.2; 116 -0.5; 128 -0.6; 141 -0.5; 155 -0.2; 170 -0.0; 187 0.2; 206 1.3; 227 2.5; 249 3.7; 274 5.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 5.4; 647 3.0; 712 1.4; 783 0.6; 861 0.3; 947 0.1; 1042 0.0; 1146 0.7; 1261 2.0; 1387 2.5; 1526 2.9; 1678 3.4; 1846 3.8; 2031 4.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.87 | 5.7 dB  |
| Peaking | 51 Hz   | 0.96 | 1.5 dB  |
| Peaking | 144 Hz  | 1.23 | -2.1 dB |
| Peaking | 370 Hz  | 1.11 | 6.9 dB  |
| Peaking | 3518 Hz | 0.76 | 6.8 dB  |
| Peaking | 563 Hz  | 4.94 | 2.9 dB  |
| Peaking | 873 Hz  | 1.82 | -2.2 dB |
| Peaking | 2134 Hz | 2.5  | 1.7 dB  |
| Peaking | 6002 Hz | 2.14 | 7.2 dB  |
| Peaking | 6572 Hz | 1.01 | -5.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Skullcandy%20Hesh%202/Skullcandy%20Hesh%202.png)