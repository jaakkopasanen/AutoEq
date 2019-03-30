# Sennheiser PX 100 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -2.0; 34 -2.7; 37 -3.4; 41 -4.2; 45 -4.8; 49 -5.3; 54 -5.8; 60 -6.2; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.4; 96 -7.7; 106 -7.8; 116 -7.8; 128 -7.8; 141 -7.8; 155 -7.8; 170 -7.8; 187 -7.5; 206 -7.4; 227 -7.1; 249 -6.9; 274 -6.6; 302 -6.4; 332 -6.1; 365 -5.8; 402 -5.6; 442 -5.3; 486 -5.0; 535 -4.7; 588 -4.5; 647 -4.2; 712 -4.2; 783 -4.0; 861 -3.9; 947 -3.9; 1042 -3.9; 1146 -3.9; 1261 -3.9; 1387 -4.1; 1526 -4.4; 1678 -4.8; 1846 -5.3; 2031 -6.0; 2234 -7.0; 2457 -8.5; 2703 -10.0; 2973 -11.4; 3270 -11.1; 3597 -8.9; 3957 -9.2; 4353 -11.9; 4788 -12.1; 5267 -10.2; 5793 -8.1; 6373 -5.9; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -6.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 100 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.64 | 6.4 dB  |
| Peaking | 1061 Hz | 0.77 | 3.1 dB  |
| Peaking | 2960 Hz | 2.96 | -5.2 dB |
| Peaking | 4713 Hz | 3.21 | -5.9 dB |
| Peaking | 6830 Hz | 5.19 | 2.8 dB  |
| Peaking | 14 Hz   | 2.23 | 0.9 dB  |
| Peaking | 43 Hz   | 2.09 | 1.1 dB  |
| Peaking | 125 Hz  | 0.64 | -1.6 dB |
| Peaking | 485 Hz  | 1.57 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20PX%20100%20II/Sennheiser%20PX%20100%20II.png)