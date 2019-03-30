# Sennheiser IE8 (min)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.3; 25 -4.2; 28 -5.3; 31 -6.2; 34 -6.9; 37 -7.5; 41 -8.1; 45 -8.7; 49 -9.1; 54 -9.5; 60 -9.9; 66 -10.2; 72 -10.4; 79 -10.6; 87 -10.7; 96 -10.9; 106 -10.9; 116 -10.9; 128 -10.7; 141 -10.6; 155 -10.6; 170 -10.5; 187 -10.3; 206 -10.2; 227 -10.2; 249 -9.9; 274 -9.6; 302 -9.3; 332 -9.3; 365 -8.9; 402 -8.3; 442 -7.6; 486 -6.9; 535 -6.1; 588 -5.2; 647 -4.4; 712 -3.5; 783 -2.7; 861 -2.0; 947 -1.3; 1042 -0.7; 1146 -0.5; 1261 -0.6; 1387 -1.0; 1526 -1.7; 1678 -2.2; 1846 -2.6; 2031 -2.9; 2234 -3.2; 2457 -3.7; 2703 -4.2; 2973 -4.4; 3270 -4.4; 3597 -4.4; 3957 -4.6; 4353 -5.2; 4788 -6.8; 5267 -10.6; 5793 -12.8; 6373 -11.3; 7010 -4.9; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE8 (min) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE8 (min) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.22 | 5.1 dB  |
| Peaking | 81 Hz   | 0.43 | -4.7 dB |
| Peaking | 402 Hz  | 0.47 | -4.2 dB |
| Peaking | 1018 Hz | 0.64 | 6.9 dB  |
| Peaking | 5754 Hz | 4.65 | -8.7 dB |
| Peaking | 4012 Hz | 5.3  | 0.8 dB  |
| Peaking | 6447 Hz | 9.05 | -3.1 dB |
| Peaking | 7119 Hz | 6.07 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20IE8%20(min)/Sennheiser%20IE8%20(min).png)