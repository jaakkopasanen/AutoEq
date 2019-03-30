# Bose On-ear headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.1; 25 -7.5; 28 -8.1; 31 -8.6; 34 -9.0; 37 -9.3; 41 -9.7; 45 -10.0; 49 -10.3; 54 -10.5; 60 -10.7; 66 -10.9; 72 -11.0; 79 -11.1; 87 -11.3; 96 -11.3; 106 -11.3; 116 -11.6; 128 -12.0; 141 -12.5; 155 -12.7; 170 -12.9; 187 -12.8; 206 -12.4; 227 -11.7; 249 -10.6; 274 -9.4; 302 -8.1; 332 -6.7; 365 -5.2; 402 -4.0; 442 -2.9; 486 -1.9; 535 -1.2; 588 -0.7; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.8; 947 -1.5; 1042 -2.4; 1146 -3.2; 1261 -3.9; 1387 -4.2; 1526 -4.6; 1678 -5.0; 1846 -5.4; 2031 -5.8; 2234 -6.3; 2457 -6.7; 2703 -6.7; 2973 -6.4; 3270 -6.2; 3597 -6.0; 3957 -5.7; 4353 -5.3; 4788 -5.5; 5267 -7.9; 5793 -11.0; 6373 -11.9; 7010 -10.5; 7711 -7.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose On-ear headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose On-ear headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 64 Hz   | 0.64 | -3.6 dB |
| Peaking | 193 Hz  | 0.92 | -6.6 dB |
| Peaking | 631 Hz  | 0.81 | 7.3 dB  |
| Peaking | 4599 Hz | 4.01 | 2.5 dB  |
| Peaking | 6209 Hz | 3.12 | -6.2 dB |
| Peaking | 681 Hz  | 3.18 | -1.2 dB |
| Peaking | 757 Hz  | 1.79 | 1.0 dB  |
| Peaking | 2460 Hz | 3.37 | -1.0 dB |
| Peaking | 8538 Hz | 6.09 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Bose%20On-ear%20headphones/Bose%20On-ear%20headphones.png)