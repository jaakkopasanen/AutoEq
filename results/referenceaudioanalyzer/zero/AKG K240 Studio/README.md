# AKG K240 Studio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.8; 49 -2.4; 54 -3.0; 60 -3.4; 66 -3.8; 72 -4.4; 79 -5.1; 87 -5.7; 96 -6.3; 106 -6.8; 116 -7.1; 128 -7.4; 141 -7.7; 155 -7.8; 170 -7.8; 187 -7.8; 206 -7.8; 227 -7.9; 249 -8.0; 274 -7.8; 302 -7.6; 332 -7.5; 365 -7.5; 402 -7.2; 442 -6.6; 486 -5.7; 535 -4.1; 588 -3.0; 647 -4.1; 712 -5.3; 783 -5.5; 861 -5.2; 947 -5.1; 1042 -4.8; 1146 -4.3; 1261 -3.6; 1387 -2.6; 1526 -1.5; 1678 -1.4; 1846 -2.4; 2031 -4.0; 2234 -5.5; 2457 -6.1; 2703 -7.1; 2973 -7.5; 3270 -7.4; 3597 -8.1; 3957 -8.4; 4353 -6.4; 4788 -2.6; 5267 -1.8; 5793 -4.9; 6373 -8.7; 7010 -11.1; 7711 -12.6; 8482 -13.9; 9330 -14.9; 10263 -15.6; 11289 -15.6; 12418 -13.9; 13660 -9.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 Studio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.99 | 6.9 dB  |
| Peaking | 592 Hz   | 5.2  | 3.6 dB  |
| Peaking | 1578 Hz  | 2.29 | 5.6 dB  |
| Peaking | 5221 Hz  | 4.76 | 8.0 dB  |
| Peaking | 9927 Hz  | 1.05 | -9.7 dB |
| Peaking | 62 Hz    | 1.77 | 1.4 dB  |
| Peaking | 180 Hz   | 0.77 | -1.9 dB |
| Peaking | 3656 Hz  | 3.72 | -1.8 dB |
| Peaking | 12414 Hz | 2.48 | -4.5 dB |
| Peaking | 14015 Hz | 1.05 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K240%20Studio/AKG%20K240%20Studio.png)