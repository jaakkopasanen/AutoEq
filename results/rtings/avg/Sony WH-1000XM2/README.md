# Sony WH-1000XM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.4; 25 -9.1; 28 -8.7; 31 -8.4; 34 -8.2; 37 -7.9; 41 -7.7; 45 -7.5; 49 -7.4; 54 -7.4; 60 -7.5; 66 -7.7; 72 -7.8; 79 -8.0; 87 -8.2; 96 -8.5; 106 -8.7; 116 -8.9; 128 -9.1; 141 -9.1; 155 -9.1; 170 -9.0; 187 -8.8; 206 -8.4; 227 -7.9; 249 -7.8; 274 -7.5; 302 -7.1; 332 -6.7; 365 -6.2; 402 -5.8; 442 -5.5; 486 -5.2; 535 -4.8; 588 -4.4; 647 -3.8; 712 -3.2; 783 -1.2; 861 -0.5; 947 -0.5; 1042 -0.7; 1146 -2.3; 1261 -4.6; 1387 -7.4; 1526 -9.2; 1678 -10.6; 1846 -12.1; 2031 -11.6; 2234 -9.6; 2457 -8.4; 2703 -8.2; 2973 -7.1; 3270 -6.6; 3597 -7.6; 3957 -8.4; 4353 -6.7; 4788 -5.2; 5267 -7.6; 5793 -7.6; 6373 -3.1; 7010 -4.7; 7711 -7.3; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.98 | -3.1 dB |
| Peaking | 147 Hz  |  0.86 | -2.8 dB |
| Peaking | 961 Hz  |  1.32 | 7.7 dB  |
| Peaking | 1783 Hz |  1.7  | -7.3 dB |
| Peaking | 6533 Hz | 10.1  | 4.2 dB  |
| Peaking | 3293 Hz |  5.22 | 1.1 dB  |
| Peaking | 3942 Hz |  3.83 | -3.2 dB |
| Peaking | 4968 Hz |  1.99 | 3.3 dB  |
| Peaking | 5500 Hz |  6.58 | -4.9 dB |
| Peaking | 7952 Hz |  7.87 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-1000XM2/Sony%20WH-1000XM2.png)