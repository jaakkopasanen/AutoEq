# HiFiMAN HE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.7; 106 5.6; 116 5.4; 128 5.1; 141 5.0; 155 4.8; 170 4.5; 187 4.4; 206 4.9; 227 4.9; 249 4.1; 274 5.4; 302 4.9; 332 4.2; 365 4.2; 402 4.3; 442 3.9; 486 4.0; 535 4.9; 588 5.8; 647 4.6; 712 3.4; 783 2.9; 861 1.1; 947 0.2; 1042 1.2; 1146 2.3; 1261 2.6; 1387 4.7; 1526 5.7; 1678 5.6; 1846 6.0; 2031 5.6; 2234 5.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.8; 4788 5.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -0.6; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.7; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.2  | 6.2 dB  |
| Peaking | 311 Hz   | 1.31 | 2.4 dB  |
| Peaking | 580 Hz   | 4.12 | 3.8 dB  |
| Peaking | 3733 Hz  | 0.43 | 6.9 dB  |
| Peaking | 9085 Hz  | 1.51 | -4.1 dB |
| Peaking | 961 Hz   | 5.65 | -2.9 dB |
| Peaking | 1606 Hz  | 3.36 | 1.9 dB  |
| Peaking | 5387 Hz  | 1.03 | -1.3 dB |
| Peaking | 5935 Hz  | 3.39 | 3.0 dB  |
| Peaking | 13705 Hz | 5.49 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)