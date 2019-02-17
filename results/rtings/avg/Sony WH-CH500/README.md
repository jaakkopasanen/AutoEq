# Sony WH-CH500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -2.5; 37 -4.2; 41 -6.2; 45 -7.7; 49 -9.0; 54 -10.1; 60 -11.0; 66 -11.7; 72 -12.0; 79 -12.0; 87 -11.7; 96 -11.3; 106 -10.7; 116 -10.2; 128 -9.5; 141 -8.8; 155 -8.2; 170 -7.6; 187 -7.1; 206 -6.7; 227 -6.3; 249 -6.1; 274 -5.9; 302 -5.8; 332 -5.8; 365 -5.6; 402 -5.1; 442 -5.2; 486 -5.8; 535 -6.2; 588 -6.4; 647 -6.0; 712 -5.8; 783 -5.9; 861 -6.1; 947 -6.4; 1042 -6.4; 1146 -6.4; 1261 -6.8; 1387 -6.9; 1526 -6.9; 1678 -6.8; 1846 -6.6; 2031 -6.3; 2234 -5.4; 2457 -5.0; 2703 -5.4; 2973 -6.5; 3270 -6.7; 3597 -6.4; 3957 -3.8; 4353 -0.9; 4788 -0.5; 5267 -1.8; 5793 -1.0; 6373 -3.6; 7010 -5.9; 7711 -8.6; 8482 -10.4; 9330 -12.0; 10263 -10.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.25 | 7.6 dB  |
| Peaking | 72 Hz   | 1.05 | -6.8 dB |
| Peaking | 1516 Hz | 4.08 | -0.6 dB |
| Peaking | 5119 Hz | 2.05 | 6.7 dB  |
| Peaking | 9079 Hz | 2.89 | -6.5 dB |
| Peaking | 250 Hz  | 3.22 | 0.8 dB  |
| Peaking | 412 Hz  | 1.98 | 1.4 dB  |
| Peaking | 2504 Hz | 4.31 | 1.7 dB  |
| Peaking | 3472 Hz | 2.27 | -2.1 dB |
| Peaking | 4287 Hz | 6.32 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | -7.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-CH500/Sony%20WH-CH500.png)