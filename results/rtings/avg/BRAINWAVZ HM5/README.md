# BRAINWAVZ HM5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.0; 25 -1.1; 28 -1.2; 31 -1.3; 34 -1.4; 37 -1.3; 41 -1.3; 45 -1.4; 49 -1.5; 54 -1.8; 60 -2.1; 66 -2.6; 72 -2.9; 79 -3.4; 87 -4.0; 96 -4.6; 106 -5.3; 116 -5.8; 128 -6.2; 141 -6.5; 155 -6.6; 170 -6.5; 187 -6.5; 206 -6.2; 227 -5.7; 249 -4.9; 274 -3.7; 302 -2.2; 332 -0.8; 365 -0.5; 402 -1.4; 442 -2.4; 486 -3.4; 535 -4.2; 588 -4.7; 647 -5.1; 712 -4.9; 783 -4.7; 861 -4.4; 947 -4.6; 1042 -4.7; 1146 -4.6; 1261 -4.8; 1387 -5.1; 1526 -5.6; 1678 -6.3; 1846 -7.1; 2031 -7.3; 2234 -6.6; 2457 -6.0; 2703 -5.8; 2973 -5.1; 3270 -5.1; 3597 -8.7; 3957 -8.4; 4353 -8.4; 4788 -8.1; 5267 -6.6; 5793 -6.9; 6373 -6.2; 7010 -2.3; 7711 -4.5; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.9; 13660 -7.6; 15026 -7.0; 16529 -4.8; 18182 -4.8; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BRAINWAVZ HM5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BRAINWAVZ HM5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 16 Hz    |  0.32 | 3.7 dB  |
| Peaking | 63 Hz    |  0.78 | 2.6 dB  |
| Peaking | 192 Hz   |  0.4  | -3.9 dB |
| Peaking | 352 Hz   |  1.57 | 7.2 dB  |
| Peaking | 4188 Hz  |  2.07 | -3.9 dB |
| Peaking | 1069 Hz  |  1.88 | 0.8 dB  |
| Peaking | 1948 Hz  |  2.91 | -2.3 dB |
| Peaking | 3135 Hz  | 10.85 | 2.4 dB  |
| Peaking | 6892 Hz  | 12.06 | 3.9 dB  |
| Peaking | 14174 Hz |  3.78 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/BRAINWAVZ%20HM5/BRAINWAVZ%20HM5.png)