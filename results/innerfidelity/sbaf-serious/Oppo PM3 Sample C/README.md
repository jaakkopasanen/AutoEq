# Oppo PM3 sample C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.6; 25 -4.7; 28 -4.9; 31 -5.0; 34 -5.0; 37 -5.0; 41 -5.1; 45 -5.1; 49 -5.0; 54 -5.1; 60 -5.3; 66 -5.4; 72 -5.4; 79 -5.5; 87 -5.6; 96 -6.0; 106 -6.9; 116 -7.5; 128 -8.1; 141 -8.4; 155 -8.2; 170 -7.3; 187 -8.1; 206 -7.7; 227 -6.9; 249 -6.2; 274 -5.3; 302 -4.5; 332 -3.9; 365 -3.5; 402 -3.8; 442 -4.2; 486 -5.1; 535 -5.9; 588 -6.1; 647 -6.7; 712 -7.1; 783 -7.0; 861 -7.0; 947 -7.0; 1042 -7.2; 1146 -7.6; 1261 -7.7; 1387 -8.2; 1526 -8.7; 1678 -8.7; 1846 -9.6; 2031 -9.6; 2234 -10.1; 2457 -9.0; 2703 -8.3; 2973 -7.8; 3270 -7.0; 3597 -7.2; 3957 -7.7; 4353 -7.0; 4788 -4.4; 5267 -1.0; 5793 -0.5; 6373 -1.1; 7010 -4.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 sample C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 sample C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 39 Hz   |  0.24 | 1.8 dB  |
| Peaking | 152 Hz  |  1.11 | -3.1 dB |
| Peaking | 364 Hz  |  1.93 | 3.4 dB  |
| Peaking | 2063 Hz |  0.96 | -3.2 dB |
| Peaking | 5747 Hz |  3.41 | 7.3 dB  |
| Peaking | 168 Hz  | 13.3  | 0.8 dB  |
| Peaking | 710 Hz  |  5.76 | -0.6 dB |
| Peaking | 4140 Hz |  4.38 | -3.4 dB |
| Peaking | 4157 Hz |  1.79 | 1.9 dB  |
| Peaking | 7961 Hz |  3.78 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3%20sample%20C/Oppo%20PM3%20sample%20C.png)