# Sound Intone CX-05

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.9; 25 2.6; 28 2.3; 31 1.9; 34 1.6; 37 1.3; 41 1.1; 45 0.9; 49 0.7; 54 0.5; 60 0.3; 66 0.2; 72 0.2; 79 0.2; 87 0.2; 96 0.1; 106 0.1; 116 0.0; 128 0.1; 141 0.0; 155 0.1; 170 0.3; 187 -0.0; 206 -0.2; 227 -0.3; 249 -0.2; 274 -1.2; 302 -2.0; 332 -2.4; 365 -3.3; 402 -3.3; 442 -3.2; 486 -2.9; 535 -2.4; 588 -2.0; 647 -1.6; 712 -1.2; 783 -0.7; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.8; 1387 1.8; 1526 2.2; 1678 2.8; 1846 3.4; 2031 4.1; 2234 5.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sound Intone CX-05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sound Intone CX-05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.75 | 3.4 dB  |
| Peaking | 440 Hz  | 1.31 | -3.6 dB |
| Peaking | 2835 Hz | 1.03 | 6.2 dB  |
| Peaking | 5416 Hz | 2.31 | 4.7 dB  |
| Peaking | 195 Hz  | 2.26 | 0.5 dB  |
| Peaking | 3094 Hz | 3.5  | -1.3 dB |
| Peaking | 4023 Hz | 1.31 | 1.9 dB  |
| Peaking | 6403 Hz | 4.55 | 4.3 dB  |
| Peaking | 6537 Hz | 1.28 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sound%20Intone%20CX-05/Sound%20Intone%20CX-05.png)