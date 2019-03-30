# StereoPravda SPearphone SB-7A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.2; 25 -9.3; 28 -9.3; 31 -9.2; 34 -9.1; 37 -9.0; 41 -8.8; 45 -8.6; 49 -8.1; 54 -7.7; 60 -7.2; 66 -6.6; 72 -6.0; 79 -5.3; 87 -4.6; 96 -3.9; 106 -3.2; 116 -2.9; 128 -2.4; 141 -2.0; 155 -1.6; 170 -1.4; 187 -1.2; 206 -1.2; 227 -1.0; 249 -0.8; 274 -0.8; 302 -0.6; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.8; 783 -0.9; 861 -1.2; 947 -1.4; 1042 -1.7; 1146 -2.0; 1261 -2.3; 1387 -2.7; 1526 -3.7; 1678 -5.6; 1846 -8.4; 2031 -11.5; 2234 -14.1; 2457 -15.7; 2703 -16.2; 2973 -15.5; 3270 -13.4; 3597 -11.1; 3957 -9.6; 4353 -8.0; 4788 -6.7; 5267 -7.0; 5793 -9.2; 6373 -10.5; 7010 -9.4; 7711 -6.0; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`StereoPravda SPearphone SB-7A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `StereoPravda SPearphone SB-7A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.57 | -5.4 dB  |
| Peaking | 586 Hz   | 0.21 | 5.0 dB   |
| Peaking | 2687 Hz  | 1.25 | -14.9 dB |
| Peaking | 22050 Hz | 2.33 | -3.8 dB  |
| Peaking | 1485 Hz  | 2.98 | 1.9 dB   |
| Peaking | 2127 Hz  | 4.99 | -1.8 dB  |
| Peaking | 4984 Hz  | 2.26 | 2.7 dB   |
| Peaking | 6551 Hz  | 2.36 | -6.9 dB  |
| Peaking | 8106 Hz  | 2.03 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | 2.2 dB  |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.7 dB |
| Peaking | 4000 Hz  | 1.41 | -5.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/StereoPravda%20SPearphone%20SB-7A/StereoPravda%20SPearphone%20SB-7A.png)