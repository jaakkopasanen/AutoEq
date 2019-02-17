# Sony WI-C300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.9; 37 -1.3; 41 -1.9; 45 -2.4; 49 -2.9; 54 -3.5; 60 -4.4; 66 -5.2; 72 -5.9; 79 -6.6; 87 -7.4; 96 -8.2; 106 -9.1; 116 -9.8; 128 -10.6; 141 -11.1; 155 -11.5; 170 -11.7; 187 -11.8; 206 -11.8; 227 -11.6; 249 -11.2; 274 -10.7; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.3; 442 -8.8; 486 -8.3; 535 -7.7; 588 -7.1; 647 -6.5; 712 -5.9; 783 -5.6; 861 -5.6; 947 -6.0; 1042 -7.0; 1146 -7.9; 1261 -8.7; 1387 -8.9; 1526 -9.3; 1678 -9.8; 1846 -10.1; 2031 -10.4; 2234 -10.0; 2457 -9.2; 2703 -9.0; 2973 -9.3; 3270 -9.7; 3597 -10.3; 3957 -10.9; 4353 -11.9; 4788 -12.4; 5267 -11.8; 5793 -9.3; 6373 -6.9; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -7.8; 10263 -10.1; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -9.0; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.56 | 6.5 dB  |
| Peaking | 177 Hz   | 0.73 | -6.0 dB |
| Peaking | 1962 Hz  | 1.65 | -3.6 dB |
| Peaking | 4568 Hz  | 2.32 | -5.9 dB |
| Peaking | 16568 Hz | 2.57 | -2.7 dB |
| Peaking | 821 Hz   | 2.74 | 2.2 dB  |
| Peaking | 1282 Hz  | 3.5  | -1.1 dB |
| Peaking | 5438 Hz  | 6.76 | -1.8 dB |
| Peaking | 7001 Hz  | 3.73 | 2.7 dB  |
| Peaking | 10164 Hz | 6.96 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-C300/Sony%20WI-C300.png)