# Skullcandy Crusher

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.2; 34 4.6; 37 4.2; 41 3.8; 45 3.6; 49 3.4; 54 3.0; 60 2.8; 66 3.1; 72 3.4; 79 3.7; 87 3.8; 96 3.7; 106 3.4; 116 3.1; 128 3.0; 141 3.1; 155 3.3; 170 3.6; 187 3.9; 206 4.2; 227 4.6; 249 4.7; 274 4.8; 302 4.4; 332 4.0; 365 3.3; 402 2.2; 442 0.9; 486 -0.2; 535 -1.0; 588 -1.5; 647 -1.7; 712 -1.1; 783 0.3; 861 0.4; 947 -0.1; 1042 0.3; 1146 1.3; 1261 2.7; 1387 4.1; 1526 4.5; 1678 4.5; 1846 4.2; 2031 4.4; 2234 5.1; 2457 6.0; 2703 5.8; 2973 5.6; 3270 5.6; 3597 5.2; 3957 3.8; 4353 4.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.1  | 4.8 dB  |
| Peaking | 255 Hz  | 1.69 | 4.3 dB  |
| Peaking | 1542 Hz | 3.28 | 3.4 dB  |
| Peaking | 2746 Hz | 1.46 | 5.7 dB  |
| Peaking | 5450 Hz | 2.35 | 5.8 dB  |
| Peaking | 33 Hz   | 0.36 | 2.0 dB  |
| Peaking | 50 Hz   | 1.15 | -3.0 dB |
| Peaking | 360 Hz  | 4.53 | 1.5 dB  |
| Peaking | 599 Hz  | 2.3  | -2.7 dB |
| Peaking | 8339 Hz | 4.31 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher/Skullcandy%20Crusher.png)