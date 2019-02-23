# Adam SP-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.3; 31 -2.3; 34 -3.3; 37 -4.1; 41 -5.2; 45 -6.1; 49 -6.9; 54 -7.8; 60 -8.5; 66 -9.1; 72 -9.3; 79 -8.8; 87 -8.3; 96 -7.8; 106 -7.4; 116 -7.9; 128 -8.0; 141 -8.4; 155 -8.3; 170 -7.9; 187 -7.1; 206 -7.0; 227 -6.4; 249 -5.6; 274 -5.1; 302 -4.5; 332 -4.7; 365 -6.2; 402 -5.2; 442 -4.7; 486 -4.5; 535 -4.4; 588 -4.4; 647 -4.6; 712 -5.0; 783 -5.4; 861 -5.9; 947 -6.4; 1042 -6.8; 1146 -6.9; 1261 -6.4; 1387 -8.0; 1526 -8.9; 1678 -9.3; 1846 -9.4; 2031 -9.2; 2234 -8.9; 2457 -8.2; 2703 -7.7; 2973 -0.6; 3270 -5.8; 3597 -5.5; 3957 -3.5; 4353 -2.8; 4788 -1.4; 5267 -7.1; 5793 -17.7; 6373 -12.6; 7010 -5.1; 7711 -6.4; 8482 -6.6; 9330 -6.5; 10263 -7.7; 11289 -13.2; 12418 -17.8; 13660 -15.6; 15026 -9.7; 16529 -8.8; 18182 -9.6; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Adam SP-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Adam SP-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 2.44 | 7.1 dB   |
| Peaking | 1933 Hz  | 0.78 | -12.3 dB |
| Peaking | 3045 Hz  | 0.27 | 10.1 dB  |
| Peaking | 5916 Hz  | 6.05 | -18.2 dB |
| Peaking | 12672 Hz | 1.65 | -14.5 dB |
| Peaking | 71 Hz    | 2.35 | -3.1 dB  |
| Peaking | 146 Hz   | 2.82 | -2.2 dB  |
| Peaking | 4888 Hz  | 6.28 | 7.2 dB   |
| Peaking | 5082 Hz  | 2.72 | -3.6 dB  |
| Peaking | 18620 Hz | 1.92 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Adam%20SP-5/Adam%20SP-5.png)