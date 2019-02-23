# AKG K701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.4; 60 -1.3; 66 -0.7; 72 -2.1; 79 -3.2; 87 -3.8; 96 -4.2; 106 -4.6; 116 -5.0; 128 -5.6; 141 -5.8; 155 -6.0; 170 -6.1; 187 -6.4; 206 -6.2; 227 -6.4; 249 -6.4; 274 -6.1; 302 -6.0; 332 -5.8; 365 -5.6; 402 -5.5; 442 -5.2; 486 -5.0; 535 -4.6; 588 -3.1; 647 -4.0; 712 -3.9; 783 -4.3; 861 -4.6; 947 -4.9; 1042 -5.1; 1146 -5.4; 1261 -5.6; 1387 -5.8; 1526 -6.5; 1678 -7.0; 1846 -8.1; 2031 -9.3; 2234 -9.6; 2457 -9.0; 2703 -7.8; 2973 -7.5; 3270 -7.0; 3597 -6.9; 3957 -7.4; 4353 -7.9; 4788 -6.9; 5267 -7.5; 5793 -10.3; 6373 -10.1; 7010 -8.8; 7711 -9.3; 8482 -8.7; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 35 Hz   |  0.58 | 6.7 dB  |
| Peaking | 697 Hz  |  1.23 | 2.8 dB  |
| Peaking | 2199 Hz |  2.81 | -3.5 dB |
| Peaking | 6050 Hz |  4.84 | -3.9 dB |
| Peaking | 7921 Hz |  3.64 | -2.6 dB |
| Peaking | 35 Hz   |  2.66 | -0.7 dB |
| Peaking | 66 Hz   |  5.91 | 1.9 dB  |
| Peaking | 172 Hz  |  1.34 | -0.7 dB |
| Peaking | 1324 Hz |  5.75 | 0.6 dB  |
| Peaking | 4299 Hz | 10.6  | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K701/AKG%20K701.png)