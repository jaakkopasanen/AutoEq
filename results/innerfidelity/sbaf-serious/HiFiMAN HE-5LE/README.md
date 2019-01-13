# HiFiMAN HE-5LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 0.0; 23 2.6; 25 1.7; 28 0.9; 31 0.8; 34 0.9; 37 1.1; 41 1.3; 45 1.4; 49 1.6; 54 1.8; 60 1.6; 66 1.4; 72 1.3; 79 1.2; 87 1.0; 96 0.6; 106 0.5; 116 0.2; 128 -0.5; 141 -1.3; 155 -2.1; 170 -2.4; 187 -2.6; 206 -2.7; 227 -2.8; 249 -3.0; 274 -3.1; 302 -3.0; 332 -3.0; 365 -3.0; 402 -2.9; 442 -2.8; 486 -2.8; 535 -3.0; 588 -2.8; 647 -1.1; 712 0.3; 783 1.5; 861 1.0; 947 0.1; 1042 -0.1; 1146 0.9; 1261 1.9; 1387 2.8; 1526 3.7; 1678 4.1; 1846 5.4; 2031 4.1; 2234 2.8; 2457 4.3; 2703 3.5; 2973 2.8; 3270 2.2; 3597 2.4; 3957 0.9; 4353 -0.5; 4788 -3.2; 5267 0.3; 5793 -1.7; 6373 -3.7; 7010 -3.2; 7711 -3.6; 8482 -6.2; 9330 -7.4; 10263 -3.8; 11289 -0.1; 12418 0.0; 13660 -0.7; 15026 -1.0; 16529 -1.0; 18182 -1.6; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 15 Hz    |  0.07 | 2.1 dB  |
| Peaking | 271 Hz   |  0.6  | -4.2 dB |
| Peaking | 1751 Hz  |  1.5  | 4.6 dB  |
| Peaking | 2814 Hz  |  2.53 | 2.4 dB  |
| Peaking | 8734 Hz  |  2.05 | -6.9 dB |
| Peaking | 33 Hz    |  3.11 | -1.1 dB |
| Peaking | 554 Hz   |  4.65 | -1.6 dB |
| Peaking | 762 Hz   |  5.83 | 2.4 dB  |
| Peaking | 6189 Hz  | 10.4  | -2.6 dB |
| Peaking | 11506 Hz |  6.12 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)