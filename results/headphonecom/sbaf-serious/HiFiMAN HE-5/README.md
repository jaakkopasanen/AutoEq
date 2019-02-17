# HiFiMAN HE-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -2.1; 37 -2.8; 41 -3.1; 45 -3.5; 49 -4.2; 54 -4.8; 60 -5.2; 66 -5.3; 72 -5.3; 79 -5.4; 87 -5.6; 96 -5.8; 106 -5.8; 116 -6.1; 128 -6.4; 141 -6.7; 155 -6.9; 170 -7.0; 187 -7.3; 206 -7.3; 227 -7.3; 249 -7.3; 274 -7.2; 302 -7.1; 332 -7.0; 365 -7.2; 402 -7.8; 442 -7.5; 486 -7.2; 535 -7.1; 588 -6.9; 647 -6.8; 712 -6.3; 783 -6.0; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -5.2; 1261 -5.0; 1387 -4.6; 1526 -5.1; 1678 -4.2; 1846 -3.0; 2031 -2.1; 2234 -3.9; 2457 -3.7; 2703 -4.0; 2973 -5.8; 3270 -6.4; 3597 -6.6; 3957 -7.5; 4353 -9.9; 4788 -8.0; 5267 -6.5; 5793 -8.3; 6373 -10.3; 7010 -11.6; 7711 -12.1; 8482 -13.7; 9330 -15.4; 10263 -13.1; 11289 -9.1; 12418 -8.5; 13660 -8.3; 15026 -7.2; 16529 -9.5; 18182 -13.1; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.95 | 6.3 dB  |
| Peaking | 2044 Hz  | 1.73 | 4.0 dB  |
| Peaking | 4298 Hz  | 7.87 | -3.2 dB |
| Peaking | 8927 Hz  | 1.82 | -8.6 dB |
| Peaking | 19007 Hz | 1.1  | -7.8 dB |
| Peaking | 331 Hz   | 0.75 | -1.0 dB |
| Peaking | 1257 Hz  | 6.09 | 0.9 dB  |
| Peaking | 5248 Hz  | 9.19 | 1.7 dB  |
| Peaking | 6673 Hz  | 7.64 | -1.9 dB |
| Peaking | 14949 Hz | 4.08 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -7.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)