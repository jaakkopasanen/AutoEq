# Sony MDR-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.1; 25 -7.8; 28 -7.5; 31 -7.1; 34 -6.9; 37 -6.6; 41 -6.4; 45 -6.3; 49 -6.3; 54 -6.4; 60 -6.6; 66 -7.0; 72 -7.3; 79 -7.6; 87 -8.0; 96 -8.3; 106 -8.7; 116 -8.9; 128 -9.1; 141 -9.1; 155 -8.8; 170 -8.5; 187 -8.1; 206 -7.6; 227 -7.1; 249 -7.0; 274 -7.2; 302 -6.8; 332 -6.2; 365 -5.6; 402 -5.6; 442 -6.1; 486 -6.2; 535 -5.8; 588 -4.5; 647 -5.0; 712 -6.6; 783 -5.7; 861 -4.0; 947 -3.7; 1042 -2.3; 1146 -0.5; 1261 -1.0; 1387 -2.4; 1526 -4.8; 1678 -6.2; 1846 -7.0; 2031 -6.6; 2234 -5.3; 2457 -3.6; 2703 -2.8; 2973 -3.4; 3270 -3.2; 3597 -3.5; 3957 -6.0; 4353 -7.6; 4788 -7.1; 5267 -8.2; 5793 -8.5; 6373 -6.3; 7010 -4.0; 7711 -5.7; 8482 -7.0; 9330 -4.7; 10263 -2.9; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -2.9; 18182 -2.9; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.79 | -5.2 dB |
| Peaking | 135 Hz  | 0.57 | -5.8 dB |
| Peaking | 529 Hz  | 1.56 | -1.8 dB |
| Peaking | 1877 Hz | 4.85 | -4.2 dB |
| Peaking | 5408 Hz | 1.75 | -5.5 dB |
| Peaking | 744 Hz  | 7.46 | -2.5 dB |
| Peaking | 1181 Hz | 4.88 | 3.5 dB  |
| Peaking | 6985 Hz | 6.16 | 2.6 dB  |
| Peaking | 8557 Hz | 3.09 | -4.4 dB |
| Peaking | 9781 Hz | 2.47 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-1000X/Sony%20MDR-1000X.png)