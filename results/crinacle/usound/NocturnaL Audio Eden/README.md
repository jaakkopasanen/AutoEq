# NocturnaL Audio Eden
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.1; 31 -1.5; 34 -1.8; 37 -2.1; 41 -2.4; 45 -2.6; 49 -2.9; 54 -3.2; 60 -3.6; 66 -3.9; 72 -4.3; 79 -4.7; 87 -5.1; 96 -5.5; 106 -6.0; 116 -6.4; 128 -6.7; 141 -7.0; 155 -7.2; 170 -7.5; 187 -7.7; 206 -7.8; 227 -7.9; 249 -7.9; 274 -7.9; 302 -7.9; 332 -7.8; 365 -7.7; 402 -7.7; 442 -7.6; 486 -7.5; 535 -7.4; 588 -7.2; 647 -7.0; 712 -6.7; 783 -6.4; 861 -6.1; 947 -5.9; 1042 -5.8; 1146 -5.8; 1261 -6.0; 1387 -6.9; 1526 -8.8; 1678 -11.3; 1846 -12.4; 2031 -10.1; 2234 -7.5; 2457 -6.2; 2703 -6.3; 2973 -6.4; 3270 -3.3; 3597 -0.5; 3957 -2.2; 4353 -5.1; 4788 -4.3; 5267 -4.9; 5793 -8.1; 6373 -6.2; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NocturnaL Audio Eden GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NocturnaL Audio Eden ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.71 | 5.7 dB  |
| Peaking | 56 Hz   | 0.96 | 1.7 dB  |
| Peaking | 230 Hz  | 0.76 | -1.7 dB |
| Peaking | 1816 Hz | 4.6  | -6.7 dB |
| Peaking | 3655 Hz | 4.29 | 6.5 dB  |
| Peaking | 1070 Hz | 1.52 | 2.7 dB  |
| Peaking | 1079 Hz | 0.76 | -1.4 dB |
| Peaking | 5103 Hz | 5.71 | 2.9 dB  |
| Peaking | 5897 Hz | 3.69 | -3.4 dB |
| Peaking | 6766 Hz | 5.27 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/NocturnaL%20Audio%20Eden/NocturnaL%20Audio%20Eden.png)