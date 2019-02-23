# Koss QZ900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.7; 23 -15.6; 25 -15.4; 28 -15.3; 31 -15.1; 34 -15.0; 37 -14.8; 41 -14.7; 45 -14.5; 49 -14.4; 54 -14.3; 60 -14.2; 66 -14.1; 72 -13.9; 79 -13.7; 87 -13.6; 96 -13.9; 106 -14.3; 116 -14.5; 128 -14.6; 141 -14.6; 155 -14.4; 170 -14.0; 187 -13.5; 206 -12.9; 227 -12.4; 249 -11.5; 274 -9.8; 302 -9.0; 332 -8.7; 365 -7.9; 402 -7.1; 442 -6.4; 486 -6.1; 535 -5.9; 588 -5.9; 647 -5.7; 712 -5.4; 783 -4.9; 861 -4.3; 947 -3.8; 1042 -3.6; 1146 -3.6; 1261 -4.1; 1387 -4.9; 1526 -5.5; 1678 -7.8; 1846 -9.5; 2031 -9.4; 2234 -5.9; 2457 -1.5; 2703 -11.4; 2973 -12.3; 3270 -5.8; 3597 -2.0; 3957 -0.9; 4353 -1.5; 4788 -0.5; 5267 -3.2; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZ900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZ900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.32 | -8.9 dB  |
| Peaking | 133 Hz   | 1.33 | -5.1 dB  |
| Peaking | 213 Hz   | 2.42 | -3.4 dB  |
| Peaking | 4998 Hz  | 1.85 | 6.0 dB   |
| Peaking | 22050 Hz | 2.4  | 3.2 dB   |
| Peaking | 1108 Hz  | 1.09 | 3.4 dB   |
| Peaking | 1902 Hz  | 3.61 | -4.6 dB  |
| Peaking | 2434 Hz  | 6.84 | 10.2 dB  |
| Peaking | 2852 Hz  | 3.08 | -11.4 dB |
| Peaking | 3575 Hz  | 3.82 | 6.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20QZ900/Koss%20QZ900.png)