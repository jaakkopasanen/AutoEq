# Jabra Elite 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -2.0; 28 -3.3; 31 -4.3; 34 -5.1; 37 -5.7; 41 -6.3; 45 -6.7; 49 -7.0; 54 -7.2; 60 -7.5; 66 -7.7; 72 -8.0; 79 -8.3; 87 -8.5; 96 -8.6; 106 -8.8; 116 -8.9; 128 -9.0; 141 -9.0; 155 -8.9; 170 -8.7; 187 -8.6; 206 -8.5; 227 -8.2; 249 -8.0; 274 -7.7; 302 -7.4; 332 -7.1; 365 -6.9; 402 -6.5; 442 -6.0; 486 -5.6; 535 -5.1; 588 -4.5; 647 -3.8; 712 -3.2; 783 -2.9; 861 -3.0; 947 -3.4; 1042 -4.2; 1146 -5.0; 1261 -5.6; 1387 -6.0; 1526 -6.3; 1678 -6.6; 1846 -7.1; 2031 -7.4; 2234 -7.3; 2457 -6.5; 2703 -5.5; 2973 -4.5; 3270 -4.2; 3597 -4.3; 3957 -5.0; 4353 -6.0; 4788 -7.2; 5267 -6.8; 5793 -4.7; 6373 -2.4; 7010 -3.7; 7711 -6.0; 8482 -8.1; 9330 -10.8; 10263 -14.6; 11289 -15.0; 12418 -10.2; 13660 -6.3; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.54 | 6.2 dB   |
| Peaking | 125 Hz   | 0.51 | -2.8 dB  |
| Peaking | 771 Hz   | 1.67 | 3.9 dB   |
| Peaking | 6586 Hz  | 4.6  | 5.1 dB   |
| Peaking | 10760 Hz | 2.85 | -10.2 dB |
| Peaking | 2136 Hz  | 2.11 | -2.1 dB  |
| Peaking | 3278 Hz  | 1.78 | 2.7 dB   |
| Peaking | 4915 Hz  | 4.67 | -2.0 dB  |
| Peaking | 13680 Hz | 5.21 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2065t/Jabra%20Elite%2065t.png)