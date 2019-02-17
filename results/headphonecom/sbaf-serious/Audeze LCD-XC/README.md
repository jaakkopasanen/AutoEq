# Audeze LCD-XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -5.9; 25 -5.8; 28 -5.6; 31 -5.5; 34 -5.6; 37 -5.7; 41 -5.6; 45 -5.5; 49 -5.5; 54 -6.1; 60 -7.0; 66 -7.3; 72 -7.4; 79 -7.6; 87 -7.9; 96 -8.1; 106 -8.3; 116 -8.2; 128 -8.5; 141 -8.6; 155 -8.6; 170 -8.7; 187 -8.7; 206 -8.6; 227 -8.2; 249 -7.8; 274 -7.1; 302 -7.2; 332 -6.4; 365 -5.3; 402 -5.4; 442 -5.3; 486 -5.4; 535 -4.6; 588 -4.4; 647 -4.0; 712 -4.0; 783 -4.6; 861 -5.3; 947 -6.0; 1042 -6.7; 1146 -7.4; 1261 -8.2; 1387 -9.4; 1526 -10.3; 1678 -10.7; 1846 -10.3; 2031 -9.2; 2234 -7.3; 2457 -5.6; 2703 -4.0; 2973 -4.0; 3270 -3.9; 3597 -6.9; 3957 -8.3; 4353 -3.6; 4788 -0.7; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.6; 15026 -11.8; 16529 -12.9; 18182 -13.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 683 Hz   |  1.92 | 3.1 dB  |
| Peaking | 1704 Hz  |  1.6  | -4.8 dB |
| Peaking | 2731 Hz  |  3.56 | 3.7 dB  |
| Peaking | 5673 Hz  |  2.38 | 6.9 dB  |
| Peaking | 17297 Hz |  0.93 | -7.7 dB |
| Peaking | 37 Hz    |  1.36 | 1.3 dB  |
| Peaking | 146 Hz   |  0.82 | -2.6 dB |
| Peaking | 880 Hz   |  0.15 | 0.4 dB  |
| Peaking | 3905 Hz  | 10.2  | -4.0 dB |
| Peaking | 11955 Hz |  5.98 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-XC/Audeze%20LCD-XC.png)