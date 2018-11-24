# Sound Intone CX-05

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.9; 28 2.4; 31 2.0; 34 1.5; 37 1.2; 41 0.9; 45 0.7; 49 0.4; 54 0.1; 60 0.0; 66 0.0; 72 0.2; 79 0.3; 87 0.5; 96 0.6; 106 0.6; 116 0.6; 128 0.6; 141 0.6; 155 0.7; 170 0.9; 187 0.5; 206 0.3; 227 0.2; 249 0.3; 274 -0.5; 302 -1.2; 332 -1.5; 365 -2.3; 402 -2.3; 442 -2.1; 486 -1.7; 535 -1.2; 588 -0.9; 647 -0.5; 712 -0.4; 783 -0.2; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.5; 1261 1.1; 1387 1.7; 1526 1.8; 1678 2.4; 1846 3.4; 2031 4.5; 2234 5.9; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sound Intone CX-05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sound Intone CX-05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.37 | 3.5 dB  |
| Peaking | 240 Hz  | 0.79 | 2.1 dB  |
| Peaking | 374 Hz  | 0.99 | -3.6 dB |
| Peaking | 2801 Hz | 1.07 | 6.2 dB  |
| Peaking | 5383 Hz | 2.22 | 4.8 dB  |
| Peaking | 1032 Hz | 4.31 | -0.5 dB |
| Peaking | 2202 Hz | 8.15 | 0.8 dB  |
| Peaking | 6469 Hz | 6.27 | 2.1 dB  |
| Peaking | 6651 Hz | 4.59 | 0.7 dB  |
| Peaking | 7719 Hz | 1.96 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sound%20Intone%20CX-05/Sound%20Intone%20CX-05.png)