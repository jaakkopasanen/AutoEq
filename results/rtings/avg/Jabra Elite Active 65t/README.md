# Jabra Elite Active 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.6; 25 -2.5; 28 -3.7; 31 -4.6; 34 -5.3; 37 -5.7; 41 -6.2; 45 -6.5; 49 -6.7; 54 -6.9; 60 -7.2; 66 -7.3; 72 -7.4; 79 -7.6; 87 -7.8; 96 -7.9; 106 -8.0; 116 -8.2; 128 -8.2; 141 -8.1; 155 -8.0; 170 -8.0; 187 -7.7; 206 -7.4; 227 -7.1; 249 -7.0; 274 -6.7; 302 -6.3; 332 -6.0; 365 -5.8; 402 -5.5; 442 -4.9; 486 -4.4; 535 -3.8; 588 -3.1; 647 -2.4; 712 -2.0; 783 -2.3; 861 -2.9; 947 -3.3; 1042 -3.9; 1146 -4.6; 1261 -5.0; 1387 -5.0; 1526 -5.0; 1678 -5.3; 1846 -5.7; 2031 -6.1; 2234 -6.0; 2457 -5.4; 2703 -4.6; 2973 -4.0; 3270 -3.7; 3597 -3.8; 3957 -4.2; 4353 -5.0; 4788 -6.1; 5267 -5.9; 5793 -4.1; 6373 -2.1; 7010 -2.9; 7711 -5.3; 8482 -7.6; 9330 -9.7; 10263 -11.7; 11289 -10.2; 12418 -5.8; 13660 -5.4; 15026 -5.4; 16529 -7.2; 18182 -8.3; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Active 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Active 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.84 | 5.6 dB  |
| Peaking | 116 Hz   | 0.46 | -2.9 dB |
| Peaking | 707 Hz   | 1.53 | 3.7 dB  |
| Peaking | 6612 Hz  | 4.74 | 4.5 dB  |
| Peaking | 10255 Hz | 2.79 | -6.9 dB |
| Peaking | 2151 Hz  | 2.62 | -1.4 dB |
| Peaking | 3336 Hz  | 1.7  | 2.0 dB  |
| Peaking | 4955 Hz  | 4.96 | -1.8 dB |
| Peaking | 13446 Hz | 3.02 | 1.3 dB  |
| Peaking | 17564 Hz | 2.47 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%20Active%2065t/Jabra%20Elite%20Active%2065t.png)