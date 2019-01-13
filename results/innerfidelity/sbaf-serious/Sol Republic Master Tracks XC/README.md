# Sol Republic Master Tracks XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.2; 25 -0.2; 28 -0.7; 31 -1.1; 34 -1.4; 37 -1.7; 41 -1.9; 45 -2.2; 49 -2.3; 54 -2.5; 60 -2.6; 66 -2.8; 72 -2.8; 79 -3.1; 87 -3.2; 96 -3.4; 106 -3.7; 116 -4.3; 128 -4.8; 141 -4.8; 155 -5.0; 170 -4.6; 187 -5.0; 206 -4.9; 227 -4.6; 249 -4.3; 274 -4.0; 302 -3.5; 332 -2.8; 365 -1.8; 402 -1.0; 442 -1.0; 486 -1.7; 535 -1.3; 588 -0.7; 647 -0.5; 712 -0.4; 783 -0.3; 861 -0.3; 947 -0.0; 1042 0.1; 1146 0.3; 1261 1.0; 1387 1.2; 1526 1.6; 1678 2.2; 1846 3.3; 2031 4.8; 2234 5.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 2.8; 4788 0.8; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sol Republic Master Tracks XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sol Republic Master Tracks XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 1.42 | -1.2 dB |
| Peaking | 182 Hz  | 0.51 | -5.0 dB |
| Peaking | 401 Hz  | 3.12 | 1.6 dB  |
| Peaking | 2793 Hz | 1.15 | 6.7 dB  |
| Peaking | 5949 Hz | 4.5  | 5.4 dB  |
| Peaking | 638 Hz  | 5.62 | 0.5 dB  |
| Peaking | 4608 Hz | 1.96 | 4.0 dB  |
| Peaking | 4673 Hz | 6.56 | -6.1 dB |
| Peaking | 5087 Hz | 0.51 | -0.8 dB |
| Peaking | 8124 Hz | 4.57 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sol%20Republic%20Master%20Tracks%20XC/Sol%20Republic%20Master%20Tracks%20XC.png)