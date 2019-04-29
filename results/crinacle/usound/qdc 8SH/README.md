# qdc 8SH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.8; 25 -5.0; 28 -5.2; 31 -5.4; 34 -5.6; 37 -5.7; 41 -5.9; 45 -6.1; 49 -6.2; 54 -6.3; 60 -6.5; 66 -6.8; 72 -7.1; 79 -7.3; 87 -7.5; 96 -7.9; 106 -8.1; 116 -8.3; 128 -8.3; 141 -8.5; 155 -8.6; 170 -8.4; 187 -8.3; 206 -8.1; 227 -7.8; 249 -7.5; 274 -7.2; 302 -6.8; 332 -6.5; 365 -6.2; 402 -6.0; 442 -5.8; 486 -5.6; 535 -5.5; 588 -5.5; 647 -5.7; 712 -6.0; 783 -6.4; 861 -7.1; 947 -7.9; 1042 -9.0; 1146 -10.1; 1261 -10.7; 1387 -10.6; 1526 -9.9; 1678 -8.9; 1846 -7.9; 2031 -7.2; 2234 -6.8; 2457 -6.2; 2703 -5.1; 2973 -3.9; 3270 -3.9; 3597 -4.1; 3957 -4.3; 4353 -5.7; 4788 -3.8; 5267 -0.5; 5793 -0.5; 6373 -3.0; 7010 -4.8; 7711 -7.6; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.7; 20000 -14.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 8SH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 8SH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.91 | 1.8 dB  |
| Peaking | 138 Hz  | 1.23 | -2.3 dB |
| Peaking | 1340 Hz | 2.32 | -4.8 dB |
| Peaking | 3191 Hz | 2.99 | 2.9 dB  |
| Peaking | 5580 Hz | 3.9  | 6.7 dB  |
| Peaking | 226 Hz  | 2.44 | -0.7 dB |
| Peaking | 558 Hz  | 1.2  | 1.4 dB  |
| Peaking | 1056 Hz | 3.9  | -1.0 dB |
| Peaking | 6685 Hz | 4.71 | 1.2 dB  |
| Peaking | 7864 Hz | 4.84 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%208SH/qdc%208SH.png)