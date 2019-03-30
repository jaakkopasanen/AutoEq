# AKG K92
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -12.3; 25 -12.8; 28 -13.5; 31 -14.1; 34 -14.6; 37 -14.9; 41 -15.2; 45 -15.3; 49 -15.3; 54 -15.3; 60 -15.2; 66 -14.8; 72 -14.3; 79 -13.5; 87 -12.8; 96 -12.7; 106 -13.1; 116 -13.7; 128 -14.2; 141 -14.6; 155 -14.9; 170 -15.3; 187 -15.6; 206 -15.4; 227 -15.3; 249 -15.0; 274 -14.5; 302 -13.4; 332 -11.8; 365 -10.1; 402 -9.2; 442 -9.1; 486 -8.8; 535 -8.7; 588 -8.9; 647 -8.5; 712 -7.4; 783 -6.6; 861 -5.8; 947 -4.5; 1042 -2.8; 1146 -0.9; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -3.2; 5267 -5.2; 5793 -11.3; 6373 -16.6; 7010 -16.2; 7711 -10.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K92 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K92 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.84 | -6.3 dB  |
| Peaking | 56 Hz   | 1.49 | -4.1 dB  |
| Peaking | 205 Hz  | 0.59 | -8.9 dB  |
| Peaking | 2738 Hz | 0.39 | 7.5 dB   |
| Peaking | 6606 Hz | 3.07 | -16.1 dB |
| Peaking | 405 Hz  | 2.29 | 3.0 dB   |
| Peaking | 722 Hz  | 0.62 | -2.4 dB  |
| Peaking | 1217 Hz | 1.99 | 3.7 dB   |
| Peaking | 3799 Hz | 0.85 | -1.7 dB  |
| Peaking | 4217 Hz | 2.05 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K92/AKG%20K92.png)