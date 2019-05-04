# Swimbuds Swimbuds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.2; 23 -16.1; 25 -16.0; 28 -15.8; 31 -15.7; 34 -15.5; 37 -15.4; 41 -15.2; 45 -15.1; 49 -15.0; 54 -14.9; 60 -14.9; 66 -14.9; 72 -15.0; 79 -15.0; 87 -15.1; 96 -15.2; 106 -15.3; 116 -15.4; 128 -15.4; 141 -15.4; 155 -15.2; 170 -15.1; 187 -14.8; 206 -14.6; 227 -14.3; 249 -14.2; 274 -14.1; 302 -13.7; 332 -13.4; 365 -13.1; 402 -12.4; 442 -11.7; 486 -11.2; 535 -10.6; 588 -10.1; 647 -9.9; 712 -10.0; 783 -10.3; 861 -10.8; 947 -11.5; 1042 -12.6; 1146 -13.4; 1261 -13.4; 1387 -12.4; 1526 -11.0; 1678 -9.5; 1846 -8.3; 2031 -7.3; 2234 -6.3; 2457 -4.0; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Swimbuds Swimbuds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Swimbuds Swimbuds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 1.43 | -9.5 dB |
| Peaking | 26 Hz   | 0.24 | -7.6 dB |
| Peaking | 209 Hz  | 0.46 | -6.5 dB |
| Peaking | 1292 Hz | 1.37 | -7.2 dB |
| Peaking | 3789 Hz | 0.88 | 7.6 dB  |
| Peaking | 2277 Hz | 4.33 | -1.9 dB |
| Peaking | 2705 Hz | 4.27 | 2.7 dB  |
| Peaking | 3856 Hz | 3.02 | -1.2 dB |
| Peaking | 6280 Hz | 2.45 | 5.1 dB  |
| Peaking | 7412 Hz | 1.52 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -5.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Swimbuds%20Swimbuds/Swimbuds%20Swimbuds.png)