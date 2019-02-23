# AKG K280 Parabolic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.4; 45 -1.9; 49 -2.5; 54 -3.1; 60 -3.8; 66 -4.4; 72 -4.6; 79 -5.0; 87 -5.6; 96 -6.1; 106 -6.6; 116 -7.0; 128 -7.3; 141 -7.6; 155 -7.8; 170 -8.0; 187 -8.2; 206 -8.4; 227 -8.5; 249 -8.6; 274 -8.6; 302 -8.5; 332 -8.7; 365 -8.6; 402 -8.6; 442 -8.7; 486 -8.7; 535 -8.8; 588 -8.8; 647 -8.8; 712 -8.8; 783 -8.8; 861 -8.7; 947 -8.4; 1042 -7.3; 1146 -5.6; 1261 -4.6; 1387 -4.4; 1526 -5.0; 1678 -6.1; 1846 -7.2; 2031 -7.1; 2234 -5.6; 2457 -4.4; 2703 -4.1; 2973 -4.4; 3270 -5.1; 3597 -5.6; 3957 -4.0; 4353 -4.2; 4788 -5.7; 5267 -9.6; 5793 -5.8; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.7; 12418 -7.5; 13660 -6.8; 15026 -6.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K280 Parabolic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K280 Parabolic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.5  | 6.5 dB  |
| Peaking | 496 Hz   | 0.17 | -2.6 dB |
| Peaking | 1322 Hz  | 3.35 | 4.1 dB  |
| Peaking | 3067 Hz  | 1    | 3.2 dB  |
| Peaking | 22050 Hz | 2.29 | 0.8 dB  |
| Peaking | 1622 Hz  | 4.48 | 1.2 dB  |
| Peaking | 1926 Hz  | 2.51 | -1.6 dB |
| Peaking | 2444 Hz  | 4.86 | 1.5 dB  |
| Peaking | 5375 Hz  | 8.74 | -5.6 dB |
| Peaking | 6340 Hz  | 4.65 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K280%20Parabolic/AKG%20K280%20Parabolic.png)