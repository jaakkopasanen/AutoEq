# AKG K420
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.7; 106 -1.1; 116 -1.5; 128 -1.9; 141 -2.1; 155 -2.5; 170 -2.6; 187 -2.8; 206 -2.9; 227 -3.2; 249 -3.3; 274 -3.5; 302 -3.6; 332 -3.8; 365 -3.8; 402 -3.8; 442 -3.8; 486 -3.8; 535 -3.6; 588 -3.5; 647 -3.5; 712 -3.6; 783 -3.8; 861 -3.8; 947 -4.1; 1042 -4.3; 1146 -4.7; 1261 -5.1; 1387 -5.6; 1526 -6.2; 1678 -6.9; 1846 -7.8; 2031 -9.0; 2234 -10.6; 2457 -12.8; 2703 -15.4; 2973 -17.4; 3270 -17.4; 3597 -15.3; 3957 -11.9; 4353 -8.4; 4788 -6.8; 5267 -10.8; 5793 -13.6; 6373 -12.9; 7010 -9.7; 7711 -7.7; 8482 -7.6; 9330 -8.1; 10263 -9.1; 11289 -11.3; 12418 -13.3; 13660 -13.1; 15026 -10.8; 16529 -7.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K420 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.22 | 6.2 dB   |
| Peaking | 913 Hz   | 0.49 | 2.9 dB   |
| Peaking | 3049 Hz  | 1.61 | -11.9 dB |
| Peaking | 13072 Hz | 1.46 | -7.1 dB  |
| Peaking | 22050 Hz | 2.09 | -4.8 dB  |
| Peaking | 3522 Hz  | 4.55 | -1.6 dB  |
| Peaking | 3944 Hz  | 1.36 | 0.9 dB   |
| Peaking | 4699 Hz  | 4.07 | 5.6 dB   |
| Peaking | 5940 Hz  | 2.49 | -7.5 dB  |
| Peaking | 7872 Hz  | 1.95 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 3.7 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | -6.8 dB |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K420/AKG%20K420.png)