# Sennheiser HD 25-1 II B (2012 model)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.6; 25 -6.0; 28 -6.6; 31 -7.0; 34 -7.4; 37 -7.7; 41 -7.9; 45 -8.1; 49 -8.2; 54 -8.2; 60 -8.3; 66 -8.5; 72 -9.0; 79 -9.3; 87 -9.2; 96 -9.0; 106 -8.7; 116 -9.0; 128 -10.3; 141 -10.9; 155 -10.4; 170 -10.0; 187 -9.9; 206 -9.1; 227 -8.2; 249 -7.5; 274 -6.8; 302 -6.6; 332 -6.4; 365 -6.2; 402 -6.2; 442 -6.3; 486 -6.5; 535 -6.6; 588 -6.3; 647 -6.5; 712 -6.6; 783 -6.6; 861 -6.8; 947 -7.0; 1042 -7.2; 1146 -7.3; 1261 -7.6; 1387 -8.2; 1526 -8.7; 1678 -9.2; 1846 -9.4; 2031 -9.5; 2234 -8.5; 2457 -6.7; 2703 -5.2; 2973 -4.0; 3270 -4.6; 3597 -4.3; 3957 -3.8; 4353 -2.7; 4788 -2.6; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -10.1; 9330 -11.2; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 II B (2012 model) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II B (2012 model) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 71 Hz   | 1.06 | -2.2 dB |
| Peaking | 154 Hz  | 1.8  | -3.9 dB |
| Peaking | 1831 Hz | 1.97 | -4.0 dB |
| Peaking | 5935 Hz | 0.96 | 6.6 dB  |
| Peaking | 8878 Hz | 2.82 | -8.4 dB |
| Peaking | 206 Hz  | 5.73 | -0.8 dB |
| Peaking | 353 Hz  | 1.79 | 0.7 dB  |
| Peaking | 2213 Hz | 7.11 | -0.9 dB |
| Peaking | 2889 Hz | 4.65 | 1.5 dB  |
| Peaking | 3938 Hz | 3.23 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model)/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model).png)