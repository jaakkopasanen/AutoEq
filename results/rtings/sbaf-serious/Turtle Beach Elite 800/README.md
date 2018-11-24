# Turtle Beach Elite 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.9; 23 -1.8; 25 -1.8; 28 -1.8; 31 -1.8; 34 -1.9; 37 -2.0; 41 -2.2; 45 -2.4; 49 -2.7; 54 -3.0; 60 -3.3; 66 -3.6; 72 -3.7; 79 -3.7; 87 -3.7; 96 -3.7; 106 -3.6; 116 -3.6; 128 -3.4; 141 -3.2; 155 -3.0; 170 -2.7; 187 -2.5; 206 -2.1; 227 -1.6; 249 -1.0; 274 -0.4; 302 0.5; 332 1.9; 365 3.9; 402 5.9; 442 6.0; 486 5.8; 535 4.4; 588 3.5; 647 2.8; 712 2.1; 783 1.4; 861 0.9; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -2.5; 1526 -3.8; 1678 -5.5; 1846 -6.9; 2031 -6.0; 2234 -4.5; 2457 -3.3; 2703 -3.0; 2973 -4.1; 3270 -5.9; 3597 -5.6; 3957 -2.2; 4353 0.5; 4788 3.4; 5267 5.4; 5793 3.9; 6373 5.5; 7010 2.5; 7711 0.0; 8482 -4.1; 9330 -5.4; 10263 -0.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 466 Hz  | 2.42 | 6.8 dB  |
| Peaking | 1860 Hz | 2.4  | -7.1 dB |
| Peaking | 3482 Hz | 2.5  | -8.3 dB |
| Peaking | 5631 Hz | 1.12 | 7.0 dB  |
| Peaking | 8894 Hz | 3.37 | -8.3 dB |
| Peaking | 54 Hz   | 0.08 | -1.1 dB |
| Peaking | 97 Hz   | 0.59 | -2.8 dB |
| Peaking | 377 Hz  | 4.29 | 2.8 dB  |
| Peaking | 709 Hz  | 2.15 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Turtle%20Beach%20Elite%20800/Turtle%20Beach%20Elite%20800.png)