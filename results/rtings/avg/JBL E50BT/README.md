# JBL E50BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.4; 25 -8.0; 28 -8.7; 31 -9.1; 34 -9.4; 37 -9.6; 41 -9.6; 45 -9.6; 49 -9.6; 54 -9.6; 60 -9.6; 66 -9.6; 72 -9.5; 79 -9.4; 87 -9.4; 96 -9.4; 106 -9.5; 116 -9.6; 128 -9.5; 141 -9.4; 155 -9.2; 170 -8.8; 187 -8.2; 206 -7.3; 227 -6.2; 249 -4.8; 274 -2.9; 302 -0.7; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.8; 486 -1.8; 535 -2.7; 588 -3.6; 647 -4.5; 712 -5.3; 783 -6.2; 861 -6.8; 947 -7.1; 1042 -7.1; 1146 -7.4; 1261 -8.2; 1387 -8.9; 1526 -9.7; 1678 -10.9; 1846 -11.2; 2031 -11.0; 2234 -10.5; 2457 -9.1; 2703 -8.6; 2973 -8.1; 3270 -7.0; 3597 -5.4; 3957 -4.9; 4353 -7.0; 4788 -8.3; 5267 -7.0; 5793 -3.5; 6373 -1.8; 7010 -4.4; 7711 -8.6; 8482 -10.7; 9330 -10.8; 10263 -11.1; 11289 -11.0; 12418 -8.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 147 Hz   |  0.23 | -4.4 dB |
| Peaking | 370 Hz   |  1.05 | 10.3 dB |
| Peaking | 1861 Hz  |  1.78 | -5.0 dB |
| Peaking | 6382 Hz  |  4.45 | 6.9 dB  |
| Peaking | 9637 Hz  |  1.51 | -5.4 dB |
| Peaking | 36 Hz    |  2.91 | -0.8 dB |
| Peaking | 299 Hz   | 10.25 | 1.3 dB  |
| Peaking | 3856 Hz  |  5.57 | 2.9 dB  |
| Peaking | 4749 Hz  |  5.86 | -2.3 dB |
| Peaking | 13911 Hz |  4.54 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 5.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E50BT/JBL%20E50BT.png)