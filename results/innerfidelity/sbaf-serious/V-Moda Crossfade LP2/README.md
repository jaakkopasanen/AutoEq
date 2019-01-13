# V-Moda Crossfade LP2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.8; 23 -1.1; 25 -1.4; 28 -1.7; 31 -1.9; 34 -2.1; 37 -2.3; 41 -2.4; 45 -2.6; 49 -2.7; 54 -2.8; 60 -2.8; 66 -2.8; 72 -2.8; 79 -3.3; 87 -3.8; 96 -4.5; 106 -5.0; 116 -5.3; 128 -5.6; 141 -5.7; 155 -5.6; 170 -5.3; 187 -5.2; 206 -4.6; 227 -3.6; 249 -2.8; 274 -1.5; 302 -0.2; 332 1.1; 365 2.6; 402 3.7; 442 4.6; 486 4.8; 535 4.7; 588 4.4; 647 3.3; 712 1.7; 783 1.0; 861 0.3; 947 0.0; 1042 -0.0; 1146 -0.0; 1261 0.2; 1387 -0.4; 1526 0.0; 1678 0.9; 1846 2.5; 2031 5.5; 2234 4.9; 2457 5.0; 2703 4.8; 2973 1.5; 3270 -1.8; 3597 0.3; 3957 3.8; 4353 5.4; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade LP2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.98 | -1.6 dB |
| Peaking | 152 Hz  | 0.71 | -6.1 dB |
| Peaking | 463 Hz  | 1.53 | 6.6 dB  |
| Peaking | 2260 Hz | 3.37 | 5.5 dB  |
| Peaking | 5304 Hz | 2.27 | 6.9 dB  |
| Peaking | 1224 Hz | 1.94 | -0.9 dB |
| Peaking | 2796 Hz | 5.74 | 3.8 dB  |
| Peaking | 3268 Hz | 4.23 | -5.0 dB |
| Peaking | 4150 Hz | 4.6  | 2.5 dB  |
| Peaking | 8369 Hz | 4.49 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20LP2/V-Moda%20Crossfade%20LP2.png)