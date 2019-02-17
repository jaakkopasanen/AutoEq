# Lear LUF 4C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.6; 25 -5.7; 28 -5.9; 31 -6.1; 34 -6.3; 37 -6.4; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.3; 60 -7.6; 66 -7.8; 72 -8.0; 79 -8.4; 87 -8.7; 96 -8.9; 106 -9.0; 116 -8.9; 128 -8.9; 141 -8.7; 155 -8.4; 170 -7.9; 187 -7.3; 206 -6.7; 227 -6.1; 249 -5.5; 274 -5.0; 302 -4.6; 332 -4.3; 365 -4.1; 402 -4.1; 442 -3.9; 486 -4.0; 535 -4.0; 588 -3.7; 647 -3.9; 712 -4.2; 783 -4.2; 861 -4.7; 947 -5.3; 1042 -6.0; 1146 -6.8; 1261 -7.8; 1387 -9.3; 1526 -10.9; 1678 -12.0; 1846 -12.8; 2031 -13.8; 2234 -14.4; 2457 -13.4; 2703 -11.3; 2973 -8.0; 3270 -6.0; 3597 -5.0; 3957 -4.2; 4353 -0.5; 4788 -1.4; 5267 -7.6; 5793 -10.7; 6373 -7.7; 7010 -5.6; 7711 -6.6; 8482 -10.5; 9330 -12.2; 10263 -9.2; 11289 -6.0; 12418 -5.8; 13660 -6.1; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lear LUF 4C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF 4C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 103 Hz  |  1.25 | -3.6 dB |
| Peaking | 2147 Hz |  1.84 | -9.7 dB |
| Peaking | 4653 Hz |  2.3  | 8.2 dB  |
| Peaking | 5570 Hz |  4.51 | -8.7 dB |
| Peaking | 9222 Hz |  4.23 | -7.2 dB |
| Peaking | 169 Hz  |  2.07 | -1.6 dB |
| Peaking | 536 Hz  |  0.57 | 2.4 dB  |
| Peaking | 1505 Hz |  2.99 | -2.4 dB |
| Peaking | 3262 Hz |  8.59 | 0.9 dB  |
| Peaking | 4004 Hz | 12.02 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB   |
| Peaking | 500 Hz   | 1.41 | 2.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF%204C/Lear%20LUF%204C.png)