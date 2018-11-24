# Logitech G430

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.2; 28 -1.0; 31 -2.0; 34 -2.9; 37 -3.5; 41 -4.1; 45 -4.5; 49 -4.8; 54 -5.0; 60 -4.9; 66 -4.7; 72 -4.3; 79 -4.0; 87 -4.0; 96 -4.2; 106 -4.4; 116 -4.4; 128 -4.1; 141 -4.0; 155 -3.7; 170 -3.3; 187 -2.9; 206 -2.6; 227 -2.1; 249 -2.2; 274 -1.7; 302 -0.5; 332 0.4; 365 1.2; 402 2.0; 442 2.7; 486 2.5; 535 1.5; 588 0.7; 647 0.5; 712 0.3; 783 0.1; 861 -0.1; 947 -0.2; 1042 0.1; 1146 0.2; 1261 0.5; 1387 0.6; 1526 -0.7; 1678 -0.9; 1846 -1.0; 2031 -0.7; 2234 0.4; 2457 2.1; 2703 3.6; 2973 4.4; 3270 5.7; 3597 6.0; 3957 5.4; 4353 0.7; 4788 0.1; 5267 1.5; 5793 1.4; 6373 -0.4; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G430 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G430 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 18 Hz   |  1.45 | 4.1 dB  |
| Peaking | 46 Hz   |  1.03 | -3.6 dB |
| Peaking | 127 Hz  |  0.49 | -3.7 dB |
| Peaking | 434 Hz  |  2.04 | 3.9 dB  |
| Peaking | 3412 Hz |  2.73 | 6.6 dB  |
| Peaking | 14 Hz   |  0.76 | -0.5 dB |
| Peaking | 1886 Hz |  3.39 | -1.7 dB |
| Peaking | 2646 Hz |  5.69 | 1.5 dB  |
| Peaking | 4586 Hz | 11.71 | -2.1 dB |
| Peaking | 6914 Hz | 13.19 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Logitech%20G430/Logitech%20G430.png)