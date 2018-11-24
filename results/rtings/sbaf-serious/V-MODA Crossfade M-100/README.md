# V-MODA Crossfade M-100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.4; 23 -0.7; 25 -1.0; 28 -1.3; 31 -1.5; 34 -1.6; 37 -1.7; 41 -1.8; 45 -1.9; 49 -2.0; 54 -2.0; 60 -2.1; 66 -2.1; 72 -2.2; 79 -2.3; 87 -2.4; 96 -2.5; 106 -2.9; 116 -3.2; 128 -3.5; 141 -3.6; 155 -3.5; 170 -3.3; 187 -2.9; 206 -2.3; 227 -1.3; 249 -0.2; 274 0.9; 302 2.6; 332 5.3; 365 5.3; 402 5.5; 442 5.4; 486 5.7; 535 5.8; 588 5.4; 647 4.8; 712 3.7; 783 2.4; 861 1.3; 947 0.4; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.2; 1526 -1.5; 1678 -1.7; 1846 -1.8; 2031 -1.7; 2234 -1.1; 2457 -0.3; 2703 0.6; 2973 0.3; 3270 1.6; 3597 3.4; 3957 4.6; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.4; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.31 | -1.8 dB |
| Peaking | 195 Hz  | 0.81 | -6.4 dB |
| Peaking | 429 Hz  | 0.56 | 10.0 dB |
| Peaking | 1303 Hz | 0.56 | -4.4 dB |
| Peaking | 4848 Hz | 1.52 | 7.4 dB  |
| Peaking | 427 Hz  | 2.15 | 1.4 dB  |
| Peaking | 437 Hz  | 4.29 | -2.2 dB |
| Peaking | 5002 Hz | 6.82 | -1.4 dB |
| Peaking | 6340 Hz | 2.79 | 3.6 dB  |
| Peaking | 7721 Hz | 1.95 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/V-MODA%20Crossfade%20M-100/V-MODA%20Crossfade%20M-100.png)