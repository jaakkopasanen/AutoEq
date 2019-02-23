# Massdrop x Sennheiser PC37X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -1.6; 66 -2.3; 72 -2.8; 79 -3.4; 87 -3.5; 96 -4.3; 106 -5.2; 116 -6.2; 128 -6.9; 141 -7.5; 155 -8.0; 170 -8.3; 187 -8.4; 206 -8.6; 227 -8.6; 249 -8.5; 274 -8.3; 302 -8.1; 332 -8.0; 365 -7.9; 402 -7.8; 442 -7.7; 486 -7.6; 535 -7.5; 588 -7.3; 647 -6.9; 712 -7.0; 783 -7.2; 861 -7.3; 947 -7.4; 1042 -7.5; 1146 -7.7; 1261 -7.4; 1387 -6.5; 1526 -5.8; 1678 -6.0; 1846 -6.6; 2031 -7.4; 2234 -7.1; 2457 -6.6; 2703 -6.6; 2973 -7.1; 3270 -5.7; 3597 -3.3; 3957 -2.5; 4353 -4.3; 4788 -7.6; 5267 -7.3; 5793 -8.6; 6373 -6.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.8; 16529 -11.2; 18182 -12.5; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser PC37X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser PC37X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 48 Hz    |  0.27 | 7.6 dB  |
| Peaking | 158 Hz   |  0.52 | -5.9 dB |
| Peaking | 3984 Hz  |  4.38 | 5.4 dB  |
| Peaking | 4864 Hz  |  3.45 | -2.3 dB |
| Peaking | 18402 Hz |  1.11 | -6.9 dB |
| Peaking | 1183 Hz  |  2.44 | -1.3 dB |
| Peaking | 1597 Hz  |  2.6  | 2.4 dB  |
| Peaking | 1926 Hz  |  1.83 | -1.5 dB |
| Peaking | 6906 Hz  | 10.7  | 3.4 dB  |
| Peaking | 16674 Hz |  6.18 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Sennheiser%20PC37X/Massdrop%20x%20Sennheiser%20PC37X.png)