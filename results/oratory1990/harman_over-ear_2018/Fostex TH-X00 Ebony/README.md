# Fostex TH-X00 Ebony
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.3; 25 -3.9; 28 -4.6; 31 -4.9; 34 -5.1; 37 -5.1; 41 -5.0; 45 -5.0; 49 -5.0; 54 -4.9; 60 -4.8; 66 -4.6; 72 -4.7; 79 -5.1; 87 -5.4; 96 -5.6; 106 -5.8; 116 -6.0; 128 -6.2; 141 -6.4; 155 -6.5; 170 -6.6; 187 -6.7; 206 -6.7; 227 -6.6; 249 -6.5; 274 -6.4; 302 -6.2; 332 -6.0; 365 -5.8; 402 -5.8; 442 -5.9; 486 -6.0; 535 -6.2; 588 -6.8; 647 -7.6; 712 -8.0; 783 -7.3; 861 -8.0; 947 -8.3; 1042 -8.3; 1146 -7.9; 1261 -7.4; 1387 -7.2; 1526 -7.3; 1678 -7.4; 1846 -7.4; 2031 -7.5; 2234 -7.7; 2457 -7.9; 2703 -6.9; 2973 -4.9; 3270 -4.0; 3597 -3.3; 3957 -1.6; 4353 -0.5; 4788 -3.9; 5267 -7.4; 5793 -9.8; 6373 -8.3; 7010 -7.2; 7711 -7.2; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -7.0; 15026 -6.3; 16529 -6.3; 18182 -10.5; 20000 -20.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH-X00 Ebony GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH-X00 Ebony ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 1.16 | 4.8 dB  |
| Peaking | 65 Hz   | 1.77 | 1.5 dB  |
| Peaking | 2115 Hz | 0.41 | -2.0 dB |
| Peaking | 4265 Hz | 1.86 | 8.3 dB  |
| Peaking | 5643 Hz | 2.99 | -5.9 dB |
| Peaking | 445 Hz  | 1.05 | 2.8 dB  |
| Peaking | 596 Hz  | 0.45 | -2.1 dB |
| Peaking | 1466 Hz | 1.62 | 1.5 dB  |
| Peaking | 2526 Hz | 4.8  | -1.1 dB |
| Peaking | 3023 Hz | 6.66 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Fostex%20TH-X00%20Ebony/Fostex%20TH-X00%20Ebony.png)