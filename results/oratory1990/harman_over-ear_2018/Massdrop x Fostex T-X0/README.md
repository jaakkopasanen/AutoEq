# Massdrop x Fostex T-X0
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.4; 34 -2.1; 37 -2.6; 41 -3.2; 45 -3.7; 49 -4.1; 54 -4.8; 60 -5.3; 66 -5.6; 72 -5.7; 79 -6.3; 87 -7.1; 96 -7.8; 106 -8.7; 116 -9.4; 128 -10.0; 141 -10.6; 155 -11.1; 170 -11.5; 187 -11.8; 206 -11.9; 227 -12.0; 249 -11.9; 274 -11.8; 302 -11.0; 332 -9.1; 365 -8.1; 402 -7.4; 442 -6.5; 486 -5.7; 535 -4.8; 588 -2.8; 647 -2.1; 712 -2.9; 783 -5.7; 861 -6.9; 947 -7.3; 1042 -7.9; 1146 -7.3; 1261 -6.0; 1387 -5.1; 1526 -4.1; 1678 -2.9; 1846 -2.1; 2031 -1.4; 2234 -1.8; 2457 -3.3; 2703 -4.1; 2973 -4.3; 3270 -4.8; 3597 -5.0; 3957 -3.8; 4353 -3.5; 4788 -5.1; 5267 -6.4; 5793 -7.2; 6373 -4.5; 7010 -4.8; 7711 -8.3; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.0; 20000 -11.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex T-X0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex T-X0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.57 | 6.2 dB  |
| Peaking | 200 Hz   | 0.81 | -6.1 dB |
| Peaking | 617 Hz   | 3.17 | 5.6 dB  |
| Peaking | 2049 Hz  | 2.27 | 5.4 dB  |
| Peaking | 4176 Hz  | 4.13 | 2.8 dB  |
| Peaking | 287 Hz   | 4    | -2.1 dB |
| Peaking | 348 Hz   | 1.48 | 1.2 dB  |
| Peaking | 1026 Hz  | 3.53 | -2.4 dB |
| Peaking | 7073 Hz  | 0.19 | 1.3 dB  |
| Peaking | 19819 Hz | 0.02 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Fostex%20T-X0/Massdrop%20x%20Fostex%20T-X0.png)