# V-Moda Crossfade M-80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 2.0; 28 1.5; 31 1.0; 34 0.7; 37 0.5; 41 0.1; 45 -0.1; 49 -0.4; 54 -0.7; 60 -1.0; 66 -1.3; 72 -1.6; 79 -1.9; 87 -2.1; 96 -2.7; 106 -2.9; 116 -2.7; 128 -2.7; 141 -3.0; 155 -3.2; 170 -2.9; 187 -2.8; 206 -2.5; 227 -4.2; 249 -4.0; 274 -3.2; 302 -2.3; 332 -1.3; 365 -0.4; 402 0.1; 442 0.6; 486 1.1; 535 2.0; 588 2.9; 647 3.1; 712 2.8; 783 2.5; 861 1.6; 947 0.7; 1042 -0.4; 1146 -1.3; 1261 -2.0; 1387 -2.4; 1526 -2.6; 1678 -2.2; 1846 -1.3; 2031 -0.2; 2234 0.5; 2457 0.7; 2703 0.1; 2973 -0.9; 3270 -1.7; 3597 -0.8; 3957 1.7; 4353 2.1; 4788 1.9; 5267 6.0; 5793 6.0; 6373 3.3; 7010 1.9; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade M-80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.83 | 3.6 dB  |
| Peaking | 126 Hz  | 0.63 | -3.0 dB |
| Peaking | 249 Hz  | 3.38 | -2.8 dB |
| Peaking | 629 Hz  | 2.55 | 3.9 dB  |
| Peaking | 5595 Hz | 3.85 | 6.7 dB  |
| Peaking | 836 Hz  | 3.31 | 1.5 dB  |
| Peaking | 1499 Hz | 1.58 | -3.2 dB |
| Peaking | 2345 Hz | 2.06 | 2.0 dB  |
| Peaking | 3299 Hz | 3.17 | -2.6 dB |
| Peaking | 4060 Hz | 6.96 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20M-80/V-Moda%20Crossfade%20M-80.png)