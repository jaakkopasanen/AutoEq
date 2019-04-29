# Clear Tune CT-300P
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.0; 25 -7.0; 28 -7.2; 31 -7.3; 34 -7.4; 37 -7.5; 41 -7.7; 45 -7.8; 49 -7.9; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.0; 79 -9.4; 87 -9.7; 96 -10.2; 106 -10.6; 116 -11.0; 128 -11.2; 141 -11.5; 155 -11.8; 170 -11.9; 187 -12.0; 206 -12.0; 227 -12.0; 249 -11.9; 274 -11.8; 302 -11.5; 332 -11.3; 365 -11.0; 402 -10.7; 442 -10.4; 486 -9.9; 535 -9.3; 588 -8.7; 647 -8.0; 712 -7.0; 783 -5.9; 861 -4.8; 947 -3.7; 1042 -2.8; 1146 -2.0; 1261 -1.1; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.7; 2234 -2.0; 2457 -2.3; 2703 -1.9; 2973 -1.4; 3270 -1.4; 3597 -2.5; 3957 -4.0; 4353 -5.1; 4788 -5.9; 5267 -5.9; 5793 -4.4; 6373 -3.7; 7010 -6.0; 7711 -10.5; 8482 -10.5; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-300P GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-300P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 249 Hz  | 0.34 | -5.9 dB |
| Peaking | 1453 Hz | 0.8  | 7.4 dB  |
| Peaking | 3202 Hz | 3.31 | 3.2 dB  |
| Peaking | 6412 Hz | 5.3  | 3.3 dB  |
| Peaking | 8023 Hz | 4.68 | -5.8 dB |
| Peaking | 4842 Hz | 7.08 | -0.9 dB |
| Peaking | 9592 Hz | 7.93 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Clear%20Tune%20CT-300P/Clear%20Tune%20CT-300P.png)