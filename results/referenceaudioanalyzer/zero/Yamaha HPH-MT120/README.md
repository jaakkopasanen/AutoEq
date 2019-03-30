# Yamaha HPH-MT120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.3; 34 -2.4; 37 -3.6; 41 -4.8; 45 -5.8; 49 -6.5; 54 -7.1; 60 -7.3; 66 -7.4; 72 -7.8; 79 -8.3; 87 -8.8; 96 -9.3; 106 -9.6; 116 -9.8; 128 -9.9; 141 -9.9; 155 -9.9; 170 -9.6; 187 -9.4; 206 -9.1; 227 -8.6; 249 -8.2; 274 -7.5; 302 -7.0; 332 -6.7; 365 -6.5; 402 -6.2; 442 -5.8; 486 -5.4; 535 -5.0; 588 -4.6; 647 -4.4; 712 -4.4; 783 -4.8; 861 -5.6; 947 -6.6; 1042 -7.4; 1146 -8.0; 1261 -8.4; 1387 -8.5; 1526 -8.3; 1678 -8.3; 1846 -8.3; 2031 -8.3; 2234 -8.3; 2457 -8.2; 2703 -7.4; 2973 -6.5; 3270 -6.0; 3597 -6.1; 3957 -6.3; 4353 -5.8; 4788 -4.6; 5267 -3.1; 5793 -2.8; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HPH-MT120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH-MT120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.25 | 6.9 dB  |
| Peaking | 132 Hz  | 0.65 | -3.8 dB |
| Peaking | 720 Hz  | 0.91 | 4.5 dB  |
| Peaking | 1228 Hz | 0.76 | -3.9 dB |
| Peaking | 5893 Hz | 2.47 | 4.6 dB  |
| Peaking | 51 Hz   | 4.19 | -0.7 dB |
| Peaking | 2410 Hz | 4.69 | -0.8 dB |
| Peaking | 3168 Hz | 4.92 | 1.0 dB  |
| Peaking | 8215 Hz | 5.16 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20HPH-MT120/Yamaha%20HPH-MT120.png)