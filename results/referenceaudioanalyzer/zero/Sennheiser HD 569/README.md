# Sennheiser HD 569
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.9; 25 -6.4; 28 -7.1; 31 -7.8; 34 -8.3; 37 -8.8; 41 -9.3; 45 -9.6; 49 -9.9; 54 -10.1; 60 -10.5; 66 -10.8; 72 -10.9; 79 -10.8; 87 -10.5; 96 -10.1; 106 -9.6; 116 -9.0; 128 -8.5; 141 -8.3; 155 -8.3; 170 -8.2; 187 -7.5; 206 -6.7; 227 -5.9; 249 -5.3; 274 -4.8; 302 -4.7; 332 -4.8; 365 -5.2; 402 -6.0; 442 -6.9; 486 -7.5; 535 -7.6; 588 -7.6; 647 -7.6; 712 -7.6; 783 -7.6; 861 -7.6; 947 -7.5; 1042 -7.2; 1146 -6.8; 1261 -6.2; 1387 -5.6; 1526 -4.9; 1678 -4.1; 1846 -3.1; 2031 -1.9; 2234 -0.6; 2457 -0.5; 2703 -2.8; 2973 -7.7; 3270 -11.9; 3597 -13.1; 3957 -11.9; 4353 -9.7; 4788 -8.9; 5267 -8.9; 5793 -9.2; 6373 -9.1; 7010 -7.1; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 569 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 569 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 72 Hz   | 0.74 | -4.4 dB |
| Peaking | 288 Hz  | 2.91 | 2.6 dB  |
| Peaking | 2414 Hz | 2.19 | 8.9 dB  |
| Peaking | 3488 Hz | 2.25 | -9.2 dB |
| Peaking | 5990 Hz | 4.8  | -2.3 dB |
| Peaking | 19 Hz   | 2.27 | 1.9 dB  |
| Peaking | 359 Hz  | 3.84 | 1.3 dB  |
| Peaking | 729 Hz  | 0.81 | -1.5 dB |
| Peaking | 1664 Hz | 2.56 | 1.1 dB  |
| Peaking | 7454 Hz | 8.09 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20569/Sennheiser%20HD%20569.png)