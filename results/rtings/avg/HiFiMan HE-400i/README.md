# HiFiMan HE-400i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.4; 41 4.8; 45 4.3; 49 3.8; 54 3.3; 60 2.9; 66 2.4; 72 2.0; 79 1.6; 87 1.2; 96 0.8; 106 0.4; 116 0.2; 128 -0.1; 141 -0.3; 155 -0.5; 170 -0.6; 187 -0.6; 206 -0.6; 227 -0.6; 249 -0.7; 274 -1.0; 302 -1.1; 332 -1.3; 365 -1.4; 402 -1.3; 442 -0.7; 486 -0.1; 535 -0.4; 588 -1.0; 647 -1.3; 712 -0.9; 783 -1.2; 861 -0.8; 947 -0.1; 1042 0.1; 1146 0.5; 1261 0.6; 1387 0.5; 1526 0.2; 1678 0.3; 1846 1.1; 2031 0.8; 2234 1.3; 2457 -0.0; 2703 -0.5; 2973 -1.8; 3270 -1.8; 3597 -2.2; 3957 -2.0; 4353 -1.3; 4788 -0.3; 5267 0.9; 5793 1.8; 6373 -2.6; 7010 -5.2; 7711 -5.8; 8482 -6.4; 9330 -4.7; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 -0.5; 15026 -2.6; 16529 -3.9; 18182 -4.7; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-400i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-400i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.57 | 6.3 dB  |
| Peaking | 251 Hz   | 0.51 | -1.2 dB |
| Peaking | 3509 Hz  | 4.39 | -2.3 dB |
| Peaking | 8081 Hz  | 3.27 | -7.0 dB |
| Peaking | 18403 Hz | 1.28 | -5.3 dB |
| Peaking | 726 Hz   | 4.08 | -0.8 dB |
| Peaking | 1957 Hz  | 2.78 | 1.3 dB  |
| Peaking | 5678 Hz  | 6.67 | 3.7 dB  |
| Peaking | 6756 Hz  | 6.92 | -2.6 dB |
| Peaking | 15754 Hz | 5.82 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20HE-400i/HiFiMan%20HE-400i.png)