# Monster Beats Tour

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -10.6; 23 -10.5; 25 -10.4; 28 -10.3; 31 -10.2; 34 -10.1; 37 -10.0; 41 -9.8; 45 -9.7; 49 -9.6; 54 -9.5; 60 -9.3; 66 -9.2; 72 -9.2; 79 -9.1; 87 -9.0; 96 -8.9; 106 -8.7; 116 -8.3; 128 -8.1; 141 -7.9; 155 -7.5; 170 -7.0; 187 -6.6; 206 -6.1; 227 -5.5; 249 -5.0; 274 -4.4; 302 -3.8; 332 -3.2; 365 -2.6; 402 -2.1; 442 -1.4; 486 -1.0; 535 -0.5; 588 0.2; 647 0.5; 712 0.7; 783 1.0; 861 0.7; 947 0.4; 1042 -0.1; 1146 -0.4; 1261 -1.0; 1387 -1.9; 1526 -3.0; 1678 -4.0; 1846 -4.9; 2031 -5.9; 2234 -7.3; 2457 -7.6; 2703 -6.1; 2973 -2.3; 3270 0.9; 3597 2.3; 3957 1.2; 4353 -2.4; 4788 -6.6; 5267 -11.7; 5793 -4.9; 6373 0.7; 7010 2.3; 7711 0.3; 8482 -0.2; 9330 -2.6; 10263 -0.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Tour GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Tour ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 24 Hz   |  0.21 | -10.2 dB |
| Peaking | 157 Hz  |  0.8  | -3.9 dB  |
| Peaking | 2366 Hz |  1.94 | -8.6 dB  |
| Peaking | 3496 Hz |  3.18 | 5.6 dB   |
| Peaking | 5176 Hz |  6.18 | -12.5 dB |
| Peaking | 772 Hz  |  1.9  | 1.9 dB   |
| Peaking | 1631 Hz |  4.4  | -1.3 dB  |
| Peaking | 5564 Hz | 11.95 | -3.2 dB  |
| Peaking | 6738 Hz |  4.7  | 3.8 dB   |
| Peaking | 9433 Hz |  7.65 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Tour/Monster%20Beats%20Tour.png)