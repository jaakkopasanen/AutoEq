# AKG K72
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -12.2; 25 -12.5; 28 -12.8; 31 -13.2; 34 -13.4; 37 -13.6; 41 -13.6; 45 -13.5; 49 -13.4; 54 -13.0; 60 -12.5; 66 -12.0; 72 -11.4; 79 -11.0; 87 -11.2; 96 -11.9; 106 -12.6; 116 -13.1; 128 -13.2; 141 -13.3; 155 -13.6; 170 -13.9; 187 -13.8; 206 -13.4; 227 -13.1; 249 -12.6; 274 -12.0; 302 -11.2; 332 -10.2; 365 -9.5; 402 -10.1; 442 -11.4; 486 -11.6; 535 -10.8; 588 -10.0; 647 -9.4; 712 -8.2; 783 -7.3; 861 -6.3; 947 -4.5; 1042 -2.3; 1146 -0.6; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -4.4; 4788 -5.3; 5267 -7.5; 5793 -12.8; 6373 -16.3; 7010 -15.8; 7711 -10.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K72 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K72 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 1.02 | -4.8 dB  |
| Peaking | 44 Hz   | 1.9  | -3.1 dB  |
| Peaking | 342 Hz  | 0.2  | -8.0 dB  |
| Peaking | 1743 Hz | 0.39 | 10.7 dB  |
| Peaking | 6478 Hz | 2.88 | -14.4 dB |
| Peaking | 84 Hz   | 4    | 1.5 dB   |
| Peaking | 346 Hz  | 2.18 | 4.1 dB   |
| Peaking | 529 Hz  | 0.45 | -2.3 dB  |
| Peaking | 1142 Hz | 2.76 | 3.6 dB   |
| Peaking | 8456 Hz | 9.39 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -4.6 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K72/AKG%20K72.png)