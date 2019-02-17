# Fischer Audio Tandem
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.1; 60 -1.9; 66 -2.6; 72 -3.2; 79 -3.9; 87 -4.7; 96 -5.5; 106 -5.9; 116 -6.3; 128 -7.0; 141 -7.3; 155 -7.7; 170 -8.0; 187 -8.1; 206 -8.3; 227 -8.3; 249 -8.5; 274 -8.4; 302 -8.3; 332 -8.3; 365 -8.0; 402 -7.9; 442 -7.6; 486 -7.5; 535 -7.3; 588 -6.8; 647 -6.5; 712 -6.6; 783 -6.3; 861 -6.3; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -6.6; 1387 -6.4; 1526 -6.3; 1678 -6.1; 1846 -5.4; 2031 -4.3; 2234 -3.1; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -3.8; 4788 -3.4; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Tandem GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Tandem ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.36 | 7.4 dB  |
| Peaking | 147 Hz  | 0.46 | -4.0 dB |
| Peaking | 3081 Hz | 1.6  | 6.6 dB  |
| Peaking | 5841 Hz | 3.47 | 5.6 dB  |
| Peaking | 800 Hz  | 1.21 | 2.3 dB  |
| Peaking | 944 Hz  | 0.71 | -1.9 dB |
| Peaking | 2478 Hz | 6.04 | 1.4 dB  |
| Peaking | 6658 Hz | 8.51 | 1.9 dB  |
| Peaking | 7903 Hz | 2.48 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20Tandem/Fischer%20Audio%20Tandem.png)