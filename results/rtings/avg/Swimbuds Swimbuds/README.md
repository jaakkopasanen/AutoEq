# Swimbuds Swimbuds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.5; 25 -11.4; 28 -11.2; 31 -11.0; 34 -10.9; 37 -10.8; 41 -10.6; 45 -10.5; 49 -10.4; 54 -10.4; 60 -10.7; 66 -10.9; 72 -11.2; 79 -11.5; 87 -11.9; 96 -12.3; 106 -12.9; 116 -13.4; 128 -13.9; 141 -14.3; 155 -14.6; 170 -14.7; 187 -14.8; 206 -14.7; 227 -14.6; 249 -14.5; 274 -14.3; 302 -14.0; 332 -13.6; 365 -13.3; 402 -12.6; 442 -12.0; 486 -11.4; 535 -10.8; 588 -10.3; 647 -10.1; 712 -10.1; 783 -10.4; 861 -10.9; 947 -11.7; 1042 -12.7; 1146 -13.5; 1261 -13.5; 1387 -12.5; 1526 -11.0; 1678 -9.5; 1846 -8.2; 2031 -7.1; 2234 -5.7; 2457 -3.4; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 14 Hz   | 0.3  | -5.2 dB |
| Peaking | 147 Hz  | 0.71 | -5.9 dB |
| Peaking | 311 Hz  | 0.87 | -4.7 dB |
| Peaking | 1278 Hz | 1.25 | -7.8 dB |
| Peaking | 3677 Hz | 0.84 | 7.7 dB  |
| Peaking | 2200 Hz | 4.53 | -1.3 dB |
| Peaking | 2700 Hz | 4.7  | 2.2 dB  |
| Peaking | 3776 Hz | 2.94 | -1.2 dB |
| Peaking | 6271 Hz | 2.38 | 5.1 dB  |
| Peaking | 7424 Hz | 1.5  | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -6.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Swimbuds%20Swimbuds/Swimbuds%20Swimbuds.png)