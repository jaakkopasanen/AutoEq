# Jabra Elite 45e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.5; 25 -10.1; 28 -10.8; 31 -11.4; 34 -11.9; 37 -12.3; 41 -12.8; 45 -13.2; 49 -13.6; 54 -13.9; 60 -14.1; 66 -14.4; 72 -14.5; 79 -14.5; 87 -14.5; 96 -14.4; 106 -14.0; 116 -13.7; 128 -13.8; 141 -13.5; 155 -13.1; 170 -12.7; 187 -12.2; 206 -11.8; 227 -11.4; 249 -11.1; 274 -10.9; 302 -10.6; 332 -10.3; 365 -9.9; 402 -9.6; 442 -9.2; 486 -8.8; 535 -8.1; 588 -7.4; 647 -6.5; 712 -5.6; 783 -4.8; 861 -4.4; 947 -4.8; 1042 -5.8; 1146 -6.7; 1261 -7.1; 1387 -7.4; 1526 -7.5; 1678 -6.9; 1846 -6.3; 2031 -5.6; 2234 -4.4; 2457 -2.6; 2703 -1.3; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -2.5; 4788 -3.1; 5267 -1.9; 5793 -1.6; 6373 -3.7; 7010 -7.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.8; 13660 -11.9; 15026 -13.0; 16529 -10.5; 18182 -7.0; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 45e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 45e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 85 Hz    | 0.33 | -8.0 dB |
| Peaking | 3641 Hz  | 1.12 | 6.3 dB  |
| Peaking | 11877 Hz | 2.68 | 3.1 dB  |
| Peaking | 14667 Hz | 1.3  | -7.5 dB |
| Peaking | 847 Hz   | 1.65 | 5.0 dB  |
| Peaking | 1688 Hz  | 0.36 | -3.3 dB |
| Peaking | 2716 Hz  | 1.9  | 3.8 dB  |
| Peaking | 5884 Hz  | 3.9  | 4.1 dB  |
| Peaking | 6891 Hz  | 6.61 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -6.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2045e/Jabra%20Elite%2045e.png)