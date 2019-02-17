# Sony WH-H900N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -4.7; 25 -4.5; 28 -4.3; 31 -4.2; 34 -4.2; 37 -4.1; 41 -4.0; 45 -4.0; 49 -4.0; 54 -4.0; 60 -4.0; 66 -4.2; 72 -4.4; 79 -4.5; 87 -4.8; 96 -5.0; 106 -5.2; 116 -5.4; 128 -5.4; 141 -5.3; 155 -5.2; 170 -4.9; 187 -4.5; 206 -4.1; 227 -3.7; 249 -3.3; 274 -3.1; 302 -2.8; 332 -2.6; 365 -2.3; 402 -1.9; 442 -1.6; 486 -1.5; 535 -1.7; 588 -2.0; 647 -2.1; 712 -2.2; 783 -0.8; 861 -1.3; 947 -2.5; 1042 -3.2; 1146 -3.8; 1261 -3.7; 1387 -3.3; 1526 -4.2; 1678 -5.0; 1846 -5.5; 2031 -5.4; 2234 -4.5; 2457 -2.7; 2703 -3.3; 2973 -6.0; 3270 -4.1; 3597 -1.7; 3957 -7.3; 4353 -7.0; 4788 -2.7; 5267 -3.2; 5793 -2.7; 6373 -1.6; 7010 -0.5; 7711 -2.7; 8482 -5.6; 9330 -4.0; 10263 -3.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-H900N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-H900N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 125 Hz  |  1.49 | -2.5 dB |
| Peaking | 1888 Hz |  3.19 | -2.8 dB |
| Peaking | 4151 Hz | 10.59 | -6.9 dB |
| Peaking | 6781 Hz |  9.29 | 3.6 dB  |
| Peaking | 11 Hz   |  0.18 | -1.5 dB |
| Peaking | 410 Hz  |  2.81 | 1.0 dB  |
| Peaking | 525 Hz  |  2.9  | 1.2 dB  |
| Peaking | 813 Hz  |  6.8  | 2.5 dB  |
| Peaking | 8687 Hz |  7.77 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-H900N/Sony%20WH-H900N.png)