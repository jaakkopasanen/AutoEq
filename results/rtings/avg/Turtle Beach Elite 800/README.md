# Turtle Beach Elite 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.3; 23 -2.2; 25 -2.0; 28 -1.9; 31 -1.9; 34 -1.9; 37 -1.9; 41 -2.0; 45 -2.1; 49 -2.3; 54 -2.6; 60 -3.0; 66 -3.4; 72 -3.7; 79 -3.9; 87 -4.1; 96 -4.1; 106 -4.1; 116 -4.1; 128 -3.9; 141 -3.8; 155 -3.6; 170 -3.3; 187 -3.1; 206 -2.6; 227 -2.0; 249 -1.5; 274 -1.0; 302 -0.3; 332 0.9; 365 2.9; 402 5.2; 442 5.9; 486 4.6; 535 3.2; 588 2.4; 647 1.8; 712 1.2; 783 0.9; 861 0.7; 947 0.3; 1042 -0.3; 1146 -0.9; 1261 -1.6; 1387 -2.4; 1526 -3.4; 1678 -5.1; 1846 -7.0; 2031 -6.5; 2234 -4.9; 2457 -3.8; 2703 -3.8; 2973 -5.6; 3270 -8.5; 3597 -8.8; 3957 -4.6; 4353 -0.8; 4788 1.8; 5267 2.4; 5793 0.0; 6373 3.8; 7010 1.6; 7711 -2.0; 8482 -5.1; 9330 -5.6; 10263 -1.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.4; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 115 Hz  | 0.37 | -4.2 dB |
| Peaking | 440 Hz  | 1.75 | 7.3 dB  |
| Peaking | 1903 Hz | 2.42 | -7.0 dB |
| Peaking | 3403 Hz | 4.74 | -9.4 dB |
| Peaking | 9085 Hz | 5.68 | -6.6 dB |
| Peaking | 20 Hz   | 2.17 | -1.4 dB |
| Peaking | 856 Hz  | 4.91 | 0.7 dB  |
| Peaking | 3814 Hz | 8.59 | -2.5 dB |
| Peaking | 6932 Hz | 1.72 | 5.7 dB  |
| Peaking | 7878 Hz | 3.17 | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20800/Turtle%20Beach%20Elite%20800.png)