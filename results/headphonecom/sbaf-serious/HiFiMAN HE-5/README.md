# HiFiMAN HE-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -1.6; 37 -2.3; 41 -2.6; 45 -3.0; 49 -3.6; 54 -4.2; 60 -4.7; 66 -4.8; 72 -4.8; 79 -4.9; 87 -5.1; 96 -5.3; 106 -5.3; 116 -5.6; 128 -5.9; 141 -6.2; 155 -6.3; 170 -6.5; 187 -6.8; 206 -6.8; 227 -6.8; 249 -6.7; 274 -6.7; 302 -6.6; 332 -6.5; 365 -6.7; 402 -7.3; 442 -7.0; 486 -6.7; 535 -6.6; 588 -6.4; 647 -6.3; 712 -5.8; 783 -5.5; 861 -5.9; 947 -5.9; 1042 -6.0; 1146 -4.7; 1261 -4.5; 1387 -4.1; 1526 -4.6; 1678 -3.7; 1846 -2.5; 2031 -1.6; 2234 -3.4; 2457 -3.2; 2703 -3.5; 2973 -5.3; 3270 -5.9; 3597 -6.1; 3957 -7.0; 4353 -9.4; 4788 -7.5; 5267 -6.0; 5793 -7.8; 6373 -9.8; 7010 -11.1; 7711 -11.6; 8482 -13.2; 9330 -14.9; 10263 -12.5; 11289 -8.6; 12418 -8.0; 13660 -7.8; 15026 -6.7; 16529 -9.0; 18182 -12.6; 20000 -11.8
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
| Peaking | 24 Hz    | 0.65 | 6.1 dB  |
| Peaking | 1915 Hz  | 1.73 | 4.2 dB  |
| Peaking | 2627 Hz  | 6    | 1.7 dB  |
| Peaking | 8909 Hz  | 1.84 | -8.0 dB |
| Peaking | 19007 Hz | 1.21 | -7.3 dB |
| Peaking | 1225 Hz  | 6.96 | 1.0 dB  |
| Peaking | 4351 Hz  | 7.61 | -2.9 dB |
| Peaking | 5175 Hz  | 9.44 | 2.0 dB  |
| Peaking | 9933 Hz  | 6.21 | -2.2 dB |
| Peaking | 11472 Hz | 1.8  | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)