# Sennheiser HD 280 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.6; 25 -6.3; 28 -7.3; 31 -8.1; 34 -8.7; 37 -9.3; 41 -9.9; 45 -10.5; 49 -10.8; 54 -10.8; 60 -9.9; 66 -8.5; 72 -6.8; 79 -4.7; 87 -4.6; 96 -6.9; 106 -9.0; 116 -9.7; 128 -9.3; 141 -8.9; 155 -9.3; 170 -8.8; 187 -7.4; 206 -6.4; 227 -6.5; 249 -6.6; 274 -6.9; 302 -7.0; 332 -7.0; 365 -7.0; 402 -7.0; 442 -7.0; 486 -6.9; 535 -6.7; 588 -6.6; 647 -6.4; 712 -6.3; 783 -6.3; 861 -6.3; 947 -6.3; 1042 -6.5; 1146 -6.9; 1261 -7.0; 1387 -6.8; 1526 -6.6; 1678 -6.6; 1846 -6.3; 2031 -5.7; 2234 -4.5; 2457 -2.2; 2703 -0.5; 2973 -0.6; 3270 -3.0; 3597 -4.8; 3957 -5.0; 4353 -5.7; 4788 -7.6; 5267 -9.1; 5793 -11.2; 6373 -13.1; 7010 -11.9; 7711 -7.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 2.98 | 2.1 dB  |
| Peaking | 47 Hz   | 2.4  | -4.8 dB |
| Peaking | 138 Hz  | 2.45 | -3.1 dB |
| Peaking | 2829 Hz | 3.02 | 6.8 dB  |
| Peaking | 6354 Hz | 3.64 | -7.5 dB |
| Peaking | 83 Hz   | 3.84 | 6.1 dB  |
| Peaking | 83 Hz   | 1.31 | -2.6 dB |
| Peaking | 211 Hz  | 6.35 | 1.1 dB  |
| Peaking | 1515 Hz | 2.14 | -0.7 dB |
| Peaking | 8241 Hz | 7.4  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)