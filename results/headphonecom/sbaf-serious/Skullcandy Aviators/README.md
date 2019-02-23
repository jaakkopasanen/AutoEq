# Skullcandy Aviators
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -2.0; 41 -3.2; 45 -4.3; 49 -5.1; 54 -5.9; 60 -6.8; 66 -7.7; 72 -8.4; 79 -9.0; 87 -9.3; 96 -9.7; 106 -10.0; 116 -10.2; 128 -10.2; 141 -10.4; 155 -10.3; 170 -10.3; 187 -10.3; 206 -10.2; 227 -10.1; 249 -9.8; 274 -9.1; 302 -8.5; 332 -8.6; 365 -8.2; 402 -8.0; 442 -7.7; 486 -7.4; 535 -7.0; 588 -5.9; 647 -4.9; 712 -5.1; 783 -3.0; 861 -0.7; 947 -0.5; 1042 -0.5; 1146 -0.7; 1261 -2.8; 1387 -4.9; 1526 -6.0; 1678 -6.7; 1846 -6.7; 2031 -6.1; 2234 -5.5; 2457 -4.9; 2703 -4.8; 2973 -5.9; 3270 -6.5; 3597 -5.9; 3957 -7.6; 4353 -11.6; 4788 -11.4; 5267 -7.3; 5793 -3.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -9.3; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Aviators GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Aviators ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.65 | 8.4 dB  |
| Peaking | 104 Hz  | 0.34 | -5.1 dB |
| Peaking | 975 Hz  | 1.95 | 7.2 dB  |
| Peaking | 4588 Hz | 5.41 | -6.8 dB |
| Peaking | 6274 Hz | 5.43 | 6.5 dB  |
| Peaking | 1195 Hz | 6.71 | 1.6 dB  |
| Peaking | 1680 Hz | 1.95 | -1.6 dB |
| Peaking | 2531 Hz | 2.82 | 1.9 dB  |
| Peaking | 9182 Hz | 1.26 | 0.6 dB  |
| Peaking | 9501 Hz | 4.25 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Aviators/Skullcandy%20Aviators.png)