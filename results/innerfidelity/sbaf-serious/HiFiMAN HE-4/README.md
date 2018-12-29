# HiFiMAN HE-4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 21 0.0; 23 3.2; 25 3.0; 28 2.7; 31 2.5; 34 2.4; 37 2.2; 41 2.1; 45 2.0; 49 2.0; 54 1.9; 60 1.7; 66 1.5; 72 1.3; 79 1.0; 87 0.6; 96 0.4; 106 -0.0; 116 -0.1; 128 -0.3; 141 -0.6; 155 -0.9; 170 -1.1; 187 -1.4; 206 -1.7; 227 -1.9; 249 -2.0; 274 -2.0; 302 -1.5; 332 -0.7; 365 -0.2; 402 -0.2; 442 -0.4; 486 -0.8; 535 -0.5; 588 -0.2; 647 0.0; 712 2.2; 783 2.4; 861 1.6; 947 0.8; 1042 0.4; 1146 2.2; 1261 1.5; 1387 1.6; 1526 1.8; 1678 2.4; 1846 3.0; 2031 2.8; 2234 1.9; 2457 2.3; 2703 1.2; 2973 0.2; 3270 -1.1; 3597 -1.8; 3957 -3.0; 4353 -4.7; 4788 -4.6; 5267 3.0; 5793 0.5; 6373 -5.4; 7010 -5.3; 7711 -5.1; 8482 -7.5; 9330 -8.5; 10263 -4.5; 11289 -2.0; 12418 -4.1; 13660 -5.7; 15026 -4.0; 16529 -3.0; 18182 -6.5; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.77 | 3.2 dB   |
| Peaking | 1826 Hz  | 1.09 | 2.8 dB   |
| Peaking | 4261 Hz  | 4.78 | -5.0 dB  |
| Peaking | 8755 Hz  | 2.11 | -7.7 dB  |
| Peaking | 20606 Hz | 0.73 | -12.9 dB |
| Peaking | 237 Hz   | 1.39 | -2.1 dB  |
| Peaking | 757 Hz   | 6.79 | 2.5 dB   |
| Peaking | 5477 Hz  | 9.64 | 6.7 dB   |
| Peaking | 6389 Hz  | 6.74 | -3.6 dB  |
| Peaking | 13598 Hz | 7.27 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-4/HiFiMAN%20HE-4.png)