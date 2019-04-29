# Clear Tune CT-300P
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.1; 25 -8.2; 28 -8.3; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.8; 45 -8.9; 49 -9.1; 54 -9.3; 60 -9.5; 66 -9.8; 72 -10.2; 79 -10.5; 87 -10.9; 96 -11.4; 106 -11.7; 116 -12.1; 128 -12.4; 141 -12.6; 155 -12.9; 170 -13.0; 187 -13.1; 206 -13.2; 227 -13.1; 249 -13.0; 274 -12.9; 302 -12.6; 332 -12.3; 365 -11.9; 402 -11.6; 442 -11.2; 486 -10.6; 535 -10.0; 588 -9.4; 647 -8.6; 712 -7.7; 783 -6.6; 861 -5.5; 947 -4.5; 1042 -3.6; 1146 -2.7; 1261 -1.6; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.9; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.7; 3957 -2.4; 4353 -3.9; 4788 -5.0; 5267 -5.0; 5793 -3.3; 6373 -2.2; 7010 -4.0; 7711 -7.5; 8482 -8.8; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -11.1; 16529 -6.5; 18182 -6.5; 20000 -9.7
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.14 | -1.0 dB |
| Peaking | 330 Hz   | 0.27 | -7.0 dB |
| Peaking | 1496 Hz  | 0.55 | 8.8 dB  |
| Peaking | 3310 Hz  | 2.62 | 2.7 dB  |
| Peaking | 14660 Hz | 4.48 | -5.9 dB |
| Peaking | 5001 Hz  | 3.9  | -2.0 dB |
| Peaking | 6390 Hz  | 3.03 | 4.1 dB  |
| Peaking | 8113 Hz  | 3.78 | -4.1 dB |
| Peaking | 12869 Hz | 5.57 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Clear%20Tune%20CT-300P/Clear%20Tune%20CT-300P.png)