# Polk Audio UltraFit 500 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.2; 60 -2.6; 66 -3.8; 72 -4.8; 79 -5.8; 87 -6.7; 96 -7.5; 106 -8.1; 116 -8.6; 128 -9.2; 141 -9.6; 155 -9.9; 170 -10.3; 187 -10.4; 206 -10.5; 227 -10.6; 249 -10.8; 274 -10.7; 302 -10.8; 332 -10.8; 365 -10.6; 402 -10.8; 442 -11.1; 486 -11.4; 535 -11.7; 588 -12.1; 647 -12.6; 712 -12.9; 783 -13.1; 861 -13.0; 947 -12.8; 1042 -11.9; 1146 -9.4; 1261 -8.0; 1387 -9.3; 1526 -8.6; 1678 -7.0; 1846 -4.9; 2031 -3.1; 2234 -2.1; 2457 -2.1; 2703 -2.3; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -5.9; 4788 -6.8; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 500 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 500 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.45 | 10.2 dB |
| Peaking | 117 Hz  | 0.34 | -6.8 dB |
| Peaking | 815 Hz  | 0.98 | -6.2 dB |
| Peaking | 2864 Hz | 1.25 | 6.4 dB  |
| Peaking | 5999 Hz | 4.72 | 5.8 dB  |
| Peaking | 1560 Hz | 3.99 | -2.8 dB |
| Peaking | 1945 Hz | 1.26 | 1.9 dB  |
| Peaking | 2735 Hz | 3.98 | -3.0 dB |
| Peaking | 4065 Hz | 2.09 | 2.9 dB  |
| Peaking | 4561 Hz | 6.8  | -6.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | -6.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%20500%20sample%202/Polk%20Audio%20UltraFit%20500%20sample%202.png)