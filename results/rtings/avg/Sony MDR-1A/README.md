# Sony MDR-1A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.5; 28 -6.7; 31 -6.9; 34 -6.9; 37 -6.9; 41 -6.9; 45 -6.8; 49 -6.7; 54 -6.7; 60 -6.6; 66 -6.7; 72 -6.8; 79 -7.1; 87 -7.4; 96 -7.7; 106 -7.9; 116 -7.9; 128 -7.7; 141 -7.3; 155 -6.8; 170 -6.1; 187 -5.3; 206 -4.7; 227 -4.5; 249 -4.7; 274 -3.7; 302 -2.7; 332 -2.3; 365 -2.0; 402 -1.9; 442 -2.1; 486 -2.7; 535 -3.1; 588 -3.5; 647 -3.8; 712 -3.9; 783 -3.8; 861 -3.9; 947 -4.1; 1042 -4.2; 1146 -4.2; 1261 -4.4; 1387 -4.7; 1526 -5.1; 1678 -5.4; 1846 -5.8; 2031 -6.1; 2234 -5.7; 2457 -4.4; 2703 -3.3; 2973 -2.6; 3270 -2.1; 3597 -1.8; 3957 -4.4; 4353 -4.3; 4788 -1.9; 5267 -2.4; 5793 -1.8; 6373 -0.5; 7010 -2.2; 7711 -6.3; 8482 -10.3; 9330 -10.0; 10263 -6.8; 11289 -4.6; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -6.9; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.66 | -2.3 dB |
| Peaking | 116 Hz  | 1.17 | -3.3 dB |
| Peaking | 382 Hz  | 1.55 | 2.9 dB  |
| Peaking | 6740 Hz | 1.48 | 5.7 dB  |
| Peaking | 8653 Hz | 2.67 | -9.8 dB |
| Peaking | 2037 Hz | 2.36 | -2.6 dB |
| Peaking | 3592 Hz | 1.56 | 3.2 dB  |
| Peaking | 4126 Hz | 5.34 | -4.2 dB |
| Peaking | 5530 Hz | 9.73 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-1A/Sony%20MDR-1A.png)