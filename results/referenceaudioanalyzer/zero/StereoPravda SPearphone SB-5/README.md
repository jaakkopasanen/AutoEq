# StereoPravda SPearphone SB-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.8; 25 -3.0; 28 -3.4; 31 -3.6; 34 -3.8; 37 -3.9; 41 -4.1; 45 -4.2; 49 -4.3; 54 -4.4; 60 -4.3; 66 -4.4; 72 -4.5; 79 -4.5; 87 -4.5; 96 -4.5; 106 -4.5; 116 -4.4; 128 -4.3; 141 -4.3; 155 -4.3; 170 -4.3; 187 -4.3; 206 -4.3; 227 -4.3; 249 -4.3; 274 -4.3; 302 -4.3; 332 -4.3; 365 -4.3; 402 -4.3; 442 -4.3; 486 -4.3; 535 -4.3; 588 -4.3; 647 -4.3; 712 -4.6; 783 -4.7; 861 -4.9; 947 -5.1; 1042 -5.5; 1146 -5.9; 1261 -6.3; 1387 -6.9; 1526 -7.5; 1678 -8.1; 1846 -8.7; 2031 -9.5; 2234 -10.5; 2457 -12.0; 2703 -13.1; 2973 -12.9; 3270 -11.5; 3597 -10.3; 3957 -11.1; 4353 -12.8; 4788 -12.5; 5267 -9.2; 5793 -3.3; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`StereoPravda SPearphone SB-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `StereoPravda SPearphone SB-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.35 | 4.2 dB  |
| Peaking | 328 Hz  | 0.25 | 1.7 dB  |
| Peaking | 2687 Hz | 1.4  | -6.8 dB |
| Peaking | 4721 Hz | 3.05 | -6.6 dB |
| Peaking | 6211 Hz | 4.03 | 8.1 dB  |
| Peaking | 1545 Hz | 1.78 | -1.6 dB |
| Peaking | 1692 Hz | 0.91 | 1.2 dB  |
| Peaking | 2866 Hz | 6.73 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -6.1 dB |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/StereoPravda%20SPearphone%20SB-5/StereoPravda%20SPearphone%20SB-5.png)