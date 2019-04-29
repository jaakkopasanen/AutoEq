# Rose BR5 Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.0; 25 -1.2; 28 -1.5; 31 -1.7; 34 -1.9; 37 -2.0; 41 -2.3; 45 -2.4; 49 -2.6; 54 -2.8; 60 -3.1; 66 -3.4; 72 -3.8; 79 -4.2; 87 -4.6; 96 -5.1; 106 -5.5; 116 -5.9; 128 -6.2; 141 -6.6; 155 -6.8; 170 -7.0; 187 -7.1; 206 -7.2; 227 -7.2; 249 -7.2; 274 -7.1; 302 -7.0; 332 -6.7; 365 -6.4; 402 -6.3; 442 -6.0; 486 -5.7; 535 -5.4; 588 -5.0; 647 -4.7; 712 -4.3; 783 -3.8; 861 -3.4; 947 -2.9; 1042 -2.9; 1146 -3.3; 1261 -4.0; 1387 -4.5; 1526 -4.3; 1678 -3.8; 1846 -3.4; 2031 -2.7; 2234 -2.0; 2457 -1.2; 2703 -0.7; 2973 -0.5; 3270 -0.9; 3597 -1.8; 3957 -2.8; 4353 -2.8; 4788 -1.9; 5267 -1.4; 5793 -1.5; 6373 -3.0; 7010 -2.6; 7711 -3.9; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -14.9; 15026 -27.4; 16529 -29.9; 18182 -25.3; 20000 -22.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rose BR5 Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rose BR5 Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.18 | 3.4 dB   |
| Peaking | 209 Hz   | 0.5  | -3.5 dB  |
| Peaking | 6291 Hz  | 0.31 | 16.3 dB  |
| Peaking | 12323 Hz | 1.37 | 17.3 dB  |
| Peaking | 15506 Hz | 0.35 | -39.3 dB |
| Peaking | 1020 Hz  | 1.86 | 2.6 dB   |
| Peaking | 1372 Hz  | 1.07 | -2.8 dB  |
| Peaking | 2867 Hz  | 1.35 | 2.3 dB   |
| Peaking | 4050 Hz  | 3.92 | -2.3 dB  |
| Peaking | 9888 Hz  | 6.59 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB   |
| Peaking | 62 Hz    | 1.41 | 0.9 dB   |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 16000 Hz | 1.41 | -30.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Rose%20BR5%20Mk2/Rose%20BR5%20Mk2.png)