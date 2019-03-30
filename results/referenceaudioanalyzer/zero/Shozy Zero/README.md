# Shozy Zero
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.3; 23 -16.1; 25 -15.9; 28 -15.6; 31 -15.4; 34 -15.1; 37 -14.9; 41 -14.6; 45 -14.3; 49 -14.0; 54 -13.7; 60 -13.3; 66 -13.0; 72 -12.7; 79 -12.4; 87 -12.0; 96 -11.7; 106 -11.4; 116 -11.1; 128 -10.8; 141 -10.5; 155 -10.2; 170 -10.0; 187 -9.7; 206 -9.4; 227 -9.1; 249 -8.7; 274 -8.4; 302 -8.3; 332 -8.3; 365 -8.3; 402 -8.0; 442 -7.6; 486 -7.2; 535 -6.9; 588 -6.5; 647 -6.1; 712 -5.6; 783 -5.2; 861 -4.9; 947 -4.4; 1042 -4.0; 1146 -3.6; 1261 -3.3; 1387 -2.9; 1526 -2.6; 1678 -2.5; 1846 -2.2; 2031 -2.1; 2234 -2.2; 2457 -2.2; 2703 -2.2; 2973 -2.1; 3270 -1.7; 3597 -1.4; 3957 -1.0; 4353 -0.7; 4788 -0.5; 5267 -0.7; 5793 -2.0; 6373 -3.5; 7010 -3.3; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy Zero GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy Zero ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 10 Hz   | 0.84 | -10.8 dB |
| Peaking | 31 Hz   | 0.35 | -7.7 dB  |
| Peaking | 208 Hz  | 0.27 | -3.2 dB  |
| Peaking | 1796 Hz | 0.6  | 3.1 dB   |
| Peaking | 4669 Hz | 1.93 | 3.7 dB   |
| Peaking | 280 Hz  | 3.57 | 0.4 dB   |
| Peaking | 375 Hz  | 3.65 | -0.4 dB  |
| Peaking | 5435 Hz | 9.15 | 0.8 dB   |
| Peaking | 8767 Hz | 1.86 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shozy%20Zero/Shozy%20Zero.png)