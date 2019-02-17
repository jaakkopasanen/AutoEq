# Koss QZ900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.0; 23 -17.9; 25 -17.7; 28 -17.5; 31 -17.4; 34 -17.2; 37 -17.1; 41 -16.9; 45 -16.8; 49 -16.7; 54 -16.6; 60 -16.5; 66 -16.4; 72 -16.2; 79 -15.9; 87 -15.9; 96 -16.2; 106 -16.6; 116 -16.8; 128 -16.9; 141 -16.9; 155 -16.7; 170 -16.3; 187 -15.8; 206 -15.2; 227 -14.7; 249 -13.7; 274 -12.1; 302 -11.3; 332 -11.0; 365 -10.2; 402 -9.3; 442 -8.7; 486 -8.3; 535 -8.2; 588 -8.2; 647 -8.0; 712 -7.6; 783 -7.2; 861 -6.5; 947 -6.1; 1042 -5.9; 1146 -5.9; 1261 -6.4; 1387 -7.2; 1526 -7.8; 1678 -10.1; 1846 -11.8; 2031 -11.7; 2234 -8.2; 2457 -3.7; 2703 -13.7; 2973 -14.6; 3270 -8.1; 3597 -4.3; 3957 -2.7; 4353 -3.7; 4788 -0.8; 5267 -5.5; 5793 -2.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.5; 18182 -9.6; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZ900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZ900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 1.35 | -11.8 dB |
| Peaking | 34 Hz    | 0.42 | -8.9 dB  |
| Peaking | 152 Hz   | 0.64 | -8.0 dB  |
| Peaking | 227 Hz   | 1.72 | -1.2 dB  |
| Peaking | 1920 Hz  | 3.07 | -6.0 dB  |
| Peaking | 2426 Hz  | 8.99 | 7.8 dB   |
| Peaking | 2882 Hz  | 3.59 | -14.1 dB |
| Peaking | 3650 Hz  | 1.45 | 6.3 dB   |
| Peaking | 6312 Hz  | 6.95 | 5.3 dB   |
| Peaking | 18819 Hz | 1.41 | -4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB  |
| Peaking | 125 Hz   | 1.41 | -9.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20QZ900/Koss%20QZ900.png)