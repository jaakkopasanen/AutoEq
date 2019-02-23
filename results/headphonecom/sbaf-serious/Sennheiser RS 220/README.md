# Sennheiser RS 220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.7; 31 -2.3; 34 -2.8; 37 -3.2; 41 -3.7; 45 -4.1; 49 -4.5; 54 -4.9; 60 -5.5; 66 -5.3; 72 -4.9; 79 -6.3; 87 -7.1; 96 -7.6; 106 -8.0; 116 -8.3; 128 -8.5; 141 -8.8; 155 -8.8; 170 -8.8; 187 -8.9; 206 -8.9; 227 -8.5; 249 -8.3; 274 -8.1; 302 -8.0; 332 -7.9; 365 -7.6; 402 -7.7; 442 -7.7; 486 -7.3; 535 -6.9; 588 -6.9; 647 -6.9; 712 -6.8; 783 -6.8; 861 -6.9; 947 -7.0; 1042 -7.2; 1146 -7.2; 1261 -7.5; 1387 -6.0; 1526 -3.5; 1678 -3.0; 1846 -3.1; 2031 -5.3; 2234 -9.1; 2457 -11.1; 2703 -9.8; 2973 -8.0; 3270 -7.0; 3597 -4.4; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -2.9; 5793 -5.0; 6373 -1.3; 7010 -7.2; 7711 -7.8; 8482 -6.5; 9330 -7.2; 10263 -8.6; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.32 | 7.3 dB  |
| Peaking | 159 Hz  | 0.7  | -2.8 dB |
| Peaking | 1813 Hz | 2.1  | 10.9 dB |
| Peaking | 2302 Hz | 1.03 | -9.7 dB |
| Peaking | 4304 Hz | 1.9  | 9.2 dB  |
| Peaking | 420 Hz  | 3.25 | -0.5 dB |
| Peaking | 986 Hz  | 0.48 | 0.4 dB  |
| Peaking | 1243 Hz | 6.72 | -1.4 dB |
| Peaking | 6407 Hz | 8.62 | 6.5 dB  |
| Peaking | 6981 Hz | 2.24 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)