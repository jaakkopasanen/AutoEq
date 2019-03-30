# Sunrise Xcape
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.7; 25 -12.8; 28 -12.9; 31 -12.9; 34 -12.9; 37 -12.9; 41 -12.9; 45 -12.9; 49 -12.9; 54 -12.9; 60 -12.9; 66 -12.8; 72 -12.6; 79 -12.5; 87 -12.6; 96 -12.4; 106 -12.2; 116 -12.1; 128 -11.9; 141 -11.6; 155 -11.5; 170 -11.2; 187 -11.3; 206 -11.5; 227 -11.6; 249 -11.3; 274 -11.0; 302 -10.7; 332 -10.5; 365 -10.3; 402 -10.0; 442 -9.7; 486 -9.3; 535 -8.9; 588 -8.5; 647 -8.2; 712 -7.8; 783 -7.4; 861 -7.0; 947 -6.5; 1042 -6.1; 1146 -5.7; 1261 -5.3; 1387 -4.9; 1526 -4.4; 1678 -4.0; 1846 -3.7; 2031 -3.3; 2234 -3.1; 2457 -2.8; 2703 -2.8; 2973 -3.1; 3270 -3.5; 3597 -4.0; 3957 -5.0; 4353 -5.8; 4788 -5.3; 5267 -3.4; 5793 -0.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sunrise Xcape GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sunrise Xcape ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.2  | -6.9 dB |
| Peaking | 335 Hz  | 0.6  | -3.0 dB |
| Peaking | 2283 Hz | 1.11 | 3.4 dB  |
| Peaking | 6122 Hz | 4.8  | 6.1 dB  |
| Peaking | 3308 Hz | 3.48 | 0.8 dB  |
| Peaking | 4562 Hz | 3.02 | -1.9 dB |
| Peaking | 5351 Hz | 3.22 | 1.3 dB  |
| Peaking | 8289 Hz | 3.77 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sunrise%20Xcape/Sunrise%20Xcape.png)