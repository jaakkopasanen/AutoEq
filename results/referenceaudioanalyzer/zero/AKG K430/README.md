# AKG K430
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.8; 128 -1.3; 141 -1.5; 155 -1.8; 170 -2.1; 187 -2.2; 206 -2.4; 227 -2.6; 249 -2.8; 274 -2.8; 302 -3.1; 332 -3.1; 365 -3.1; 402 -3.1; 442 -3.1; 486 -3.1; 535 -3.4; 588 -4.1; 647 -5.5; 712 -7.3; 783 -9.2; 861 -10.7; 947 -11.6; 1042 -11.9; 1146 -11.6; 1261 -10.9; 1387 -9.7; 1526 -8.4; 1678 -7.5; 1846 -6.7; 2031 -5.7; 2234 -4.6; 2457 -4.0; 2703 -4.4; 2973 -6.0; 3270 -8.4; 3597 -10.8; 3957 -12.0; 4353 -11.8; 4788 -10.6; 5267 -12.0; 5793 -14.4; 6373 -14.6; 7010 -12.2; 7711 -8.9; 8482 -7.2; 9330 -7.2; 10263 -7.4; 11289 -8.4; 12418 -10.6; 13660 -11.3; 15026 -8.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K430 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K430 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.06 | 5.6 dB  |
| Peaking | 1010 Hz  | 1.93 | -7.5 dB |
| Peaking | 5809 Hz  | 1.84 | -8.0 dB |
| Peaking | 13329 Hz | 3.14 | -5.1 dB |
| Peaking | 22050 Hz | 2.43 | -1.9 dB |
| Peaking | 229 Hz   | 2.31 | -1.0 dB |
| Peaking | 2650 Hz  | 1.7  | 8.0 dB  |
| Peaking | 4139 Hz  | 0.77 | -8.0 dB |
| Peaking | 5042 Hz  | 2.83 | 7.1 dB  |
| Peaking | 8515 Hz  | 2.11 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | 4.4 dB  |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -7.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K430/AKG%20K430.png)