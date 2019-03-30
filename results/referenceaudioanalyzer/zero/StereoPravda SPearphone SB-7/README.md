# StereoPravda SPearphone SB-7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.8; 31 -1.3; 34 -1.7; 37 -2.1; 41 -2.5; 45 -2.8; 49 -3.1; 54 -3.2; 60 -3.3; 66 -3.5; 72 -3.6; 79 -3.8; 87 -3.9; 96 -4.2; 106 -4.1; 116 -4.2; 128 -4.4; 141 -4.5; 155 -4.5; 170 -4.5; 187 -4.5; 206 -4.5; 227 -4.7; 249 -4.8; 274 -4.8; 302 -4.8; 332 -4.8; 365 -4.8; 402 -4.8; 442 -4.8; 486 -4.8; 535 -4.8; 588 -4.8; 647 -5.0; 712 -5.1; 783 -5.1; 861 -5.2; 947 -5.4; 1042 -5.5; 1146 -5.8; 1261 -6.0; 1387 -6.3; 1526 -6.9; 1678 -7.9; 1846 -9.6; 2031 -11.6; 2234 -13.4; 2457 -14.7; 2703 -15.5; 2973 -15.4; 3270 -13.6; 3597 -10.4; 3957 -7.9; 4353 -6.7; 4788 -6.1; 5267 -6.6; 5793 -8.2; 6373 -9.8; 7010 -9.1; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`StereoPravda SPearphone SB-7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `StereoPravda SPearphone SB-7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.61 | 5.1 dB   |
| Peaking | 154 Hz   | 0.12 | 1.8 dB   |
| Peaking | 1180 Hz  | 1.3  | 0.7 dB   |
| Peaking | 2648 Hz  | 1.85 | -10.2 dB |
| Peaking | 22048 Hz | 2.24 | -1.0 dB  |
| Peaking | 3232 Hz  | 6    | -2.3 dB  |
| Peaking | 3954 Hz  | 2.6  | 0.5 dB   |
| Peaking | 4728 Hz  | 2.2  | 2.4 dB   |
| Peaking | 6557 Hz  | 3.45 | -4.2 dB  |
| Peaking | 7999 Hz  | 3    | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/StereoPravda%20SPearphone%20SB-7/StereoPravda%20SPearphone%20SB-7.png)