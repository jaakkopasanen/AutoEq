# Polk Audio UltraFit 1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.3; 45 -2.4; 49 -3.3; 54 -4.3; 60 -5.4; 66 -6.4; 72 -7.2; 79 -7.9; 87 -8.7; 96 -9.4; 106 -10.0; 116 -10.5; 128 -11.1; 141 -11.8; 155 -12.3; 170 -12.8; 187 -13.2; 206 -13.6; 227 -13.9; 249 -14.2; 274 -14.4; 302 -14.5; 332 -14.5; 365 -14.5; 402 -14.4; 442 -14.2; 486 -13.8; 535 -13.9; 588 -13.9; 647 -14.0; 712 -14.0; 783 -14.0; 861 -13.9; 947 -12.8; 1042 -9.1; 1146 -10.9; 1261 -11.6; 1387 -12.4; 1526 -12.9; 1678 -12.0; 1846 -9.8; 2031 -7.2; 2234 -4.3; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.7  | 7.2 dB  |
| Peaking | 299 Hz  | 0.34 | -8.1 dB |
| Peaking | 785 Hz  | 2.32 | -3.2 dB |
| Peaking | 1618 Hz | 2.03 | -8.6 dB |
| Peaking | 3101 Hz | 0.67 | 8.4 dB  |
| Peaking | 2471 Hz | 8.11 | 2.5 dB  |
| Peaking | 2806 Hz | 4.65 | 1.7 dB  |
| Peaking | 2876 Hz | 1.94 | -2.0 dB |
| Peaking | 6227 Hz | 2.08 | 5.7 dB  |
| Peaking | 7432 Hz | 1.42 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | -6.1 dB |
| Peaking | 1000 Hz  | 1.41 | -5.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%201000/Polk%20Audio%20UltraFit%201000.png)