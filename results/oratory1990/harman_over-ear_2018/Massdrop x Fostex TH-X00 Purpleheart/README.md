# Massdrop x Fostex TH-X00 Purpleheart
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.7; 25 -5.5; 28 -6.5; 31 -7.2; 34 -7.6; 37 -7.9; 41 -8.2; 45 -8.4; 49 -8.4; 54 -8.4; 60 -8.2; 66 -8.2; 72 -8.3; 79 -8.5; 87 -8.6; 96 -8.8; 106 -9.0; 116 -9.2; 128 -9.3; 141 -9.4; 155 -9.4; 170 -9.3; 187 -9.2; 206 -9.0; 227 -8.8; 249 -8.6; 274 -8.2; 302 -8.0; 332 -7.8; 365 -7.5; 402 -7.1; 442 -6.8; 486 -6.1; 535 -5.0; 588 -3.8; 647 -4.5; 712 -5.2; 783 -5.2; 861 -5.9; 947 -7.0; 1042 -7.3; 1146 -7.5; 1261 -7.6; 1387 -7.9; 1526 -8.0; 1678 -7.9; 1846 -7.8; 2031 -7.6; 2234 -7.7; 2457 -7.9; 2703 -6.3; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -6.2; 5267 -8.5; 5793 -9.2; 6373 -6.8; 7010 -5.7; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -8.1; 12418 -11.2; 13660 -12.8; 15026 -9.2; 16529 -6.5; 18182 -8.6; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 Purpleheart GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 Purpleheart ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  2.61 | 3.7 dB  |
| Peaking | 514 Hz   |  0.09 | -3.2 dB |
| Peaking | 625 Hz   |  1.12 | 5.2 dB  |
| Peaking | 3513 Hz  |  2.34 | 9.4 dB  |
| Peaking | 13668 Hz |  2.81 | -6.7 dB |
| Peaking | 2617 Hz  |  4.88 | -2.2 dB |
| Peaking | 2939 Hz  | 10.37 | 3.8 dB  |
| Peaking | 4241 Hz  |  8.35 | 3.2 dB  |
| Peaking | 5729 Hz  |  2.45 | -5.4 dB |
| Peaking | 6600 Hz  |  2.08 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Fostex%20TH-X00%20Purpleheart/Massdrop%20x%20Fostex%20TH-X00%20Purpleheart.png)