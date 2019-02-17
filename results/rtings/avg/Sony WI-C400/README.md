# Sony WI-C400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.3; 72 -2.2; 79 -3.3; 87 -4.5; 96 -5.7; 106 -6.9; 116 -8.0; 128 -9.1; 141 -10.0; 155 -10.6; 170 -11.1; 187 -11.4; 206 -11.5; 227 -11.5; 249 -11.2; 274 -11.1; 302 -11.0; 332 -10.6; 365 -10.1; 402 -9.5; 442 -8.9; 486 -8.3; 535 -7.6; 588 -7.0; 647 -6.4; 712 -5.9; 783 -5.5; 861 -5.4; 947 -6.0; 1042 -6.8; 1146 -7.6; 1261 -8.6; 1387 -9.0; 1526 -9.1; 1678 -9.4; 1846 -9.8; 2031 -10.1; 2234 -9.7; 2457 -9.2; 2703 -9.4; 2973 -10.1; 3270 -10.9; 3597 -11.4; 3957 -11.9; 4353 -12.8; 4788 -13.3; 5267 -13.8; 5793 -13.0; 6373 -11.6; 7010 -9.7; 7711 -9.3; 8482 -11.0; 9330 -10.6; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -11.7; 18182 -11.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.41 | 7.3 dB  |
| Peaking | 182 Hz   | 0.74 | -7.2 dB |
| Peaking | 3979 Hz  | 0.58 | -4.0 dB |
| Peaking | 5317 Hz  | 2.04 | -3.7 dB |
| Peaking | 17521 Hz | 2.12 | -6.6 dB |
| Peaking | 360 Hz   | 2.51 | -1.2 dB |
| Peaking | 822 Hz   | 1.73 | 2.6 dB  |
| Peaking | 1462 Hz  | 1.75 | -1.6 dB |
| Peaking | 9010 Hz  | 4.35 | -4.9 dB |
| Peaking | 10266 Hz | 1.22 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | -5.7 dB |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-C400/Sony%20WI-C400.png)