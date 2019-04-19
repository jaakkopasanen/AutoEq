# Fostex TH-X00 Mahogany
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.3; 25 -4.1; 28 -5.1; 31 -6.0; 34 -6.5; 37 -6.8; 41 -6.9; 45 -6.8; 49 -6.8; 54 -6.9; 60 -7.0; 66 -6.8; 72 -6.5; 79 -6.6; 87 -6.7; 96 -6.8; 106 -7.0; 116 -7.1; 128 -7.2; 141 -7.3; 155 -7.2; 170 -7.2; 187 -7.1; 206 -6.9; 227 -6.6; 249 -6.2; 274 -5.9; 302 -5.5; 332 -5.2; 365 -4.8; 402 -4.7; 442 -4.9; 486 -5.3; 535 -5.9; 588 -6.7; 647 -7.9; 712 -9.3; 783 -10.4; 861 -10.0; 947 -9.3; 1042 -9.9; 1146 -9.8; 1261 -9.5; 1387 -9.5; 1526 -9.5; 1678 -9.3; 1846 -9.3; 2031 -9.2; 2234 -8.7; 2457 -7.8; 2703 -6.6; 2973 -4.5; 3270 -1.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -4.2; 5793 -8.4; 6373 -9.1; 7010 -10.2; 7711 -12.6; 8482 -8.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.6; 13660 -12.7; 15026 -8.5; 16529 -6.5; 18182 -6.7; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH-X00 Mahogany GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH-X00 Mahogany ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 2.95 | 4.2 dB  |
| Peaking | 1656 Hz  | 0.7  | -4.3 dB |
| Peaking | 3977 Hz  | 1.52 | 8.8 dB  |
| Peaking | 7165 Hz  | 2.58 | -6.5 dB |
| Peaking | 13703 Hz | 4.27 | -6.9 dB |
| Peaking | 422 Hz   | 1.9  | 2.6 dB  |
| Peaking | 781 Hz   | 3.94 | -2.7 dB |
| Peaking | 5907 Hz  | 6.67 | -3.9 dB |
| Peaking | 7642 Hz  | 1.74 | 4.0 dB  |
| Peaking | 7819 Hz  | 5.58 | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Fostex%20TH-X00%20Mahogany/Fostex%20TH-X00%20Mahogany.png)