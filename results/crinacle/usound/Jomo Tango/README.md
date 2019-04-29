# Jomo Tango
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.2; 28 -7.5; 31 -7.7; 34 -7.9; 37 -8.0; 41 -8.2; 45 -8.4; 49 -8.5; 54 -8.7; 60 -8.9; 66 -9.2; 72 -9.5; 79 -9.8; 87 -10.1; 96 -10.4; 106 -10.7; 116 -10.9; 128 -11.0; 141 -11.1; 155 -11.1; 170 -11.0; 187 -10.9; 206 -10.6; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.2; 332 -8.6; 365 -7.9; 402 -7.3; 442 -6.6; 486 -5.8; 535 -5.1; 588 -4.3; 647 -3.5; 712 -2.6; 783 -1.7; 861 -0.9; 947 -0.5; 1042 -0.5; 1146 -1.0; 1261 -1.7; 1387 -2.1; 1526 -2.1; 1678 -1.7; 1846 -1.4; 2031 -1.4; 2234 -1.7; 2457 -2.4; 2703 -3.2; 2973 -3.4; 3270 -3.4; 3597 -3.4; 3957 -3.9; 4353 -4.8; 4788 -6.9; 5267 -8.4; 5793 -6.4; 6373 -4.2; 7010 -4.6; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Tango GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Tango ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 0.32 | -1.8 dB |
| Peaking | 177 Hz  | 0.5  | -4.7 dB |
| Peaking | 882 Hz  | 1.23 | 4.5 dB  |
| Peaking | 2089 Hz | 0.71 | 3.1 dB  |
| Peaking | 5209 Hz | 5.91 | -4.3 dB |
| Peaking | 1463 Hz | 3.44 | -1.0 dB |
| Peaking | 1883 Hz | 1.37 | 0.8 dB  |
| Peaking | 2769 Hz | 4.37 | -1.0 dB |
| Peaking | 6500 Hz | 8.29 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Tango/Jomo%20Tango.png)