# Sennheiser HD 25 Aluminum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.7; 25 -9.9; 28 -10.2; 31 -10.4; 34 -10.5; 37 -10.6; 41 -10.7; 45 -10.7; 49 -10.7; 54 -10.7; 60 -10.6; 66 -10.6; 72 -10.5; 79 -10.0; 87 -9.9; 96 -11.1; 106 -12.5; 116 -13.1; 128 -13.1; 141 -12.6; 155 -11.7; 170 -11.3; 187 -10.5; 206 -9.5; 227 -8.5; 249 -7.3; 274 -5.8; 302 -4.9; 332 -4.2; 365 -3.7; 402 -3.4; 442 -3.3; 486 -3.9; 535 -4.1; 588 -4.2; 647 -4.5; 712 -4.9; 783 -4.9; 861 -5.4; 947 -5.7; 1042 -6.1; 1146 -6.3; 1261 -6.8; 1387 -7.7; 1526 -8.7; 1678 -9.7; 1846 -10.2; 2031 -10.4; 2234 -9.7; 2457 -8.3; 2703 -6.8; 2973 -5.5; 3270 -5.1; 3597 -5.5; 3957 -5.4; 4353 -3.8; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.8; 8482 -12.2; 9330 -10.9; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25 Aluminum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25 Aluminum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.68 | -4.3 dB |
| Peaking | 129 Hz  | 1.85 | -6.3 dB |
| Peaking | 1969 Hz | 2.72 | -4.8 dB |
| Peaking | 5722 Hz | 1.58 | 7.2 dB  |
| Peaking | 8499 Hz | 3.65 | -8.5 dB |
| Peaking | 205 Hz  | 1.86 | -3.1 dB |
| Peaking | 389 Hz  | 0.77 | 3.8 dB  |
| Peaking | 1552 Hz | 4.53 | -1.3 dB |
| Peaking | 4140 Hz | 6.38 | -2.0 dB |
| Peaking | 4702 Hz | 6.87 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025%20Aluminum/Sennheiser%20HD%2025%20Aluminum.png)