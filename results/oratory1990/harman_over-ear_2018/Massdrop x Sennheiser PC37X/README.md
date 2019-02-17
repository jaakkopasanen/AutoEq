# Massdrop x Sennheiser PC37X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.4; 72 -1.9; 79 -2.5; 87 -2.6; 96 -3.4; 106 -4.2; 116 -5.3; 128 -6.0; 141 -6.6; 155 -7.1; 170 -7.4; 187 -7.5; 206 -7.6; 227 -7.7; 249 -7.6; 274 -7.3; 302 -7.2; 332 -7.1; 365 -6.9; 402 -6.9; 442 -6.8; 486 -6.7; 535 -6.6; 588 -6.4; 647 -6.0; 712 -6.1; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.5; 1387 -5.6; 1526 -4.8; 1678 -5.0; 1846 -5.7; 2031 -6.5; 2234 -6.2; 2457 -5.7; 2703 -5.6; 2973 -6.2; 3270 -4.8; 3597 -2.4; 3957 -1.6; 4353 -3.4; 4788 -6.7; 5267 -6.4; 5793 -7.7; 6373 -5.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -10.3; 18182 -11.6; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser PC37X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser PC37X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.68 | 7.0 dB  |
| Peaking | 731 Hz   | 2.8  | 0.2 dB  |
| Peaking | 3866 Hz  | 4.25 | 5.5 dB  |
| Peaking | 18391 Hz | 1.18 | -5.8 dB |
| Peaking | 22049 Hz | 1.92 | 0.4 dB  |
| Peaking | 87 Hz    | 1.63 | 1.9 dB  |
| Peaking | 178 Hz   | 0.89 | -2.0 dB |
| Peaking | 1586 Hz  | 4.83 | 1.8 dB  |
| Peaking | 5967 Hz  | 3.76 | -2.4 dB |
| Peaking | 6727 Hz  | 6.41 | 4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Sennheiser%20PC37X/Massdrop%20x%20Sennheiser%20PC37X.png)