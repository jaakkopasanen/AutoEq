# Pioneer Monitor 10II B in box
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.0; 23 -9.1; 25 -9.1; 28 -9.1; 31 -9.1; 34 -9.2; 37 -9.2; 41 -9.1; 45 -9.0; 49 -9.0; 54 -9.1; 60 -9.0; 66 -9.0; 72 -9.0; 79 -8.9; 87 -8.7; 96 -8.2; 106 -7.1; 116 -5.5; 128 -5.4; 141 -9.8; 155 -11.4; 170 -7.5; 187 -10.9; 206 -11.2; 227 -11.5; 249 -11.1; 274 -10.2; 302 -9.5; 332 -8.5; 365 -7.4; 402 -6.1; 442 -4.7; 486 -3.5; 535 -2.0; 588 -0.1; 647 1.1; 712 1.7; 783 1.3; 861 0.3; 947 0.2; 1042 0.0; 1146 1.2; 1261 -0.4; 1387 -3.9; 1526 -8.8; 1678 -13.1; 1846 -14.0; 2031 -8.7; 2234 -2.8; 2457 -0.3; 2703 -2.4; 2973 -0.2; 3270 3.0; 3597 2.3; 3957 5.7; 4353 6.0; 4788 5.6; 5267 5.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.9; 11289 -1.2; 12418 0.0; 13660 0.0; 15026 -0.7; 16529 -0.1; 18182 0.0; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10II B in box GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10II B in box ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.87 | -5.5 dB  |
| Peaking | 57 Hz   | 0.48 | -7.6 dB  |
| Peaking | 240 Hz  | 1.21 | -10.2 dB |
| Peaking | 1782 Hz | 4.15 | -16.4 dB |
| Peaking | 4795 Hz | 1.47 | 6.5 dB   |
| Peaking | 121 Hz  | 9.7  | 2.9 dB   |
| Peaking | 715 Hz  | 1.9  | 5.7 dB   |
| Peaking | 1172 Hz | 4.65 | 4.5 dB   |
| Peaking | 2585 Hz | 0.16 | -3.7 dB  |
| Peaking | 4098 Hz | 0.47 | 3.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20Monitor%2010II%20B%20in%20box/Pioneer%20Monitor%2010II%20B%20in%20box.png)