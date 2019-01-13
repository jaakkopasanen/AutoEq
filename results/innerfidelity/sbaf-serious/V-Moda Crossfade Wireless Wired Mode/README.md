# V-Moda Crossfade Wireless Wired Mode
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.7; 25 1.1; 28 0.2; 31 -0.6; 34 -1.2; 37 -1.7; 41 -2.3; 45 -2.8; 49 -3.1; 54 -3.4; 60 -3.6; 66 -3.5; 72 -3.1; 79 -4.1; 87 -5.4; 96 -5.2; 106 -5.0; 116 -5.9; 128 -6.4; 141 -6.5; 155 -6.3; 170 -5.6; 187 -5.5; 206 -4.8; 227 -3.5; 249 -2.0; 274 -0.3; 302 1.4; 332 3.2; 365 5.3; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 5.2; 712 3.9; 783 2.9; 861 1.6; 947 0.5; 1042 -0.4; 1146 -1.0; 1261 -1.6; 1387 -2.2; 1526 -2.7; 1678 -2.9; 1846 -2.5; 2031 -2.0; 2234 -2.2; 2457 -2.1; 2703 -1.1; 2973 -2.0; 3270 -3.3; 3597 -4.2; 3957 -1.2; 4353 1.5; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.2; 9330 -4.4; 10263 -3.1; 11289 -0.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade Wireless Wired Mode GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Wired Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 179 Hz  |  0.51 | -10.3 dB |
| Peaking | 444 Hz  |  0.65 | 13.2 dB  |
| Peaking | 1903 Hz |  0.32 | -4.9 dB  |
| Peaking | 5568 Hz |  1.94 | 9.8 dB   |
| Peaking | 9296 Hz |  4.1  | -5.2 dB  |
| Peaking | 16 Hz   |  1.2  | 4.2 dB   |
| Peaking | 42 Hz   |  2.04 | -1.3 dB  |
| Peaking | 2692 Hz |  3.3  | 2.1 dB   |
| Peaking | 3545 Hz |  4.45 | -3.4 dB  |
| Peaking | 4695 Hz | 10.58 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Wired%20Mode/V-Moda%20Crossfade%20Wireless%20Wired%20Mode.png)