# Yamaha HPH-200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.5; 54 -3.9; 60 -5.2; 66 -6.1; 72 -6.7; 79 -7.2; 87 -7.7; 96 -8.0; 106 -8.2; 116 -8.2; 128 -8.3; 141 -8.1; 155 -7.8; 170 -7.6; 187 -7.3; 206 -7.0; 227 -6.8; 249 -6.6; 274 -6.5; 302 -6.2; 332 -5.7; 365 -5.4; 402 -5.1; 442 -4.9; 486 -4.7; 535 -4.7; 588 -4.5; 647 -4.3; 712 -4.3; 783 -4.4; 861 -4.6; 947 -4.6; 1042 -4.7; 1146 -5.0; 1261 -5.3; 1387 -5.6; 1526 -5.9; 1678 -6.2; 1846 -6.3; 2031 -6.3; 2234 -6.3; 2457 -6.5; 2703 -6.4; 2973 -5.9; 3270 -4.8; 3597 -4.9; 3957 -5.2; 4353 -3.1; 4788 -0.5; 5267 -0.9; 5793 -5.8; 6373 -9.8; 7010 -12.1; 7711 -14.8; 8482 -16.8; 9330 -16.3; 10263 -13.8; 11289 -12.1; 12418 -10.5; 13660 -7.0; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HPH-200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH-200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.53 | 8.6 dB   |
| Peaking | 82 Hz    | 0.6  | -5.5 dB  |
| Peaking | 651 Hz   | 0.69 | 2.4 dB   |
| Peaking | 4986 Hz  | 2.83 | 9.1 dB   |
| Peaking | 8633 Hz  | 1.39 | -11.3 dB |
| Peaking | 2905 Hz  | 1.63 | -0.8 dB  |
| Peaking | 3321 Hz  | 3.62 | 2.0 dB   |
| Peaking | 3941 Hz  | 6.59 | -1.0 dB  |
| Peaking | 12166 Hz | 2.64 | -2.5 dB  |
| Peaking | 13969 Hz | 1.66 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB   |
| Peaking | 62 Hz    | 1.41 | -0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20HPH-200/Yamaha%20HPH-200.png)