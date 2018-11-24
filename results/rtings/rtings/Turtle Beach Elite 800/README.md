# Turtle Beach Elite 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.3; 23 -2.2; 25 -2.0; 28 -1.9; 31 -1.9; 34 -1.9; 37 -1.9; 41 -2.0; 45 -2.1; 49 -2.3; 54 -2.6; 60 -3.0; 66 -3.4; 72 -3.7; 79 -3.9; 87 -4.1; 96 -4.1; 106 -4.1; 116 -4.1; 128 -3.9; 141 -3.8; 155 -3.6; 170 -3.3; 187 -3.1; 206 -2.6; 227 -2.0; 249 -1.5; 274 -1.0; 302 -0.3; 332 0.9; 365 2.9; 402 5.2; 442 5.9; 486 4.6; 535 3.2; 588 2.4; 647 1.8; 712 1.2; 783 0.9; 861 0.7; 947 0.3; 1042 -0.3; 1146 -0.9; 1261 -1.6; 1387 -2.4; 1526 -3.4; 1678 -5.1; 1846 -7.0; 2031 -6.5; 2234 -4.9; 2457 -3.8; 2703 -3.6; 2973 -5.1; 3270 -7.8; 3597 -7.8; 3957 -3.4; 4353 0.5; 4788 3.5; 5267 5.0; 5793 2.5; 6373 5.0; 7010 2.5; 7711 -0.6; 8482 -4.4; 9330 -6.9; 10263 -3.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 449 Hz  | 3.42 | 6.5 dB   |
| Peaking | 1896 Hz | 2.23 | -7.6 dB  |
| Peaking | 3489 Hz | 2.39 | -13.2 dB |
| Peaking | 5074 Hz | 0.75 | 8.0 dB   |
| Peaking | 9107 Hz | 2.91 | -10.4 dB |
| Peaking | 16 Hz   | 0.59 | -2.3 dB  |
| Peaking | 76 Hz   | 1.03 | -1.9 dB  |
| Peaking | 141 Hz  | 0.68 | -3.1 dB  |
| Peaking | 378 Hz  | 5.64 | 2.1 dB   |
| Peaking | 665 Hz  | 2.12 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Turtle%20Beach%20Elite%20800/Turtle%20Beach%20Elite%20800.png)