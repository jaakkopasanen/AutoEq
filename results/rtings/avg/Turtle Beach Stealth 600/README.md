# Turtle Beach Stealth 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.2; 28 -0.4; 31 -0.8; 34 -1.0; 37 -1.2; 41 -1.3; 45 -1.4; 49 -1.5; 54 -1.5; 60 -1.5; 66 -1.6; 72 -1.7; 79 -1.6; 87 -1.6; 96 -1.6; 106 -1.6; 116 -1.6; 128 -1.6; 141 -1.5; 155 -1.3; 170 -1.0; 187 -0.8; 206 -0.4; 227 0.0; 249 0.4; 274 0.7; 302 0.9; 332 1.2; 365 1.6; 402 2.1; 442 2.4; 486 2.3; 535 2.1; 588 1.9; 647 1.9; 712 1.9; 783 1.6; 861 1.1; 947 0.3; 1042 -0.1; 1146 -0.2; 1261 0.0; 1387 0.3; 1526 1.1; 1678 2.1; 1846 2.8; 2031 3.1; 2234 4.1; 2457 4.3; 2703 4.4; 2973 5.7; 3270 4.9; 3597 3.6; 3957 0.0; 4353 0.0; 4788 1.4; 5267 3.4; 5793 4.1; 6373 0.8; 7010 1.0; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.63 | 2.0 dB  |
| Peaking | 77 Hz   | 0.37 | -1.9 dB |
| Peaking | 453 Hz  | 1.08 | 2.7 dB  |
| Peaking | 2740 Hz | 1.78 | 5.3 dB  |
| Peaking | 5660 Hz | 6.36 | 3.9 dB  |
| Peaking | 1173 Hz | 3.55 | -1.2 dB |
| Peaking | 1855 Hz | 3.5  | 1.3 dB  |
| Peaking | 3442 Hz | 4.14 | 4.5 dB  |
| Peaking | 3949 Hz | 1.8  | -4.1 dB |
| Peaking | 5043 Hz | 3.96 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20600/Turtle%20Beach%20Stealth%20600.png)