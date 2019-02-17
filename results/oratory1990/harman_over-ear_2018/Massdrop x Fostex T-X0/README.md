# Massdrop x Fostex T-X0
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -1.0; 37 -1.5; 41 -2.1; 45 -2.5; 49 -3.0; 54 -3.6; 60 -4.2; 66 -4.5; 72 -4.5; 79 -5.1; 87 -6.0; 96 -6.6; 106 -7.5; 116 -8.3; 128 -8.8; 141 -9.4; 155 -9.9; 170 -10.4; 187 -10.6; 206 -10.8; 227 -10.8; 249 -10.8; 274 -10.7; 302 -9.9; 332 -7.9; 365 -7.0; 402 -6.2; 442 -5.4; 486 -4.5; 535 -3.7; 588 -1.6; 647 -1.0; 712 -1.7; 783 -4.6; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -6.1; 1261 -4.8; 1387 -3.9; 1526 -3.0; 1678 -1.7; 1846 -1.0; 2031 -0.5; 2234 -0.7; 2457 -2.1; 2703 -3.0; 2973 -3.2; 3270 -3.7; 3597 -3.9; 3957 -2.6; 4353 -2.3; 4788 -4.0; 5267 -5.1; 5793 -6.2; 6373 -3.3; 7010 -4.0; 7711 -7.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.9; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex T-X0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex T-X0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.5  | 6.2 dB  |
| Peaking | 199 Hz  | 0.91 | -5.1 dB |
| Peaking | 615 Hz  | 2.63 | 6.2 dB  |
| Peaking | 2018 Hz | 1.92 | 6.0 dB  |
| Peaking | 4199 Hz | 1.91 | 3.2 dB  |
| Peaking | 289 Hz  | 3.83 | -2.3 dB |
| Peaking | 338 Hz  | 1.8  | 1.6 dB  |
| Peaking | 1030 Hz | 4.97 | -1.7 dB |
| Peaking | 6696 Hz | 5.76 | 6.3 dB  |
| Peaking | 6806 Hz | 2.15 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Fostex%20T-X0/Massdrop%20x%20Fostex%20T-X0.png)