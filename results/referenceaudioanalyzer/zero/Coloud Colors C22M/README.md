# Coloud Colors C22M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.4; 60 -2.1; 66 -2.6; 72 -2.9; 79 -3.2; 87 -3.4; 96 -3.6; 106 -4.1; 116 -4.4; 128 -4.6; 141 -4.8; 155 -5.0; 170 -5.0; 187 -5.0; 206 -5.0; 227 -4.8; 249 -4.6; 274 -4.7; 302 -5.5; 332 -6.3; 365 -6.7; 402 -6.9; 442 -7.4; 486 -8.0; 535 -8.6; 588 -9.3; 647 -10.0; 712 -10.8; 783 -11.3; 861 -11.5; 947 -11.3; 1042 -10.3; 1146 -9.1; 1261 -8.6; 1387 -8.2; 1526 -7.3; 1678 -6.0; 1846 -4.6; 2031 -3.8; 2234 -3.7; 2457 -4.3; 2703 -5.4; 2973 -6.5; 3270 -7.0; 3597 -6.5; 3957 -5.5; 4353 -4.8; 4788 -4.4; 5267 -4.9; 5793 -7.3; 6373 -9.4; 7010 -9.6; 7711 -7.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Coloud Colors C22M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Coloud Colors C22M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.13 | 6.4 dB  |
| Peaking | 843 Hz  | 1.36 | -5.4 dB |
| Peaking | 2107 Hz | 2.87 | 3.7 dB  |
| Peaking | 4873 Hz | 3.62 | 2.8 dB  |
| Peaking | 6640 Hz | 4.01 | -4.0 dB |
| Peaking | 47 Hz   | 2.33 | 1.2 dB  |
| Peaking | 117 Hz  | 0.24 | -0.5 dB |
| Peaking | 256 Hz  | 2.08 | 1.9 dB  |
| Peaking | 3203 Hz | 1.82 | 1.1 dB  |
| Peaking | 3233 Hz | 4.01 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -5.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Coloud%20Colors%20C22M/Coloud%20Colors%20C22M.png)