# A Audio Elite NC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -4.4; 25 -3.9; 28 -3.2; 31 -2.6; 34 -2.1; 37 -1.7; 41 -1.3; 45 -1.1; 49 -0.9; 54 -0.7; 60 -0.6; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.0; 96 -1.7; 106 -2.1; 116 -2.1; 128 -2.4; 141 -2.8; 155 -2.9; 170 -2.9; 187 -3.1; 206 -3.0; 227 -2.7; 249 -2.4; 274 -2.0; 302 -1.8; 332 -1.7; 365 -1.7; 402 -2.0; 442 -2.5; 486 -2.9; 535 -3.8; 588 -4.2; 647 -4.2; 712 -5.3; 783 -7.3; 861 -8.9; 947 -10.5; 1042 -11.2; 1146 -11.7; 1261 -10.6; 1387 -9.5; 1526 -8.4; 1678 -7.5; 1846 -6.3; 2031 -5.1; 2234 -3.9; 2457 -2.8; 2703 -2.1; 2973 -2.2; 3270 -3.0; 3597 -3.5; 3957 -5.0; 4353 -7.4; 4788 -7.0; 5267 -3.9; 5793 -1.1; 6373 -0.6; 7010 -2.6; 7711 -4.2; 8482 -4.7; 9330 -5.9; 10263 -4.8; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`A Audio Elite NC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.84 | 4.1 dB  |
| Peaking | 401 Hz  | 0.79 | 3.1 dB  |
| Peaking | 1117 Hz | 1.32 | -8.4 dB |
| Peaking | 4194 Hz | 0.95 | 5.8 dB  |
| Peaking | 4384 Hz | 3.19 | -9.1 dB |
| Peaking | 1720 Hz | 4.9  | -0.6 dB |
| Peaking | 2587 Hz | 5.14 | 1.2 dB  |
| Peaking | 5142 Hz | 5    | -1.4 dB |
| Peaking | 6178 Hz | 4.89 | 3.0 dB  |
| Peaking | 9095 Hz | 2.47 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -8.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20NC%20Active/A%20Audio%20Elite%20NC%20Active.png)