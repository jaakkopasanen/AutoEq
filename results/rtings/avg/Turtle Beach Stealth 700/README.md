# Turtle Beach Stealth 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 -4.3; 23 -4.6; 25 -4.9; 28 -5.1; 31 -5.3; 34 -5.4; 37 -5.4; 41 -5.4; 45 -5.4; 49 -5.4; 54 -5.5; 60 -5.6; 66 -5.7; 72 -5.9; 79 -6.0; 87 -6.1; 96 -6.1; 106 -6.3; 116 -6.6; 128 -6.9; 141 -7.1; 155 -7.3; 170 -7.3; 187 -7.4; 206 -7.3; 227 -7.1; 249 -6.8; 274 -6.2; 302 -5.5; 332 -4.7; 365 -3.9; 402 -3.0; 442 -2.1; 486 -1.1; 535 -0.4; 588 -0.5; 647 -1.3; 712 -1.9; 783 -2.0; 861 -1.5; 947 -0.4; 1042 0.3; 1146 1.0; 1261 1.5; 1387 2.0; 1526 2.8; 1678 3.5; 1846 3.8; 2031 2.9; 2234 1.9; 2457 1.8; 2703 1.5; 2973 1.8; 3270 2.4; 3597 5.2; 3957 2.1; 4353 -0.8; 4788 -0.7; 5267 0.2; 5793 1.6; 6373 1.8; 7010 1.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.2  | -5.3 dB |
| Peaking | 156 Hz  | 1.16 | -2.2 dB |
| Peaking | 253 Hz  | 1.36 | -3.1 dB |
| Peaking | 1767 Hz | 1.92 | 4.0 dB  |
| Peaking | 3614 Hz | 7.17 | 5.2 dB  |
| Peaking | 539 Hz  | 4.23 | 1.5 dB  |
| Peaking | 771 Hz  | 3.93 | -1.8 dB |
| Peaking | 3934 Hz | 2.1  | 1.2 dB  |
| Peaking | 4451 Hz | 3.89 | -2.9 dB |
| Peaking | 6154 Hz | 4.97 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20700/Turtle%20Beach%20Stealth%20700.png)