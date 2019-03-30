# Razer Kraken Pro V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.9; 25 -7.6; 28 -8.5; 31 -9.2; 34 -9.9; 37 -10.5; 41 -11.1; 45 -11.7; 49 -12.1; 54 -12.6; 60 -13.1; 66 -13.4; 72 -13.7; 79 -13.9; 87 -14.0; 96 -14.2; 106 -14.2; 116 -14.2; 128 -14.2; 141 -13.9; 155 -13.9; 170 -13.8; 187 -13.5; 206 -13.3; 227 -12.8; 249 -12.1; 274 -12.1; 302 -13.1; 332 -13.7; 365 -13.0; 402 -11.6; 442 -10.1; 486 -8.5; 535 -7.6; 588 -7.4; 647 -7.4; 712 -6.9; 783 -7.0; 861 -7.6; 947 -7.4; 1042 -6.3; 1146 -4.8; 1261 -3.1; 1387 -1.6; 1526 -0.6; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.6; 3957 -1.8; 4353 -1.9; 4788 -2.9; 5267 -4.1; 5793 -4.8; 6373 -4.3; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken Pro V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken Pro V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 0.89 | -3.3 dB |
| Peaking | 144 Hz  | 0.49 | -6.8 dB |
| Peaking | 346 Hz  | 3.22 | -3.9 dB |
| Peaking | 1606 Hz | 2.32 | 4.3 dB  |
| Peaking | 2999 Hz | 0.92 | 5.9 dB  |
| Peaking | 550 Hz  | 4.69 | 0.9 dB  |
| Peaking | 938 Hz  | 4.26 | -1.8 dB |
| Peaking | 1303 Hz | 5.85 | 0.9 dB  |
| Peaking | 6810 Hz | 8.52 | 2.3 dB  |
| Peaking | 8254 Hz | 1.87 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Razer%20Kraken%20Pro%20V2/Razer%20Kraken%20Pro%20V2.png)