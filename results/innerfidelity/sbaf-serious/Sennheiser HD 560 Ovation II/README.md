# Sennheiser HD 560 Ovation II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.4; 72 -2.3; 79 -3.1; 87 -3.9; 96 -4.6; 106 -5.2; 116 -5.6; 128 -6.1; 141 -6.5; 155 -6.9; 170 -7.0; 187 -7.1; 206 -7.2; 227 -7.2; 249 -7.1; 274 -7.1; 302 -7.0; 332 -7.1; 365 -6.8; 402 -6.8; 442 -6.6; 486 -6.6; 535 -6.7; 588 -6.2; 647 -6.3; 712 -6.4; 783 -6.2; 861 -6.5; 947 -6.6; 1042 -6.8; 1146 -6.7; 1261 -7.2; 1387 -7.9; 1526 -8.6; 1678 -9.1; 1846 -9.3; 2031 -9.6; 2234 -10.2; 2457 -10.5; 2703 -11.0; 2973 -10.5; 3270 -9.7; 3597 -8.6; 3957 -8.6; 4353 -9.2; 4788 -9.0; 5267 -7.3; 5793 -1.1; 6373 -1.3; 7010 -5.7; 7711 -9.8; 8482 -11.1; 9330 -8.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.2; 15026 -6.7; 16529 -6.5; 18182 -6.7; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 560 Ovation II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 560 Ovation II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.71 | 7.0 dB  |
| Peaking | 2524 Hz | 1.25 | -4.3 dB |
| Peaking | 4962 Hz | 3.21 | -4.0 dB |
| Peaking | 6036 Hz | 3.47 | 8.8 dB  |
| Peaking | 8213 Hz | 3.73 | -5.8 dB |
| Peaking | 40 Hz   | 2.89 | -1.4 dB |
| Peaking | 61 Hz   | 2.09 | 1.7 dB  |
| Peaking | 178 Hz  | 1.08 | -1.3 dB |
| Peaking | 9168 Hz | 7.61 | -1.3 dB |
| Peaking | 9925 Hz | 4.35 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20560%20Ovation%20II/Sennheiser%20HD%20560%20Ovation%20II.png)