# Oppo PM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.5; 25 -2.4; 28 -2.2; 31 -2.0; 34 -1.7; 37 -1.5; 41 -0.9; 45 -0.5; 49 -0.6; 54 -1.6; 60 -2.6; 66 -3.2; 72 -4.1; 79 -4.9; 87 -5.4; 96 -6.2; 106 -6.9; 116 -7.3; 128 -7.4; 141 -7.5; 155 -7.4; 170 -6.9; 187 -6.3; 206 -5.8; 227 -5.0; 249 -4.0; 274 -3.0; 302 -2.2; 332 -1.7; 365 -1.3; 402 -1.6; 442 -1.9; 486 -2.3; 535 -3.0; 588 -3.2; 647 -3.3; 712 -3.3; 783 -3.3; 861 -3.4; 947 -3.5; 1042 -3.8; 1146 -4.7; 1261 -5.3; 1387 -5.4; 1526 -5.6; 1678 -6.0; 1846 -6.5; 2031 -5.9; 2234 -5.6; 2457 -6.0; 2703 -6.1; 2973 -5.3; 3270 -5.3; 3597 -4.1; 3957 -3.4; 4353 -4.0; 4788 -3.5; 5267 -2.4; 5793 -4.2; 6373 -8.6; 7010 -7.0; 7711 -7.1; 8482 -7.7; 9330 -3.8; 10263 -3.6; 11289 -3.6; 12418 -7.6; 13660 -7.7; 15026 -3.7; 16529 -3.6; 18182 -3.6; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 1.61 | 3.4 dB  |
| Peaking | 128 Hz   | 1.52 | -4.6 dB |
| Peaking | 1980 Hz  | 1.51 | -2.8 dB |
| Peaking | 7241 Hz  | 2.8  | -4.2 dB |
| Peaking | 13226 Hz | 5.16 | -5.7 dB |
| Peaking | 202 Hz   | 2.47 | -1.5 dB |
| Peaking | 360 Hz   | 1.54 | 2.8 dB  |
| Peaking | 2758 Hz  | 5.12 | -0.9 dB |
| Peaking | 5260 Hz  | 7.85 | 2.6 dB  |
| Peaking | 15556 Hz | 3.54 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Oppo%20PM3/Oppo%20PM3.png)