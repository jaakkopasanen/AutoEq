# Sony MDR-XB950B1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.7; 23 -14.9; 25 -15.1; 28 -15.3; 31 -15.3; 34 -15.3; 37 -15.2; 41 -15.1; 45 -15.0; 49 -15.0; 54 -15.0; 60 -15.2; 66 -15.4; 72 -15.6; 79 -15.9; 87 -16.3; 96 -16.6; 106 -16.9; 116 -17.0; 128 -16.9; 141 -16.6; 155 -16.0; 170 -15.3; 187 -15.2; 206 -14.3; 227 -12.8; 249 -11.3; 274 -9.5; 302 -7.1; 332 -4.5; 365 -3.2; 402 -4.4; 442 -6.7; 486 -8.3; 535 -9.1; 588 -9.4; 647 -9.4; 712 -9.2; 783 -9.0; 861 -8.7; 947 -8.5; 1042 -7.9; 1146 -7.1; 1261 -7.1; 1387 -6.6; 1526 -6.4; 1678 -6.2; 1846 -5.8; 2031 -5.5; 2234 -4.8; 2457 -3.7; 2703 -2.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -5.8; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950B1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950B1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.34 | -8.6 dB |
| Peaking | 136 Hz  |  1.14 | -7.6 dB |
| Peaking | 2927 Hz |  0.3  | -2.3 dB |
| Peaking | 3118 Hz |  1.49 | 8.1 dB  |
| Peaking | 5806 Hz |  2.61 | 7.0 dB  |
| Peaking | 41 Hz   |  3.24 | 0.5 dB  |
| Peaking | 218 Hz  |  3.09 | -2.5 dB |
| Peaking | 362 Hz  |  2.99 | 6.3 dB  |
| Peaking | 596 Hz  |  1.83 | -2.5 dB |
| Peaking | 4335 Hz | 16.91 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.5 dB  |
| Peaking | 125 Hz   | 1.41 | -10.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB950B1/Sony%20MDR-XB950B1.png)