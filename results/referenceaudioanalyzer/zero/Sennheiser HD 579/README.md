# Sennheiser HD 579
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.3; 31 -2.3; 34 -3.1; 37 -3.8; 41 -4.6; 45 -5.1; 49 -5.4; 54 -5.8; 60 -6.3; 66 -6.8; 72 -7.1; 79 -7.4; 87 -7.7; 96 -8.0; 106 -8.3; 116 -8.3; 128 -8.5; 141 -8.4; 155 -8.4; 170 -8.4; 187 -8.3; 206 -8.0; 227 -7.8; 249 -7.6; 274 -7.4; 302 -7.1; 332 -6.9; 365 -6.7; 402 -6.4; 442 -6.1; 486 -5.7; 535 -5.4; 588 -5.1; 647 -4.7; 712 -4.1; 783 -3.8; 861 -3.8; 947 -3.6; 1042 -3.1; 1146 -2.8; 1261 -2.2; 1387 -1.7; 1526 -1.5; 1678 -1.6; 1846 -2.2; 2031 -3.3; 2234 -4.1; 2457 -4.8; 2703 -5.8; 2973 -7.4; 3270 -8.6; 3597 -9.0; 3957 -10.0; 4353 -11.6; 4788 -12.7; 5267 -13.7; 5793 -14.5; 6373 -13.7; 7010 -10.1; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 579 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 579 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.97 | 6.2 dB   |
| Peaking | 135 Hz  | 0.64 | -2.3 dB  |
| Peaking | 1537 Hz | 0.74 | 5.8 dB   |
| Peaking | 6049 Hz | 1.03 | -15.4 dB |
| Peaking | 7641 Hz | 1.13 | 9.8 dB   |
| Peaking | 741 Hz  | 2.05 | 1.1 dB   |
| Peaking | 951 Hz  | 1.24 | -0.9 dB  |
| Peaking | 1665 Hz | 3.88 | 0.6 dB   |
| Peaking | 3201 Hz | 5.24 | -1.3 dB  |
| Peaking | 3219 Hz | 2.04 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20579/Sennheiser%20HD%20579.png)