# AKG K3003 Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.8; 25 -3.2; 28 -3.8; 31 -4.3; 34 -4.7; 37 -5.1; 41 -5.5; 45 -5.9; 49 -6.2; 54 -6.7; 60 -7.2; 66 -7.6; 72 -7.9; 79 -8.4; 87 -8.7; 96 -9.0; 106 -9.3; 116 -9.5; 128 -9.8; 141 -9.9; 155 -10.1; 170 -10.1; 187 -10.0; 206 -9.9; 227 -9.8; 249 -9.6; 274 -9.2; 302 -8.9; 332 -8.4; 365 -7.9; 402 -7.4; 442 -7.1; 486 -6.8; 535 -6.3; 588 -5.8; 647 -5.4; 712 -5.0; 783 -4.8; 861 -4.9; 947 -5.0; 1042 -5.5; 1146 -5.9; 1261 -6.2; 1387 -6.3; 1526 -6.8; 1678 -7.4; 1846 -7.6; 2031 -7.5; 2234 -7.0; 2457 -5.9; 2703 -4.1; 2973 -2.4; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -3.6; 4788 -8.2; 5267 -7.3; 5793 -3.2; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -13.9; 10263 -11.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  1.04 | 4.3 dB  |
| Peaking | 156 Hz  |  0.77 | -3.9 dB |
| Peaking | 3509 Hz |  3.24 | 7.0 dB  |
| Peaking | 6409 Hz |  6.09 | 6.1 dB  |
| Peaking | 9485 Hz |  4.75 | -8.7 dB |
| Peaking | 811 Hz  |  1.75 | 2.2 dB  |
| Peaking | 1958 Hz |  2.2  | -1.8 dB |
| Peaking | 2867 Hz |  6.3  | 1.6 dB  |
| Peaking | 4122 Hz | 10.35 | 3.4 dB  |
| Peaking | 4853 Hz |  6.92 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)