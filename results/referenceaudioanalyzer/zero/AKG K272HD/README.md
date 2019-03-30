# AKG K272HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.9; 96 -1.2; 106 -1.5; 116 -1.9; 128 -2.3; 141 -2.6; 155 -2.7; 170 -2.6; 187 -2.6; 206 -2.6; 227 -3.0; 249 -4.0; 274 -5.3; 302 -6.4; 332 -7.0; 365 -7.6; 402 -8.1; 442 -8.4; 486 -8.7; 535 -9.2; 588 -10.1; 647 -10.6; 712 -9.3; 783 -6.8; 861 -5.6; 947 -5.9; 1042 -6.5; 1146 -7.0; 1261 -7.4; 1387 -7.7; 1526 -8.2; 1678 -8.9; 1846 -9.4; 2031 -8.8; 2234 -7.5; 2457 -6.9; 2703 -7.0; 2973 -7.1; 3270 -6.8; 3597 -6.1; 3957 -5.3; 4353 -4.5; 4788 -3.0; 5267 -0.7; 5793 -0.8; 6373 -5.3; 7010 -10.5; 7711 -13.2; 8482 -13.6; 9330 -13.8; 10263 -15.2; 11289 -16.6; 12418 -16.3; 13660 -12.9; 15026 -7.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K272HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.26 | 5.1 dB   |
| Peaking | 128 Hz   | 0.32 | 3.9 dB   |
| Peaking | 499 Hz   | 1.01 | -4.7 dB  |
| Peaking | 5475 Hz  | 2.85 | 10.1 dB  |
| Peaking | 10318 Hz | 0.87 | -10.3 dB |
| Peaking | 889 Hz   | 5.76 | 2.5 dB   |
| Peaking | 1812 Hz  | 3.4  | -2.7 dB  |
| Peaking | 12210 Hz | 4.33 | -3.0 dB  |
| Peaking | 13661 Hz | 3.11 | -3.4 dB  |
| Peaking | 14936 Hz | 1.1  | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 3.6 dB  |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K272HD/AKG%20K272HD.png)