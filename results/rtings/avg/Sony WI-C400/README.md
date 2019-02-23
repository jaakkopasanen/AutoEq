# Sony WI-C400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.4; 96 -2.6; 106 -3.8; 116 -4.9; 128 -5.9; 141 -6.8; 155 -7.5; 170 -8.0; 187 -8.3; 206 -8.4; 227 -8.3; 249 -8.1; 274 -8.0; 302 -7.9; 332 -7.5; 365 -7.0; 402 -6.4; 442 -5.8; 486 -5.1; 535 -4.5; 588 -3.9; 647 -3.3; 712 -2.8; 783 -2.3; 861 -2.3; 947 -2.9; 1042 -3.7; 1146 -4.5; 1261 -5.4; 1387 -5.8; 1526 -5.9; 1678 -6.3; 1846 -6.7; 2031 -7.0; 2234 -6.6; 2457 -6.0; 2703 -6.2; 2973 -7.0; 3270 -7.7; 3597 -8.3; 3957 -8.8; 4353 -9.7; 4788 -10.2; 5267 -10.7; 5793 -9.9; 6373 -8.5; 7010 -6.6; 7711 -6.2; 8482 -7.9; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.6; 18182 -8.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 59 Hz    |  0.28 | 7.6 dB  |
| Peaking | 181 Hz   |  0.74 | -6.7 dB |
| Peaking | 782 Hz   |  1.43 | 4.6 dB  |
| Peaking | 4966 Hz  |  2    | -4.3 dB |
| Peaking | 17491 Hz |  2.92 | -3.2 dB |
| Peaking | 18 Hz    |  1.15 | 1.8 dB  |
| Peaking | 41 Hz    |  0.58 | -0.9 dB |
| Peaking | 79 Hz    |  3.34 | 1.5 dB  |
| Peaking | 7304 Hz  | 10.06 | 1.7 dB  |
| Peaking | 14578 Hz |  3.59 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-C400/Sony%20WI-C400.png)