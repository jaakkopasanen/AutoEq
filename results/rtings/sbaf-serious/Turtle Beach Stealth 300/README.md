# Turtle Beach Stealth 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.5; 25 -2.0; 28 -2.7; 31 -3.2; 34 -3.6; 37 -4.0; 41 -4.3; 45 -4.5; 49 -4.7; 54 -4.8; 60 -4.8; 66 -4.8; 72 -4.6; 79 -4.5; 87 -4.3; 96 -4.2; 106 -4.0; 116 -3.9; 128 -3.8; 141 -3.5; 155 -3.2; 170 -2.8; 187 -2.4; 206 -1.9; 227 -1.3; 249 -0.7; 274 -0.1; 302 0.8; 332 1.8; 365 2.9; 402 3.6; 442 3.1; 486 1.8; 535 0.8; 588 0.8; 647 1.3; 712 1.4; 783 0.8; 861 0.3; 947 0.1; 1042 0.1; 1146 0.8; 1261 1.6; 1387 2.2; 1526 2.8; 1678 4.1; 1846 5.0; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 1.9; 4353 -1.1; 4788 0.8; 5267 2.3; 5793 3.7; 6373 1.6; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 71 Hz   | 0.39 | -4.8 dB |
| Peaking | 392 Hz  | 2.01 | 4.4 dB  |
| Peaking | 2186 Hz | 1.61 | 6.1 dB  |
| Peaking | 3293 Hz | 4.17 | 4.5 dB  |
| Peaking | 5884 Hz | 5.96 | 3.3 dB  |
| Peaking | 15 Hz   | 0.44 | 1.4 dB  |
| Peaking | 36 Hz   | 1.25 | -1.1 dB |
| Peaking | 1007 Hz | 4.93 | -1.1 dB |
| Peaking | 2333 Hz | 0.33 | 0.3 dB  |
| Peaking | 4329 Hz | 9.18 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Turtle%20Beach%20Stealth%20300/Turtle%20Beach%20Stealth%20300.png)