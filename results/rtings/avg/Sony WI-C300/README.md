# Sony WI-C300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.0; 60 -1.9; 66 -2.7; 72 -3.4; 79 -4.2; 87 -4.9; 96 -5.8; 106 -6.6; 116 -7.3; 128 -8.1; 141 -8.6; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.3; 227 -9.1; 249 -8.7; 274 -8.2; 302 -7.7; 332 -7.5; 365 -7.1; 402 -6.8; 442 -6.3; 486 -5.8; 535 -5.2; 588 -4.6; 647 -4.0; 712 -3.4; 783 -3.1; 861 -3.1; 947 -3.5; 1042 -4.5; 1146 -5.4; 1261 -6.2; 1387 -6.4; 1526 -6.8; 1678 -7.3; 1846 -7.6; 2031 -7.9; 2234 -7.5; 2457 -6.7; 2703 -6.5; 2973 -6.8; 3270 -7.2; 3597 -7.8; 3957 -8.4; 4353 -9.4; 4788 -9.9; 5267 -9.3; 5793 -6.8; 6373 -4.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.38 | 6.8 dB  |
| Peaking | 157 Hz  | 0.74 | -4.7 dB |
| Peaking | 770 Hz  | 1.73 | 4.0 dB  |
| Peaking | 5407 Hz | 1.38 | -5.1 dB |
| Peaking | 6473 Hz | 2.93 | 6.6 dB  |
| Peaking | 950 Hz  | 6.06 | 0.8 dB  |
| Peaking | 2079 Hz | 1.65 | -2.0 dB |
| Peaking | 2647 Hz | 2.19 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-C300/Sony%20WI-C300.png)