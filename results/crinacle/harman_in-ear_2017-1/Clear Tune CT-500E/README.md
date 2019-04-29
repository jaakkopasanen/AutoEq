# Clear Tune CT-500E
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.1; 25 -5.2; 28 -5.4; 31 -5.5; 34 -5.6; 37 -5.8; 41 -5.9; 45 -6.1; 49 -6.3; 54 -6.5; 60 -6.8; 66 -7.1; 72 -7.4; 79 -7.8; 87 -8.2; 96 -8.7; 106 -9.1; 116 -9.4; 128 -9.7; 141 -10.1; 155 -10.3; 170 -10.5; 187 -10.6; 206 -10.6; 227 -10.6; 249 -10.5; 274 -10.4; 302 -10.1; 332 -9.7; 365 -9.3; 402 -9.0; 442 -8.5; 486 -8.0; 535 -7.3; 588 -6.5; 647 -5.7; 712 -4.7; 783 -3.6; 861 -2.6; 947 -2.1; 1042 -2.3; 1146 -3.5; 1261 -5.6; 1387 -7.8; 1526 -9.4; 1678 -10.2; 1846 -10.1; 2031 -9.0; 2234 -7.5; 2457 -6.1; 2703 -5.0; 2973 -4.3; 3270 -3.8; 3597 -4.4; 3957 -5.6; 4353 -6.9; 4788 -6.8; 5267 -3.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -7.7; 15026 -14.4; 16529 -9.2; 18182 -6.4; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-500E GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-500E ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 244 Hz   | 0.52 | -4.6 dB |
| Peaking | 997 Hz   | 1.02 | 5.9 dB  |
| Peaking | 1623 Hz  | 2.41 | -6.7 dB |
| Peaking | 6041 Hz  | 3.94 | 6.6 dB  |
| Peaking | 15239 Hz | 3.54 | -9.0 dB |
| Peaking | 26 Hz    | 0.88 | 1.5 dB  |
| Peaking | 2041 Hz  | 4.84 | -1.6 dB |
| Peaking | 3198 Hz  | 2.28 | 2.6 dB  |
| Peaking | 4581 Hz  | 5.65 | -2.7 dB |
| Peaking | 13035 Hz | 7.37 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -5.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Clear%20Tune%20CT-500E/Clear%20Tune%20CT-500E.png)