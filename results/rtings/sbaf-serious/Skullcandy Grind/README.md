# Skullcandy Grind

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 21 -2.4; 23 -2.9; 25 -3.5; 28 -4.1; 31 -4.6; 34 -4.9; 37 -5.2; 41 -5.4; 45 -5.6; 49 -5.7; 54 -5.9; 60 -6.0; 66 -6.0; 72 -6.0; 79 -5.9; 87 -5.8; 96 -5.7; 106 -5.8; 116 -5.8; 128 -5.7; 141 -5.6; 155 -5.5; 170 -5.4; 187 -5.4; 206 -5.4; 227 -5.3; 249 -5.2; 274 -5.1; 302 -5.1; 332 -4.5; 365 -3.9; 402 -3.2; 442 -2.6; 486 -2.0; 535 -1.3; 588 -0.7; 647 0.3; 712 1.3; 783 1.9; 861 1.9; 947 1.1; 1042 -1.0; 1146 -3.2; 1261 -2.3; 1387 -4.3; 1526 -5.2; 1678 -5.5; 1846 -7.3; 2031 -9.0; 2234 -9.3; 2457 -8.4; 2703 -6.9; 2973 -5.2; 3270 -3.1; 3597 -1.5; 3957 -3.9; 4353 -3.1; 4788 -0.7; 5267 2.6; 5793 3.0; 6373 -1.2; 7010 -4.9; 7711 -7.7; 8482 -10.1; 9330 -9.5; 10263 -2.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Grind GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Grind ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 88 Hz    | 0.28 | -6.3 dB  |
| Peaking | 1813 Hz  | 2.43 | -3.4 dB  |
| Peaking | 2367 Hz  | 1.88 | -7.7 dB  |
| Peaking | 5604 Hz  | 5.77 | 5.9 dB   |
| Peaking | 8506 Hz  | 2.92 | -11.2 dB |
| Peaking | 313 Hz   | 1.9  | -1.7 dB  |
| Peaking | 872 Hz   | 1.75 | 5.4 dB   |
| Peaking | 1115 Hz  | 1.93 | -3.5 dB  |
| Peaking | 9552 Hz  | 6.91 | -3.9 dB  |
| Peaking | 10787 Hz | 3.09 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Skullcandy%20Grind/Skullcandy%20Grind.png)