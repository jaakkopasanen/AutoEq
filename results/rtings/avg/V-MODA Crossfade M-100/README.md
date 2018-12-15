# V-MODA Crossfade M-100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.8; 23 -1.1; 25 -1.2; 28 -1.5; 31 -1.6; 34 -1.6; 37 -1.6; 41 -1.6; 45 -1.6; 49 -1.7; 54 -1.7; 60 -1.8; 66 -2.0; 72 -2.2; 79 -2.5; 87 -2.8; 96 -3.0; 106 -3.4; 116 -3.7; 128 -4.0; 141 -4.2; 155 -4.2; 170 -3.9; 187 -3.5; 206 -2.8; 227 -1.8; 249 -0.7; 274 0.2; 302 1.8; 332 4.3; 365 4.2; 402 4.5; 442 4.2; 486 4.5; 535 4.7; 588 4.4; 647 3.7; 712 2.8; 783 1.9; 861 1.1; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -0.9; 1387 -1.1; 1526 -1.1; 1678 -1.3; 1846 -1.8; 2031 -2.1; 2234 -1.6; 2457 -0.8; 2703 -0.2; 2973 -1.3; 3270 -1.0; 3597 0.2; 3957 2.2; 4353 4.7; 4788 5.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.6; 10263 -0.3; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.21 | -1.2 dB |
| Peaking | 183 Hz  | 0.75 | -6.2 dB |
| Peaking | 421 Hz  | 0.65 | 8.4 dB  |
| Peaking | 2568 Hz | 0.23 | -3.4 dB |
| Peaking | 5292 Hz | 1.51 | 9.6 dB  |
| Peaking | 443 Hz  | 9.36 | -0.8 dB |
| Peaking | 2633 Hz | 5.13 | 2.9 dB  |
| Peaking | 2850 Hz | 2.15 | -2.1 dB |
| Peaking | 7889 Hz | 0.44 | 0.8 dB  |
| Peaking | 8450 Hz | 2.31 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20Crossfade%20M-100/V-MODA%20Crossfade%20M-100.png)