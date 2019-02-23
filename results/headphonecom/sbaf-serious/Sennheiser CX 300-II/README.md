# Sennheiser CX 300-II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.1; 25 -7.4; 28 -7.8; 31 -8.1; 34 -8.3; 37 -8.5; 41 -8.8; 45 -9.1; 49 -9.3; 54 -9.7; 60 -10.1; 66 -10.3; 72 -10.6; 79 -10.9; 87 -11.3; 96 -11.6; 106 -11.8; 116 -12.0; 128 -12.1; 141 -12.3; 155 -12.4; 170 -12.4; 187 -12.3; 206 -12.1; 227 -11.8; 249 -11.5; 274 -11.2; 302 -10.7; 332 -10.2; 365 -9.6; 402 -9.0; 442 -8.5; 486 -7.9; 535 -7.2; 588 -6.6; 647 -5.9; 712 -5.4; 783 -4.9; 861 -4.7; 947 -4.6; 1042 -4.5; 1146 -4.6; 1261 -4.6; 1387 -4.6; 1526 -4.5; 1678 -4.4; 1846 -4.1; 2031 -3.7; 2234 -3.0; 2457 -2.1; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.9; 4788 -4.8; 5267 -6.0; 5793 -9.4; 6373 -10.6; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 300-II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 300-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 78 Hz   | 0.51 | -2.1 dB |
| Peaking | 200 Hz  | 0.48 | -4.9 dB |
| Peaking | 833 Hz  | 0.89 | 2.6 dB  |
| Peaking | 3280 Hz | 1.24 | 6.5 dB  |
| Peaking | 6080 Hz | 5.1  | -6.5 dB |
| Peaking | 4030 Hz | 8.89 | 1.3 dB  |
| Peaking | 4659 Hz | 5.76 | -0.8 dB |
| Peaking | 7168 Hz | 9.9  | 1.5 dB  |
| Peaking | 8724 Hz | 1.01 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20300-II/Sennheiser%20CX%20300-II.png)