# Pioneer Monitor 10 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.3; 23 -4.4; 25 -4.5; 28 -4.5; 31 -4.6; 34 -4.6; 37 -4.6; 41 -4.6; 45 -4.7; 49 -4.8; 54 -4.9; 60 -4.9; 66 -4.9; 72 -4.9; 79 -4.8; 87 -4.7; 96 -4.6; 106 -5.0; 116 -5.0; 128 -3.9; 141 -2.9; 155 -6.4; 170 -4.1; 187 -4.3; 206 -5.5; 227 -6.1; 249 -6.4; 274 -6.4; 302 -5.7; 332 -5.5; 365 -4.4; 402 -3.2; 442 -1.7; 486 -0.6; 535 1.0; 588 2.8; 647 3.8; 712 4.1; 783 3.2; 861 1.6; 947 0.1; 1042 0.3; 1146 -0.1; 1261 -1.3; 1387 -4.2; 1526 -7.5; 1678 -9.2; 1846 -7.5; 2031 -3.8; 2234 -0.6; 2457 0.3; 2703 -0.2; 2973 2.3; 3270 3.7; 3597 3.2; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.4  | -4.6 dB  |
| Peaking | 126 Hz  | 0.94 | -2.4 dB  |
| Peaking | 269 Hz  | 2.06 | -5.9 dB  |
| Peaking | 1697 Hz | 3.73 | -10.8 dB |
| Peaking | 4649 Hz | 1.31 | 6.6 dB   |
| Peaking | 375 Hz  | 3.43 | -2.0 dB  |
| Peaking | 639 Hz  | 2.83 | 4.0 dB   |
| Peaking | 760 Hz  | 4.35 | 2.4 dB   |
| Peaking | 6357 Hz | 3.93 | 4.7 dB   |
| Peaking | 7128 Hz | 1.5  | -2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20Monitor%2010%20II/Pioneer%20Monitor%2010%20II.png)