# Koss QZ900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.4; 25 -15.2; 28 -15.1; 31 -14.9; 34 -14.8; 37 -14.6; 41 -14.5; 45 -14.4; 49 -14.3; 54 -14.2; 60 -14.0; 66 -13.9; 72 -13.7; 79 -13.5; 87 -13.5; 96 -13.7; 106 -14.1; 116 -14.4; 128 -14.5; 141 -14.4; 155 -14.1; 170 -13.8; 187 -13.3; 206 -12.8; 227 -12.3; 249 -11.4; 274 -9.8; 302 -8.9; 332 -8.6; 365 -7.9; 402 -7.0; 442 -6.4; 486 -6.1; 535 -6.0; 588 -6.0; 647 -5.9; 712 -5.5; 783 -5.0; 861 -4.4; 947 -3.9; 1042 -3.8; 1146 -3.7; 1261 -4.3; 1387 -5.1; 1526 -5.7; 1678 -7.9; 1846 -9.8; 2031 -9.9; 2234 -6.6; 2457 -3.2; 2703 -11.3; 2973 -12.6; 3270 -5.9; 3597 -1.4; 3957 -0.7; 4353 -1.0; 4788 -0.5; 5267 -3.4; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZ900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZ900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.31 | -8.7 dB  |
| Peaking | 134 Hz   | 1.32 | -5.0 dB  |
| Peaking | 216 Hz   | 2.47 | -3.3 dB  |
| Peaking | 4873 Hz  | 1.97 | 6.2 dB   |
| Peaking | 22050 Hz | 2.36 | 3.2 dB   |
| Peaking | 1895 Hz  | 2.46 | -13.2 dB |
| Peaking | 2067 Hz  | 0.84 | 9.8 dB   |
| Peaking | 2903 Hz  | 5.11 | -13.3 dB |
| Peaking | 3628 Hz  | 8.57 | 2.2 dB   |
| Peaking | 5200 Hz  | 7.78 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20QZ900/Koss%20QZ900.png)