# Sony WH-H900N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.4; 25 -4.2; 28 -4.0; 31 -3.9; 34 -3.8; 37 -3.8; 41 -3.7; 45 -3.7; 49 -3.7; 54 -3.7; 60 -3.7; 66 -3.9; 72 -4.0; 79 -4.2; 87 -4.5; 96 -4.7; 106 -4.9; 116 -5.1; 128 -5.1; 141 -5.0; 155 -4.9; 170 -4.5; 187 -4.2; 206 -3.8; 227 -3.4; 249 -3.0; 274 -2.8; 302 -2.5; 332 -2.3; 365 -1.9; 402 -1.6; 442 -1.3; 486 -1.2; 535 -1.3; 588 -1.7; 647 -1.8; 712 -1.9; 783 -0.5; 861 -1.0; 947 -2.2; 1042 -2.9; 1146 -3.5; 1261 -3.4; 1387 -3.0; 1526 -3.9; 1678 -4.7; 1846 -5.2; 2031 -5.1; 2234 -4.2; 2457 -2.4; 2703 -3.0; 2973 -5.7; 3270 -3.8; 3597 -1.4; 3957 -7.0; 4353 -6.7; 4788 -2.4; 5267 -2.9; 5793 -2.4; 6373 -1.3; 7010 -0.6; 7711 -2.8; 8482 -5.2; 9330 -3.7; 10263 -3.1; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -3.1; 16529 -3.1; 18182 -3.1; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-H900N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-H900N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 132 Hz  |  0.79 | -2.2 dB |
| Peaking | 512 Hz  |  0.64 | 2.1 dB  |
| Peaking | 1831 Hz |  2.58 | -2.5 dB |
| Peaking | 4142 Hz | 12.08 | -6.6 dB |
| Peaking | 6691 Hz |  7.58 | 3.6 dB  |
| Peaking | 19 Hz   |  1.47 | -1.5 dB |
| Peaking | 615 Hz  |  6.39 | -0.7 dB |
| Peaking | 1149 Hz |  6.06 | -1.2 dB |
| Peaking | 2355 Hz |  0.15 | 0.2 dB  |
| Peaking | 8673 Hz |  7.29 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-H900N/Sony%20WH-H900N.png)