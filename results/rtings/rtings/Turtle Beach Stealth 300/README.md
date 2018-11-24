# Turtle Beach Stealth 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.3; 23 -1.8; 25 -2.2; 28 -2.8; 31 -3.3; 34 -3.6; 37 -3.8; 41 -4.1; 45 -4.3; 49 -4.4; 54 -4.5; 60 -4.5; 66 -4.6; 72 -4.6; 79 -4.7; 87 -4.7; 96 -4.6; 106 -4.5; 116 -4.4; 128 -4.3; 141 -4.0; 155 -3.8; 170 -3.4; 187 -3.0; 206 -2.4; 227 -1.8; 249 -1.3; 274 -0.8; 302 -0.0; 332 0.9; 365 1.9; 402 2.5; 442 2.0; 486 0.6; 535 -0.3; 588 -0.3; 647 0.3; 712 0.5; 783 0.4; 861 0.1; 947 0.1; 1042 0.1; 1146 0.6; 1261 1.3; 1387 2.2; 1526 3.2; 1678 4.4; 1846 4.9; 2031 5.4; 2234 6.0; 2457 6.0; 2703 6.0; 2973 5.9; 3270 4.9; 3597 4.8; 3957 0.7; 4353 -1.1; 4788 1.0; 5267 1.9; 5793 2.3; 6373 -0.9; 7010 0.8; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.36 | -4.8 dB |
| Peaking | 382 Hz  | 2.49 | 3.7 dB  |
| Peaking | 2035 Hz | 1.69 | 5.1 dB  |
| Peaking | 2993 Hz | 2.67 | 4.4 dB  |
| Peaking | 547 Hz  | 7.99 | -0.8 dB |
| Peaking | 1025 Hz | 6.26 | -0.7 dB |
| Peaking | 3599 Hz | 9.07 | 2.3 dB  |
| Peaking | 4169 Hz | 6.29 | -3.2 dB |
| Peaking | 5443 Hz | 6.63 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Turtle%20Beach%20Stealth%20300/Turtle%20Beach%20Stealth%20300.png)