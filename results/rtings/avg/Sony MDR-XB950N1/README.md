# Sony MDR-XB950N1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -14.0; 25 -14.2; 28 -14.3; 31 -14.3; 34 -14.2; 37 -14.1; 41 -14.0; 45 -13.8; 49 -13.6; 54 -13.5; 60 -13.4; 66 -13.4; 72 -13.5; 79 -13.8; 87 -14.2; 96 -14.6; 106 -14.8; 116 -14.7; 128 -14.4; 141 -13.8; 155 -13.2; 170 -12.5; 187 -11.6; 206 -10.5; 227 -9.2; 249 -7.9; 274 -6.6; 302 -5.5; 332 -4.9; 365 -4.9; 402 -5.2; 442 -5.7; 486 -6.2; 535 -6.5; 588 -6.6; 647 -6.6; 712 -6.5; 783 -6.5; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -6.8; 1387 -6.4; 1526 -6.2; 1678 -6.1; 1846 -5.9; 2031 -4.8; 2234 -3.1; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -3.7; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950N1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950N1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.71 | -6.4 dB |
| Peaking | 132 Hz  | 0.42 | -8.2 dB |
| Peaking | 314 Hz  | 1.15 | 6.4 dB  |
| Peaking | 3246 Hz | 1.43 | 6.7 dB  |
| Peaking | 5912 Hz | 3.78 | 5.1 dB  |
| Peaking | 1911 Hz | 1.62 | -1.4 dB |
| Peaking | 2465 Hz | 3.14 | 2.3 dB  |
| Peaking | 3203 Hz | 4.15 | -1.2 dB |
| Peaking | 4185 Hz | 7.75 | 1.5 dB  |
| Peaking | 8359 Hz | 3.62 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB950N1/Sony%20MDR-XB950N1.png)