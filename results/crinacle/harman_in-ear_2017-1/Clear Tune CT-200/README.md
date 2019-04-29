# Clear Tune CT-200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.4; 72 -2.0; 79 -2.7; 87 -3.3; 96 -4.1; 106 -4.9; 116 -5.4; 128 -5.9; 141 -6.5; 155 -7.0; 170 -7.3; 187 -7.5; 206 -7.8; 227 -7.9; 249 -8.1; 274 -8.1; 302 -8.1; 332 -8.0; 365 -7.9; 402 -7.8; 442 -7.7; 486 -7.6; 535 -7.4; 588 -7.1; 647 -6.9; 712 -6.7; 783 -6.4; 861 -6.2; 947 -6.3; 1042 -6.7; 1146 -7.3; 1261 -7.9; 1387 -8.1; 1526 -7.8; 1678 -7.6; 1846 -7.4; 2031 -7.1; 2234 -6.1; 2457 -4.7; 2703 -3.8; 2973 -3.5; 3270 -3.8; 3597 -4.2; 3957 -4.6; 4353 -5.3; 4788 -5.5; 5267 -5.3; 5793 -4.5; 6373 -4.6; 7010 -7.2; 7711 -7.9; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.0; 15026 -14.5; 16529 -7.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.32 | 7.5 dB  |
| Peaking | 164 Hz   | 0.46 | -4.3 dB |
| Peaking | 3252 Hz  | 2.08 | 3.1 dB  |
| Peaking | 12954 Hz | 3.41 | 2.3 dB  |
| Peaking | 14764 Hz | 3.31 | -9.7 dB |
| Peaking | 921 Hz   | 1.43 | 2.4 dB  |
| Peaking | 1291 Hz  | 0.88 | -2.6 dB |
| Peaking | 2609 Hz  | 4.57 | 1.7 dB  |
| Peaking | 6184 Hz  | 3.3  | 2.6 dB  |
| Peaking | 7336 Hz  | 5    | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Clear%20Tune%20CT-200/Clear%20Tune%20CT-200.png)