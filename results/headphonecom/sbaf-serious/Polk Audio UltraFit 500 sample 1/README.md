# Polk Audio UltraFit 500 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.7; 66 -2.7; 72 -3.6; 79 -4.5; 87 -5.4; 96 -6.2; 106 -6.9; 116 -7.5; 128 -8.3; 141 -9.0; 155 -9.7; 170 -10.3; 187 -10.9; 206 -11.4; 227 -11.9; 249 -12.3; 274 -12.7; 302 -13.1; 332 -13.2; 365 -13.4; 402 -13.6; 442 -13.8; 486 -13.8; 535 -13.8; 588 -13.6; 647 -13.5; 712 -13.4; 783 -13.2; 861 -13.1; 947 -12.6; 1042 -12.0; 1146 -11.4; 1261 -10.6; 1387 -9.8; 1526 -8.9; 1678 -7.6; 1846 -5.7; 2031 -4.3; 2234 -2.7; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.3; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 500 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 500 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.43 | 7.3 dB  |
| Peaking | 990 Hz  | 0.12 | -8.6 dB |
| Peaking | 2634 Hz | 0.91 | 11.3 dB |
| Peaking | 5090 Hz | 0.94 | 7.4 dB  |
| Peaking | 54 Hz   | 2.74 | 1.9 dB  |
| Peaking | 54 Hz   | 1.13 | -1.2 dB |
| Peaking | 5401 Hz | 9.43 | -4.2 dB |
| Peaking | 6305 Hz | 2.65 | 3.3 dB  |
| Peaking | 7527 Hz | 3.25 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -6.1 dB |
| Peaking | 1000 Hz  | 1.41 | -6.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%20500%20sample%201/Polk%20Audio%20UltraFit%20500%20sample%201.png)