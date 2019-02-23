# Audeze LCD-XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.5; 25 -6.4; 28 -6.2; 31 -6.2; 34 -6.3; 37 -6.4; 41 -6.2; 45 -6.1; 49 -6.2; 54 -6.7; 60 -7.6; 66 -7.9; 72 -8.1; 79 -8.3; 87 -8.5; 96 -8.7; 106 -8.9; 116 -8.9; 128 -9.1; 141 -9.2; 155 -9.2; 170 -9.3; 187 -9.4; 206 -9.2; 227 -8.9; 249 -8.4; 274 -7.8; 302 -7.9; 332 -7.0; 365 -5.9; 402 -6.1; 442 -6.0; 486 -6.0; 535 -5.3; 588 -5.0; 647 -4.7; 712 -4.7; 783 -5.3; 861 -5.9; 947 -6.7; 1042 -7.3; 1146 -8.0; 1261 -8.9; 1387 -10.1; 1526 -10.9; 1678 -11.4; 1846 -11.0; 2031 -9.9; 2234 -7.9; 2457 -6.2; 2703 -4.7; 2973 -4.7; 3270 -4.5; 3597 -7.6; 3957 -8.9; 4353 -4.3; 4788 -1.2; 5267 -2.0; 5793 -0.5; 6373 -1.2; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.5; 13660 -11.2; 15026 -12.5; 16529 -13.6; 18182 -14.1; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 141 Hz   | 0.94 | -3.2 dB |
| Peaking | 1695 Hz  | 2.25 | -5.6 dB |
| Peaking | 2772 Hz  | 4.9  | 2.7 dB  |
| Peaking | 5793 Hz  | 2.51 | 6.6 dB  |
| Peaking | 17318 Hz | 0.9  | -8.6 dB |
| Peaking | 394 Hz   | 4.81 | 0.8 dB  |
| Peaking | 663 Hz   | 2.68 | 2.4 dB  |
| Peaking | 3961 Hz  | 7.2  | -4.3 dB |
| Peaking | 4615 Hz  | 9.57 | 3.7 dB  |
| Peaking | 11738 Hz | 5.23 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -9.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-XC/Audeze%20LCD-XC.png)