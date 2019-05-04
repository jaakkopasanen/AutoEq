# Bose QuietComfort 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.6; 25 -6.4; 28 -6.1; 31 -6.0; 34 -6.0; 37 -6.1; 41 -6.3; 45 -6.6; 49 -6.8; 54 -6.9; 60 -7.0; 66 -7.0; 72 -7.0; 79 -7.1; 87 -7.3; 96 -7.4; 106 -7.6; 116 -7.8; 128 -8.0; 141 -8.1; 155 -8.1; 170 -8.0; 187 -7.9; 206 -7.6; 227 -7.3; 249 -7.1; 274 -7.0; 302 -6.8; 332 -6.6; 365 -6.3; 402 -6.2; 442 -6.2; 486 -6.1; 535 -5.9; 588 -5.6; 647 -5.3; 712 -4.8; 783 -4.6; 861 -4.3; 947 -4.1; 1042 -4.3; 1146 -5.2; 1261 -7.0; 1387 -8.3; 1526 -8.7; 1678 -9.9; 1846 -10.9; 2031 -11.0; 2234 -10.3; 2457 -8.7; 2703 -6.3; 2973 -4.7; 3270 -6.8; 3597 -9.6; 3957 -8.8; 4353 -5.6; 4788 -1.7; 5267 -0.5; 5793 -5.9; 6373 -11.9; 7010 -6.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.8; 12418 -7.9; 13660 -6.5; 15026 -8.4; 16529 -10.8; 18182 -11.0; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 909 Hz   | 1.95 | 2.9 dB  |
| Peaking | 1887 Hz  | 2.32 | -5.3 dB |
| Peaking | 3845 Hz  | 5.79 | -5.0 dB |
| Peaking | 5263 Hz  | 2.63 | 8.2 dB  |
| Peaking | 6267 Hz  | 5.63 | -9.5 dB |
| Peaking | 144 Hz   | 1.17 | -1.7 dB |
| Peaking | 1867 Hz  | 4.7  | 1.4 dB  |
| Peaking | 2268 Hz  | 1.65 | -1.5 dB |
| Peaking | 2897 Hz  | 5.98 | 3.6 dB  |
| Peaking | 19133 Hz | 0.62 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)